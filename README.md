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

# community-server
community server - NICK DWTYAY Ltd
