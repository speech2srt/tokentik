# Tokentik

A lightweight Python utility for estimating token counts in text, specifically optimized for modern LLMs using the `o200k_base` encoding.

## Installation

```bash
pip install tokentik
```

## Usage

```python
from tokentik import count_tokens

text = "Hello, world! 你好，世界！"
token_count = count_tokens(text)
print(f"Token count: {token_count}")
```

## Configuration

### Environment Variables

`tiktoken` needs to download and cache the BPE (Byte Pair Encoding) vocabulary files. By default, it uses a temporary directory. To specify a persistent location for these files, set the `TIKTOKEN_CACHE_DIR` environment variable:

```bash
export TIKTOKEN_CACHE_DIR="/path/to/your/models/tiktoken"
```

This is highly recommended for production environments or Cloud Run environments where the storage might be mounted (e.g., at `/mnt/models/tiktoken`).

## License

MIT

---
Created at: 2026-01-13 01:33 (Europe/Athens)
