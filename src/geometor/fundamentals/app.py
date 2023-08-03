"""
run the main app
"""
from .fundamentals import Fundamentals


def run() -> None:
    reply = Fundamentals().run()
    print(reply)
