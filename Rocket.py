import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Rocket Parameters
# -----------------------------

g = 9.81                 # Gravity (m/s²)

rocket_mass = 500        # Dry mass (kg)
fuel_mass = 300          # Fuel mass (kg)

thrust = 15000           # Engine thrust (N)

burn_rate = 2            # Fuel burn rate (kg/s)

dt = 0.1                 # Time step (s)

# -----------------------------
# Initial Conditions
# -----------------------------

time = 0

velocity = 0

altitude = 0

acceleration = 0

# Total Mass
mass = rocket_mass + fuel_mass

# Data Storage
times = []
altitudes = []
velocities = []
accelerations = []
fuel_remaining = []

# -----------------------------
# Simulation Loop
# -----------------------------

while altitude >= 0:

    # Fuel Consumption
    if fuel_mass > 0:

        fuel_used = burn_rate * dt

        fuel_mass -= fuel_used

        if fuel_mass < 0:
            fuel_mass = 0

        mass = rocket_mass + fuel_mass

        current_thrust = thrust

    else:

        current_thrust = 0

        mass = rocket_mass

    # Newton's Second Law
    net_force = current_thrust - (mass * g)

    acceleration = net_force / mass

    # Update Velocity
    velocity += acceleration * dt

    # Update Altitude
    altitude += velocity * dt

    # Update Time
    time += dt

    # Store Data
    times.append(time)

    altitudes.append(altitude)

    velocities.append(velocity)

    accelerations.append(acceleration)

    fuel_remaining.append(fuel_mass)

    # Stop when rocket falls back
    if altitude < 0:
        break

    # Safety Stop
    if time > 500:
        break

# -----------------------------
# Flight Statistics
# -----------------------------

max_altitude = max(altitudes)

max_velocity = max(velocities)

flight_time = max(times)

print("\n===== ROCKET FLIGHT REPORT =====")

print(f"Maximum Altitude : {max_altitude:.2f} m")

print(f"Maximum Velocity : {max_velocity:.2f} m/s")

print(f"Flight Time      : {flight_time:.2f} s")

print(f"Final Fuel       : {fuel_mass:.2f} kg")

# -----------------------------
# Plot Altitude
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(
    times,
    altitudes,
    linewidth=2
)

plt.title("Rocket Altitude vs Time")

plt.xlabel("Time (seconds)")

plt.ylabel("Altitude (meters)")

plt.grid(True)

plt.show()

# -----------------------------
# Plot Velocity
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(
    times,
    velocities,
    linewidth=2
)

plt.title("Rocket Velocity vs Time")

plt.xlabel("Time (seconds)")

plt.ylabel("Velocity (m/s)")

plt.grid(True)

plt.show()

# -----------------------------
# Plot Fuel Remaining
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(
    times,
    fuel_remaining,
    linewidth=2
)

plt.title("Fuel Remaining vs Time")

plt.xlabel("Time (seconds)")

plt.ylabel("Fuel (kg)")

plt.grid(True)

plt.show()
