from dronekit import connect, VehicleMode
import time

# Connect to the vehicle (adjust connection string as needed)
# vehicle = connect('127.0.0.1:14550', wait_ready=True)
vehicle = connect('/dev/ttyACM0', baud=115200, wait_ready=True)

# Check if the vehicle is armable
# while not vehicle.is_armable:
#     print(" Waiting for vehicle to initialize...")
#     time.sleep(1)

# Set mode to TAKEOFF and arm
print("Arming vehicle...")
vehicle.mode = VehicleMode("TAKEOFF")
vehicle.arm()

while not vehicle.armed:
    print(" Waiting for arming...")
    time.sleep(1)

print("Armed successfully!")

# Take off to a target altitude (e.g., 10 meters)
aTargetAltitude = 10000
vehicle.simple_takeoff(aTargetAltitude)

# Wait until the vehicle reaches the target altitude
# while True:
#     print(" Altitude: ", vehicle.location.global_relative_frame.alt)
#     if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
#         print("Target altitude reached")
#         break
#     time.sleep(1)

# Optionally, disarm and land
# vehicle.mode = VehicleMode("LAND")
time.sleep(3)

# Stop the motors (set throttle back to 0)
# vehicle.channels.overrides['3'] = 1000  # Set throttle to minimum (0%)

# Wait for motor spin to stop
vehicle.mode = VehicleMode("RTL")

# Disarm the vehicle
# vehicle.disarm()

# Close the connection
vehicle.close()

# Close the connection after the flight
# vehicle.close()
