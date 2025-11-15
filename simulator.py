# Simula la MT paso por paso

from tape import Tape

class Simulator:
    def __init__(self, mt):
        self.mt = mt

    # Simula una cadena
    def run(self, input_string):
        tape = Tape(input_string)
        state = self.mt.initial_state
        ids = []  # Guardamos todas las IDs

        # Guardamos la ID inicial
        ids.append(tape.render(state))

        # Ciclo principal
        while True:
            symbol = tape.read()
            tr = self.mt.find_transition(state, symbol)

            if tr is None:
                break

            # Nuevo símbolo
            tape.write(tr["write"][0])

            # Movimiento
            tape.move(tr["move"])

            # Nuevo estado
            state = tr["next"]

            # Guardar ID
            ids.append(tape.render(state))

            # Si llegamos a estado final, fin
            if state in self.mt.accept_states:
                break

        accepted = state in self.mt.accept_states
        return ids, accepted
