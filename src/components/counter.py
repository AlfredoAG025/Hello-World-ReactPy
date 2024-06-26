from reactpy import component, html, use_state

from src.components.button import Button

# styles = {
#     "counter": {
#         "height": "100vh",
#         "font-size": "32px",
#         "display": "flex",
#         "justify-content": "center",
#         "align-items": "center",
#         "gap": "20px",
#         "font-weight": "bold"
#     },
# }


@component
def Counter():
    counter, set_counter = use_state(0)

    def increase_by(value):
        set_counter(counter + value)

    return html.div(
        {
            # "style": styles['counter'],
            "className": "flex text-5xl font-bold justify-center items-center gap-10"
        },
        Button(label="-", color="red", on_click=lambda e: increase_by(-1)),
        html.h2(counter),
        Button(label="+", color="blue", on_click=lambda e: increase_by(+1)),
    )
