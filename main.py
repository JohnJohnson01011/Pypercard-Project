"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


def lose(app, card):
    if card == "card2":
        return "card3"


cards = [
    Card("start"),
    Card("bombexploding"),
    Card("timerjump"),
    Card("grounded"),
    Card("mad"),
    Card("ok"),
    Card("voltage"),
    Card("parry"),
    Card("lake"),
    Card("cops")
]

# , auto_advance=10, transition="card2"

carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0}, cards=cards
)

@carousel_app.transition("start", "click", "progress")

def reset(app, card):
    return "card3"

def progress(app, card):
    return "parry"


carousel_app.start("start")