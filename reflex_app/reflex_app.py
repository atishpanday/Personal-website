import reflex as rx


class State(rx.State):
    "App State"


def index() -> rx.Component:
    return rx.center(
        rx.vstack(summary(), profession(), education(), margin="120px", spacing="6")
    )


def summary() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("About me", size="9"),
            rx.hstack(
                rx.text(
                    "I am a dynamic professional pursuing an MS in Statistics - Data Science at California State University, East Bay, blending a robust physics foundation from the Indian Institute of Technology with hands-on experience as a Full Stack Engineer at Wisestep and Lead Full Stack Engineer at Daffodil Health. With expertise in JavaScript, Typescript, Java, and Python, I drive innovation in web development and data science. My academic involvement includes tutoring and diverse projects like Codenames and graph classification using CNN, reflecting my commitment to impactful solutions. Eager for full-time roles, I bring a unique skill set, from test-driven development to high-performance back-end coding and research in parallel computing, all fueled by a passion for innovation and continuous learning.",
                ),
                rx.image(
                    src="/atish.png",
                    width="300px",
                    height="auto",
                    alt="Me",
                    border_radius="10px",
                ),
            ),
        ),
    )


def profession() -> rx.Component:
    return rx.vstack(
        rx.heading("Career", size="9"),
        rx.heading("Full Stack Engineer", size="6"),
        rx.heading("Wisestep", size="4", color_scheme="gray"),
        rx.text(
            "Implemented test-driven development for microservices APIs, enhancing efficiency by 20\%\ and reducing API errors by 15%."
        ),
        rx.text(
            "Spearheaded the migration of legacy front-end code to React.js, boosting website performance and increasing user engagement by 30\%\."
        ),
        rx.text(
            "Ensured consistent and high-quality user experience in collaboration with UI/UX designers, resulting in a 25\%\ decrease in user complaints and a 15\%\ increase in customer satisfaction."
        ),
        rx.text(
            "Developed modular and intuitive user interfaces, aligning with the evolution of the Design System for efficient web application development."
        ),
        rx.text(
            "Translated product design and wireframes into code, emphasizing performance and usability while contributing to the foundational blocks of the Design System."
        ),
        rx.heading("Full Stack Engineer (Lead)", size="6"),
        rx.heading("Daffodil Health", size="4", color_scheme="gray"),
        rx.text(
            "Developed and led a team of 5 developers in the successful creation and launch of a front-end mobile app using React Native, Ionic React, and Capacitor, resulting in a 30% increase in user engagement within the first month."
        ),
        rx.text(
            "Implemented high-performance back-end code using Node.js, resulting in an average response time of less than 100 milliseconds and handling over 10,000 concurrent requests per minute."
        ),
        rx.text(
            "Designed an efficient database architecture using PostgreSQL that allowed for seamless data storage and retrieval, reducing query response time by 50% and improving overall app performance."
        ),
    )


def education() -> rx.Component:
    return rx.vstack(
        rx.heading("Education", size="9"),
        rx.heading("MS, Statistics", size="6"),
        rx.heading(
            "California State University, East Bay", size="4", color_scheme="gray"
        ),
        rx.text(
            "Relevant Courses: Deep Learning, Statistical Theory, Analysis of Variance Models, Statistical Learning, Natural Language Processing"
        ),
        rx.heading("MS, Physics", size="6"),
        rx.heading(
            "Indian Institute of Technology, Indore", size="4", color_scheme="gray"
        ),
        rx.text(
            "Published a paper on machine learning techniques applied to complex system analyses."
        ),
        rx.text(
            "Relevant Courses: C++, Pattern Recognition, Complex Systems, Machine Learning, Computer Simulations"
        ),
        rx.heading("BS, Physics", size="6"),
        rx.heading(
            "Birla Institute of Technology, Mesra", size="4", color_scheme="gray"
        ),
        rx.text("First Class with Distinction"),
        rx.text(
            "Relevant Courses: Unix and C Programming, Java, Data Structures and Algorithms, CAD, LabVIEW"
        ),
    )


app = rx.App()
app.add_page(index)
