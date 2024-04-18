
import re
import csv

# Parse the output to extract IPv4 addresses and subnet masks
ipv4_subnet_data = re.findall(r'IPv4 Address\. . . . . . . . . . . : ([0-9.]+).*\n\s+Subnet Mask . . . . . . . . . . . : ([0-9.]+)', output)

# Write the data to a CSV file
with open('network_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['IPv4 Address', 'Subnet Mask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for ipv4, subnet_mask in ipv4_subnet_data:
        writer.writerow({'IPv4 Address': ipv4, 'Subnet Mask': subnet_mask})
