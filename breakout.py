"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball_dx = graphics.get_dx()
    ball_dy = graphics.get_dy()
    life = NUM_LIVES
    while True:
        if graphics.time == 0:
            pause(FRAME_RATE)
        if graphics.time == 1:
            graphics.ball.move(ball_dx, ball_dy)
            obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj1 = graphics.window.get_object_at(graphics.ball.x + graphics.b_r * 2, graphics.ball.y)
            obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.b_r * 2)
            obj3 = graphics.window.get_object_at(graphics.ball.x + graphics.b_r * 2, graphics.ball.y + graphics.b_r * 2)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                ball_dx = -ball_dx
            elif graphics.ball.y <= 0:
                ball_dy = -ball_dy
            elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                life -= 1
                graphics.time = 0
                graphics.window.remove(graphics.ball)
                graphics.beginning()
                if life == 0 or graphics.score == 100:
                    break
            else:
                if obj is None:
                    if obj1 is None:
                        if obj2 is None:
                            if obj3 is not None:
                                graphics.remove_or_change(obj3)
                                ball_dy = graphics.get_dy()
                        else:
                            graphics.remove_or_change(obj2)
                            ball_dy = graphics.get_dy()
                    else:
                        graphics.remove_or_change(obj1)
                        ball_dy = graphics.get_dy()
                else:
                    graphics.remove_or_change(obj)
                    ball_dy = graphics.get_dy()
            pause(FRAME_RATE)
        if graphics.score == 100:
            break

if __name__ == '__main__':
    main()
