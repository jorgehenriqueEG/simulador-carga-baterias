def calcular_autonomia(mah, brilho, gpu_ativa):
    consumo_base = 20.0
    if brilho > 50:
        consumo_base += (brilho - 50) * 0.5
    if gpu_ativa:
        consumo_base += 15.0
    if consumo_base == 0:
        return 0
    return mah / (consumo_base * 60)

mah = 5000
brilho = 80
gpu = True
horas = calcular_autonomia(mah, brilho, gpu)
print(f"Autonomia estimada: {horas:.1f} horas")