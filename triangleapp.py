#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off to 10m'
drone.take_off(10.0)
print 'adjusting altitiude to 5m'
drone.position_set(0,0, 5, relative=True)
print ' going along the setpoints'
drone.position_set(-5,10, 0, relative=True)
drone.position_set(-5,-10, 0, relative=True)
drone.position_set(10,0, 0, relative=True)

print 'Landing'
drone.land(async=False)
print 'Landed'
# shutdown the instance
drone.disconnect()
