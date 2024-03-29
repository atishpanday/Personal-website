import reflex as rx
from .blog_layout import blog_layout


@rx.page(route="/reflex-blog")
def reflex_blog():
    return blog_layout(
        rx.vstack(
            rx.heading(
                "Reflex: A pure python based web framework",
                size="8",
                color_scheme="indigo",
            ),
            rx.text(
                "As a full stack engineer, I love React, and all the capabilities it brings to the table. However, with all its glory, it is ultimately a javascript framework. And javascript, no matter how good, can be difficult to work with at times."
            ),
            rx.text(
                "How good would it be if there was an alternative to javascript for writing front-end code? The answer - Reflex - a pure python framework to write front-end code."
            ),
            rx.text(
                "I had to try it. And I did. And here I am, writing an appreciation post about it. I built my website (https://lnkd.in/gyQqd-5K) in pure python. What's more, I was able to deploy it with a single command on the terminal."
            ),
            rx.text(
                "I would definitely recommend python programmers or anyone hesitating to learn javascript, to try Reflex."
            ),
            width="70%",
            margin="40px",
            spacing="7",
        ),
    )
