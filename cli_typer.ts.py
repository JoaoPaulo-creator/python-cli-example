import sys
from json import JSONDecodeError

import typer
from httpx import post, get

app = typer.Typer()


@app.command()
def create_user(
        name: str,
        salary: str,
        age: str
):
    endpoint: str = 'https://dummy.restapiexample.com/api/v1/create'
    payload: dict = {"name": f"{name}", "salary": f"{salary}", "age": f"{age}"}
    request = post(endpoint, json=payload).json()
    print(request)


@app.command()
def get_info(_id: str):
    try:
        endpoint: str = f'https://dummy.restapiexample.com/api/v1/employee/{_id}'
        request = get(endpoint, timeout=None)
        print(request)
        request_to_json = request.json()
        print(request_to_json)

    except JSONDecodeError:
        print('Error while requesting employee info')


if __name__ == "__main__":
    app()
    raise SystemExit
