import reflex as rx


def blog_layout(child: rx.Component) -> rx.Component:
    return rx.center(
        child,
        width="100%",
    )
