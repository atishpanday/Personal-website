import reflex as rx

from . import about_me, profession, education, projects, footer


class State(rx.State):
    "App State"


def index() -> rx.Component:
    return rx.vstack(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("About Me", value="about-me"),
                rx.tabs.trigger("Experience", value="experience"),
                rx.tabs.trigger("Education", value="education"),
                rx.tabs.trigger("Projects", value="projects"),
            ),
            rx.tabs.content(
                rx.center(about_me.about_me()),
                value="about-me",
            ),
            rx.tabs.content(
                rx.center(profession.profession()),
                value="experience",
            ),
            rx.tabs.content(
                rx.center(education.education()),
                value="education",
            ),
            rx.tabs.content(
                rx.center(projects.projects()),
                value="projects",
            ),
            default_value="about-me",
            width="100%",
        ),
        footer.footer(),
    )


app = rx.App()
app.add_page(index)
