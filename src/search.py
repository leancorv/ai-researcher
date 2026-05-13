import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search(query: str, max_results: int = 5) -> list[dict]:
    """
    Busca en la web y devuelve resultados limpios.
    Cada resultado tiene: title, url, content, score
    """
    response = client.search(
        query=query,
        search_depth="basic",  # "advanced" usa 2 créditos pero es más profundo
        max_results=max_results
    )
    return response["results"]

def format_for_llm(results: list[dict]) -> str:
    """
    Convierte los resultados en texto plano para pasarle a Gemini.
    """
    formatted = []
    for i, r in enumerate(results, 1):
        formatted.append(f"""
[Fuente {i}]: {r['title']}
URL: {r['url']}
Contenido: {r['content']}
""")
    return "\n---\n".join(formatted)

if __name__ == "__main__":
    # Test
    results = search("OpenAI nuevos modelos 2025")
    content = format_for_llm(results)
    print(content)