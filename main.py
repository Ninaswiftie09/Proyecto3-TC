# Punto de entrada del programa

from parser_mt import load_mt_config
from turing_machine import TuringMachine
from simulator import Simulator

# Elección del archivo YAML
print("Seleccione la Máquina de Turing a ejecutar:")
print("1. MT reconocedora")
print("2. MT alteradora")

op = input("Ingrese 1 o 2: ")

# Archivo elegido
if op == "1":
    yaml_file = "mt_reconocedora.yaml"
elif op == "2":
    yaml_file = "mt_alteradora.yaml"
else:
    print("Opción inválida.")
    exit()

# Cargar configuración
config = load_mt_config(yaml_file)

# Crear MT
mt = TuringMachine(config)

# Crear simulador
sim = Simulator(mt)

# Correr cada input definido en el YAML
for s in config["inputs"]:
    print("\n====================")
    print("Simulando:", s)
    print("====================")

    ids, accepted = sim.run(s)

    # Mostrar IDs paso por paso
    for idx, idd in enumerate(ids):
        print(f"Paso {idx}: {idd}")

    # Resultado final
    if accepted:
        print("Resultado: ACEPTADA")
    else:
        print("Resultado: RECHAZADA")
