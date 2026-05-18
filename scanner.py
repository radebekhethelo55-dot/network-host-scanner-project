import subprocess
from datetime import datetime

def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "500", ip],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except:
        return False

def scan_network(base_ip, start=1, end=20):
    print(f"\n{'='*40}")
    print(f" Network Scanner | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*40}\n")
    
    active_hosts = []
    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        if ping_host(ip):
            print(f"[+] HOST UP: {ip}")
            active_hosts.append(ip)
        else:
            print(f"[-] No response: {ip}")
    
    print(f"\n[*] Scan complete. {len(active_hosts)} host(s) found.")

if __name__ == "__main__":
    scan_network("192.168.1", 1, 20)