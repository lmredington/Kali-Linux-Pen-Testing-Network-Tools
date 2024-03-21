# Referenced Tools

| Tools				| Phases Used												|  Interface 	| Features 																																											| 	Example Commands						| Referenced Material 								|
|-------------------|-----------------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------|
| AutoGPT			| Reconnaissance & Planning[4]								| --- 			| Devise an external penetration testing plan; identify potential phishing targets (on Web page)																					| --- 										| Mentioned: [4]									| 
| Blisqy			| Scanning, Exploitation									| --- 			| Find and exploit Time-based Blind SQL injection vulnerabilities in HTTP headers																									| --- 										| Analysis: [6]										| 
| Censys			| * Bullet 1 <br> * Bullet 2 <br> * Bullet 3 | --- 			| Vulnerability detection and filtering													 																							| --- 										| Used: [2]											| 
| Checkov			| Scanning													| --- 			| --- 																																												| --- 										| Mentioned: [6]									| 
| CyberCheck		| Reconnaissance & Planning, Scanning						| --- 			| Open-Source usercustomizable OSINT and Web Vulnerability scanner													 																| --- 										| Used: [2]											| 
| dig				| Reconnaissance)[5]										| --- 			| DNS name servers information; Troubleshoot DNS problems													 																		| --- 										| Analysis: [5]										| 
| Dirbuster			| Exploitation[3]											| --- 			| Directory Enumeration													 																											| --- 										| Used: [1]											| 
| Enum4linux		|															| --- 			| 																																													| --- 										| Used: [1]											| 
| FFUF				|															| --- 			| 																																													| --- 										| Used: [1]											| 
| Footholder		|															| --- 			| Access tools; Tool operation instruction 																																			| --- 										| Used: [1]											| 
| FTP				| Service Enumeration										| --- 			| 																																													| --- 										| Used: [1]											| 
| Gobuster			| Exploitation												| --- 			| Directory Enumeration													 																											| --- 										| Used: [1]											| 
| hackingBuddyGPT	| Gaining Access[4], Retaining Access[4], Exploitation[4] 	| --- 			| Gain root privileges in VM (produce commands), identify potential security vulnerabilities; provide exploitation examples					 										| --- 										| Used: [4]											| 
| Hydra				| Exploitation[3]											| --- 			| Brute Forcing													 																													| --- 										| Used: [1]; Mentioned: [3]							| 
| jSQL Injection	| Scanning, Exploitation									| --- 			| Detect and exploit SQL injection vulnerabilities in web applications that use SQL databases																						| --- 										| Analysis: [6]										| 
| Maltego			| Reconnaissance											| --- 			| OSINT tool for reconnaissance													 																									| --- 										| Analysis: [3]; Used: [2]							|
| Metasploit 		| Gaining Access[3], Exploitation[3]						| --- 			| discovery, exploitation, and validation of vulnerabilities [6]; Leverge known exploits and techniques, simulate real-world attacks; Gain system access through shell-based access	| 											| Used: [1]; Mentioned: [3],[6]						|
| MySQL				|															| --- 			| 																																													|  											| Used: [1]											| 
| NetDiscover 		| Reconnaissance & Planning[1], Network Enumeration[1] 		| --- 			| target IP													 																														| 											| Used: [1]											|
| Nexpose			| Scanning[3]												| --- 			| 																																													|  											| Mentioned: [3]									| 
| Nmap 				| Reconnaissance & Planning[1, 5], Network Enumeration[1] 	| --- 			| ports, services, OS, fundamental vulnerabilities, host detection 																													| "nmap disperindag.xxxprov.id"[5] 			| Analysis: [3],[5]; Used:[2],[3]; Mentioned: [6] 	|
| nslookup			| Reconnaissance[5]											| --- 			| DNS lookup; server and address information of website 																															| "nslookup disperindog.xxxprov.go.id"[5] 	| Analysis: [5]										| 
| Open VAS			| Scanning[3]												| --- 			| Vulnerability Scanner - produces report, denoting severity 																														| 											| Analysis: [3]										| 
| Paros				|															| --- 			| 																																													| 											| Mentioned: [5]									| 
| Shodan			|															| --- 			| IoT device search engine, vulnerability scanner, and port scanning 																												|  											| Used: [2]											| 
| SQLMap			| Scanning													| --- 			| Automated detection of SQL injection vulnerabilities 																																|  											| Analysis: [6]										| 
| Snyk				| Scanning, Vuln Analysis									| --- 			| (in Containers and IaC:) Scan and prioritize information security, Detect vulnerabilities in modules hosted and/or not hosted in a tested repository, Identify vulnerabilities	| ---										| Mentioned: [6]									| 
| SSH				|															| --- 			| 																																													| ---										| Used: [1]											| 
| Telnet			| Service Enumeration										| --- 			| 																																													| ---										| Used: [1]											| 
| Trivy				| Scanning [6]												| --- 			| Analyzes layers and dependencies within a container image to identify potential security issues, returns detailed report					 										| ---										| Mentioned: [6]									| 
| Wireshark			| Exploitation[3]											| --- 			| Capture network packets 																																							| ---										| Mentioned: [3]									| 
| ZapBurp			| Access (Vuln. Analysis Phase)[3]							| --- 			| Perform vulnerability scan; Provide mitigation measures 																															| ---										| Analysis: [3]										| 


<br> 

| Tools				| Phases Used												|  Interface 	| Features 																																											| 	Example Commands						| Referenced Material 								|
|-------------------|-----------------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------|
| Acunetix			|															| --- 			| 																																													| ---										| Analysis: [7]; Mentioned: [5]						| 
| HP Web Inspect	|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| NetSparker		|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| APPSCAN			|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| Nessus			| Scanning[3]												| --- 			| 																																													| ---										| Analysis: [7]; Mentioned: [3]						| 
| OWASP ZAP			| Vulnerability Analysis[5]									| --- 			| Identify Vulnerabilities on target website 																																		| ---										| Analysis: [7]; Mentioned: [5]						| 
| Nikto				|															| --- 			| 																																													| ---										| Analysis: [7]; Used: [1]							| 
| W3af				|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| Wapiti			|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| Arachni			|															| --- 			| 																																													| ---										| Analysis: [7]										| 
| Burp Suite		| Exploitation[3]											| --- 			| 																																													| ---										| Analysis: [3], [7]; Mentioned: [2]				| 
| ZAP				|															| --- 			| 																																													| ---										| Analysis: [7]										| 



[1] Footholder

[2] CyberCheck

[3] An Analysis of Vulnerability Scanners in Web Applications for VAPT

[4] AI

[5] Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website

[6] Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

[7] SAT