"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


#def lose(app, card):
#    if card == "card2":
#        return "card3"


cards = [
    Card("start", auto_advance=10, transition="lose"),
    Card("bombexploding", auto_advance=8, transition="lose"),
    Card("timerjump", auto_advance=5, transition="lose"),
    Card("grounded"),
    Card("mad"),
    Card("ok"),
    Card("voltage"),
    Card("parry"),
    Card("lake"),
    Card("cops"),
    Card("lose", auto_advance=3.5, transition="start")
]

# , auto_advance=10, transition="card2" or function name

carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0}, cards=cards
)

#---------------------- Start

@carousel_app.transition("start", "click", "path1")

def path1(app, card):
    return "bombexploding"

@carousel_app.transition("start", "click", "path2")

def path2(app, card):
    return "timerjump"

#---------------------- Path 1

@carousel_app.transition("bombexploding", "click", "parryB")

def parryB(app, card):
    return "parry"

@carousel_app.transition("bombexploding", "click", "lakeB")

def lakeB(app, card):
    return "lake"

@carousel_app.transition("bombexploding", "click", "copsB")

def copsB(app, card):
    return "cops"

#---------------------- Path 2

@carousel_app.transition("timerjump", "click", "madB")

def madB(app, card):
    return "grounded"

@carousel_app.transition("timerjump", "click", "jumpB")

def jumpB(app, card):
    return "start"

@carousel_app.transition("timerjump", "click", "unplugB")

def unplugB(app, card):
    return "mad"

#---------------------- Path 2 End

@carousel_app.transition("mad", "click", "okB")

def okB(app, card):
    return "ok"

@carousel_app.transition("mad", "click", "voltageB")

def voltageB(app, card):
    return "voltage"

@carousel_app.transition("mad", "click", "blue")

def blue(app, card):
    return "bombexploding"

#---------------------- Second jump

@carousel_app.transition("mad", "click", "jumpB")

def jumpB(app, card):
    return "bombexploding"

carousel_app.start("start")