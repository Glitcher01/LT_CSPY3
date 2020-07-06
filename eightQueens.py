import pygame


def draw_board(the_board):
    """ Draw a chess board with queens, from the_board. """
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    for row in range(n):  # Draw each row of the board.
        c_index = row % 2  # Change starting color on each row
        for col in range(n):  # Run through cols drawing squares
            the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
            surface.fill(colors[c_index], the_square)
            # now flip the color index for the next square
            c_index = (c_index + 1) % 2


draw_board([6, 4, 2, 0, 5, 7, 1, 3])
