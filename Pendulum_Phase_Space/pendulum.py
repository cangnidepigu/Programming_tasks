import numpy as np
import matplotlib.pyplot as plt

def pendulum_phase_space(theta_0, theta_dot_0, g, L, damping=0, time=10, dt=0.01):
    t = np.arange(0, time, dt)
    theta = np.zeros_like(t)
    theta_dot = np.zeros_like(t)
    theta[0] = theta_0
    theta_dot[0] = theta_dot_0

    for i in range(1, len(t)):
        theta_double_dot = -g/L * np.sin(theta[i-1]) - damping * theta_dot[i-1]
        theta_dot[i] = theta_dot[i-1] + theta_double_dot * dt
        theta[i] = theta[i-1] + theta_dot[i] * dt

    return theta, theta_dot

# Parameters
theta_0 = np.pi / 4  # Initial angular displacement
theta_dot_0 = 0.0    # Initial angular velocity
g = 9.81            # Acceleration due to gravity (change as desired)
L = 1.0             # Length of the pendulum (change as desired)
damping = 0.2       # Damping coefficient (change as desired)

# Calculate phase space
theta, theta_dot = pendulum_phase_space(theta_0, theta_dot_0, g, L, damping)

# Plot phase space diagram
plt.plot(theta, theta_dot)
plt.xlabel('Theta (angle)')
plt.ylabel('Theta_dot (angular velocity)')
plt.title('Phase Space Diagram: Pendulum Motion')
plt.grid(True)
plt.show()