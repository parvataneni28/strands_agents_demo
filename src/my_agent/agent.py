from strands import Agent, tool
from strands.models.openai import OpenAIModel
from strands.models.ollama import OllamaModel
import os



def build_agent():
    # Switch provider based on env
    # provider = os.getenv("PROVIDER", "openai").lower()

    # if provider == "openai":
    #     # OpenAI (works when installed as strands-agents[openai])
    #     model = OpenAIModel(model_id=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

    # else:
    model = OllamaModel(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            model_id=os.getenv("OLLAMA_MODEL", "llama3")
        )
    return Agent(model=model, tools=[], load_tools_from_directory=True)
