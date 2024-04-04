import reflex as rx


def blogs_list():
    return rx.vstack(
        rx.link(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "CUDA: Solving Kuramoto oscillators using GPU parallelization",
                        size="8",
                        color_scheme="indigo",
                    ),
                    rx.text("Date: 1 April 2024", color_scheme="gray"),
                    justify="between",
                ),
                variant="classic",
                width="100%",
                padding="10px",
                cursor="pointer",
            ),
            href="/kuramoto-cuda-blog",
            width="100%",
        ),
        width="70%",
        spacing="7",
        margin="40px",
    )
