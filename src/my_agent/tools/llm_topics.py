from strands import tool

SYSTEM_PROMPT = """You extract high-quality customer support TOPICS from call transcripts.
Return JSON only with fields: name, description, keywords (<=5), confidence (0-1),
and evidence (list of {text_span,start,end})."""

@tool
def propose_topics_llm(context: str, max_topics: int = 6) -> str:
    """
    Ask the model to propose topics with evidence spans.
    The agent will send this as a prompt; response must be JSON.
    """
    return f"""{SYSTEM_PROMPT}

Transcript:
<<<
{context}
>>>

Instructions:
- Produce 1–{max_topics} topics.
- Respond with a JSON array only.
"""
