import socket
import subprocess
import time

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return None

def ping_server(ip):
    try:
        response = subprocess.check_output(['ping', '-n', '1', ip])  # Use 'ping' command
        return f"Server {ip} is online."
    except subprocess.CalledProcessError:
        return f"Server {ip} is offline."

if __name__ == "__main__":
    url = input("Enter a URL: ")
    ip = get_ip_address(url)

    if ip:
        print(f"IP address of {url}: {ip}")
        while True:
            ping_result = ping_server(ip)
            print(ping_result)
            time.sleep(0.5)  # Wait for 0.5 second before the next ping
    else:
        print(f"Unable to resolve the host: {url}")
