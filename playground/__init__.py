"""Agent playground - minimal framework for running and comparing agents."""

from playground.agents import baseline_agent, keyword_agent, random_agent
from playground.run import run
from playground.scoring import score_similarity
from playground.results import aggregate_results

__all__ = [
    'baseline_agent',
    'keyword_agent',
    'random_agent',
    'run',
    'score_similarity',
    'aggregate_results',
]

