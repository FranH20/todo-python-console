from typing import List
from rich.console import Console, OverflowMethod

console = Console(width=20)
blue_console = Console(style="white on blue")
supercali = "supercalifragilisticexpialidocious"
overflow_methods: List[OverflowMethod] = ["fold", "crop", "ellipsis"]

def run():
    console.print([1, 2, 3])
    console.print("[blue underline]Looks like a link")
    console.print(locals())
    console.print("FOO", style="white on blue")
    console.log("Hello, World!")
    console.out("Locals", locals())
    console.rule("[bold red]Chapter 2")
    style = "bold white on blue"
    console.print("Rich", style=style)
    console.print("Rich", style=style, justify="left")
    console.print("Rich", style=style, justify="center")
    console.print("Rich", style=style, justify="right")
    for overflow in overflow_methods:
        console.rule(overflow)
        console.print(supercali, overflow=overflow, style="bold blue")
        console.print()
    blue_console.print("I'm blue. Da ba dee da ba di.")



if __name__ == "__main__":
    run()