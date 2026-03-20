# AI Travel Agent 🤖✈️

An AI agent that combines real-time weather data and web search to generate
personalized travel packing recommendations.

Built as my first hands-on project with **agentic AI architecture** and **LLM tool use**,
following a GenAI seminar by Zone01.

---

## 🧠 How It Works

The agent is powered by **Qwen2.5-Coder-32B** (via HuggingFace) and uses two tools:

1. **Weather Tool** — fetches real-time weather data for any city via `wttr.in` API
2. **Web Search Tool** — falls back to DuckDuckGo if the weather API is unavailable

Given a destination, the agent reasons over the weather conditions and produces
a practical packing list for the traveler.

---

## 🏗️ Architecture

```
User Prompt
     │
     ▼
 CodeAgent (smolagents)
     │
     ├── get_weather() ──► wttr.in API
     │                         │
     │                    (if fails)
     │                         │
     └── DuckDuckGoSearchTool ◄─┘
     │
     ▼
 Qwen2.5-Coder-32B (HuggingFace)
     │
     ▼
 Packing Recommendations
```

---

## 🛠️ Tech Stack

- **Python**
- **smolagents** — agentic AI framework by HuggingFace
- **Qwen2.5-Coder-32B-Instruct** — open-source LLM
- **HuggingFace Hub** — model hosting & inference
- **wttr.in** — weather REST API
- **DuckDuckGo Search** — web search fallback

---

## 🚀 How to Run

**1. Install dependencies**
```bash
pip install smolagents requests
```

**2. Set your HuggingFace token**
```bash
export HUGGINGFACE_HUB_TOKEN=your_token_here
```

**3. Run the agent**
```bash
python travel_agent.py
```

---

## 📌 Notes

This is a learning project built during a GenAI seminar (Zone01).
It was my first introduction to agentic AI — tool use, LLM inference,
and building systems where the model decides how to act.
