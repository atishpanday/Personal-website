import reflex as rx


def projects():
    return rx.vstack(
        rx.heading("Projects", size="9"),
        rx.grid(
            rx.card(
                rx.heading("Codenames App", size="7", color_scheme="indigo"),
                rx.image(src="/codenames.jpg", width="100%", height="auto"),
                rx.text(
                    "Implemented the famous board game Codenames on a web app using React.js, MUI, and Flask."
                ),
                rx.text(
                    "Used NLP and DETECT (Ref.) algorithms to generate clues for the words used in Codenames."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Codenames",
                ),
                variant="classic",
            ),
            rx.card(
                rx.heading("2048 Game", size="7", color_scheme="indigo"),
                rx.image(src="/2048game.jpg", width="100%", height="auto"),
                rx.text(
                    "Implemented the popular 2048 game on the web using React.js and transitions with react-spring."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Two-zero-four-eight",
                ),
                variant="classic",
            ),
            rx.card(
                rx.heading("Kuramoto Model in CUDA", size="7", color_scheme="indigo"),
                rx.image(src="/kuramoto.jpg", width="100%", height="auto"),
                rx.text(
                    "Implemented CUDA parallel computing for Kuramoto oscillator equations, enhancing accuracy with a 4th-order Runge-Kutta method and achieving a 1000\%\ speed increase for large networks."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Kuramoto-Oscillators",
                ),
                variant="classic",
            ),
            rx.card(
                rx.heading(
                    "Graph Classification using CNN", size="7", color_scheme="indigo"
                ),
                rx.image(src="/graph_classification.jpg", width="100%", height="auto"),
                rx.text(
                    "Efficiently classified diverse graph types using Convolutional Neural Networks (CNN), analyzed time-series data from the Kuramoto Model with MATLAB, and conducted high-performance network simulations in C++."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Machine-learning-assisted-graph-classification",
                ),
                variant="classic",
            ),
            rx.card(
                rx.heading("Twitter Data Analysis", size="7", color_scheme="indigo"),
                rx.image(src="/twitter_data.jpg", width="100%", height="auto"),
                rx.text(
                    "Analyzed millions of tweets, created a network using tweet mentions, and identified a 20% spread of Covid-19-related rumors in the Twitter network."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Twitter-Data-Analysis",
                ),
                variant="classic",
            ),
            rx.card(
                rx.heading(
                    "Equivalent Resistance Calculator", size="7", color_scheme="indigo"
                ),
                rx.image(src="/equivalent_resistance.jpg", width="100%", height="auto"),
                rx.text(
                    "Developed a C++ program employing nodal analysis to determine the equivalent resistance between two junctions, calculate potentials at each junction, and ascertain the current flow through all the wires."
                ),
                rx.link(
                    "Link to the code",
                    href="https://www.github.com/atishpanday/Resistance-calculator",
                ),
                variant="classic",
            ),
            columns="2",
            spacing="4",
        ),
        width="70%",
        margin_y="40px",
        spacing="7",
    )
