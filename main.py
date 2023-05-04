import typer
from typing_extensions import Annotated

from controllers.proposals.create_proposal import create_proposal
from controllers.simulations.create_simulation_controller import create_simulation_id

app = typer.Typer()


@app.command()
def should_create_proposal(
        car: Annotated[str, typer.Option('--car', '-c')],
        approve: bool = False
):
    simulation_id = create_simulation_id()
    proposal = create_proposal(simulation_id)
    proposal_id = proposal
    print(f'Proposal created: {proposal_id}')

    if approve:
        'approve proposal analysis'


if __name__ == "__main__":
    app()
    raise SystemExit
