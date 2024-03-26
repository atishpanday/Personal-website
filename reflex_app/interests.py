import reflex as rx


fizz_buzz_code = """def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print('\n'.join(fizz_buzz(100)))"""


def interests() -> rx.Component:
    return rx.vstack(
        rx.heading("My Interests", size="9"),
        leetcode(),
        public_speaking(),
        guitar(),
        art(),
        other_interests(),
        width="100%",
        spacing="8",
    )


def leetcode() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.code_block(fizz_buzz_code, language="python", show_line_numbers=True),
            flex=1,
        ),
        rx.vstack(
            rx.heading("Leetcode", size="7", color_scheme="indigo"),
            rx.text(
                "I love puzzles, and what better way to challenge myself than to solve programming puzzles?"
            ),
            rx.text(
                "It's like diving into a fun maze where I get to figure out how to make things work."
            ),
            rx.text(
                "What's even better is finding simple solutions to tricky problems—it's like unlocking a whole new level of satisfaction!"
            ),
            rx.text(
                "Each puzzle solved is a little victory that keeps me motivated to tackle even more challenges and learn along the way."
            ),
            flex=1,
        ),
        spacing="6",
    )


def public_speaking() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("Public Speaking", size="7", color_scheme="indigo"),
            rx.text(
                "Stage freight? Yes. But do I still love it? Yes! It's a challege, and I love challenges, remember?"
            ),
            rx.text(
                "I was very young when I first anchored an event at school, and loved it. I haven't pursued it any further, but I would very much love to."
            ),
            flex=1,
        ),
        rx.box(
            rx.image(
                src="/public_speaking.jpg",
                width="100%",
                height="auto",
                border_radius="10px",
            ),
            flex=1,
        ),
        spacing="6",
    )


def guitar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(
                src="/guitar.jpg",
                width="100%",
                height="auto",
                border_radius="10px",
            ),
            flex=1,
        ),
        rx.vstack(
            rx.heading("Guitar", size="7", color_scheme="indigo"),
            rx.text(
                "Nothing better than playing the guitar to yourself and letting your thoughts flow along your own music."
            ),
            flex=1,
        ),
        spacing="6",
    )


def art() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("Art", size="7", color_scheme="indigo"),
            rx.text("Probably the first thing I ever learnt was how to draw."),
            rx.text(
                "I owe all my creativity to my time spent sketching, painting, and just generally throwing colors around on a piece of paper as a child."
            ),
            rx.text("To the right is just one of many of my works."),
            flex=1,
        ),
        rx.box(
            rx.image(
                src="/art.jpg",
                width="100%",
                height="auto",
                border_radius="10px",
            ),
            flex=1,
        ),
    )


def other_interests() -> rx.Component:
    return rx.vstack(
        rx.heading("Other Interests", size="7", color_scheme="indigo"),
        rx.hstack(
            rx.card(
                rx.image(src="/football.jpg", height=120, width="auto"),
            ),
            rx.card(
                rx.image(src="/table_tennis.jpg", height=120, width="auto"),
            ),
            rx.card(
                rx.image(src="/swimming.jpg", height=120, width="auto"),
            ),
            rx.card(
                rx.image(src="/fifa.jpg", height=120, width="auto"),
            ),
            width="100%",
            wrap="wrap",
            justify="between",
        ),
        width="100%",
    )
