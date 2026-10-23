import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Load API key and model settings from the .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL", "openai/gpt-4o-mini")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. Please add it to your .env file."
    )

# Ask the user which city they want to explore
city = input("Which city would you like to explore? ")

# Create the Travel Planner agent
planner = Agent(
    role="Travel Planner",
    goal="Recommend exactly three interesting places to visit in the given city.",
    backstory=(
        "You are an experienced travel planner who helps first-time "
        "visitors discover a city's highlights. You write for travelers "
        "who want practical, easy-to-understand suggestions. You briefly "
        "explain why each place is worth visiting."
    ),
    llm=model,
    verbose=True
)

# Create one task for the agent
task = Task(
    description=(
        "Suggest exactly 3 places to visit in {city}. Choose relevant "
        "attractions and give a short reason for visiting each place. "
        "Do not include more or fewer than 3 places."
    ),
    expected_output=(
        "A numbered list containing exactly 3 places. For each place, "
        "provide its name and one brief sentence explaining why it is "
        "worth visiting. Do not include an introduction, conclusion, "
        "or extra recommendations."
    ),
    agent=planner
)

# Assemble the agent and task into a crew
crew = Crew(
    agents=[planner],
    tasks=[task],
    verbose=True
)

# Run the crew with the city supplied by the user
result = crew.kickoff(inputs={"city": city})

# Print the final travel plan
print("\n--- YOUR TRAVEL PLAN ---")
print(result)
