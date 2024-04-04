import reflex as rx

wisestep_skills: list[str] = [
    "Java",
    "TypeScript",
    "React.js",
    "Spring Boot",
    "Spring MVC",
    "PostgreSQL",
    "Elasticsearch",
    "Kafka",
    "Docker",
    "Linux",
    "Mockito",
    "Redux",
    "AWS",
]

daffodil_skills: list[str] = [
    "Typescript",
    "Javascript",
    "Java",
    "React.js",
    "React Native",
    "Ionic",
    "Capacitor",
    "Node.js",
    "Express.js",
    "Spring Boot",
    "Google App Engine",
    "AWS",
    "PostgreSQL",
]


def skill_badge(skill: str) -> rx.Component:
    return rx.badge(skill, size="2", color_scheme="indigo")


def profession() -> rx.Component:
    return rx.vstack(
        rx.heading("Experience", size="9"),
        rx.hstack(
            rx.vstack(
                rx.text("August 2022", weight="bold"),
                rx.divider(orientation="vertical", size="4"),
                rx.text("October 2021", weight="bold"),
                height="100%",
                justify="between",
                align="end",
                flex=1,
            ),
            # rx.divider(orientation="vertical", size="4"),
            rx.vstack(
                rx.heading("Full Stack Engineer", size="6", color_scheme="indigo"),
                rx.heading("Wisestep", size="4", color_scheme="gray"),
                rx.text(
                    "Implemented test-driven development for microservices APIs using JUnit, Mockito."
                ),
                rx.text(
                    "Developed communication APIs such as emailing, SMS as well as calling services, using Twilio, Java and Spring Boot."
                ),
                rx.text(
                    "Spearheaded the migration of legacy front-end code to React.js, developing highly robust and adaptive components, boosting website performance."
                ),
                rx.text(
                    "Ensured consistent and high-quality user experience in collaboration with UI/UX designers."
                ),
                rx.text(
                    "Developed modular and intuitive user interfaces, aligning with the evolution of the Design System for efficient web application development."
                ),
                rx.hstack(rx.foreach(wisestep_skills, skill_badge), wrap="wrap"),
                flex=3,
            ),
            spacing="6",
        ),
        rx.hstack(
            rx.vstack(
                rx.text("October 2021", weight="bold"),
                rx.divider(orientation="vertical", size="4"),
                rx.text("October 2020", weight="bold"),
                height="100%",
                justify="between",
                align="end",
                flex=1,
            ),
            # rx.divider(orientation="vertical", size="4"),
            rx.vstack(
                rx.heading(
                    "Full Stack Engineer (Lead)", size="6", color_scheme="indigo"
                ),
                rx.heading("Daffodil Health", size="4", color_scheme="gray"),
                rx.text(
                    "Developed and led a team of 5 developers in the successful creation and launch of a front-end mobile app using React Native, Ionic React, and Capacitor."
                ),
                rx.text(
                    "Implemented high-performant back-end code using Node.js, ensuring a RESTful design, authenticationa and authorization, error handling, performance optimizationa and testing."
                ),
                rx.text(
                    "Designed an efficient database architecture using PostgreSQL that allowed for seamless data storage and retrieval, reducing query response time and improving overall app performance."
                ),
                rx.hstack(rx.foreach(daffodil_skills, skill_badge), wrap="wrap"),
                flex=3,
            ),
            spacing="6",
        ),
        height="120vh",
        width="70%",
        margin="40px",
        spacing="7",
    )
