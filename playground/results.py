"""Result aggregation and formatting utilities."""


def aggregate_results(results: list[dict]) -> list[dict]:
    """Sort results by score descending and return JSON-serializable format."""
    sorted_results = sorted(results, key=lambda x: x.get('score', 0.0), reverse=True)
    return sorted_results

