import reflex as rx


class Education(rx.State):
    csu_skills = [
        {"name": "Python", "prof": 90},
        {"name": "R", "prof": 70},
        {"name": "Tableau", "prof": 50},
        {"name": "NLP", "prof": 90},
        {"name": "DL", "prof": 75},
    ]

    iit_skills = [
        {"name": "C++", "prof": 80},
        {"name": "MATLAB", "prof": 80},
        {"name": "Python", "prof": 70},
        {"name": "ML", "prof": 50},
    ]

    bit_skills = [
        {"name": "C", "prof": 90},
        {"name": "Java", "prof": 70},
        {"name": "Unix", "prof": 85},
        {"name": "DS/Algo", "prof": 75},
    ]


def education():
    return rx.vstack(
        rx.heading("Education", size="9"),
        rx.hstack(
            rx.vstack(
                rx.heading("MS, Statistics", size="6", color_scheme="indigo"),
                rx.heading(
                    "California State University, East Bay",
                    size="4",
                    color_scheme="gray",
                ),
                # rx.text(
                #     "Relevant Courses: Deep Learning, Statistical Theory, Analysis of Variance Models, Statistical Learning, Natural Language Processing"
                # ),
            ),
            rx.recharts.bar_chart(
                rx.recharts.bar(data_key="prof", fill="#3a5bc7"),
                rx.recharts.x_axis(type_="number"),
                rx.recharts.y_axis(data_key="name", type_="category"),
                data=Education.csu_skills,
                layout="vertical",
                width=600,
                height=300,
            ),
            width="100%",
            justify="between",
        ),
        rx.hstack(
            rx.vstack(
                rx.heading("MS, Physics", size="6", color_scheme="indigo"),
                rx.heading(
                    "Indian Institute of Technology, Indore",
                    size="4",
                    color_scheme="gray",
                ),
                # rx.text(
                #     "Published a paper on machine learning techniques applied to complex system analyses."
                # ),
                # rx.text(
                #     "Relevant Courses: C++, Pattern Recognition, Complex Systems, Machine Learning, Computer Simulations"
                # ),
            ),
            rx.recharts.bar_chart(
                rx.recharts.bar(data_key="prof", fill="#3a5bc7"),
                rx.recharts.x_axis(type_="number"),
                rx.recharts.y_axis(data_key="name", type_="category"),
                data=Education.iit_skills,
                layout="vertical",
                width=600,
                height=300,
            ),
            width="100%",
            justify="between",
        ),
        rx.hstack(
            rx.vstack(
                rx.heading("BS, Physics", size="6", color_scheme="indigo"),
                rx.heading(
                    "Birla Institute of Technology, Mesra",
                    size="4",
                    color_scheme="gray",
                ),
                # rx.text("First Class with Distinction"),
                # rx.text(
                #     "Relevant Courses: Unix and C Programming, Java, Data Structures and Algorithms, CAD, LabVIEW"
                # ),
            ),
            rx.recharts.bar_chart(
                rx.recharts.bar(data_key="prof", fill="#3a5bc7"),
                rx.recharts.x_axis(type_="number"),
                rx.recharts.y_axis(data_key="name", type_="category"),
                data=Education.bit_skills,
                layout="vertical",
                width=600,
                height=300,
            ),
            width="100%",
            justify="between",
        ),
        width="70%",
        spacing="7",
        margin="40px",
    )
