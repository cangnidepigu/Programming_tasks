import pygame
import math

width = 800
height = 600


def draw_point(a, b, delta, time, screen, clock, line_surface):
    # Calculate the current position on the Lissajous curve
    x = width / 2 + (width / 2 - 50) * math.sin(a * time)
    y = height / 2 + (height / 2 - 50) * math.sin(b * time + delta)

    pygame.draw.circle(line_surface, (255, 255, 255), (int(x), int(y)), 2)

    screen.blit(line_surface, (0, 0))

    # Draw the point
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(60)

    return x, y


def main():
    print("Lissajous Curve Simulator")
    print("-------------------------")
    a = float(input("Enter the value of 'a' (frequency ratio of the x-component): "))
    b = float(input("Enter the value of 'b' (frequency ratio of the y-component): "))
    delta = float(
        input("Enter the value of 'δ' (delta) (phase difference between x and y): ")
    )

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lissajous Curve")
    clock = pygame.time.Clock()

    # Create a separate surface for drawing the line segments
    line_surface = pygame.Surface((width, height))

    time = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a = float(input("Enter the new value of 'a': "))
                elif event.key == pygame.K_b:
                    b = float(input("Enter the new value of 'b': "))
                elif event.key == pygame.K_d:
                    delta = float(input("Enter the new value of 'δ' (delta): "))
                elif event.key == pygame.K_r:
                    screen.fill((255, 255, 255))
                    line_surface.fill((0, 0, 0))
                elif event.key == pygame.K_e:
                    pygame.quit()

        draw_point(a, b, delta, time, screen, clock, line_surface)

        time += 0.01

    pygame.quit()


if __name__ == "__main__":
    main()
