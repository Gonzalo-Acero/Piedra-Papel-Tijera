import random

def jugar():
    usuario = input("Decida su jugada: 'piedra' para PIEDRA, 'papel' para PAPEL o 'tijera' para TIJERA.\n").lower()
    computadora = random.choice(['piedra', 'papel', 'tijera'])
    
    
    if usuario == computadora:
        return '¡Empate!'
    
    
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'


    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    # Retornar True si gana el jugador.
    # Piedra gana a Tijera
    # Tijera gana a Papel
    # Papel gana a Piedra
    
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False 
    
    
print(jugar())