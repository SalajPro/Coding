import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the host"

if __name__ == "__main__":
    url = input("Enter a URL: ")
    ip = get_ip_address(url)
    print(f"IP address of {url}: {ip}")
