from src import agent
from src.output import save_result

if __name__ == "__main__":
    topics = [
        "Coderhouse expansión latinoamérica 2025",
        "tendencias inteligencia artificial empresas 2025",
    ]

    for topic in topics:
        result = agent.run(topic)

        print(f"\n📋 RESULTADO: {result['status'].upper()}")
        if result.get("summary"):
            print(f"\n{result['summary']}")

        # Guardar en Sheets solo si no fue descartado
        if result["status"] != "discarded":
            save_result(result)

        print("\n" + "=" * 50)