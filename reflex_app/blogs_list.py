import reflex as rx


def blogs_list() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "CUDA: Solving Kuramoto oscillators using GPU parallelization",
                        size="8",
                        color_scheme="indigo",
                    ),
                    rx.text(
                        "CUDA is a programming model developed by NVIDIA to run code on the GPU, taking advantage of parallelization across GPU cores. I explore how this can be used to solve Kuramoto oscillator equations using GPU parallelization."
                    ),
                    rx.text("Date: 4 April 2024", color_scheme="gray"),
                    justify="between",
                ),
                variant="classic",
                width="100%",
                padding="40px",
                cursor="pointer",
            ),
            href="/kuramoto-cuda-blog",
            width="100%",
            underline="none",
        ),
        width="70%",
        spacing="7",
        margin="40px",
    )
