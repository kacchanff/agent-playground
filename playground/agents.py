"""Agent implementations for the playground.

Agents are simple functions that take a task string and return a string output.
"""

import random
import re


def baseline_agent(task: str) -> str:
    """Simple baseline agent that returns first 100 characters of task."""
    return task[:100] if len(task) > 100 else task


def keyword_agent(task: str) -> str:
    """Extracts keywords from the task (words longer than 3 characters)."""
    words = re.findall(r'\b\w{4,}\b', task.lower())
    return ', '.join(sorted(set(words))[:10])


def random_agent(task: str) -> str:
    """Intentionally bad but deterministic agent using task hash as seed."""
    random.seed(hash(task) % (2**32))
    responses = [
        "I don't know.",
        "Maybe.",
        "Could be.",
        "Not sure about that.",
        "Let me think...",
    ]
    return random.choice(responses)

