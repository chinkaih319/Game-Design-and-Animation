"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2, y=self.window.height -
                            paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width)/2, (self.window.height - self.ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = random.randint(1, INITIAL_Y_SPEED)
        # Attributes needed in later function
        self.p_o = paddle_offset
        self.b_r = ball_radius
        # Draw bricks
        every_horizon = 0
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'Red'
                    self.window.add(self.brick, every_horizon, brick_offset)
                elif 2 <= j < 4:
                    self.brick.fill_color = 'Orange'
                    self.window.add(self.brick, every_horizon, brick_offset)
                elif 4 <= j < 6:
                    self.brick.fill_color = 'Yellow'
                    self.window.add(self.brick, every_horizon, brick_offset)
                elif 6 <= j < 8:
                    self.brick.fill_color = 'Green'
                    self.window.add(self.brick, every_horizon, brick_offset)
                else:
                    self.brick.fill_color = 'Blue'
                    self.window.add(self.brick, every_horizon, brick_offset)
                every_horizon += brick_width + brick_spacing
            every_horizon = 0
            brick_offset += brick_height + brick_spacing
        # Initialize our mouse listeners
        self.time = 0
        self.score = 0
        onmouseclicked(self.start_game)

        # The dx getter
    def get_dx(self):
        return self.__dx

        # The dy getter
    def get_dy(self):
        return self.__dy

    def start_game(self, event):
        self.time = 1
        if self.time == 1:
            onmousemoved(self.move_the_paddle)

    def move_the_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width/2
        self.paddle.y = self.window.height - self.p_o
        if event.x <= 0:
            self.paddle.x = 0
            self.paddle.y = self.window.height - self.p_o
        if event.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.window.height - self.p_o

    def remove_or_change(self, x):
        if self.ball.y <= self.paddle.y:
            if x is not None and x is self.paddle:
                self.__dy = -self.__dy
                self.ball.y = self.paddle.y - self.ball.height
            if x is not None and x is not self.paddle:
                self.window.remove(x)
                self.score += 1
                self.__dy = -self.__dy

    def beginning(self):
        self.ball = GOval(self.b_r * 2, self.b_r * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2, (self.window.height - self.ball.height) /
                        2)
