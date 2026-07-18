import requests

BASE_URL = "http://127.0.0.1:8000"


def ask_question(question: str):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "question": question
        }
    )

    response.raise_for_status()

    return response.json()



def ingest_source(source: str):

    try:
        response = requests.post(
            f"{BASE_URL}/ingest",
            json={"source": source},
            timeout=60,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        return {
            "error": str(e)
        }