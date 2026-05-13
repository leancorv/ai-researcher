import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize(topic: str, content: str) -> str:
    prompt = f"""
    Sos un analista de inteligencia de mercado.
    Tema: {topic}
    Contenido a analizar:
    {content}

    Generá un resumen estructurado en español con:
    - 3 puntos clave
    - 1 insight accionable
    Sé conciso y directo.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # gratis y muy capaz
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    resultado = summarize(
        topic="OpenAI lanza nuevo modelo",
        content="OpenAI anunció GPT-5 con mejoras en razonamiento lógico y capacidad multimodal."
    )
    print(resultado)