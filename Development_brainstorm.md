# Development Brainstorm

**Use SAT framework as template. **

## Process Initiator (PI): responsible for host discovery and initialization of the scanning process of the target URL

Host discovery tools: Nmap, Netcraft, Zenmap

**(1) Produce List of Hosts/targets**

Done with PI
	
	(1) scan and get list of hosts using nmap
		
	(2) make database/spreadsheet listing each host
	(3) use nslookup to see if there is a domain - note in spreadsheet
		

**(2) Scan for vuln**

**(3) Analyze Vuln**

Use Vulnerability database:

 - [NVD API](https://nvd.nist.gov/developers/vulnerabilities) (CVSS, CVE, CPE)
 
 - [EPSS](https://www.first.org/epss/) (Likelihood of a particular vulnerability is to be exploited in the wild)
	
	ex: curl -X GET https://api.first.org/data/v1/epss?cve="+ key_attr
	
**(4) Produce Report**
 


w3af

Prerequisites
Make sure you have the following software ready before starting the installation:

Git client: sudo apt-get install git
Python 2.7, which is installed by default in most systems
Pip version 1.1: sudo apt-get install python-pip
Installation
git clone https://github.com/andresriancho/w3af.git
cd w3af/
./w3af_console
. /tmp/w3af_dependency_install.sh