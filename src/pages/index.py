from reactpy import component, html

from src.layouts.base import BaseLayout


@component
def IndexPage(title: str):
    return BaseLayout(
        html._(
            html.title(title),
            html.h1(
                {
                    "className": "text-6xl text-center"
                },
                f"Home"
            )
        )
    )
