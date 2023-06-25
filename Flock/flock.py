import pygame
import random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Window dimensions
width = 800
height = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Flocking parameters
num_boids = 100
neighborhood_radius = 300
desired_separation = 25
alignment_factor = 0.8
cohesion_factor = 0.12
separation_factor = 1.5
vector_color = (0, 255, 0)
vector_scale = 20

# Boid class
class Boid(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)

    def update(self, flock, obstacles):
        # Apply flocking rules
        separation = Vector2(1, 0)
        alignment = Vector2(1, 0)
        cohesion = Vector2(1, 0)
        total_boids = 0

        for boid in flock:
            distance = self.position.distance_to(boid.position)
            if distance < neighborhood_radius and distance > 0:
                separation += (self.position - boid.position) / distance**2
                alignment += boid.velocity
                cohesion += boid.position
                total_boids += 1

        if total_boids > 0:
            separation /= total_boids
            alignment /= total_boids
            cohesion /= total_boids

        # Apply the three flocking rules
        separation.normalize_ip()
        separation *= separation_factor
        alignment.normalize_ip()
        alignment *= alignment_factor
        cohesion = (cohesion - self.position).normalize() * cohesion_factor

        # Update velocity and position
        self.velocity += separation + alignment + cohesion
        self.velocity.scale_to_length(5)  # Limit the speed
        self.position += self.velocity

        # Avoid obstacles
        avoidance = Vector2(1, 0)
        for obstacle in obstacles:
            distance = self.position.distance_to(obstacle.position)
            if distance < neighborhood_radius and distance > 0:
                avoidance += (self.position - obstacle.position) / distance**2

        avoidance.normalize_ip()
        avoidance *= separation_factor
        self.velocity += avoidance

        # Wrap around the screen edges
        if self.position.x < 0:
            self.position.x = width
        elif self.position.x > width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = height
        elif self.position.y > height:
            self.position.y = 0

        self.rect.center = self.position

    def draw_vector(self, screen):
        vector_end = self.position + self.velocity.normalize() * vector_scale
        pygame.draw.line(screen, vector_color, self.position, vector_end)

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(position)

# Create the flock and obstacles
flock = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
for _ in range(num_boids):
    position = (random.randint(0, width), random.randint(0, height))
    velocity = (random.uniform(-1, 1), random.uniform(-1, 1))
    boid = Boid(position, velocity)
    flock.add(boid)

obstacle_position = (width // 2, height // 2)
obstacle = Obstacle(obstacle_position)
obstacel2 = Obstacle((width // 3, height // 3))
obstacles.add(obstacle)
obstacles.add(obstacel2)

# Set up the screen
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the flock and obstacles
    flock.update(flock, obstacles)

    # Render the scene
    screen.fill(BLACK)
    for boid in flock:
        boid.draw_vector(screen)
    flock.draw(screen)
    obstacles.draw(screen)
    pygame.display.flip()
    clock.tick(15)

# Quit the application
pygame.quit()
