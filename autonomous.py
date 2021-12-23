# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:22:28 2021

@author: hp
"""

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


def arm_and_takeoff(aTargetAltitude):
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude"
            break
        time.sleep(1)



print "connecting"
vehicle = connect('/dev/ttyACM0', baud = 57600)
print "connected"

print "\nSet Vehicle.mode = (currently: %s)" % vehicle.mode.name
while not vehicle.mode=='GUIDED':
    vehicle.mode = VehicleMode('GUIDED')
    vehicle.flush()

print "vehicle mode: %s" % vehicle.mode

vehicle.armed = True
while not vehicle.armed:
    vehicle.armed = True
    vehicle.flush()
    print " trying to change mode and arming ..."
    time.sleep(1)

print "its armed"

arm_and_takeoff(1)

print "Set default/target airspeed to 3"
vehicle.airspeed = 3

print "Going towards first point for 30 seconds ..."
point21 = LocationGlobalRelative(lat, long, alt)
vehicle.simple_goto(point1)

time.sleep(30)

print "Going towards second point for 30 seconds (groundspeed set to 10 m/s) ..."
point2 = LocationGlobalRelative(lat, long, alt)
vehicle.simple_goto(point2, groundspeed=10)

time.sleep(30)

print "Returning to Launch"
vehicle.mode = VehicleMode("RTL")
print "Close vehicle"
vehicle.close()