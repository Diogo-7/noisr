import pygame
import sys
import random
import math

pygame.init()

#constants
width, height = 800, 600
FPS = 60
Particle_radius=10
num_particles=50
max_speed=2

#Colors
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

#Particle class
class Particle:
    def __init__(self, x, y, is_tracer=False):
        self.x = x
        self.y = y
        self.radius = Particle_radius
        self.color = blue if is_tracer else red
        self.speed = random.randint(0, max_speed)
        self.angle = random.randint(0, 2 * math.pi)
        self.is_tracer = is_tracer
        self.path = []

    def move(self):
        return
    
    def check_collision(self, other_particles):
        return
    
particles=[]

tracer_index=random.randint(0,num_particles-1)

