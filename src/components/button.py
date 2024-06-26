from reactpy import component, html

# styles = {
#     "button": {
#         "display": "flex",
#         "justify-content": "center",
#         "align-items": "center",
#         "width": "128px",
#         "height": "40px",
#         "border": "none",
#         "border-radius": "20px",
#         "cursor": "pointer",
#         "color": "white",
#         "font-weight": "bold",
#         "font-size": "16px"
#     }
# }


@component
def Button(label: str, color: str, on_click: callable):
    return html._(
        html.button(
            {
                # "style": {
                #     **styles['button'],
                #     "background-color": "#C80036"
                # },
                "className": f"text-xl flex justify-center items-center w-32 h-8 rounded-lg text-white bg-{color}-500 focus:outline-none",
                "on_click": on_click
            },
            label,
        ),
    )
