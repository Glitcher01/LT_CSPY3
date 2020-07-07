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
        new_y_pos = y + self.y_velocity * 3000 / 36
        (target_x, target_y) = self.target_posn  # Unpack the position
        dist_to_go = target_y - new_y_pos  # How far to our floor?

        if dist_to_go < 0:  # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity  # Bounce
            new_y_pos = target_y + dist_to_go  # Move back above floor

        self.posn = (x, new_y_pos)  # Set our new position.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.2


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count + 1) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0,
                      50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains  pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width() / 10
        my_height = self.image.get_height()
        (x, y) = pt
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5


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

    # Load the sprite sheet
    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")
    duke_offset_x = (sq_sz - 44) // 2
    duke_offset_y = (sq_sz + 26) // 2
    # Instantiate two duke instances, put them on the chessboard
    duke1 = DukeSprite(duke_sprite_sheet, (sq_sz * 2 + duke_offset_x, duke_offset_y))
    duke2 = DukeSprite(duke_sprite_sheet, (sq_sz * 5 + duke_offset_x, sq_sz + duke_offset_y))

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz - ball.get_width()) // 2
    all_sprites = []
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))
        all_sprites.append(a_queen)

    # Add them to the list of sprites which our game loop manages
    all_sprites.append(duke1)
    all_sprites.append(duke2)
    my_clock = pygame.time.Clock()
    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            if key == 27:  # On Escape key ...
                break  # leave the game loop.
            if key == ord('r'):
                colors[0] = (255, 0, 0)  # Change to red + black.
            elif key == ord('g'):
                colors[0] = (0, 255, 0)  # Change to green + black.
            elif key == ord('b'):
                colors[0] = (0, 0, 255)  # Change to blue + black.

        if ev.type == pygame.MOUSEBUTTONDOWN:  # Mouse gone down?
            pos_of_click = ev.dict['pos']  # Get the coordinates.
            for sprite in all_sprites:
                if sprite.contains_point(pos_of_click):
                    sprite.handle_click()
                    break

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

        my_clock.tick(60)  # Waste time so that frame rate becomes 60 fps
        pygame.display.flip()  # Display it

    pygame.quit()


draw_board(list(range(13)))
