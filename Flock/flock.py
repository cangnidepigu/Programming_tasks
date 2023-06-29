import pygame
import random
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Flocking parameters
NUM_BOIDS = 100
BOID_SIZE = 10
BOID_SPEED = 2
BOID_FORCE = 0.05
BOID_ALIGNMENT_RADIUS = 50
BOID_COHESION_RADIUS = 50
BOID_SEPARATION_RADIUS = 25
OBSTACLE_SIZE = 25


class Boid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BOID_SIZE, BOID_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.velocity = pygame.Vector2(
            random.uniform(-1, 1), random.uniform(-1, 1)
        ).normalize()
        self.position = pygame.Vector2(
            random.randint(0, WIDTH), random.randint(0, HEIGHT)
        )

    def update(self, boids, obstacles, cursor_position):
        alignment = pygame.Vector2(0, 0)
        cohesion = pygame.Vector2(0, 0)
        separation = pygame.Vector2(0, 0)
        total = 0

        cohesion_direction = pygame.Vector2(0, 0)

        for boid in boids:
            if boid != self:
                distance = self.position.distance_to(boid.position)

                if distance < BOID_ALIGNMENT_RADIUS:
                    alignment += boid.velocity
                    total += 1

                if distance < BOID_COHESION_RADIUS:
                    cohesion += boid.position
                    total += 1

                if distance < BOID_SEPARATION_RADIUS:
                    diff = self.position - boid.position
                    diff /= distance
                    separation += diff
                    total += 1

        # Calculate influence of objects on boids
        for obstacle in obstacles:
            distance = self.position.distance_to(obstacle.rect.center)

            if (
                distance < BOID_SIZE * 3 + OBSTACLE_SIZE
            ):  # Adjust the collision radius based on the sizes of the boid and obstacle
                avoidance = self.position - obstacle.rect.center
                avoidance = avoidance.normalize() * BOID_FORCE
                self.velocity += avoidance

                # Prevent penetration by adjusting position
                if distance < BOID_SIZE + OBSTACLE_SIZE:
                    penetration = BOID_SIZE + OBSTACLE_SIZE - distance
                    correction = self.position - obstacle.rect.center
                    correction = correction.normalize() * penetration
                    self.position += correction

        if total > 0:
            alignment /= total
            if alignment.length() > 0:
                alignment = alignment.normalize() * BOID_SPEED

            cohesion /= total
            cohesion_direction = (cohesion - self.position).normalize() * BOID_SPEED

            separation /= total
            if separation.length() > 0:
                separation = separation.normalize() * BOID_SPEED

        self.velocity += alignment + cohesion_direction + separation
        self.velocity = self.velocity.normalize() * BOID_SPEED

        # Calculate direction to cursor
        cursor_direction = cursor_position - self.position
        cursor_direction = cursor_direction.normalize() * BOID_SPEED

        self.velocity += cursor_direction
        self.velocity = self.velocity.normalize() * BOID_SPEED

        self.position += self.velocity
        self.rect.center = self.position

        # Wrap around the screen
        if self.position.x < 0:
            self.position.x = WIDTH
        elif self.position.x > WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = HEIGHT
        elif self.position.y > HEIGHT:
            self.position.y = 0


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = position


def run_flock(num_boids=100):
    NUM_BOIDS = num_boids

    obstacles = pygame.sprite.Group()
    obstacle1 = Obstacle((200, 300), [OBSTACLE_SIZE, OBSTACLE_SIZE])
    obstacle2 = Obstacle((500, 400), (OBSTACLE_SIZE, OBSTACLE_SIZE))
    obstacles.add(obstacle1, obstacle2)

    boids = pygame.sprite.Group()
    for _ in range(NUM_BOIDS):
        boid = Boid()
        boids.add(boid)

    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flock")

    # Game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        cursor_position = pygame.mouse.get_pos()

        boids.update(boids, obstacles, cursor_position)

        screen.fill(BLACK)
        boids.draw(screen)
        obstacles.draw(screen)
        pygame.display.flip()

    pygame.quit()


menu_options = {1: "Default parameters", 2: "Custom number of boids", 3: "Exit"}


def print_menu():
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


if __name__ == "__main__":
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Wrong input. Please enter a number ...")
        if option == 1:
            run_flock()
        elif option == 2:
            num_boids = int(input("Enter number of boids: "))
            run_flock(num_boids)
        elif option == 3:
            print("Thank you!")
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 3.")
