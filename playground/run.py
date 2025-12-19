"""Orchestrates agent execution and scoring."""

from typing import Callable


def run(
    task: str,
    agents: list[Callable[[str], str]],
    scorer: Callable[[str, str], float],
    expected: str | None = None,
) -> list[dict]:
    """Run multiple agents on a task and score their outputs.
    
    Args:
        task: The task string to pass to agents
        agents: List of agent functions (task -> output)
        scorer: Scoring function (output, expected) -> float
        expected: Optional expected output for scoring
    
    Returns:
        List of result dicts with keys: agent_name, output, score
    """
    results = []
    
    for agent in agents:
        output = agent(task)
        score = scorer(output, expected) if expected else 0.0
        
        results.append({
            'agent_name': agent.__name__,
            'output': output,
            'score': score,
        })
    
    return results

