# Monday.com Business Intelligence Agent

## Overview

This project implements an **AI-powered Business Intelligence Agent** that helps founders and executives quickly answer business questions using operational and sales data from monday.com.

The agent integrates with two monday.com boards:

- **Deals Board** – represents the sales pipeline
- **Work Orders Board** – represents operational project execution

Using these data sources, the system can:

- Analyze pipeline performance
- Identify operational workload
- Detect data quality issues
- Generate leadership updates
- Answer founder-level business questions using AI

The system combines **data integration, analytics, and AI-powered insights** into a single conversational dashboard.

---

## Live Hosted Prototype

Access the deployed application here:

https://monday-bi-agent-5dan95kdwpejxbjs2anahy.streamlit.app/

The hosted prototype demonstrates:

- Monday.com API integration
- Business metrics dashboard
- Conversational interface
- AI-powered business insights

---

## System Architecture

The system consists of four main layers.

### 1. Streamlit UI

Provides the interactive dashboard and conversational interface.

Features include:

- Data visualization
- Business metrics dashboard
- Founder question interface
- Leadership update generator

---

### 2. Monday.com API Integration

The system retrieves live data from monday.com boards using the **GraphQL API**.

The `monday_client.py` module handles:

- API authentication
- Querying board data
- Transforming responses into structured DataFrames

---

### 3. Data Processing Layer

Using **Pandas**, the system cleans and processes messy real-world data.

Key processing steps include:

- Handling missing values
- Converting numeric fields
- Aggregating pipeline metrics
- Detecting data quality issues

This ensures the system remains **robust even with incomplete or inconsistent data**.

---

### 4. AI Insight Generation

Founder questions are interpreted using an **LLM powered by Groq**.

The system uses:

- **LLaMA 3 (8B)**
- **Groq Cloud inference API**

The AI receives structured business metrics and generates responses including:

- Key business numbers
- Strategic insights
- Potential risks in the pipeline

This enables the system to produce **actionable business intelligence rather than raw data outputs**.

---

## Project Structure

```
monday-bi-agent
│
├── app.py               # Main Streamlit application
├── monday_client.py     # Monday.com API integration
├── llm_agent.py         # AI insight generation using Groq
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── decision_log.pdf     # Design decisions and tradeoffs
```

---

## Setup Instructions (Local Run)

### 1. Clone the repository

```bash
git clone <repository_url>
cd monday-bi-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

The application requires two API keys:

```
MONDAY_API_KEY=your_monday_api_key
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the application

```bash
streamlit run app.py
```

The app will be available at:

```
http://localhost:8501
```

---

## Example Founder Questions

The AI agent can answer questions such as:

- How is our pipeline performing?
- What insights can you derive from the current deal pipeline?
- Are there risks in our sales pipeline?
- What does the deal status distribution suggest about performance?
- Are there operational risks based on current work orders?

---

## Leadership Updates

The system includes a **Leadership Update Generator**.

This feature summarizes key business metrics including:

- Total pipeline value
- Number of deals
- Operational workload
- Deal status distribution

This allows executives to quickly prepare **leadership reports and internal updates**.

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Monday.com GraphQL API
- Groq Cloud
- LLaMA 3 (Open-source LLM)

---

## Data Resilience

The system is designed to handle **messy real-world business data**.

Implemented resilience features include:

- Handling missing deal values
- Managing incomplete records
- Detecting data quality issues
- Graceful error handling for API failures

This ensures the system continues to produce **useful insights even with imperfect data**.

---

## Future Improvements

With additional development time, the following improvements could be added:

- Sector-based pipeline analysis
- Revenue forecasting
- Time-based trend analysis
- Advanced conversational query understanding
- Enhanced visual dashboards
- Multi-board cross analytics

---

## Author

**Jonah Mathew**  
BTech Computer Science and Engineering (Data Science)  
Christ University, Bangalore

---

