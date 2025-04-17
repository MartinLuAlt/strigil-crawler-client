
from typing import Optional, Dict, Any, List, Literal
from pydantic import BaseModel
from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class LLMAction(BaseModel):
    action: Literal["click", "stop"]
    target: Optional[str] = None
    reason: str
    goal: Optional[str] = None



class WebScraperError(BaseModel):
    """Base error model for web scraper errors"""
    error_type: str
    message: str
    details: Optional[Dict[str, Any]] = None

class CrawlError(WebScraperError):
    """Error during the crawling process"""
    pass

class LLMError(WebScraperError):
    """Error during LLM processing"""
    pass

class NetworkError(WebScraperError):
    """Error during network requests"""
    pass

class ParsingError(WebScraperError):
    """Error during parsing of web content"""
    pass

class ValidationError(WebScraperError):
    """Error during validation of data"""
    pass

class ErrorResponse(BaseModel):
    """Response model for error cases"""
    success: bool = False
    errors: List[WebScraperError]
    message: str 


class CrawlRequest(BaseModel):
    start_url: str
    user_instruction: str
    max_depth: Optional[int] = 3

class PageDetailsPublic(BaseModel):
    url: str 
    title: str
    body_text: str

class PageActionPublic(BaseModel):
    url: str
    action_key: str

class PageContextPublic(BaseModel):
    depth: int
    details: PageDetailsPublic
    prev_page_action: Optional[PageActionPublic] = None
    summary: str
    actions: List[LLMAction]
    visited_keys: List[str]  # convert from set

class CrawlResponse(BaseModel):
    success: bool = True
    history: List[PageContextPublic]
    errors: Optional[List[WebScraperError]] = None
    message: Optional[str] = None
