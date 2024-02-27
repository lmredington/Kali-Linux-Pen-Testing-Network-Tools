# FOOTHOLDER: Collection of tools and scripts used to learn and experiment the exploitation of vulnerable machines (Apr. 2023)

### Goal: Educate users about tools and how to use them

"In this paper, we suggest the creation of a **single location** where users may access all other significant **tools** and receive **instruction** on how to operate them."
	
	
| Resources	| Link |
|----------|----------|
| Database | https://doi-org.ezproxy.semo.edu:2443/10.1109/ICNWC57852.2023.10127486 |
| DOI | 10.1109/ICNWC57852.2023.10127486 |
| PDF | https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=10127486 |
	

## Main Topics: (State of the Art)

### New approaches

Phases:

	(1) Observation (Reconnaissance): used to identify susceptible machines in order to launch attacks against them

	(2) Searching (Scanning)
		* where enumerating and scanning network or computer system occurs
		* NetDiscover: if the user is lacking the IP address of the target computer. Now that the user is associated with a network, NetDiscover will scan that network to find all of the active machines present and collect their IP addresses. The user may now identify the IP address that will be utilized for the test
		
	(3) Exploitation: method used to take control of the system

	(4) Post-exploitation: process of keeping access to or maintaining knowledge of the exploited system

	(5) Documentation: evaluation of the machine, connectivity, and weaknesses and offer control suggestions or vulnerability fixes

They advised utilizing a more requires immediate medical attention, doing port scans without looking, and carefully considering the effects of scans on network traffic, job completion time, potential effects on the victim PC, and network architecture

Most tools require root permission


### Solutions

During NMAP, learn more about ports, their services, and how to get around the susceptible service by using this as an instructional tool

This footnote lists the available tools and when the choice is made a brief explanation of the tool's features is
shown

### Tools (for reconnaissance and planning)
	* Network enumeration:
		* NMAP: evaluates the IP and delivers information on the weak device
			* gives port number of the services operating
			* `-h` tag :: list of arguments that can be used along with the basic nmap scan.
			* Common tags:
				* ‘-sV’ -- find version-trace
				* ‘-sC’ -- script-scan
				* ’-sS’ -- TCP SYN scan
				* ‘-sL’ -- Identify Hostnames

and open service that may be attacked
		* NetDiscover: used to get the target IP
			* launched to recon the internal network and offer a list of IPs nearby if the user does not have the IP
			
	* Directory enumeration:
		* Gobuster
		* Dirbuster
	* Service enumeration:
		* telnet
		* ftp
	* Brute Forcing:
		* Hydra
		
		
### Methods (ex: Raspberry Pi)

Since **KALI Machine** is the most popular ethical hacking Linux Distro, it is preferable that the programme be operating on it during the initial step of resource confirmation

### Misc
* Novices prefer the GUI model