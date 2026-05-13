from src import agent

if __name__ == "__main__":
    topics = [
        "Coderhouse expansión latinoamérica 2025",
        "tendencias inteligencia artificial empresas 2025",
    ]

    for topic in topics:
        result = agent.run(topic)
        print(f"\n📋 RESULTADO FINAL: {result['status'].upper()}")
        if result.get("summary"):
            print(f"\n{result['summary']}")
        print("\n" + "=" * 50)