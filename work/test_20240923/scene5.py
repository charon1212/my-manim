from manim import *


class ShowVariousObjects(ThreeDScene):
    def construct(self):
        self.showTitle("Shapes")
        self.showObjectAndFadeOut("1. circle", Circle())
        self.showObjectAndFadeOut("2. square", Square())
        self.showObjectAndFadeOut("3. rectangle", Rectangle())
        self.showObjectAndFadeOut("4. triangle", Triangle())
        self.showObjectAndFadeOut("5. polygon", self.getHexagon())

        self.showTitle("Text")
        self.showObjectAndFadeOut("5. text", Text("text"))
        self.showObjectAndFadeOut("6. mathtex", MathTex("x^2 + y^2 = 1"))
        self.showObjectAndFadeOut("7. tex", Tex("quadratic function $y = x^2$"))

        self.showTitle("Graphs")
        self.showObjectAndFadeOut("8. axes", Axes())
        self.showObjectAndFadeOut("9. numberPlane", NumberPlane())
        self.showObjectAndFadeOut("10. graph", self.getGraph())

        self.showTitle("Lines")
        self.showObjectAndFadeOut("11. line", Line())
        self.showObjectAndFadeOut("12. dashedLine", DashedLine())
        self.showObjectAndFadeOut("13. arrow", Arrow())
        self.showObjectAndFadeOut("14. doubleArrow", DoubleArrow())
        self.showObjectAndFadeOut("15. curvedArrow", self.getCurvedArrow())

        self.showTitle("3D Objects")
        self.showObjectAndFadeOut("16. sphere", Sphere(), is3d=True)
        self.showObjectAndFadeOut("17. cube", Cube(), is3d=True)
        self.showObjectAndFadeOut("18. cone", Cone(), is3d=True)
        self.showObjectAndFadeOut("19. cylinder", Cylinder(), is3d=True)

    def showObjectAndFadeOut(self, title, obj, is3d=False):
        """
        Displays an object with a title, then fades it out.

        Parameters:
        title (str): The title text to display.
        obj (Mobject): The object to be displayed and faded out.
        is3d (bool, optional): If True, sets the camera orientation for 3D objects. Defaults to False.

        Returns:
        None
        """
        title_text = Text(title)
        title_text.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title_text)
        if is3d:
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(obj))
        self.wait(1)
        self.play(FadeOut(obj))
        self.remove(title_text)
        if is3d:
            self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

    def showTitle(self, title):
        title = Text(title)
        self.play(Create(title))
        self.wait(1)
        self.play(FadeOut(title))

    def getHexagon(self):
        return Polygon(
            [1, 0, 0],
            [0.5, 0.866, 0],
            [-0.5, 0.866, 0],
            [-1, 0, 0],
            [-0.5, -0.866, 0],
            [0.5, -0.866, 0],
        )

    def getGraph(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        return Graph(vertices, edges)

    def getCurvedArrow(self):
        start_point = [1, 0, 0]
        end_point = [-1, 0, 0]
        return CurvedArrow(start_point, end_point, angle=TAU / 4)
