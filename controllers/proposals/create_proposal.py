from httpx import post

from payloads.proposals.proposal import set_simulation_id


def create_proposal(simulation_id) -> str:
    request = post('endpoint', json=set_simulation_id(simulation_id))
    response = request.json()
    proposal_id = response['id']
    return str(proposal_id)
