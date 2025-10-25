import requests
import random
import html

# Función para obtener preguntas desde la API
def obtener_preguntas(cantidad=5):
    url = f"https://opentdb.com/api.php?amount={cantidad}&type=multiple"
    response = requests.get(url)
    data = response.json()
    preguntas = []

    for item in data['results']:
        pregunta = html.unescape(item['question'])  # Decodifica caracteres HTML
        correcta = html.unescape(item['correct_answer'])
        incorrectas = [html.unescape(ans) for ans in item['incorrect_answers']]
        opciones = incorrectas + [correcta]
        random.shuffle(opciones)
        preguntas.append({
            'pregunta': pregunta,
            'opciones': opciones,
            'correcta': opciones.index(correcta)
        })
    return preguntas


# Función del juego
def juego_trivia():
    preguntas = obtener_preguntas(5)
    score = 0

    for i, q in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {q['pregunta']}")
        for idx, opcion in enumerate(q['opciones']):
            print(f"{idx + 1}. {opcion}")

        while True:
            try:
                eleccion = int(input("Tu respuesta (número): "))
                if 1 <= eleccion <= len(q['opciones']):
                    break
                else:
                    print("Ingresa un número válido.")
            except:
                print("Ingresa un número válido.")

        if eleccion - 1 == q['correcta']:
            print("✅ Correcto!")
            score += 1
        else:
            print(f"❌ Incorrecto! La respuesta correcta era: {q['opciones'][q['correcta']]}")

    print(f"\n🎉 Juego terminado! Tu puntaje: {score}/{len(preguntas)}")


# Ejecutar el juego
if __name__ == "__main__":
    juego_trivia()
