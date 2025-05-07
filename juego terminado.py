import time
import random
import os

# Configuración del juego
VIDA_JUGADOR = 100
VIDA_COMPAÑERO = 80
ATAQUE_JUGADOR = 20
ATAQUE_COMPAÑERO = 15
DEFENSA_BASE = 0.5

nivel = 1
jugador_vida = VIDA_JUGADOR
compañero_vida = VIDA_COMPAÑERO

os.system('cls' if os.name == 'nt' else 'clear')
print("⚔️ HEROES DEL TURNO ⚔️")

while jugador_vida > 0 and compañero_vida > 0:
    # Configuración del enemigo para este nivel
    enemigo_nivel = nivel
    enemigo_vida = 40 + (enemigo_nivel * 10)
    enemigo_ataque = 10 + (enemigo_nivel * 2)
    defensa_jugador = 0

    while jugador_vida > 0 and compañero_vida > 0 and enemigo_vida > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Jugador: ❤️{jugador_vida} | Compañero: 🔰{compañero_vida} | Enemigo: 💀{enemigo_vida}")
        print("──────────────────────────────────")

        # MENÚ DE COMBATE
        print("\nACCIONES:")
        print("1) Atacar 🗡️ 2) Defender 🛡️")
        eleccion = ""
        while eleccion not in ['1', '2']:
            eleccion = input("Elección: ").strip()
            if eleccion not in ['1', '2']:
                print("¡Opción inválida! Elige 1 o 2")

        defensa_jugador = 0
        if eleccion == '1':
            danio = ATAQUE_JUGADOR
            enemigo_vida = max(0, enemigo_vida - danio)
            print(f"\n¡Atacas al enemigo! (-{danio}❤️)")
        elif eleccion == '2':
            print("\n🛡️ Te preparas para defender el próximo ataque")
            defensa_jugador = DEFENSA_BASE

        # Turno del compañero
        if compañero_vida > 0:
            accion_compañero = 'atacar' if random.random() < 0.7 else 'defender'
            if accion_compañero == 'atacar':
                danio = ATAQUE_COMPAÑERO
                enemigo_vida = max(0, enemigo_vida - danio)
                print(f"Compañero ataca! (-{danio}❤️)")
            else:
                print("Compañero se defiende 🔰")

        # Turno del enemigo
        accion_enemigo = random.choice(['atacar', 'defender'])
        if accion_enemigo == 'atacar':
            objetivo = random.choice(['jugador', 'compañero'])
            danio = int(enemigo_ataque * (1 - (defensa_jugador if objetivo == 'jugador' else 0)))
            if objetivo == 'jugador':
                jugador_vida = max(0, jugador_vida - danio)
                print(f"\nEl enemigo te ataca! (-{danio}❤️)")
            else:
                compañero_vida = max(0, compañero_vida - danio)
                print(f"\nEl enemigo ataca a tu compañero! (-{danio}🔰)")
        else:
            print("\nEl enemigo se defiende.")

        time.sleep(1.5)

    if jugador_vida > 0 and compañero_vida > 0:
        print(f"\n¡VICTORIA! Nivel {nivel} completado")
        print(f"Vida restante: Jugador {jugador_vida}❤️, Compañero {compañero_vida}🔰")
        nivel += 1
        time.sleep(2)
    else:
        print("\n☠️ HAS SIDO DERROTADO ☠️")
        break
