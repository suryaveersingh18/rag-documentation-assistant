from app.services.llm import get_llm

llm = get_llm()

response = llm.invoke("Say hello in one sentence.")

# Handle both old and new response formats
if isinstance(response.content, list):
    for block in response.content:
        if block.get("type") == "text":
            print(block["text"])
else:
    print(response.content)