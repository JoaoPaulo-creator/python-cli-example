import click


@click.group()
def cli():
    """A simple calculator app."""


@click.command()
@click.argument('x', type=float)
@click.argument('y', type=float)
def add(x, y):
    """Add two numbers."""
    click.echo(x + y)


@click.command()
@click.argument('x', type=float)
@click.argument('y', type=float)
def subtract(x, y):
    """Subtract two numbers."""
    click.echo(x - y)


@click.command()
@click.argument('x', type=float)
@click.argument('y', type=float)
def multiply(x, y):
    """Multiply two numbers."""
    click.echo(x * y)


@click.command()
@click.argument('x', type=float)
@click.argument('y', type=float)
def divide(x, y):
    """Divide two numbers."""
    click.echo(x / y)


cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

if __name__ == '__main__':
    cli()
