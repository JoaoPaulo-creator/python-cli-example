from httpx import post
import typer

app = typer.Typer()


def run_teste():
    request = post("localhost:3000", json={
        "teste": "teste"
    })

    return request


@app.command()
def should_create_proposal(
        approve: bool = False
):
    try:
        if approve:
            run_teste()
    except:
        print("Um erro ocorreu ao tentar rodar a requisicao")


if __name__ == "__main__":
    app()
    #aise SystemExit
