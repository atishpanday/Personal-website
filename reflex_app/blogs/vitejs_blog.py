import reflex as rx
from .blog_layout import blog_layout


@rx.page(route="/vitejs-blog")
def vitejs_blog() -> rx.Component:
    return blog_layout(
        rx.vstack(
            rx.heading(
                "Vitejs: The fastest build tool for frontend frameworks",
                size="8",
                color_scheme="indigo",
            ),
            rx.text("Frontend developers, did you put React.js in your resume?"),
            rx.text("If you did, you probably have it mastered too, right? …right?"),
            rx.text(
                "Well sure, a lot of us developers simply put a framework as a skill in our resumes after writing one or two basic applications using said framework. This is all fine and well if that's not the focus of your intended job title. If not, maybe you’d like to really understand the framework that you boast about in your CV."
            ),
            rx.text(
                "So, here it is, a small but important piece of knowledge of the React framework for frontend development."
            ),
            rx.text(
                "React uses Webpack out of the box for ‘transforming its code into whatever the browser can understand’. Meaning, it uses a tool called Webpack that bundles, transforms, and performs build, static analysis and code splitting of your source code, before sending it to the browser to render stuff on your screen. This can become a tedious process as the size of your application grows."
            ),
            rx.text(
                "What’s better? Vite.js. Pronounced veet (French for quick), Vite is a build tool that utilizes the native ESM support of modern browsers to send individual JavaScript modules to the browser, eliminating the need for bundling the entire code. Meaning? Most modern browsers now support ES modules natively, which means they do part of the job of the traditional bundlers like Webpack. Vite takes advantage of this feature and runs your code in the development server much faster than others."
            ),
            rx.text(
                "On top of that, Vite uses esbuild, another build tool written in Go, to pre-bundle the dependencies 10-100x faster than other JavaScript based bundlers."
            ),
            rx.text(
                "So, perhaps next time you want to start writing your web app, consider using Vite.js as your build tool. I doubt you’ll be disappointed."
            ),
            width="70%",
            margin="40px",
            spacing="7",
        ),
    )
