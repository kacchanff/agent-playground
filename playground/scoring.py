"""Deterministic scoring functions for agent outputs."""


def score_similarity(output: str, expected: str) -> float:
    """Calculate normalized token overlap score between output and expected.
    
    Returns a float between 0.0 and 1.0 representing similarity.
    Uses simple token overlap: intersection / union of tokens.
    """
    if not expected:
        return 0.0
    
    # Normalize: lowercase and split into tokens
    output_tokens = set(output.lower().split())
    expected_tokens = set(expected.lower().split())
    
    if not output_tokens or not expected_tokens:
        return 0.0
    
    # Jaccard similarity: intersection / union
    intersection = len(output_tokens & expected_tokens)
    union = len(output_tokens | expected_tokens)
    
    return intersection / union if union > 0 else 0.0

