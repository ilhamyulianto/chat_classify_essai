# AI Assistant Demo

## Short Brief

This project is a simple **AI chat assistant demo** built with **Streamlit** that connects to a **local Ollama server** to generate responses using Google's **Gemma 3:1B** model. It provides a clean chat UI, maintains conversation history within a session, and allows users to interact with a locally hosted LLM through a web interface.

---

## Installation Guide

### Prerequisites

* Python **3.9+**
* [Ollama](https://ollama.com) installed and running
* Gemma model pulled:

  ```bash
  ollama pull gemma3:1b
  ```

* use ollama run to check if model downloaded properly, and running.

* Ollama server running on:

  ```text
  http://localhost:11434
  ```

---

### Option 1: Using `venv`

1. **Create virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the environment**

   * Windows:

     ```bash
     venv\\Scripts\\activate
     ```

3. **Install dependencies**

   ```bash
   pip install streamlit requests
   ```

---

### Option 2: Using Conda

1. **Create conda environment**

   ```bash
   conda create -n ai-assistant python=3.10 -y
   ```

2. **Activate environment**

   ```bash
   conda activate ai-assistant
   ```

3. **Install dependencies**

   ```bash
   pip install streamlit requests
   ```

---

## Usage

1. **Start Ollama server** (if not already running)

   ```bash
   ollama serve
   ```

2. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

3. **Open browser**
   Streamlit will open automatically or navigate to:

   ```text
   http://localhost:8501
   ```

4. **Chat with the assistant**

   * Type questions in the chat input
   * Conversation history is preserved per session
   * Use **Clear Chat** from the sidebar to reset

---

## Notes

* The app communicates directly with Ollama's API (`/api/generate`).
* Model name is hardcoded to `gemma3:1b`.
* Ensure Ollama is running before starting the app, otherwise an error message will be shown.

---

## Demo Purpose

This project is intended for **local demos, experimentation, and learning** how to integrate Streamlit with local LLMs using Ollama.
