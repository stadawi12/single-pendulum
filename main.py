import matplotlib.pyplot as plt
import math as m

class Pendulum:
    def __init__(self, length, mass, initial_angle):
        self.length = length
        self.mass = mass
        self.initial_angle = initial_angle
        self.current_angle = initial_angle
        self.current_angular_velocity = 0

    def update(self, dt):
        # Update the angular velocity and angle using simple physics equations
        g = 9.81  # acceleration due to gravity in m/s^2
        angular_acceleration = -(g / self.length) * m.sin(m.radians(self.current_angle))
        new_angular_velocity = self.current_angular_velocity + angular_acceleration * dt
        new_angle = self.current_angle + new_angular_velocity * dt
        self.current_angular_velocity = new_angular_velocity
        self.current_angle = new_angle

pendulum = Pendulum(length=0.5, mass=1.0, initial_angle=30)

# Simulation parameters
dt = 0.01  # time step in seconds

# Lists to store the angle and time for plotting
angles = []
times = []

# Run the simulation for a certain duration
simulation_duration = 20  # seconds 

for t in range(int(simulation_duration / dt)):
    angles.append(pendulum.current_angle)
    times.append(t * dt)
    pendulum.update(dt)
    

plt.plot(times, angles)
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.title('Pendulum Motion')
plt.grid(True)
plt.show()
