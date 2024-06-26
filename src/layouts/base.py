from reactpy import component, html
from reactpy_router import link


@component
def BaseLayout(content: component):
    return html._(
        html.link(
            {
                "href": "https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css",
                "rel": "stylesheet",
            }
        ),
        html.ul(
            {
                "className": "flex gap-10 font-bold text-xl border p-4"
            },
            html.li(link("Home", to="/")),
            html.li(link("Counter", to="/counter")),
            html.li(link("Hello World", to="/hello_world")),
        ),
        html.main(
            content,
        )
    )
