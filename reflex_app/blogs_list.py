import reflex as rx


def blogs_list():
    return rx.vstack(
        rx.link(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Reflex: A pure python based web framework",
                        size="8",
                        color_scheme="indigo",
                    ),
                    rx.text("Date: 29 March 2024", color_scheme="gray"),
                    justify="between",
                ),
                variant="classic",
                width="100%",
                padding="10px",
                cursor="pointer",
            ),
            href="/reflex-blog",
            width="100%",
        ),
        rx.link(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Vitejs: Fastest build tool for your frontend frameworks",
                        size="8",
                        color_scheme="indigo",
                    ),
                    rx.text("Date: 29 March 2024", color_scheme="gray"),
                    justify="between",
                ),
                variant="classic",
                width="100%",
                padding="10px",
                cursor="pointer",
            ),
            href="/vitejs-blog",
            width="100%",
        ),
        width="70%",
        spacing="7",
        margin="40px",
    )
