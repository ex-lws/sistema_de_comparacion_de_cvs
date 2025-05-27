#Metodo para realizar la comparacion de los curriculums utilizando openAI

import openai

KeydeChatgpt = "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"
openai.api_key = KeydeChatgpt

def comparar_curriculums(curriculums, perfilEncontrado):
    prompt = (
        "Compara el siguiente perfil con los curriculums del txt y dinos por porcentaje cual es el mas adecuado para el perfil:\n\n"
        "Perfil :\n" + perfilEncontrado + "\n\n"
        "curriculums:\n" + curriculums + "\n\n"
        "Resumen de comparación:"
    )
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en recursos humanos."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()