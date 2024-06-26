from reactpy import component
from reactpy.backend.fastapi import configure

from reactpy_router import route, simple

from fastapi import FastAPI

from src.pages.counter import CounterPage
from src.pages.index import IndexPage
from src.pages.hello_world import HelloWorldPage


@component
def root():
    return simple.router(
        route('/', IndexPage(title="Home")),
        route('/counter', CounterPage(title="Counter")),
        route('/hello_world', HelloWorldPage(title="Hello World!"),
        ),
    )


app = FastAPI()
configure(app, root)
