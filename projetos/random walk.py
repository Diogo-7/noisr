import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):

    particle_paths = []

    for i in range(num_particles):
        path = [0] 
        for i in range(num_steps):
            move = random.random()
            if move <= prob_right:
                path.append(path[-1] + 1) 
            else:
                path.append(path[-1] - 1)  
        particle_paths.append(path)

    create_plot(num_steps, particle_paths)

    return particle_paths

def create_plot(num_steps, particle_paths):
    time = [x for x in range(len(particle_paths[0]))]

    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title(f'Random Walk - {num_particles} particles')
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.show()

num_steps = 100
prob_right = 0.5
num_particles = 100

random_walk(num_steps,prob_right,num_particles)