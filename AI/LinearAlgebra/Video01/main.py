from manim import *
import numpy as np

class HomotopyDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        dot = Dot()

        plane.prepare_for_nonlinear_transform()
        plane.add(dot)

        def homotopy(x, y, z, t):
            norm = np.linalg.norm([x, y])
            tau = interpolate(5, -5, t) + norm / 480
            alpha = sigmoid(tau)
            return [x, y + 0.5 * np.sin(2 * np.pi * alpha), z]

        self.play(
            Homotopy(homotopy, plane, run_time=3)
        )
        self.wait(2)

        self.play(
            plane.animate.apply_matrix([[2, 1], [1, 2]])
        )

        print("the end")

demo = HomotopyDemo()
demo.construct()