# StrigilCrawler Python Client

A lightweight Python client for interacting with the StrigilCrawler API. This tool lets you submit a URL and a user prompt, and returns structured crawl results ready for use in LLM or RAG pipelines.

## Installation

You can clone this repository and install the package locally:

```bash
git clone https://github.com/your-username/strigil-crawler-client.git
cd strigil-crawler-client
pip install -e .
```

## Usage

Here’s an example of how to use the client in your Python script or Jupyter notebook:

```python
from strigil_crawler import StrigilCrawlerClient

# Create the client
client = StrigilCrawlerClient()

# Crawl a website with a prompt
response = client.crawl(
    start_url="https://example.com",
    prompt="Find any contact information or FAQ",
    max_depth=1
)

# Print the response
print(response.model_dump_json(indent=2))
```

## Output

The response will include a list of visited pages, each with the extracted content, a summary, and the LLM-recommended actions for the next crawl steps.

## License

MIT