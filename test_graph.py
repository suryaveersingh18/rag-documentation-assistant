from app.graph.workflow import graph


response = graph.invoke(
    {
        "question": "How do I install FastAPI?"
    }
)

print("\nQUESTION\n")
print(response["question"])

print("\nANSWER\n")
print(response["answer"])