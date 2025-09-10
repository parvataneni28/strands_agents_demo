from strands import tool
import re
from typing import List, Dict, Any

@tool
def preprocess(transcript: str) -> str:
    """Normalize whitespace, fix artifacts, and standardize speaker tags."""
    txt = re.sub(r'\r\n?', '\n', transcript)
    txt = re.sub(r'[ \t]+', ' ', txt).strip()
    return txt

@tool
def segment_by_turns(transcript: str) -> List[Dict[str, Any]]:
    """Split into turns of [{'speaker': 'Agent|Customer', 'text': '...'}]."""
    turns = []
    for line in transcript.splitlines():
        m = re.match(r'^(Agent|Customer)[:\-]\s*(.*)$', line, flags=re.I)
        if m:
            speaker, text = m.group(1).title(), m.group(2).strip()
            turns.append({"speaker": speaker, "text": text})
        elif turns:
            turns[-1]["text"] += " " + line.strip()
    if not turns:
        turns = [{"speaker": "Unknown", "text": transcript}]
    return turns

@tool
def local_keywords(text: str, top_k: int = 20) -> List[str]:
    """Naive keyword extraction."""
    stop = set("the a an to of for in on with and or is it this that".split())
    tokens = [w.lower().strip(".,!?;:()[]") for w in text.split()]
    counts = {}
    for t in tokens:
        if t and t not in stop and len(t) > 2:
            counts[t] = counts.get(t, 0) + 1
    return [w for w,_ in sorted(counts.items(), key=lambda x: -x[1])[:top_k]]
