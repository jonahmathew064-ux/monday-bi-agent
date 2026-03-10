# Monday.com Business Intelligence Agent

## Overview

This project implements an AI-powered Business Intelligence agent capable of answering founder-level questions using operational and sales data stored in Monday.com boards.

The system dynamically retrieves data from Monday.com using its GraphQL API, processes and cleans the data, and generates insights through a conversational interface powered by an open-source Large Language Model.

The goal of this system is to help founders quickly understand:

- Sales pipeline health
- Deal performance
- Operational workload
- Potential risks in business data

without manually querying multiple data sources.

---
## Running with LLM Support

The AI insight generation uses the open-source Mistral model via Ollama.

To run the full LLM-powered version locally:

1. Install Ollama
2. Pull the Mistral model

ollama pull mistral

3. Start Ollama

ollama run mistral

4. Run the application

streamlit run app.py

Note: The deployed Streamlit Cloud prototype does not execute the Ollama model because the hosting environment does not support running local LLM runtimes.

## System Architecture

The system follows a layered architecture:

User Question  
↓  
Streamlit Interface  
↓  
Monday.com API Integration  
↓  
Data Cleaning & Processing  
↓  
Business Metrics Engine  
↓  
LLM Insight Generation  
↓  
Founder-Level Business Insight

---

## Components

### 1. Streamlit UI
Provides the dashboard and conversational interface where users can:
- view data tables
- see business metrics
- ask founder-level questions
- generate leadership summaries

### 2. Monday API Client
Fetches data dynamically from the **Deals** and **Work Orders** boards using the Monday GraphQL API.

### 3. Data Processing Layer
Handles messy real-world data by:
- cleaning missing values
- normalizing numeric formats
- identifying incomplete records

### 4. Business Intelligence Layer
Calculates key business metrics such as:
- total pipeline value
- number of deals
- operational workload
- deal status distribution

### 5. AI Insight Layer
Uses the **Mistral open-source LLM via Ollama** to interpret founder questions and generate meaningful insights.

---

## Project Structure


monday-bi-agent
│
├── app.py # Main Streamlit application
├── monday_client.py # Monday.com API integration
├── llm_agent.py # LLM-based insight generation
├── requirements.txt # Python dependencies
└── README.md


---

## Setup Instructions

### 1. Clone the repository


git clone <repository_url>
cd monday-bi-agent


### 2. Install dependencies


pip install -r requirements.txt


### 3. Add Monday API Key

Edit `monday_client.py` and add your Monday API key:


API_KEY = "YOUR_MONDAY_API_KEY"


### 4. Run the application


streamlit run app.py


The application will start locally at:


http://localhost:8501


---

## Example Questions

Founders can ask questions such as:

- How is our pipeline performing?
- What insights can you derive from the current deal pipeline?
- Are there any risks in our sales pipeline?
- What does the deal status distribution suggest about performance?

The AI agent analyzes the business data and provides founder-level insights.

---

## Leadership Updates

The system includes a **Leadership Update Generator** that summarizes key operational and sales metrics including:

- Total pipeline value
- Number of deals
- Operational workload
- Deal status distribution

This feature helps founders and executives quickly prepare leadership reports.

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Monday.com GraphQL API
- Ollama
- Mistral (Open-source LLM)

---

## Future Improvements

With additional development time, the following improvements could be implemented:

- Query understanding for sector-based filtering
- Time-based pipeline forecasting
- Automated leadership report generation
- Multi-board analytics
- Advanced data visualization

---

## Author

**Jonah Mathew**  
BTech Computer Science and Engineering (Data Science)  
Christ University