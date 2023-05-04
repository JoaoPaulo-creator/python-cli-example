from httpx import post

from payloads.simulations.create_simulation import new_car


def create_simulation_id() -> str:
    request = post('endpoint', json=new_car)
    response = request.json()
    simulation_id = response['id']
    return str(simulation_id)
