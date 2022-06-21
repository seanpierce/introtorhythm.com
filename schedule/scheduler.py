import configparser
import os
import glob
import datetime
import xml.etree.ElementTree as XML
from repositories.schedule import ScheduleRepository as repo

def delete_existing_config():
    """Deletes any existing pid or config files."""

    config_list = glob.glob('%s/scheduler.xml' %os.path.dirname(os.path.abspath(__file__)))
    pid_list = glob.glob('%s/pid.txt' %os.path.dirname(os.path.abspath(__file__)))

    # there should only be one, but just in case
    for config in config_list:
        os.remove(config)

    #  again, there should only be one...
    for pid_file in pid_list:
        # read pid from file
        with open("%s/pid.txt" %os.path.dirname(os.path.abspath(__file__))) as file:
            pid = file.readline().strip()
            # kill process (if exists)
            # note: ezstream process will always be 1 more than the pid on file
            os.system("kill -9 %s" %(int(pid) + 1))

        # delete file
        os.remove(pid_file)


def create_ezstream_config(filename):
    """Creates ezstream xml config file."""

    config = configparser.RawConfigParser()
    config.read('./env.ini')

    # create the file structure
    ezstream = XML.Element('ezstream')
    servers = XML.SubElement(ezstream, 'servers')
    server = XML.SubElement(servers, 'server')
    hostname = XML.SubElement(server, 'hostname')
    port = XML.SubElement(server, 'port')
    password = XML.SubElement(server, 'password')
    streams = XML.SubElement(ezstream, 'streams')
    stream = XML.SubElement(streams, 'stream')
    mountpoint = XML.SubElement(stream, 'mountpoint')
    format_element = XML.SubElement(stream, 'format')
    intakes = XML.SubElement(ezstream, 'intakes')
    intake = XML.SubElement(intakes, 'intake')
    filename_element = XML.SubElement(intake, 'filename')
    shuffle = XML.SubElement(intake, 'shuffle')
    stream_once = XML.SubElement(intake, 'stream_once')

    # populate element values
    hostname.text = config.get('Ezstream', 'HOST')
    port.text = config.get('Ezstream', 'PORT')
    password.text = config.get('Ezstream', 'PASSWORD')
    mountpoint.text = config.get('Ezstream', 'MOUNTPOINT')
    format_element.text = config.get('Ezstream', 'FORMAT')
    filename_element.text = '%s/%s' %(config.get('Ezstream', 'UPLOAD_DIR'), filename)
    shuffle.text = '0'
    stream_once.text = '1'

    # write file
    ezstream_config = XML.tostring(ezstream)
    path = "%s/scheduler.xml" %os.path.dirname(os.path.abspath(__file__))
    ezstream_config_file = open(path, "wb")
    ezstream_config_file.write(ezstream_config)


def start_ezstream():
    """Compiles a command to execute an ezstream process.

    Saves the process id (pid) to a file for furure reference when
    replacing the current ezstream config.
    """

    path_to_config = "%s/scheduler.xml" %os.path.dirname(os.path.abspath(__file__))
    path_to_pid = "%s/pid.txt" %os.path.dirname(os.path.abspath(__file__))
    command = 'echo $$ > %s; ezstream -c %s' %(path_to_pid, path_to_config)
    os.system(command)

def run():
    show = repo.get_current_show()

    if show is None:
        now = datetime.datetime.now()
        date = now.strftime('%m/%d/%Y')
        time = now.strftime('%H:%M:%S')
        message = 'No show for this time slot %s - %s' %(date, time)
        return message

    audio = show['pre_record_audio']
    if audio is None:
        now = datetime.datetime.now()
        date = now.strftime('%m/%d/%Y')
        time = now.strftime('%H:%M:%S')
        message = 'Show for this time slot %s - %s does not have pre recorded autio' %(date, time)
        return message

    try:
        delete_existing_config()
    except Exception as ex:
        return str(ex)

    try:
        create_ezstream_config(audio)
    except Exception as ex:
        return str(ex)

    try:
        start_ezstream()
    except Exception as ex:
        return str(ex)

    return True