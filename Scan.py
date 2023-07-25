import socket

port_range = range(1, 1025)
openPorts = []
count = 0

def scanner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.05)
            result = s.connect_ex((host, port))
            if result == 0:
                openPorts.append(port)
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":

    target = input("Enter the target host (domain name or IP): ")

    print("Scanning...")

    for port in port_range:
        scanner(target, port)

    for port in openPorts:
        print(f"Port {port} is open.")
