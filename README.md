# Tokentik

A lightweight Python utility for estimating token counts in text, specifically optimized for modern LLMs using the `o200k_base` encoding.

## Installation

```bash
pip install tokentik
```

## Usage

```python
from tokentik import count_tokens

text = "Hello, world!"

# Estimate tokens using the default 'o200k_base' encoding (GPT-4o)
token_count = count_tokens(text)
print(f"Token count: {token_count}")

# Specify a different encoding model (e.g., 'cl100k_base' for GPT-4/GPT-3.5)
token_count_v2 = count_tokens(text, model="cl100k_base")
print(f"Token count (cl100k_base): {token_count_v2}")
```

## Configuration

### Environment Variables

`tiktoken` needs to download and cache the BPE (Byte Pair Encoding) vocabulary files. By default, it uses a temporary directory. To specify a persistent location for these files, set the `TIKTOKEN_CACHE_DIR` environment variable:

```bash
export TIKTOKEN_CACHE_DIR="/path/to/your/models/tiktoken"
```

This is highly recommended for production environments or Cloud Run environments where the storage might be mounted (e.g., at `/mnt/models/tiktoken`).

## Acknowledgments

Special thanks to [OpenAI](https://openai.com/) for their [tiktoken](https://github.com/openai/tiktoken) library, which this utility is built upon.

## License

MIT
