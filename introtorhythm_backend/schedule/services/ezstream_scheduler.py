import os
import signal
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path

from django.conf import settings
from django.utils import timezone

from schedule.models import Show


SCHEDULER_DIR = Path(settings.EZSTREAM_SCHEDULER_DIR)
CONFIG_PATH = SCHEDULER_DIR / "scheduler.xml"
PID_PATH = SCHEDULER_DIR / "scheduler.pid"


def get_show_for_current_hour():
    now = timezone.localtime()

    return Show.objects.filter(
        active=True,
        date=now.date(),
        start_time=now.hour
    ).first()


def build_ezstream_config(audio_path: str):
    SCHEDULER_DIR.mkdir(parents=True, exist_ok=True)

    ezstream = ET.Element("ezstream")

    servers = ET.SubElement(ezstream, "servers")
    server = ET.SubElement(servers, "server")
    ET.SubElement(server, "hostname").text = settings.EZSTREAM_HOST
    ET.SubElement(server, "port").text = str(settings.EZSTREAM_PORT)
    ET.SubElement(server, "password").text = settings.EZSTREAM_PASSWORD

    streams = ET.SubElement(ezstream, "streams")
    stream = ET.SubElement(streams, "stream")
    ET.SubElement(stream, "mountpoint").text = settings.EZSTREAM_MOUNTPOINT
    ET.SubElement(stream, "format").text = settings.EZSTREAM_FORMAT

    intakes = ET.SubElement(ezstream, "intakes")
    intake = ET.SubElement(intakes, "intake")
    ET.SubElement(intake, "filename").text = audio_path
    ET.SubElement(intake, "shuffle").text = "0"
    ET.SubElement(intake, "stream_once").text = "1"

    tree = ET.ElementTree(ezstream)
    tree.write(CONFIG_PATH, encoding="utf-8", xml_declaration=True)


def pid_matches_scheduler_process(pid: int) -> bool:
    cmdline_path = Path(f"/proc/{pid}/cmdline")

    if not cmdline_path.exists():
        return False

    cmdline = cmdline_path.read_text(errors="ignore").replace("\x00", " ")
    return "ezstream" in cmdline and str(CONFIG_PATH) in cmdline


def stop_existing_scheduler_ezstream():
    if not PID_PATH.exists():
        return

    try:
        pid = int(PID_PATH.read_text().strip())
    except ValueError:
        PID_PATH.unlink(missing_ok=True)
        return

    if not pid_matches_scheduler_process(pid):
        PID_PATH.unlink(missing_ok=True)
        return

    try:
        os.killpg(pid, signal.SIGTERM)
        time.sleep(2)

        if pid_matches_scheduler_process(pid):
            os.killpg(pid, signal.SIGKILL)

    except ProcessLookupError:
        pass
    finally:
        PID_PATH.unlink(missing_ok=True)


def start_scheduler_ezstream():
    log_path = SCHEDULER_DIR / "scheduler-ezstream.log"

    process = subprocess.Popen(
        ["ezstream", "-c", str(CONFIG_PATH)],
        cwd=str(SCHEDULER_DIR),
        stdout=open(log_path, "ab"),
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )

    PID_PATH.write_text(str(process.pid))


def run_pre_recorded_show_scheduler():
    show = get_show_for_current_hour()
    now = timezone.localtime()

    if not show:
        return {
            "started": False,
            "message": f"No show for current time slot: {now}",
        }

    if not show.pre_recorded_show:
        return {
            "started": False,
            "message": f"Show '{show}' has no pre-recorded audio.",
        }

    audio_path = show.pre_recorded_show.path

    if not Path(audio_path).exists():
        return {
            "started": False,
            "message": f"Audio file does not exist: {audio_path}",
        }
    
    file_name = os.path.basename(show.pre_recorded_show.name)

    stop_existing_scheduler_ezstream()

    CONFIG_PATH.unlink(missing_ok=True)
    build_ezstream_config(file_name)
    start_scheduler_ezstream()

    return {
        "started": True,
        "show_id": show.id,
        "audio": file_name,
        "config": str(CONFIG_PATH)
    }