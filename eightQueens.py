import pygame

gravity = 0.0001

class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)  # Start ball at top of its column
        self.y_velocity = 0  # with zero initial velocity

    def update(self):
        self.y_velocity += gravity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn  # Unpack the position
        dist_to_go = target_y - new_y_pos  # How far to our floor?

        if dist_to_go < 0:  # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity  # Bounce
            new_y_pos = target_y + dist_to_go  # Move back above floor

        self.posn = (x, new_y_pos)  # Set our new position.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)


def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, (int(sq_sz * 4 / 5), int(sq_sz * 4 / 5)))

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz - ball.get_width()) // 2
    all_sprites = []
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))
        all_sprites.append(a_queen)
    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type != 0:
            print(ev)

        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for sprite in all_sprites:
            sprite.update()
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()


draw_board(list(range(9)))
