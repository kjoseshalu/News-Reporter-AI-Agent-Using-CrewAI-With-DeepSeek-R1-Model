
# News Reporter AI Agent Using CrewAI and DeepSeek-R1 Model

News-Reporter-AI-Agent-Using-CrewAI-With-DeepSeek-R1-Model is an autonomous AI agent system that simulates a professional news reporter.
Built using CrewAI, enhanced with LangChain modules, and powered by DeepSeek R1 running locally via Ollama, it can autonomously research, summarize, and generate full news reports.






## 🚀 Features
🧠 Multi-agent collaboration using CrewAI

🔎 Autonomous research, writing, and editing

📚 Uses DeepSeek R1 model served through Ollama

⚙️ Integrated with LangChain tools for external data interaction

🌐 Environment configuration via `.env`

📝 Output news articles, headlines, and summaries

🔄 Supports both manual and autonomous workflows




## Project Structure

- `agents.py`: Defines the individual AI agents and their roles.

- `crew.py`: Sets up the CrewAI environment and coordinates tasks.

- `tasks.py`: Lists all news-related tasks and their descriptions.

- `tools.py`: Additional helper tools for agents.

- `output-file.md`: Contains sample generated news output.

- `requirements.txt`: Python dependencies.
## 🛠️ Tech Stack

- **Python** 3.11

- **CrewAI:** Autonomous Agent Framework.
 
- **Ollama:** Local Model Serving.

- **DeepSeek R1 Model:** LLM for text generation.

- **langchain_google_genai:** LangChain's Google GenAI Toolkit (optional future use).

- **load_dotenv:** Load environment variables.

- **crewai-tools:**  Tools for extending CrewAI functionality.

- **langchain-community:** LangChain community toolkits and integrations.

## 📦 Installation & Setup


1. 📥 Clone the Repository
Clone the GitHub repository to your local system to get the source code.

```sh
git clone https://github.com/your-username/gemini-qa-app.git
cd gemini-qa-app

```

This command copies the repository files to your machine and changes the current directory to the project folder.

2. 🐍 Create a Virtual Environment

Create an isolated Python environment using conda to manage dependencies easily.
```sh
conda create -p venv python=3.10 -y
```
-p venv creates a virtual environment in a folder named venv.
python=3.10 specifies the Python version.
-y auto-confirms the environment creation.

3. ⚡ Activate the Virtual Environment

Activate the environment you just created.
```sh
conda activate venv/
```
This ensures all the packages are installed and run within the isolated environment.

4. 📦 Install Required Dependencies
Install all the Python libraries specified in requirements.txt.
```sh
pip install -r requirements.txt
```
This step is crucial to ensure the app runs without missing any dependencies.

5. 🐳 Install and Run [Ollama](https://ollama.ai/)
Make sure Ollama is installed and running.

Pull the DeepSeek R1 model:
```sh
ollama pull deepseek:latest
```

6. 🚀 Run the News Reporter Agent
Start the application by running the Python script:

```sh
python run crew.py
```
ℹ️ Note: This runs directly in your terminal (CMD/PowerShell/Linux terminal), 


## 📷 Screenshot

![App Screenshot](https://github.com/kjoseshalu/News-Reporter-AI-Agent-Using-CrewAI-With-DeepSeek-R1-Model/blob/main/Screenshot.png)



