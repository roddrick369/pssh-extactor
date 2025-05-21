import json
from pathlib import Path

def load_site_mapping() -> dict:
    """
    Load the site-to-method mapping from a JSON file.

    Returns:
        dict: A dictionary containing the site mapping.
    """
    # Define the path to the site mapping file
    site_mapping_path = Path(__file__).parent / "site_mapping.json"

    # Load the site mapping from the JSON file
    with open(site_mapping_path, 'r') as f:
        site_mapping = json.load(f)

    return site_mapping