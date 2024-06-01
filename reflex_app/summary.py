import reflex as rx


def summary() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.code_block(
                "print('Hello World! My name is Atish Panday')",
                language="python",
            ),
            rx.text(
                "Full Stack Engineer | Data Scientist | Physicist",
                size="8",
                weight="bold",
                color_scheme="indigo",
            ),
            rx.box(
                rx.text("A programmer for fun", size="5", weight="bold"),
                bg_color="aqua",
                padding="5px",
                border_radius="5px",
            ),
            rx.text(
                "I am a self taught full stack engineer, with 2+ years of experience arranging bits in just the right order.",
                size="5",
            ),
            rx.text(
                "I graduated from the Indian Institute of Technology, and I have a passion for learning. I want to build things that make an impact on the world.",
                size="5",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("github", size=28, color="#3a5bc7"),
                    href="https://www.github.com/atishpanday",
                ),
                rx.link(
                    rx.icon("linkedin", size=28, color="#3a5bc7"),
                    href="https://www.linkedin.com/in/atishpanday",
                ),
                rx.link(
                    rx.icon("instagram", size=28, color="#3a5bc7"),
                    href="https://www.instagram.com/a.t.i.s.h.p",
                ),
                spacing="4",
            ),
            rx.button(
                "Download Resume",
                on_click=rx.download(
                    url="/Atish_Panday_CV_SDE.pdf", filename="CV_Atish_Panday.pdf"
                ),
                variant="outline",
                size="4",
                color_scheme="indigo",
                cursor="pointer",
            ),
            spacing="4",
        ),
        rx.image(
            src="/linkedin.jpeg",
            width="240px",
            height="auto",
            alt="Me",
            border_radius="120px",
        ),
        width="100%",
        justify="between",
        align="center",
        spacing="9",
    )
