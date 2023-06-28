import numpy as np
import matplotlib.pyplot as plt

default_gravity = 9.807

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

def main():
    print("Pendulum Phase Space Simulator")
    print("-------------------------")
    g = input(f"Enter the value of 'g' (Acceleration due to gravity, leave empty for default gravity: {default_gravity}): ")
    if g == '':
        g = default_gravity
    g = float(g)
    
    L = float(input("Enter the value of 'L' (Length of the pendulum): "))
    damping = float(input("Enter the value of damping (Damping coefficient): "))

    theta_0 = np.pi / 4  # Initial angular displacement
    theta_dot_0 = 0.0    # Initial angular velocity

    theta, theta_dot = pendulum_phase_space(theta_0, theta_dot_0, g, L, damping)

    plt.plot(theta, theta_dot)
    plt.xlabel('Theta (angle)')
    plt.ylabel('Theta_dot (angular velocity)')
    plt.title('Phase Space Diagram: Pendulum Motion')
    plt.show()

if __name__ == "__main__":
    main()