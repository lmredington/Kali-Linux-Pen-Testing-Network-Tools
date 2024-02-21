# FOOTHOLDER: Collection of tools and scripts used to learn and experiment the exploitation of vulnerable machines (Apr. 2023)
**Database:**

	https://doi-org.ezproxy.semo.edu:2443/10.1109/ICNWC57852.2023.10127486

**PDF:**

	https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=10127486
	
	
### Overall
* Goal: educate users about tools and how to use them

	"In this paper, we suggest the creation of a **single location** where users may access all other significant **tools** and receive **instruction** on how to operate them."
* Novices prefer the GUI model
	
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
* Tools (for reconnaissance and planning)
	* Network enumeration:
		* NMAP
		* NetDiscover
			* used to get the target IP
			
	* Directory enumeration:
		* Gobuster
		* Dirbuster
	* Service enumeration:
		* telnet
		* ftp
	* Brute Forcing:
		* Hydra
		
### Methods (ex: Raspberry Pi)