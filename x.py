from typing import TypedDict

class X(TypedDict):
    x: str

Y = TypedDict("Y", { "y": str })

def _(x: X):
    reveal_type(x)
    reveal_type(x["x"])

def _(y: Y):
    reveal_type(y["y"])
