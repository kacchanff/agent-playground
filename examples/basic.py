"""Basic example demonstrating agent playground usage."""

import json
import sys
from pathlib import Path

# Add parent directory to path to import playground
sys.path.insert(0, str(Path(__file__).parent.parent))

from playground import (
    baseline_agent,
    keyword_agent,
    random_agent,
    run,
    score_similarity,
    aggregate_results,
)


def main():
    """Run a simple example comparing agents."""
    task = "Write a summary of artificial intelligence and machine learning"
    expected = "artificial intelligence machine learning summary"
    
    agents = [baseline_agent, keyword_agent, random_agent]
    
    results = run(task, agents, score_similarity, expected)
    sorted_results = aggregate_results(results)
    
    output = {
        'task': task,
        'expected': expected,
        'results': sorted_results,
    }
    
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()

