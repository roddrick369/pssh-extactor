import json
from pathlib import Path

def load_site_mapping() -> dict:
    """
    Load the site-to-method mapping from a JSON file.

    Returns:
        dict: A dictionary containing the site mapping.
    """
    # Define the path to the site mapping file
    site_mapping_path = Path(__file__).parent.parent / "site_mapping.json"

    # Check if the file exists
    if not site_mapping_path.exists():
        site_mapping.path.write_text("{}")

    # Load the site mapping from the JSON file
    with open(site_mapping_path, 'r') as f:
        site_mapping = json.load(f)

    return site_mapping

def get_method_for_site(domain: str) -> dict:
    """
    Returns the method config for a given domain from the JSON file.
    If not found, return a default dict with method = "auto".

    Args:
        domain (str): The domain for which to get the method.

    Returns:
        dict: A dictionary containing the method for the domain.
    """
    # Load the site mapping
    site_mapping = load_site_mapping()

    # Check if the domain is in the site mapping
    if domain in site_mapping:
        return site_mapping[domain]
    
    # If not found, return a default dict
    return {
        "method": "auto",
        "notes": "not mapped yet"
    }