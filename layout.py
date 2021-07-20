from rich.layout import Layout
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)