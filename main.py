import requests
from GetCSRF import GetCSRF_Token
from GetMID import Get_MID
import urllib3

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get Tokens
csrf_token_value, device_id = GetCSRF_Token()
print("Is Printet from main.py CSRF Token:", csrf_token_value)
print("Is Printet from main.py ig_did:", device_id)

# Get the MID
mid_value = Get_MID(csrf_token_value)
print("Is Printet from main.py MID:", mid_value)

# Input your Login Data
username = "carolasdasdasdasdasdez9dy"
password = "sadasdasdasd"

cookies = {
    'csrftoken': csrf_token_value,  # Get from CSRF.py
    'mid': mid_value,
    'ig_did': device_id,
}

headers = {
    'Host': 'www.instagram.com',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
    'X-Mid': mid_value,
    'X-Ig-Www-Claim': '0',
    'Accept-Language': 'de-DE',
    'Sec-Ch-Ua-Platform-Version': '""',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Web-Device-Id': device_id,
    'Dpr': '1',
    'X-Csrftoken': csrf_token_value,
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'X-Ig-App-Id': '936619743392459',
    'Sec-Ch-Prefers-Color-Scheme': 'light',
    'Sec-Ch-Ua-Mobile': '?0',
    'X-Instagram-Ajax': '1014580710',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
    'Viewport-Width': '1278',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Asbd-Id': '129477',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav',
    'Priority': 'u=1, i',
}

data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:10:1719696829:AZRQACoI4t/YVwcVeTIfrudbIu6C8lLugcOTNh7vQtdWW2l9BZLX7D/QlCc7a9IMA3U+XCPYBjjzIYUvUZtFlvF7DJafGCYhGuMuVsGFA3S1eBblOzTw0I18jjbn4c0rxoePu4CK3hioCoqf',
    'optIntoOneTap': 'false',
    'queryParams': '{"next":"/login/","source":"desktop_nav"}',
    'trustedDeviceRecords': '{}',
    'username': username,
}

response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
