import requests
from typing import Union

def fetch_page_with_cookies(url: str, cookies: Union[str, dict]) -> str:
    """
    Fetches the content of the page using HTTP GET and provided cookies.

    Args:
        url (str): The URL of the webpage to fetch.
        cookies (Union[str, dict]): Cookies to be sent with the request. 
                                    Can be a string or a dictionary.

    Returns:
        str: The response HTML/text from the page.
    """
    # Convert string cookies to dictionary if necessary
    if isinstance(cookies, str):
        cookies = dict(item.split("=") for item in cookies.split("; "))

    try:
        # Send GET request with cookies
        response = requests.get(url, cookies=cookies, headers={"User-Agent": "Mozilla/5.0"})
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return ""

    return response.text

html = fetch_page_with_cookies("https://plataforma.fullcycle.com.br/courses/3b8c4f2c-aff9-4399-a72a-ad879e5689a2/242/catalog/215/list/1/module/231/conteudos?capitulo=231&conteudo=14754", "sessionid=your_session_id; other_cookie=other_value")
print(html)  # Print the first 500 characters of the HTML content
# Note: The above code is a simplified example. In a real-world scenario, you would want to handle cookies and sessions more securely.