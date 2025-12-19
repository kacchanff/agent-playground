# agent-playground

A tiny, readable Python playground to run multiple AI agents on the same task, score their outputs deterministically, and compare results.

## What it is

This is **not** a framework or platform. It's a minimal (~300 lines), explicit playground for experimenting with agent logic. Everything is plain Python functions, no magic, no dependencies beyond the standard library.

## Why it exists

Sometimes you just need to compare a few agent implementations side-by-side with deterministic scoring. No configs, no YAML, no async, no LLM SDKs—just functions that take a task and return an output.

## 30-second example

```python
from playground import baseline_agent, keyword_agent, random_agent, run, score_similarity

task = "Write a summary of AI"
expected = "artificial intelligence summary"

agents = [baseline_agent, keyword_agent, random_agent]
results = run(task, agents, score_similarity, expected)

# Results are sorted by score descending
for result in results:
    print(f"{result['agent_name']}: {result['score']:.2f}")
```

Run the full example:
```bash
python examples/basic.py
```

## What it is NOT

- A production framework
- An LLM integration library
- A web server or UI
- A configuration-driven system
- An async runtime

It's a playground. Use it to prototype, compare, and understand agent behavior. When you need something more, build it.

## Project structure

```
agent-playground/
├── playground/
│   ├── agents.py     # Agent implementations
│   ├── scoring.py    # Deterministic scoring
│   ├── run.py        # Execution orchestrator
│   └── results.py    # Result aggregation
├── examples/
│   └── basic.py      # Runnable example
└── README.md
```

## Requirements

- Python 3.10+
- Standard library only (no external dependencies)
