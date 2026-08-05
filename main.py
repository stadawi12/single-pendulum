import matplotlib.pyplot as plt
import math as m
import pygame

class Pendulum:
    def __init__(self, length, mass, initial_angle):
        self.length = length
        self.mass = mass
        self.initial_angle = initial_angle
        self.current_angle = initial_angle
        self.current_angular_velocity = 0
        self.time_period = 2 * m.pi * m.sqrt(length / 9.81)  # Calculate the time period of the pendulum

    def update(self, dt):
        # Update the angular velocity and angle using simple physics equations
        g = 9.81  # acceleration due to gravity in m/s^2
        angular_acceleration = -(g / self.length) * m.sin(self.current_angle)
        new_angular_velocity = self.current_angular_velocity + angular_acceleration * dt
        new_angle = self.current_angle + new_angular_velocity * dt
        self.current_angular_velocity = new_angular_velocity
        self.current_angle = new_angle

    def reset(self):
        self.current_angle = self.initial_angle
        self.current_angular_velocity = 0

    def generate_motion_data(self, duration, dt):
        angles = []
        times = []
        for t in range(int(duration / dt)+1):
            angles.append(self.current_angle)
            times.append(t * dt)
            self.update(dt)
        return times, angles

    def generate_single_oscillation_data(self, dt):
        times, angles = self.generate_motion_data(duration=self.time_period * 1.5, dt=dt)
        running_index = 0
        for i, current_angle in enumerate(angles):
            previous_angle = angles[i - 1] if i > 0 else current_angle + 1  # Ensure the first angle is not considered a maximum
            next_angle = angles[i + 1] if i < len(angles) - 1 else float('-inf')
            if i > 0 and current_angle > previous_angle and current_angle > next_angle:
                running_index = i
                break
        return angles[:running_index+1], times[:running_index+1], running_index

def single_oscillation_plot():
    pendulum = Pendulum(length=1, mass=1.0, initial_angle=m.radians(10))  # Create a pendulum with length 0.5 m, mass 1 kg, and initial angle of 30 degrees
    print(pendulum.time_period)  # Print the time period for verification
        
    truncated_angles, truncated_times, maximumg_index = pendulum.generate_single_oscillation_data(dt=0.001)  # Generate motion data for a single oscillation with a time step of 0.01 seconds

    print(truncated_times[0], truncated_angles[0])  # Print the first time and angle for verification
    print(truncated_times[-1], truncated_angles[-1])  # Print the last time and angle for verification

    plt.plot(truncated_times, truncated_angles)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (radians)')
    plt.title('Pendulum Motion')
    plt.grid(True)
    plt.show()

def run_pygame_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    frame_rate = 120
    dt = 1 / frame_rate  # Time step for the simulation

    pendulum = Pendulum(length=0.5, mass=0.5, initial_angle=m.radians(50))
    truncated_angles, truncated_times, maximumg_index = pendulum.generate_single_oscillation_data(dt=dt)
  
    i = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))

        # Calculate the position of the pendulum bob
        x = 400 + 3 * 100 * m.sin(truncated_angles[i])
        y = 100 + 3 * 100 * m.cos(truncated_angles[i])

        i += 1
        if i >= len(truncated_angles):
            i = 0  # Loop back to the start of the oscillation

        # Draw the pendulum rod
        pygame.draw.line(screen, (0, 0, 0), (400, 100), (x, y), 2)
        # Draw the pendulum bob
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 45)

        pygame.display.flip()
        clock.tick(frame_rate)  # Limit to the specified frame rate

    pygame.quit()
    
if __name__ == "__main__":
    
    run_pygame_simulation()