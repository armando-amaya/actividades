import random

categorias = {
    "programacion": ["python", "variable", "funcion", "bucle", "lista"],
    "equipos": ["estudiantes", "boca", "river", "racing", "independiente"],
    "paises": ["argentina", "brasil", "uruguay", "colombia", "chile"]
}


guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

print("Categorías disponibles:")
for categoria in categorias:
    print("-", categoria)

cat_elegida = input("Elegí una categoría: ").lower()

if cat_elegida in categorias:
    words = categorias[cat_elegida]
else:
    print("Categoría no válida. Se usará 'programacion'")
    words = categorias["programacion"]

word = random.choice(words)


while attempts > 0:
    # Mostrar progreso : letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        print(f"Puntaje final: {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if len(letter) == 1 and 'a' <= letter <= 'z':
        if letter in guessed:
            print(f"Ya usaste la letra {letter}. Intenta con otra")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
    else:
        print("Entrada no válida. Ingresa solo una letra (a-z).")

    print()

else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {puntaje}")
