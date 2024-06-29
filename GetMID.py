import requests
import re
import urllib3

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Get_MID(csrf_token_value):
    cookies = {
        'csrftoken': csrf_token_value,
    }

    headers = {
        'Host': 'www.instagram.com',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
        'X-Ig-Www-Claim': '0',
        'Accept-Language': 'de-DE',
        'Sec-Ch-Ua-Platform-Version': '""',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Web-Device-Id': '263003BD-948B-452A-9B51-82038EB5D043',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'X-Csrftoken': csrf_token_value,
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Ig-App-Id': '936619743392459',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
        'Accept': '*/*',
        'X-Asbd-Id': '129477',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.instagram.com/',
        'Priority': 'u=1, i',
    }

    response = requests.get('https://www.instagram.com/api/v1/web/data/shared_data/', cookies=cookies, headers=headers, verify=False)

    # Extract the mid value from the Set-Cookie header
    set_cookie_header = response.headers.get('Set-Cookie', '')
    mid = re.search(r'mid=([^;]+)', set_cookie_header)

    mid_value = None
    if mid:
        mid_value = mid.group(1)
        print("Is Printet from GetMID.py mid:", mid_value)
    else:
        print("mid nicht gefunden.")
    
    return mid_value
