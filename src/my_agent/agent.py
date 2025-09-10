import os
from strands import Agent
from strands.models.ollama import OllamaModel
from strands.models.openai import OpenAIModel

from my_agent.tools.topics import preprocess, segment_by_turns, local_keywords
from my_agent.tools.llm_topics import propose_topics_llm

SYSTEM_INSTRUCTIONS = (
    "You are a pipeline controller. When solving a task:\n"
    "- USE tools when they help. Do NOT describe plans or tool calls.\n"
    "- Never print code blocks of the tool calls.\n"
    "- Final answer must be a JSON array of topics only, no prose."
)

def build_agent():
    provider = os.getenv("PROVIDER", "ollama").lower()
    if provider == "openai":
        model = OpenAIModel(model_id=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    else:
        model = OllamaModel(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            model_id=os.getenv("OLLAMA_MODEL", "llama3.1:8b"),
            stream=False,
        )

    tools = [
        preprocess,
        segment_by_turns,
        local_keywords,
        propose_topics_llm,
    ]

    return Agent(model=model, tools=tools, load_tools_from_directory=False,)
