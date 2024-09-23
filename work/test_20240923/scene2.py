from manim import *

# <https://docs.manim.community/en/stable/tutorials/quickstart.html#transforming-a-square-into-a-circle>
class CreateCircle(Scene):
    def construct(self):

        # create a square
        square = Square()
        square.rotate(PI / 4)  # rotate the square
        self.play(Create(square))  # show the square on screen

        # transform to circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Transform(square, circle))

        # fade out
        self.play(FadeOut(square))

