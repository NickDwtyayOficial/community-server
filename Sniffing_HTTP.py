    import socket
from scapy.all import *

def get_server_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = f"Sistema operacional: {socket.getfqdn()}, {socket.gethostbyname_ex(hostname)[-1]}"
    return f"Nome do host: {hostname}\nEndereço IP: {ip_address}\n{os_info}"

def sniff_http_traffic(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        if packet.haslayer(Raw) and packet[TCP].dport == 80:
            http_payload = str(packet[Raw].load)
            if 'HTTP' in http_payload:
                print(f"Src: {src_ip}:{src_port} --> Dst: {dst_ip}:{dst_port}\nHTTP Payload: {http_payload}\n")

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((ip, port))
        return f"A porta {port} está ABERTA."
    except socket.error:
        return f"A porta {port} está FECHADA."

if __name__ == "__main__":
    server_info = get_server_info()
    print(server_info)

    # Adicione aqui a lógica para chamar a função de farejamento de tráfego
    sniff(prn=sniff_http_traffic, filter="tcp port 80", store=0)

    ip_address = '192.168.1.1'
    port_number = 80
    result = check_port(ip_address, port_number)
    print(result)
