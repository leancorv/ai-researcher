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
    
def score_relevance(topic: str, summary: str) -> dict:
    """
    Le pide al LLM que evalúe la relevancia del resumen.
    Devuelve un dict con score (1-10) y justificación.
    """
    prompt = f"""
    Evaluá la relevancia de este resumen para el tema solicitado.
    
    Tema solicitado: {topic}
    Resumen obtenido: {summary}
    
    Respondé ÚNICAMENTE con este JSON, sin texto adicional, sin backticks:
    {{
        "score": <número del 1 al 10>,
        "reason": "<una oración explicando el score>",
        "is_useful": <true si score >= 7, false si no>
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    import json
    raw = response.choices[0].message.content.strip()
    return json.loads(raw)