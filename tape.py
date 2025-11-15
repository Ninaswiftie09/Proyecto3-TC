# Manejo de la cinta de la MT

class Tape:
    def __init__(self, input_string):
        # Convertimos string en lista para poder mutarla
        self.tape = list(input_string)
        self.head = 0  # Apunta al primer símbolo
        self.blank = "B"

    # Lee símbolo bajo el cabezal
    def read(self):
        if self.head < 0:
            return self.blank
        if self.head >= len(self.tape):
            return self.blank
        return self.tape[self.head]

    # Escribe en la posición del cabezal
    def write(self, symbol):
        if self.head < 0:
            # Extender cinta a la izquierda
            self.tape.insert(0, symbol)
            self.head = 0
        elif self.head >= len(self.tape):
            # Extender a la derecha
            self.tape.append(symbol)
        else:
            self.tape[self.head] = symbol

    # Mover el cabezal
    def move(self, direction):
        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head -= 1

    # Mostrar la cinta en formato bonito para las ID
    def render(self, state):
        s = ""
        for i, c in enumerate(self.tape):
            if i == self.head:
                s += f"{state}({c})"
            else:
                s += c
        return s
