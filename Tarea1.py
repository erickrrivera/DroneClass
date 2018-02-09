from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time
#dronekit-sitl copter --home=20.737541,-103.457088,1350,180  
#The line 3 text is to program the coordinates of the take off.
#Code to arm the drone, the while is to assure the drone is already armed, before proceeding to the next steps.
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




#vehicle Connection, these are for guiding the drone through different coordinates.
drone = connect("127.0.0.1:14551", wait_ready=True)
arm_and_takeoff(20)

drone.airspeed = 10

Waypoint1 = LocationGlobalRelative(20.737380,-103.454985,20)

Waypoint2 = LocationGlobalRelative(20.735393,-103.455146,20)

Waypoint3 = LocationGlobalRelative(20.735513,-103.457260,20)

print ("On the way to first point")
drone.simple_goto(Waypoint1)
time.sleep(20)
print ("On the way to second point")
drone.simple_goto(Waypoint2)
time.sleep(20)
print ("On the way to third point")
drone.simple_goto(Waypoint3)
time.sleep(20)

#BATERIA
DroneBattery= drone.battery.voltage 
print ("The drone battery is: ",DroneBattery, "v")

#Regreso al Takeoff

print ("The drone is turning back to the takeoff point")
drone.mode = VehicleMode("RTL")

