from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
def arm_and_takeoff(TargetAltitude): 
	print ("Executin Takeoff")
	while not drone.is_armable: 
		print ("Vehicle is not armable, waiting...")
		time.sleep(1)


	print("Ready to arm")
	drone.mode = VehicleMode("GUIDED")	
	drone.armed = True

	while not drone.armed: 
		print ("Waiting for arming...")
		time.sleep(1)


	print("Ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude: ", Altitude)
		time.sleep(1)
		if Altitude >=TargetAltitude * 0.95:
			print ("Altitude reached")
			break




#vehicle Connection
drone = connect("127.0.0.1:14551", wait_ready=True)
arm_and_takeoff(20)

drone.airspeed = 10

a_location = LocationGlobalRelative(-35.362653, 149.165827, 20)
drone.simple_goto(a_location)

time.sleep(50)
