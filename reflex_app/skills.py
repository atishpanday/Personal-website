import reflex as rx

programming_languages: list[dict] = [
    {"lang": "C++", "prof": 75, "total": 100},
    {"lang": "C", "prof": 85, "total": 100},
    {"lang": "Python", "prof": 95, "total": 100},
    {"lang": "Javascript", "prof": 90, "total": 100},
    {"lang": "Java", "prof": 60, "total": 100},
]

technologies: list[dict] = [
    {"tech": "React.js", "prof": 95},
    {"tech": "Angular.js", "prof": 60},
    {"tech": "Node.js", "prof": 85},
    {"tech": "Flask", "prof": 90},
    {"tech": "Spring Boot", "prof": 70},
    {"tech": "SQL", "prof": 75},
]


def skills() -> rx.Component:
    return rx.vstack(
        rx.heading("Skills", size="9"),
        programming_skills(),
        framework_skills(),
        common_skills(),
        width="100%",
        spacing="8",
    )


def programming_skills() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("My journey in programming...", size="7", color_scheme="indigo"),
            rx.text(
                "C++, the first programming language I was formally introduced to, became easily one of my favorite languages. I loved the 'low-levelness', the abstraction, the object-oriented attributes of the language."
            ),
            rx.text(
                "Soon enough, I learnt C and Java as part of my curriculum at BIT, and found myself being able to grasp them very easily, thanks to my strong foundation in algorithms and data structures."
            ),
            rx.text(
                "As I completed my undergraduate studies, I was well versed with C/C++ and Java. I went on to learn Python as a way to understand machine learning and artifical intelligence in IIT. I was blown by the simplicity and flexibility of Python. I was hooked."
            ),
            rx.text(
                "After I finished college, I started working as a full stack engineer at a start-up company named 'Daffodil Health'. I was the first engineer at the company and learnt Javascript/Typescript as well as React/Node."
            ),
            flex=1,
        ),
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="prof",
                fill="#3a5bc7",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="lang"),
            data=programming_languages,
            height=400,
            width=400,
        ),
        direction="row-reverse",
        spacing="9",
    )


def framework_skills() -> rx.Component:
    return rx.vstack(
        rx.heading("Technologies in my arsenal...", size="7", color_scheme="indigo"),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key="prof",
                fill="#3a5bc7",
            ),
            rx.recharts.x_axis(data_key="tech", type_="category"),
            rx.recharts.y_axis(type_="number"),
            data=technologies,
            width="100%",
            height=400,
        ),
        width="100%",
        spacing="7",
    )


def common_skills() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Of course, everyone must know these...", size="7", color_scheme="indigo"
        ),
        rx.hstack(
            rx.card(
                rx.image(src="/html_css_logo.jpg", height=100, width="auto"),
            ),
            rx.card(
                rx.image(src="/git_logo.jpg", height=100, width="auto"),
            ),
            rx.card(
                rx.image(src="/aws_logo.jpg", height=100, width="auto"),
            ),
            rx.card(
                rx.image(src="/bash_logo.jpg", height=100, width="auto"),
            ),
            rx.card(
                rx.image(src="/linux_logo.jpg", height=100, width="auto"),
            ),
            align="center",
            wrap="wrap",
        ),
        width="100%",
        spacing="7",
    )
