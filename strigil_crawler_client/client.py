from typing import Optional
import requests
from pydantic import HttpUrl, ValidationError
from .models import CrawlRequest, CrawlResponse, ErrorResponse, LLMAction


class StrigilCrawlerClient:
    def __init__(self, base_url: str = "http://strigil-public-load-balancer-1010299699.us-east-2.elb.amazonaws.com", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key  # Placeholder for future support

    def crawl(
        self,
        start_url: str,
        prompt: str,
        max_depth: int = 3,
    ) -> CrawlResponse:
        """
        Submits a crawl request to the StrigilCrawler API and returns the parsed response.
        Raises requests.exceptions.RequestException on network errors.
        Raises ValueError if the start_url is invalid or the response cannot be parsed.
        """
        try:
            validated_url = HttpUrl(start_url)
        except ValidationError as e:
            raise ValueError(f"Invalid URL provided: {e}")

        request_data = CrawlRequest(
            start_url=str(validated_url),
            user_instruction=prompt,
            max_depth=max_depth
        )

        headers = {
            "Content-Type": "application/json"
        }

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        response = requests.post(
            f"{self.base_url}/crawl",
            headers=headers,
            json=request_data.dict()
        )

        if response.status_code != 200:
            try:
                error_data = ErrorResponse.model_validate(response.json())
                raise Exception(f"API Error: {error_data.message}")
            except Exception:
                raise Exception(f"Unexpected error: {response.text}")

        try:
            return CrawlResponse.model_validate(response.json())
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}")
