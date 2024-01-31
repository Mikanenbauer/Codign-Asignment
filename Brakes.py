import argparse
import math
import matplotlib.pyplot as plt
import numpy as np

#I followed a youtube tutorial as a reference to understand argparse: https://www.youtube.com/watch?v=FbEJN8FsJ9U&t=306s"
#For the equations for velocity and distance to brake I followed the ones that we saw in class and the ones in the pptx of the assignement

print("To call the script use python Brake.py and the values for mass, velocity and coefficient of friction")

def braking_distance(mass, initial_velocity, friction):
    # Gravity Constant
    g = 9.81  

    # Braking force
    braking_force = friction * mass * g * (1 + mass * g / (friction * mass * g))

    # Deceleration
    deceleration = braking_force / mass

    # Braking time formula
    braking_time = initial_velocity / abs(deceleration)

    # Braking distance formula
    braking_distance = initial_velocity * braking_time + 0.5 * deceleration * braking_time**2

    return braking_distance, braking_time

def plot_graph(initial_velocity, time, deceleration):
    t = np.linspace(0, time, 100000)  # 100 points between 0 and braking time
    s = initial_velocity * t + 0.5 * deceleration * t**2

    plt.plot(t, s, label='Braking Distance')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance (m)')
    plt.show()

def plot_velocity_over_time(initial_velocity, time, deceleration):
    t = np.linspace(0, time, 100)  # 100 points between 0 and braking time
    v = initial_velocity - deceleration * t 

    plt.plot(t, v, label='Velocity')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (m/s)')
    plt.show()   

def main():
    parser = argparse.ArgumentParser(description="This program will calculate and graph the braking distance")
    parser.add_argument("mass", type=float, help="Introduce the mass of the car in kg")
    parser.add_argument("initial_velocity", type=float, help="What is the velocity of the car in m/s")
    parser.add_argument("friction", type=float, help="Introduce the friction coefficient")
    
    #Here I used the argument to call for the variable inputs which all are numbers with decimals, so I use float

    args = parser.parse_args()

    # This section prints the braking distance and the braking time
    distance, time = braking_distance(args.mass, args.initial_velocity, args.friction)
    print(f"The braking distance is {distance:.2f} meters.")
    print(f"The braking time is {time:.2f} seconds.")
    

    # here we plot for distance over time and velocity over time
    plot_graph(args.initial_velocity, time, time) 

    plot_velocity_over_time(args.initial_velocity, time, time) 

    

if __name__ == "__main__":
    main()