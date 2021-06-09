#!/usr/bin/env python3
from time import asctime
from datetime import datetime
from http.server import HTTPServer
from server import Server
from tv_serial import TvSerial
from threading import Thread

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8000
VALUE_EXPIRATION = 3

def start_webserver(httpd):
    httpd.serve_forever()


def manage_status():
    if manage_status.last_time == None or (datetime.now() - manage_status.last_time).seconds >= VALUE_EXPIRATION:
        Server.power_status = TvSerial.writeCommand("POWR   ?") == "1"
        Server.mute_status = TvSerial.writeCommand("MUTE   ?") == "1"
        manage_status.last_time = datetime.now()

    if Server.req_power_status != None:
        if Server.req_power_status != Server.power_status:
            TvSerial.writeCommand("POWR0001" if Server.req_power_status else "POWR0000")
            manage_status.last_time = None
        Server.req_power_status = None

    if Server.req_mute_status != None:
        if Server.req_mute_status != Server.mute_status:
            TvSerial.writeCommand("MUTE0001" if Server.req_mute_status else "MUTE0000")
            manage_status.last_time = None
        Server.req_mute_status = None


if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        daemon = Thread(name='daemon_server', target=start_webserver, args=([httpd]))
        daemon.setDaemon(True)
        daemon.start()

        manage_status.last_time = None
        while(True):
            manage_status()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))
