from dotenv import load_dotenv
from my_agent.agent import build_agent


if __name__ == "__main__":
    load_dotenv()  # loads .env if present
    agent = build_agent()
    print(agent("Say hello, then use add(2,3) and square(5)."))
