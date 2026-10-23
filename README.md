# CrewAI Travel Planner Agent

## Overview
This project demonstrates a simple CrewAI agent that asks the user for a city and recommends exactly three places to visit there, with a brief reason for each suggestion.

## Features
- Accepts a city name using Python's `input()`.
- Defines one Travel Planner agent with a role, goal, and backstory.
- Uses one task with a clear expected output.
- Groups the agent and task into a Crew.
- Runs the crew with `crew.kickoff()` and prints the result.
- Loads the OpenAI API key and model configuration from a `.env` file.

## Project Structure
```text
travel-planner/
├── travel_planner.py
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

## Requirements
- Python
- An OpenAI API key with API access and any required billing/credits
- The Python packages listed in `requirements.txt`

## Setup

### 1. Create and activate a virtual environment (Windows PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 2. Install dependencies
Ensure `requirements.txt` contains:
```text
crewai
python-dotenv
```

Then run:
```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project folder:
```text
OPENAI_API_KEY=your_actual_api_key
MODEL=openai/gpt-4o-mini
```

Replace `your_actual_api_key` with your real API key. Do not share it or commit `.env` to GitHub.

### 4. Run the application
```powershell
python travel_planner.py
```

Enter a city when prompted. The agent should return a numbered list of three places, each with a short explanation.

## How It Works
1. `load_dotenv()` loads variables from `.env`.
2. `os.getenv()` reads the model and API key configuration.
3. `input()` asks the user for a city.
4. `Agent` defines the Travel Planner's role, goal, backstory, and model.
5. `Task` specifies the assignment and expected output.
6. `Crew` combines the agent and task.
7. `crew.kickoff(inputs={"city": city})` executes the task with the chosen city.
8. `print(result)` displays the final travel plan.

## Troubleshooting
- **401 / `invalid_api_key`:** Check that `.env` contains your actual, valid OpenAI API key, not the example placeholder. Confirm that `.env` is in the same folder from which you run the script.
- **Missing API key:** Confirm the variable is named `OPENAI_API_KEY` and that you called `load_dotenv()`.
- **Model or billing error:** Confirm your API account has access to the selected model and sufficient API billing/credits. ChatGPT subscriptions and API billing are separate.

## Security
The `.env` file contains a secret and should not be committed to version control. Add the following to `.gitignore`:
```text
.env
venv/
__pycache__/
```

## Learning Outcomes
- Understand the basic CrewAI building blocks: Agent, Task, and Crew.
- Practice loading configuration from environment variables.
- Pass user input into a task using `crew.kickoff(inputs=...)`.
