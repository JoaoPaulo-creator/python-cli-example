import typer
from typing_extensions import Annotated


def main(
        name: Annotated[str, typer.Option('--name', '-n')],
        formal: bool = False
):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == '__main__':
    typer.run(main)
