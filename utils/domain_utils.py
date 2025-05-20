from urllib.parse import urlparse

def extract_domain(url: str) -> str:
    """
    Receives a complete URL and returns the domain (netloc).

    Args:
        url (str): The URL from which to extract the domain.

    Returns:
        str: The extracted domain.
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc

    # Remove 'www.' prefix
    if domain.startswith("www."):
        domain = domain[4:]

    return domain