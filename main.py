from utils.domain_utils import extract_domain
from utils.site_mapping import  get_method_for_site

def main():
    url = input("Enter a URL: ")
    domain = extract_domain(url)
    method_config = get_method_for_site(domain)

    print(f"\nSite: {domain}")
    print(f"Suggested method: {method_config['method']}")
    print(f"Notes: {method_config['notes']}\n")

if __name__ == "__main__":
    main()