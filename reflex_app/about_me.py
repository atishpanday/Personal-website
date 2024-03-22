import reflex as rx
from . import summary, skills, interests


def about_me() -> rx.Component:
    return rx.vstack(
        summary.summary(),
        rx.divider(size="4"),
        skills.skills(),
        rx.divider(size="4"),
        interests.interests(),
        width="70%",
        margin="80px",
        spacing="9",
    )
