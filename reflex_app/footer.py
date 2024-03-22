import reflex as rx


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Wanna chat?", size="9", color="white"),
            rx.text(
                "Interested in working together or discussing ideas? Shoot me a text and let's make it happen!",
                size="7",
                weight="light",
                color="white",
                align="center",
            ),
            rx.hstack(
                rx.link(rx.icon("phone", color="white"), href="tel:+14153423952"),
                rx.link(
                    rx.icon("mail", color="white"), href="mailto:atishpanday1@gmail.com"
                ),
                rx.link(
                    rx.icon("linkedin", color="white"),
                    href="https://www.linkedin.com/in/atishpanday",
                ),
                rx.link(
                    rx.icon("instagram", color="white"),
                    href="https://www.instagram.com/a.t.i.s.h.p",
                ),
                width="20%",
                justify="between",
            ),
            width="50%",
            spacing="9",
            align="center",
        ),
        bg_color="#3a5bc7",
        height="60vh",
        width="100%",
        margin_top="100px",
    )
