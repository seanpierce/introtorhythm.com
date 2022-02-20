import os
import glob
import datetime
import xml.etree.ElementTree as XML
from repositories.schedule import ScheduleRepository as repo

def run():
    show = repo.get_current_show()

    if show is None:
        now = datetime.datetime.now()
        date = now.strftime('%m/%d/%Y')
        time = now.strftime('%H:%M:%S')
        message = 'No show for this time slot %s - %s' %(date, time)
        return message

    # delete_existing_config()
    # create_ezstream_config(SHOW['audio'])
    # set_config_permissions()
    # start_ezstream()