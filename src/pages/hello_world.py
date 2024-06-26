from reactpy import component, html, use_state
from reactpy_router.core import use_query
from reactpy_router import link

from src.layouts.base import BaseLayout


@component
def HelloWorldPage(title: str):
    name, set_name = use_state('')
    name_query = use_query().get('name', '')

    if len(name_query):
        name_query = name_query[0]
    else:
        name_query = 'World'

    return BaseLayout(
        html._(
            html.title(title),
            html.h1(
                {
                    "className": "text-6xl text-center"
                },
                f"Hello {name_query}!"
            ),
            html.input({
                'className': 'border',
                'value': name,
                'onChange': lambda e: set_name(e['target']['value'])
            },
            ),
            link(
                f'Hello World to your name',
                to=f'/hello_world?name={name}'
            ),
        )
    )
