#!/usr/bin/env python2
# -*-coding:UTF-8 -*
"""
The Text Geolocation Module
==============================


"""

import time
import re
from pubsublogger import publisher
from packages import Paste
from Helper import Process
from mordecai import Geoparser


def search_geolocation(message):
    paste = Paste.Paste(message)
    content = paste.get_p_content()

    # Load Geoparser
    geo = Geoparser()
    geolocation = geo.geoparse(message)
    
    # regex ton find latitude and longitude
    reg_lat = re.compile(r'(\'lat\': \'([-\d.]+)\',)')
    reg_lon = re.compile(r'(\'lon\': \'([-\d.]+)\',)')

    #lat = set(reg_lat.findall(content))
    #lon = set(reg_lat.findall(content))

    lat = reg_lat.search(message).group(2)
    lon = reg_lon.search(message).group(2)

    print('latitude: {}'.format(lat))
    print('longitude: {}'.format(lon))
    
    
    print('{} text geolocation'.format(paste.p_name))
    publisher.warning('{} contains geolocation'.format(paste.p_name))


if __name__ == '__main__':
    # If you wish to use an other port of channel, do not forget to run a subscriber accordingly (see launch_logs.sh)
    # Port of the redis instance used by pubsublogger
    publisher.port = 6380
    # Script is the default channel used for the modules.
    publisher.channel = 'Script'

    # Section name in bin/packages/modules.cfg
    config_section = 'Geolocation'

    # Setup the I/O queues
    p = Process(config_section)

    # Sent to the logging a description of the module
    publisher.info("Run Geolocation module")

    # Endless loop getting messages from the input queue
    while True:
        # Get one message from the input queue
        message = p.get_from_set()
        if message is None:
            publisher.debug("{} queue is empty, waiting".format(config_section))
            time.sleep(1)
            continue

        # Do something with the message from the queue
        search_geolocation(message)

