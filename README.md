## Usage

Ensure you provide accurate information about the network, subnet mask, and default gateway before executing the code.

### Network Variables

- `network = '10.2.2.0/24'`: Network address.
- `subnet_mask = '255.255.255.255'`: Subnet mask.
- `default_gateway = '10.13.28.0'`: Default gateway.

### Execution

The loop traverses all possible IP addresses within the specified network using `subnet.hosts()`. Then, for each IP address, it executes a ping command using the system's subprocess. If there's a response from the device to the ping, it prints that the IP address is active.

## Known Issues

There's a potential inconsistency in the subnet mask definition for the address '10.82.23.0/24', which may cause unexpected results when pinging addresses. Additionally, the format of the default gateway (`default_gateway`) doesn't correspond to a valid IP address.

Make sure to understand these issues before using the script.

---

# Sniffing_HTTP.py

This is a Python script to check if a specific port on an IP is open and to sniff HTTP traffic on port 80 using the Scapy module.

## How to Use

### Prerequisites

- Python 3.x
- Installed Scapy (`pip install scapy`)

### Running the Script

1. Clone the repository:
   ```bash
   git clone https://github.com/NickDwtyayOficial/community-server/tree/main
   cd community-server

----

# Get Nameservers from Domain
#Namesrv.py
This Python script retrieves the nameservers associated with a domain using the `socket` and `whois` libraries.

## How It Works

The script defines a function `get_nameservers(domain_name)` that does the following:

1. Uses `socket.gethostbyname(domain_name)` to obtain the IP address associated with the domain.
2. Utilizes `whois.whois(domain_name)` to retrieve registration information for the domain, including the nameservers.
3. Checks if the nameservers are returned as a list or a single server and processes the result accordingly.

## Example Usage

```python
import socket
import whois

def get_nameservers(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    w = whois.whois(domain_name)
    if isinstance(w.name_servers, list):
        return w.name_servers
    else:
        return [w.name_servers]

# Example Usage
domain = "nickdwtyay.com.br"
nameservers = get_nameservers(domain)
print(f"Nameservers for the domain {domain}:")
for ns in nameservers:
    print(ns)




# community-server
community server - NICK DWTYAY Ltd
