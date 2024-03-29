import pygame
import matplotlib.pyplot as plt
import numpy as np


def generate_barnsley_fern(n_points):
    x, y = 0, 0
    points = [(x, y)]

    for _ in range(n_points):
        r = np.random.random()

        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        points.append((x, y))

    return points


def draw_barnsley_fern():
    points = generate_barnsley_fern(n_points=100000)
    x, y = zip(*points)

    plt.scatter(x, y, color="green", s=0.2, edgecolor=None)
    plt.title("Barnsley Fern")
    plt.axis("off")
    plt.show()


def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iter


def draw_mandelbrot():
    width = 800
    height = 800
    x_min, x_max = -2.5, 1
    y_min, y_max = -1.5, 1.5
    max_iter = 500

    image = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            real = x * (x_max - x_min) / (width - 1) + x_min
            imag = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color

    plt.imshow(image.T, cmap="hot", extent=(x_min, x_max, y_min, y_max))
    plt.title("Mandelbrot Fractal")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()


def draw_custom_fractal():
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Custom Fractal")
    clock = pygame.time.Clock()

    def custom_fractal(x, y, size, depth):
        if depth <= 0:
            return
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, size, size), 1)

            # Recursively draw smaller fractals in each corner
            new_size = size / 3

            custom_fractal(x, y, new_size, depth - 1)
            custom_fractal(x + new_size, y, new_size, depth - 1)
            custom_fractal(x + 2 * new_size, y, new_size, depth - 1)
            custom_fractal(x, y + new_size, new_size, depth - 1)
            custom_fractal(x + 2 * new_size, y + new_size, new_size, depth - 1)
            custom_fractal(x, y + 2 * new_size, new_size, depth - 1)
            custom_fractal(x + new_size, y + 2 * new_size, new_size, depth - 1)
            custom_fractal(x + 2 * new_size, y + 2 * new_size, new_size, depth - 1)

    def game_loop():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            custom_fractal(100, 100, 600, 5)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    game_loop()


def print_menu():
    for key, value in menu_options.items():
        print(key, "--", value)


if __name__ == "__main__":
    menu_options = {
        1: "Barnsley Fern",
        2: "Mandelbrot",
        3: "Custom",
        4: "Exit",
    }

    while True:
        print_menu()
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            draw_barnsley_fern()
        elif option == 2:
            draw_mandelbrot()
        elif option == 3:
            draw_custom_fractal()
        elif option == 4:
            print("Thank you!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
