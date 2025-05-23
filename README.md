# LangChain Demo

## Overview

**LangChain Demo** is a project that explores the integration of Large Language Models (LLMs) using the LangChain framework. It includes scripts and notebooks demonstrating how to set up LLMs and build applications like a travel planner chatbot.

## Repository Structure

* `llm.py`: Sets up and configures the LLM using LangChain.
* `travel_planner_llm.py`: Implements a travel planner chatbot leveraging the configured LLM.
* `practice.ipynb`: A Jupyter Notebook for experimenting with LangChain and LLM functionalities.
* `README.md`: Provides an overview and documentation for the project.

## File Descriptions

### `llm.py`

This script is responsible for initializing and configuring the Large Language Model using LangChain. It includes:

* Importing necessary modules from LangChain.
* Setting up API keys or authentication for the LLM provider.
* Defining the LLM with specific parameters (e.g., temperature, model name).
* Creating a function or class to return the configured LLM instance for use in other parts of the application.

### `travel_planner_llm.py`

This script builds upon the configured LLM to create a travel planner chatbot. Its functionalities include:

* Importing the LLM configuration from `llm.py`.
* Defining prompts or chains that guide the LLM to act as a travel planner.
* Handling user inputs and generating travel plans or suggestions.
* Possibly integrating with external APIs for real-time travel data (e.g., flights, hotels).

### `practice.ipynb`

This Jupyter Notebook serves as a sandbox for experimenting with LangChain and LLMs. It covers:

* Basic usage of LangChain components.
* Testing different prompts and observing LLM responses.
* Exploring various configurations and their effects on output.
* Documenting findings and insights during experimentation.

## Getting Started

To run the project locally:

1. **Clone the repository:**

```bash
git clone https://github.com/fatima-amani/ai-track-langchain.git
cd ai-track-langchain
```

2. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
   
   Create a `.env` file and add your LLM provider API keys and other necessary configurations.

5. **Run the travel planner chatbot:**

```bash
python travel_planner_llm.py
```

6. **Explore the Jupyter Notebook:**

```bash
jupyter notebook practice.ipynb
```

## Author

👩‍💻 Fatima Amani  
GitHub: [@fatima-amani](https://github.com/fatima-amani)
