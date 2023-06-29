import pygame
import math

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lissajous Curve")
clock = pygame.time.Clock()


def draw_point_for_lissajous_curve(a, b, delta, time):
    screen.fill((255, 255, 255))

    # Calculate the current position on the Lissajous curve
    x = width / 2 + (width / 2 - 50) * math.sin(a * time)
    y = height / 2 + (height / 2 - 50) * math.sin(b * time + delta)

    # Draw the point
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(60)


def main():
    print("Lissajous Curve Simulator")
    print("-------------------------")
    a = float(input("Enter the value of 'a' (frequency ratio of the x-component): "))
    b = float(input("Enter the value of 'b' (frequency ratio of the y-component): "))
    delta = float(
        input("Enter the value of 'δ' (delta) (phase difference between x and y): ")
    )

    time = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_point_for_lissajous_curve(a, b, delta, time)

        time += 0.01

    # Quit the application
    pygame.quit()


if __name__ == "__main__":
    main()
