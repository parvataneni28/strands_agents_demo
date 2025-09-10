import os, json, subprocess
from dotenv import load_dotenv
from my_agent.agent import build_agent

TRANSCRIPT = """Agent: Hi, thanks for calling. How can I help?
Customer: I was charged twice on my last invoice and also need to cancel next month.
Agent: I’m sorry about that. I can issue a refund for the duplicate charge...
Customer: Also my address changed to 10 York Street, Toronto.
"""

def ensure_model(model_id: str, host: str = None):
    try:
        env = os.environ.copy()
        if host:
            env["OLLAMA_HOST"] = host
        subprocess.run(
            ["ollama", "pull", model_id],
            check=True,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f"✅ Ensured model {model_id}")
    except Exception as e:
        print(f"⚠️ Could not pull model {model_id}: {e}")

if __name__ == "__main__":
    load_dotenv()

    model_id = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    ensure_model(model_id, host)

    agent = build_agent()
    instruction = f"""
Use your tools to preprocess, segment, extract keywords, and propose topics.
Finally return a JSON list of topics with name, description, keywords, confidence, evidence.
Transcript:
{TRANSCRIPT}
"""
    result = agent(instruction)
    text = getattr(result, "output_text", str(result))
    try:
        start = text.find('[')
        end = text.rfind(']') + 1
        topics = json.loads(result[start:end])
    except Exception:
        topics = [{"raw": text}]

    print(json.dumps(topics, indent=2))

