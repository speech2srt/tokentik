"""
Tokentik - A simple utility to estimate token counts for text using tiktoken.
"""

import tiktoken

__version__ = "0.1.1"


def count_tokens(text: str, model: str = "o200k_base") -> int:
    """
    Estimate the number of tokens in a given text.
    Defaults to 'o200k_base' encoding (used by GPT-4o).

    Args:
        text: The text to count tokens for.
        model: The encoding model name. Defaults to "o200k_base".

    Returns:
        The number of tokens.
    """
    if not text:
        return 0

    try:
        # Get the encoding
        encoding = tiktoken.get_encoding(model)
        # Encode the text and return the number of tokens
        return len(encoding.encode(text))
    except Exception:
        # Fallback to return 0 if an error occurs
        return 0


__all__ = ["count_tokens"]
