clima = "sol"
dinheiro = 650
lugar = ""



if clima == "sol" and (dinheiro >= 300 and dinheiro <=500):
    lugar = "clube"
else:
    lugar = "cinema"

print(f"Vou ao {lugar}")