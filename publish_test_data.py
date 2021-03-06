#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

import paho.mqtt.publish as publish

from common import hostname, client_id

if __name__ == '__main__':
    device_ids = [0, 2, 4, 6, 8]
    device_id = random.choice(device_ids)
    HR = random.randrange(50, 120)
    RR = random.randrange(6, 30)

    publish.single("/vitalerter/adrian/vitals", "%d,%d,%d" % (device_id, HR, RR), hostname=hostname,
                   client_id=client_id)
