import reflex as rx

from . import about_me, profession, education, projects, footer, blogs_list

from .blogs.reflex_blog import reflex_blog
from .blogs.vitejs_blog import vitejs_blog


class State(rx.State):
    "App State"


@rx.page(route="/", title="Atish Panday")
def index() -> rx.Component:
    return rx.vstack(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("About Me", value="about-me"),
                rx.tabs.trigger("Experience", value="experience"),
                rx.tabs.trigger("Education", value="education"),
                rx.tabs.trigger("Projects", value="projects"),
                rx.tabs.trigger("My Blogs", value="blogs"),
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
            rx.tabs.content(
                rx.center(blogs_list.blogs_list()),
                value="blogs",
            ),
            default_value="about-me",
            width="100%",
        ),
        footer.footer(),
    )


app = rx.App()
app.add_page(index)
app.add_page(reflex_blog)
app.add_page(vitejs_blog)
