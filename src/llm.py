import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    resultado = summarize(
        topic="OpenAI lanza nuevo modelo",
        content="OpenAI anunció hoy GPT-5, con mejoras significativas en razonamiento lógico y capacidad multimodal."
    )
    print(resultado)