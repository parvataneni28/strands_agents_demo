# Strands Local Agent

## Setup
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# set PROVIDER=openai or PROVIDER=ollama inside .env
