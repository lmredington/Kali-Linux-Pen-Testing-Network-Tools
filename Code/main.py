# Latest update: 4/16/2024 - 4/17: adding requirements

'''
HAVE \logs created

Installs: 
sudo apt install python3
sudo apt install net-tools
sudo apt install nmap
X hackingBuddyGPT (reference Requirements_instructions.md)
X OpenAI (reference Requirements_instructions.md)
X git clone https://github.com/lmredington/AutoGPT.git
    sudo apt install python3-pip
    sudo apt install python3-click
    sudo apt install curl
sudo apt install nuclei
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh

Misc:
Have OpenAI account (min. Tier 1)

'''

'''

Commands:
nuclei -silent -u 192.168.56.115            https://github.com/projectdiscovery/nuclei
sudo ./linpeas.sh -t                net and host discover/scan


'''

import re
import csv
import subprocess
import os
import xml.etree.ElementTree as ET

## Run a Command
def run_command(command):
    print("\nRunning ", command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        # Command was successful
        print("Output:", output.decode())
        print("Command executed successfully\n")
        
    else:
        # Command failed
        print("Error output:", error.decode())
        print(f"Error executing command. Return code: {return_code}")
        
    return return_code, output.decode()

## Get CIDR Notation
def ip_subnet_to_cidr(ip_address, subnet_mask):
    # Convert IP address and subnet mask to binary strings
    ip_binary = ''.join(format(int(x), '08b') for x in ip_address.split('.'))
    subnet_binary = ''.join(format(int(x), '08b') for x in subnet_mask.split('.'))
    
    # Count the number of significant bits in the subnet mask
    cidr_count = sum([1 for bit in subnet_binary if bit == '1'])
    
    # Create the CIDR notation
    cidr_notation = f"{ip_address}/{cidr_count}"
    
    return cidr_notation

## Get Host Per Network
def extract_host_ip(host_data, xml_file):
    # Parse the XML content
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate over each 'host' element in the XML
    for host in root.findall('.//host'):
        # Extract IPv4 address
        address_elem = host.find("./address[@addrtype='ipv4']")
        ipv4 = address_elem.attrib['addr'] if address_elem is not None else "n\a"
    
        # Extract hostname
        hostname_elem = host.find("./hostnames/hostname")
        hostname = hostname_elem.attrib['name'] if hostname_elem is not None else None
        
    
        # If hostname is not available, extract vendor information
        if not hostname:
            address_mac_elem = host.find("./address[@addrtype='mac']")
            vendor = address_mac_elem.attrib['vendor'] if address_mac_elem is not None else None
            host_data.append((ipv4, vendor))
        else:
            host_data.append((ipv4, hostname))

    return host_data

# ======================================BEGIN MAIN CODE========================================= #

#--------------Init Variables---------------#
Windows = 1

network_ip_data = []
network_host_data = []

#---------------Get Network IP addresses------------#

if(Windows==1):
    ip_command = "ipconfig /all > logs\ipconfig_output.xml"
    result, output = run_command(ip_command)
else:
    ip_command = "ifconfig /all > logs\ipconfig_output.xml"

# Get IP and subnet mask
with open('logs/ipconfig_output.xml', 'r') as file: # Read the content of the ipconfig_output.xml file
    xml_content = file.read()
    # Parse the output to extract IPv4 addresses and subnet masks
    ipv4_subnet_data = re.findall(r'IPv4 Address\. . . . . . . . . . . : ([0-9.]+).*\n\s+Subnet Mask . . . . . . . . . . . : ([0-9.]+)', xml_content)

# Get CIDR
for ipv4, subnet_mask in ipv4_subnet_data:
    cidr = ip_subnet_to_cidr(ipv4, subnet_mask)     # Get CIDR
    print("\n"+cidr)                                # Print each CIDR found into terminal
    network_ip_data.append((ipv4, subnet_mask, cidr))   # Add IP address, Subnet_mask, and CIDR to network_data

## Get Host IPs
for ipv4, subnet_mask, cidr in network_ip_data:  
    network_host_scan_file = "logs/"+ipv4+"_host_scan.xml"                              # Set Output file name
    host_discover_command = "nmap -T5 -sn -oX "+network_host_scan_file+" "+cidr     # Set Host Discover Nmap Command
    run_command(host_discover_command)
    network_host_data = extract_host_ip(network_host_data, network_host_scan_file)              # Save data into host_data

#for ipv4, hostname in network_host_data:
 #   print(hostname+"\t"+ipv4+"\n")
    
print(network_host_data)
print("\n")
print(network_ip_data)
    
#----------------------Get Host Details----------------------#

for ipv4, hostname in network_host_data:
    host_scan_file = "logs/"+ipv4+"nmap.xml"
    host_command = "nmap -v -A -oX "+host_scan_file+" "+ipv4

    '''
        * nmap -v -A 192.168.1.116
        * nmap -Pn -O --script vuln -oA nmapscanCVE 192.168.1.71
        * nmap -Pn -O --script vuln -oA nmapscanCVE 192.168.1.24    -- could give tcp/ip fingerprint, ports, state, service
        * nmap -sV --version-trace 192.168.1.71 -- Gave DNS server
        * nmap -Pn --script-trace 192.168.1.10
        * nmap -v -A scanme.nmap.org -- LOTS OF INFO
        * nmap -Pn -iflist
        '''

#----------------------Print Hosts----------------------#

print("Hosts Detected:\n")
for ipv4 in network_ip_data:
    print(ipv4)   
    
#---------------WRITE DATA TO CSV FILE------------#
    
with open('network_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['IPv4 Address', 'Subnet Mask', 'CIDR', 'Hostname']    # Setup Field Names of CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for ipv4, subnet_mask, cidr in network_ip_data:         # For each Network IP
        writer.writerow({'IPv4 Address': ipv4, 
                         'Subnet Mask': subnet_mask, 
                         'CIDR': cidr})                     # Save Network IP data into CSV (IP, Subnet, CIDR)
        print('IPv4 Address: '+ipv4+',  Subnet Mask: '+subnet_mask+',   CIDR: '+cidr+'\n')      # Print data
    for ipv4, hostname in network_host_data:                # For each Host
        writer.writerow({'IPv4 Address': ipv4,
                         'Hostname': hostname})             # Save Hostname and IP