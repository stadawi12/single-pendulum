# Single Pendulum Simulation

A small Python project that simulates the motion of a simple pendulum using the forward Euler numerical integration method. The simulation calculates the bob's angular acceleration from gravity, updates its angular velocity and angle over time, and displays the motion as a looping Pygame animation.

## Example

<p align="center">
    <img src="assets/pendulum gif.gif" width=30% height=30%>
</p>

## Run the simulation

Install the required packages:

```bash
pip install pygame matplotlib
```

Start the animation from the project directory:

```bash
python forward_euler.py
```

Close the Pygame window to exit.

## Configuration

The `run_pygame_simulation` function in `forward_euler.py` accepts the initial angle in degrees, pendulum length, bob mass, and time step. For example, change the call at the bottom of the file to:

```python
run_pygame_simulation(initial_angle_degrees=40, length=0.5, mass=0.5)
```

The mass is included as a parameter, but does not affect the pendulum's motion in this idealized model. The animation uses a fixed frame rate and loops through one generated oscillation.