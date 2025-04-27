from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
import litellm

load_dotenv()

# Using local Ollama model
MODEL_NAME = "ollama/deepseek-r1"    
OLLAMA_BASE_URL = "http://localhost:11434"  # default Ollama server

response = litellm.completion(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Your task"}],
    base_url=OLLAMA_BASE_URL,    # very important for local models
    api_key=None,                # Ollama does not need API key
    provider="ollama"            # provider must be "ollama"
)

from crewai.llm import LLM

llm = LLM(
    model=MODEL_NAME,
    base_url=OLLAMA_BASE_URL,
    provider="ollama",
    api_key=None,
)

news_researcher = Agent(
    role="senior_researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, eager to explore "
        "and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

news_writer = Agent(
    role="Tech_Researcher",
    goal="Craft accessible and captivating blog posts about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex ideas, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)