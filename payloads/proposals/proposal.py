def set_simulation_id(simulation_id: str) -> dict[str, str]:
    return {
        'simulationId': simulation_id,
        'aksdjkas': 'manual_release'
    }


# example
a = 'simulation_id_test'
s = set_simulation_id(a)
print(s['simulationId'])
