from rich.layout import Layout
layout = Layout()
layout.split_column(
    Layout(name="main"),
    Layout(name="lower")
)
layout["main"].split_row(
    Layout(name="options"),
    Layout(name="table"),
)
