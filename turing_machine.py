# Guarda la definición formal de la MT

class TuringMachine:
    def __init__(self, config):
        self.states = config["states"]
        self.input_alphabet = config["input_alphabet"]
        self.tape_alphabet = config["tape_alphabet"]
        self.initial_state = config["initial_state"]
        self.accept_states = config["accept_states"]
        self.transitions = config["transitions"]

    # Busca la transición que coincida
    def find_transition(self, state, symbol):
        for t in self.transitions:
            if t["state"] == state and t["read"][0] == symbol:
                return t
        return None
