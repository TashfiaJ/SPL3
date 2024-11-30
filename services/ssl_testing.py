import requests

def check_ssl_urls(url_list):
    results = {}
    for url in url_list:
        try:
            # Ensure the URL starts with 'https://' for SSL checks
            if not url.startswith("https://"):
                url = "https://" + url
            response = requests.get(url, timeout=5)
            results[url] = {
                "status": response.status_code,
                "ssl_valid": response.ok
            }
        except requests.exceptions.SSLError:
            results[url] = {"status": "SSL error"}
        except Exception as e:
            results[url] = {"error": str(e)}
    
    return results
