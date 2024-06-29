import requests
import re
import urllib3

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def GetCSRF_Token():
    headers = {
        'Host': 'www.instagram.com',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'de-DE',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Priority': 'u=0, i',
    }

    response = requests.get('https://www.instagram.com/', headers=headers, verify=False)

    # Extract the CSRF token from the Set-Cookie header
    set_cookie_header = response.headers.get('Set-Cookie', '')
    csrf_token = re.search(r'csrftoken=([a-zA-Z0-9\-_]+)', set_cookie_header)

    csrf_token_value = None
    if csrf_token:
        csrf_token_value = csrf_token.group(1)
        print("Is Printet from GetCSRF.py CSRF-Token:", csrf_token_value)
    else:
        print("CSRF-Token nicht gefunden.")

    # Extract the device_id from the HTML content
    html_content = response.text
    device_id_match = re.search(r'"device_id":"([a-zA-Z0-9\-]+)"', html_content)

    device_id = None
    if device_id_match:
        device_id = device_id_match.group(1)
        print("Is Printet from GetCSRF.py ig_did:", device_id)
    else:
        print("ig_did nicht gefunden.")

    return csrf_token_value, device_id
