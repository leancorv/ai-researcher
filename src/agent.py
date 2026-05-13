from src.search import search, format_for_llm
from src.llm import summarize, score_relevance

MAX_RETRIES = 2

def refine_query(original_query: str, attempt: int) -> str:
    """Modifica el query en cada reintento para buscar diferente.""" 
    return f"{original_query} {modifiers[attempt % len(modifiers)]}"

def run(topic: str) -> dict:
    """
    Ejecuta el agente completo para un tema dado.
    Devuelve un dict con el resultado final y metadata.
    """
    print(f"\n🤖 Agente iniciado para: '{topic}'")
    print("-" * 50)

    for attempt in range(MAX_RETRIES + 1):
        # 1. Definir query (refinado si es reintento)
        query = topic if attempt == 0 else refine_query(topic, attempt)
        if attempt > 0:
            print(f"🔄 Reintento {attempt} con query: '{query}'")

        # 2. Buscar
        print(f"🔍 Buscando en la web...")
        results = search(query)
        content = format_for_llm(results)

        # 3. Sintetizar
        print(f"📝 Sintetizando con LLM...")
        summary = summarize(topic, content)

        # 4. Evaluar relevancia
        print(f"⚖️  Evaluando relevancia...")
        evaluation = score_relevance(topic, summary)
        score = evaluation["score"]
        
        print(f"📊 Score: {score}/10 — {evaluation['reason']}")

        # 5. Decidir
        if score >= 7:
            print(f"✅ Resultado aceptado (score {score}/10)")
            return {
                "status": "success",
                "topic": topic,
                "query_used": query,
                "summary": summary,
                "score": score,
                "reason": evaluation["reason"],
                "attempts": attempt + 1
            }
        elif score >= 4:
            print(f"⚠️  Relevancia media (score {score}/10), reintentando...")
            if attempt == MAX_RETRIES:
                print(f"⚠️  Máximo de reintentos alcanzado, guardando igual.")
                return {
                    "status": "low_quality",
                    "topic": topic,
                    "query_used": query,
                    "summary": summary,
                    "score": score,
                    "reason": evaluation["reason"],
                    "attempts": attempt + 1
                }
        else:
            print(f"❌ Resultado descartado (score {score}/10)")
            return {
                "status": "discarded",
                "topic": topic,
                "query_used": query,
                "summary": None,
                "score": score,
                "reason": evaluation["reason"],
                "attempts": attempt + 1
            }

    return {"status": "failed", "topic": topic}