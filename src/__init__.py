"""
Tokentik - A simple utility to estimate token counts for text using tiktoken.
"""

import tiktoken

__version__ = "0.1.0"

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
        # 获取编码器
        encoding = tiktoken.get_encoding(model)
        # 编码并返回长度
        return len(encoding.encode(text))
    except Exception:
        # 兜底返回 0 或抛出异常，这里选择返回 0
        return 0

__all__ = ["count_tokens"]
