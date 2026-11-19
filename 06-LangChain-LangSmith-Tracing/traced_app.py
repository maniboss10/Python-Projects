import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():
    load_dotenv(Path(__file__).with_name(".env"))

    openai_api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not openai_api_key:
        raise SystemExit("Set OPENAI_API_KEY in .env or PowerShell before running this app.")

    prompts = [
        "What is Python? Explain in one sentence.",
        "Explain Python lists and tuples with examples.",
        "Explain Python decorators, generators, and context managers with practical examples.",
    ]

    try:
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, max_retries=0)
    except Exception as error:
        raise SystemExit(f"Could not initialize ChatOpenAI ({type(error).__name__}).") from None

    failed = False
    for number, prompt in enumerate(prompts, start=1):
        print(f"\nPrompt {number}: {prompt}", flush=True)
        try:
            response = llm.invoke(prompt)
        except Exception as error:
            print(f"Request {number} failed ({type(error).__name__}).")
            failed = True
            continue
        print(response.content)

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
