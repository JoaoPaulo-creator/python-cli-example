import click


@click.command()
@click.argument('name')
def create_user(name):
    """Create a new user."""
    click.echo(f"Creating user '{name}'")


@click.command()
@click.argument('surname')
@click.option('--age', type=int)
@click.option('--email', type=str)
def create_another_user(age, email):
    if age is not None:
        click.echo(f"Age: {age}")
    if email is not None:
        click.echo(f"Email: {email}")


if __name__ == '__main__':
    create_user()
    create_another_user()
