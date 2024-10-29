# AI Chat Application

A real-time chat application with an AI assistant built using FastAPI and LangChain, featuring server-sent events for streaming responses.

## Tech Stack

- **Backend**
  - FastAPI (Python web framework)
  - LangChain (LLM framework)
  - Ollama (Local LLM runtime)
  - Uvicorn (ASGI server)

- **Frontend**
  - HTML/CSS
  - Petite Vue (Lightweight Vue.js alternative)
  - Server-Sent Events (Real-time streaming)

## Prerequisites

- Python 3.10 or higher
- Poetry (Python package manager)
- Ollama installed with llama3.2 1B model

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Make sure you have Ollama installed and the llama3.2 1B model pulled:
   ```bash
   # Install Ollama (if not already installed)
   curl https://ollama.ai/install.sh | sh

   # Pull the llama3.2 1B model
   ollama pull llama3.2:1b
   ```

## Running the Application

1. Activate the Poetry virtual environment:
   ```bash
   poetry shell
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```