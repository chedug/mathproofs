from manim import *




class Markov(Scene):
    def construct(self):
        title_ineq = Text(r"Markov Inequality", color=BLUE, font_size= 76)

        assumptions = Tex(
            r"$X > 0$ nonnegative random variable, with $\mathbb{E}[X] < \inf$ \\"
            r"Then for any $\lambda>0$: \\ "
            )

        markov_ineq = MathTex(r"\mathbb{P}(X>\lambda) \leq \frac{\mathbb{E}(X)}{\lambda}")

        self.play(Write(title_ineq))


        group = VGroup(assumptions,markov_ineq)
        group.arrange(DOWN)
        group.set(width=config["frame_width"] - LARGE_BUFF)

        self.play(title_ineq.animate.next_to(assumptions, UP, buff=0.5))
        self.play(Write(assumptions))
        self.play(Write(markov_ineq))
        self.wait(3)


class MarkovProof(Scene):

    pass
