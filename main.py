from src.search import search, format_for_llm
from src.llm import summarize

def research(topic: str):
    print(f"\n🔍 Buscando: {topic}")
    results = search(topic)
    
    print(f"✅ {len(results)} fuentes encontradas")
    content = format_for_llm(results)
    
    print("🤖 Analizando con Gemini...\n")
    summary = summarize(topic, content)
    
    print("=" * 50)
    print(summary)
    print("=" * 50)

if __name__ == "__main__":
    research("Coderhouse expansión latinoamérica 2025")