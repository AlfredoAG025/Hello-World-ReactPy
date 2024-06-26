from reactpy import component, html

from src.layouts.base import BaseLayout
from src.components.counter import Counter


@component
def CounterPage(title: str):
    return BaseLayout(
        html._(
            html.title(title),
            html.div(
                {
                    "className": "flex flex-col justify-center items-center w-full mt-16"
                },
                html.h1(
                    {
                        "className": 'text-center text-5xl font-bold',
                    },
                    "Counter"
                ),
                Counter(),
            )
        )
    )
