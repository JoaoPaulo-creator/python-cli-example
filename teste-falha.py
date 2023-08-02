import traceback

from httpx import post, get
import typer
import rich

app = typer.Typer()


def run_teste():
    t = get("https://cep.awesomeapi.com.br/json/80010012").json()
    # try:
    # except Exception:
    #     with open("error.txt", 'w') as file:
    #         traceback_str = traceback.format_exc()
    #         file.write(f'{traceback_str}')
    #         file.close()
    #
    #     read_error_instruction = 'Execute o comando cat error.txt (mac e linux) ou more error.txt (windows)'
    #
    #     rich.print({
    #         "message": f"Um erro ocorreu ao tentar rodar a requisicao. {read_error_instruction}"
    #     })
    #
    return t

@app.command()
def should_create_proposal(
        approve: bool = False
):
    if approve:
        rich.print(run_teste())


if __name__ == "__main__":
    app()
    # aise SystemExit
