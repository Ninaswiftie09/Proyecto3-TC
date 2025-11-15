# Lee y valida el YAML de la MT

import yaml

def load_mt_config(path):
    # Abre archivo YAML
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    mt = data["mt"]

    # Estructura que regresamos
    config = {
        "states": mt["states"],
        "input_alphabet": mt["input_alphabet"],
        "tape_alphabet": mt["tape_alphabet"],
        "initial_state": mt["initial_state"],
        "accept_states": mt["accept_states"],
        "transitions": mt["transitions"],
        "inputs": mt["inputs"]
    }

    return config
