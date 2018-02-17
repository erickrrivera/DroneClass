import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#In this part we are making sure the drone is ready to arm before proceeding to the next instructions
def arm_and_takeoff(TargetAltitude):

	print ("Executin Takeoff")
	while not drone.is_armable: 
		print ("Vehicle is not armable, waiting...")
		time.sleep(1)

#This puts the guided mode on, this allows the user to guide drone to his own way.
	print("Ready to arm")
	drone.mode = VehicleMode("GUIDED")	
	drone.armed = True
#It assures the drone is armed before proceeding to next instructions
	while not drone.armed: 
		print ("Waiting for arming...")
		time.sleep(1)

#Code to make the drone take off
	print("Ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)
#The altitude sensor is not 100% precise, so this makes that the drone reaches ALMOST the altitude we want it to reach.
	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude: ", Altitude)
		time.sleep(1)
		if Altitude >=TargetAltitude * 0.95:
			print ("Altitude reached")
			break

#With these series of commands we tell the drone how many meters to move in which direction, whenever we press which key. LIke Up, 5 meters, etc.
def key(event):
    if event.char == event.keysym:
        if event.keysym == 'r': #this enable the letter "r" to open the Tk thing to move the drone with the keys
            drone.mode = VehicleMode("RTL")          
	else: 
        	if event.keysym == 'Up':
           		set_velocity_body(drone,5,0,0)
        	elif event.keysym == 'Down':
           		set_velocity_body(drone,-5,0,0)
        	elif event.keysym == 'Left':
           		set_velocity_body(drone,0,-5,0)
        	elif event.keysym == 'Right':
        		set_velocity_body(drone,0,5,0)
#The command to connect the drone to the computer or the device we want it to connect
drone = connect("127.0.0.1:14551", wait_ready=True)

# Take off to 10 m altitude
arm_and_takeoff(10)
 
# Launching the Tk command in order to use the keys to move the drone
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()
