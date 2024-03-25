# SAT: Integrated Multi-agent Blackbox Security Assessment Tool using Machine Learning (March 2022)
 
| Resources	|
|----------|
| [Database](https://doi-org.ezproxy.semo.edu:2443/10.1109/ICAI55435.2022.9773750) |
| DOI: 10.1109/ICAI55435.2022.9773750 |
| [PDF](https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=9773750) 	|

----

### Goal: Evaluate publicly available web vulnerability scanners and propose an Integrated Multi-Agent Blackbox Security Assessment Tool (SAT)

**Goal 1:** Evaluation of publicly available web vulnerability scanners is performed against the top ten OWASP vulnerabilities and their performance is measured on the precision of their results

**Goal 2:** Proposed an Integrated Multi-Agent Blackbox Security Assessment Tool (SAT) for the security assessment of web applications


<br>
### Additional Notes

Changes in configuration settings are adequate to affix only 17% of vulnerabilities, most of those have a low severity level. 

On average, 33 vulnerabilities are found in each web application, among 6 of those are of high severity.

Examples of attacks: CSS, SQLi, remote code execution, file inclusion, XSS

Automated tools have to check every possible flaw in web app

Access Control flaws, hardcoded back-door, and identification of multi cover attack is **difficult** to detect and **harder** to detect with these tools

**Tool Assessment Parameters**
- [Quality of Crawling (QoC)](#qoc)
- [Quality of Fuzzing (QoF)](#qof)
- **Quality of Analyzing (QoA)**

**Precision Rate:** percentage of correctly detected vulnerabilities

<br>
----

<br>
<a id="approach"></a>
## Approach
* Black-box
	- higher possibility scanner generates falsify detected vulnerabilities
	
### SAT

**Process Initiator (PI)**
	
	Def: User input targeted URL in this module.
	
	Use:  host discovery and initialization of the scanning process
	
	Additional:
	
		Unreachable hosts are screened here and further process is terminated
	
**Security Assessment Unit (SAU)**
	
	Def: performs scanning of the input web application
	
	Subsections: 
	- Scanning Engine
		- In mutual compliance with Zap, Nikto, and W3af
		- Uses Arachni Crawler and provides features for costom plugin scripts like OAuth, etc.
	- Vulnerabilities database: contains a list of all possible vulnerabilities of OWASP top 10
	- Knowledgebase
		- AI (Artificial Intelligence) based analysis engine
		- responsible to identify security trends, Information leakage and highlight compromised critical data of scanned organizations.
	

<br>
<a id="tools"></a>
## Tools

**(Mentioned by other resources):**
- AppScan
- AWVS
- NetSparker
- Vega
- W3af
- Paros
- Wapiti
- Skipfish
- Nikto
- Wfuzz
- NetSparker
- HP web inspect
- Arachni
- OWASP Zed Attack Proxy (ZAP)
- Havij
- Fimap
- Metasploit
- Acunetix
- Nexpose

<br>

**Analyzed (Commercial Scanners):**
- [Acunetix](#acunetix): web vulnerability checker
- [HP web inspect](#hp-webinspect): launch attacks on web systems
- [NetSparker](#netsparker): web scanner to discover web vulnerabilities
- [AppScan](#appscan): centralized control with additional functionalities
- [Nessus](#nessus): detect vulnerabilities in OS, software patches, and services

<br>

**Analyzed (Open-Source Scanners):**
- [ZAP](#zap): web security assessment tool
- [Nikto](#nikto):
- [W3af](#w3af): Web Application Attack and Audit Framework
- [Wapiti](#wapiti): automate audit process
- [Arachni](#arachni):
- [Burpsuite](#burpsuite): pen testing toolkit

<br>
<a id="equipment"></a>
## Equipment (ex: Raspberry Pi)  

**DVWA:** potentially vulnerable web app that is developed to test tools and professionals’ skills in a legal environmen

<br>

<a id="methods"></a>
## Methods



<br> 
----

## Misc

<a id="acunetix"></a>
**Acunetix (Commerical Scanner):**
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
| Precision (CSS & SQLi) 	| 100%			| 1 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 115 		| 115 	| 1 	|
| Broken Authentication (A2) 				| 3 		| 3		| 1 	|
| Excessive Data Exposure (A3) 				| 145  		| 145 	| 1		|
| Lack of Resources and Rate Limiting (A4) 	| 2 		| 11	| 2 	|
| Broken Function Level Authorization (A5)	| 51 		| 51	| 1	 	|
| Mass Assignment (A6) 						| 23 		| 27	| 3		|
| SecurityMisconfiguration (A7) 			| 165 		| 743 	| 7		|
| Injection (A8) 							| 133 		| 133	| 1		|
| Improper Assets Management (A9) 			| 12 		| 15	| 3		|
| Insufficient Logging and Monitoring (A10) | 65 		| 95	| 2		|

	Definition: web vulnerability checker

	Use: Exploits XSS, SQL injections, Host Header Injection, and over 3000 other web vulnerabilities
	
	Pros:
		
		Higher detection of CSS, File Injection, Sensitive Data Exposure, CSRF, and Broken Authentication vulnerabilities

	Additional Info:
	
		

<br>

<a id="hp-webinspect"></a>
**HP WebInspect (Commerical Scanner):**

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 44.1%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|
	
	Definition: launch attacks on web systems

	Goal: 

	Provides: 
	
	Exploit: 
	

<br>

<a id="netsparker"></a>
**NetSparker (Commerical Scanner):**
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 98.5%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|
	
	Definition: web scanner to discover web vulnerabilities

	Goal: 

	Provides:
	
	Attacks: XSS and SQLi
	
	Precision: 98.5% for SQLi and CSS

	
	Additional Info:

<br>

<a id="appscan"></a>
**AppScan (Commerical Scanner):**

Definition: Provides centralized control several additional functionalities such as advanced application scanning, remediation capabilities, enterprise application security status metrics along seamless integration with AppScan Standard.

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 84%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Goal: 

	Provides: user's administration
	
	Attacks: 
	
	Additional Info:
	
		84% of the detected vulnerabilities correct for SQLi and CSS vulnerabilities

<br>

<a id="nessus"></a>
**Nessus (Commerical Scanner):**

Detect multiple security vulnerabilities in the OS of targeted hosts [18], software patches, and services.

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 90.88%		| - 	|
	
| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Definition: 
	
	Provides:
	
	Attacks: 
	
	Additional Info:
	
	- has hundreds of plugins that can be employed for detailed and customized scans.

<br>
<a id="zap"></a>
**ZAP (Open-Source Scanner):**
	
Definition: web security assessment tool	

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 100%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Goal: 

	Provides: 
	
	Attacks: 
	
	Pros:
		
		Good to detect security configurations
		
		Ranked 1st for open-source tools in detecting low severity vulnerabilities
	
	Cons:
	
		Lower detection of CSS, File Injection, and Insecure Communication
	
	Additional Info:
	
		
		

<br>

<a id="nikto"></a>
**Nikto (Open-Source Scanner):**
	
Use: Execute and scan for multiple items including malicious files/ programs, and outdated versions in both software libraries and web servers.

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 71.4%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Definition: 


	Provides: 
	- scan configuration files of web servers (ex: multiple index files, server fingerprinting, and HTTP calls settings)

	Attacks: 
	
	Additional Info:

<br>

<a id="w3af"></a>
**W3af (Open-Source Scanner):**
	
Definition: Web Application Attack and Audit Framework
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 94.3%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Goal: detect and exploit web application vulnerabilities
	
	Additional Info:
		
		available as command line and graphical interface
		
		aka Metasploit of web
		
		uses black-box technique

<br>

<a id="wapiti"></a>
**Wapiti (Open-Source Scanner):**

Def: Automates audit process
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 53%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Use: detects Injection, CSS, Command Execution Attacks, CRLF Injection, and File Disclosure

	Cons: 
	
		unable to detect broken authentication and improper assets management
		
* Additional Info:
	
	- generic command-line tool
		
	- requires minimum user interaction

<br>

<a id="arachni"></a>
**Arachni (Open-Source Scanner):**
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 81.32%		| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|

	Definition: 

	Goal: 

	Provides: 
	
	Attacks: 
	
	Additional Info:
	
		Based on modular and Ruby languages
		
		Trains itself by learning from HTTP responses received during the scanning and testing during assessment
		

<br>

<a id="burpsuite"></a>
**BurpSuite (Open-Source Scanner):**
	
Definition: Penetration testing toolkit

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 98.5%			| - 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| - 		| 115 	| - 	|
| Broken Authentication (A2) 				| - 		| 3		| - 	|
| Excessive Data Exposure (A3) 				| -  		| 145 	| -		|
| Lack of Resources and Rate Limiting (A4) 	| - 		| 11	| - 	|
| Broken Function Level Authorization (A5)	| - 		| 51	| -	 	|
| Mass Assignment (A6) 						| - 		| 27	| -		|
| SecurityMisconfiguration (A7) 			| - 		| 743 	| -		|
| Injection (A8) 							| - 		| 133	| -		|
| Improper Assets Management (A9) 			| - 		| 15	| -		|
| Insufficient Logging and Monitoring (A10) | - 		| 95	| -		|
	

	Goal: verify attack vectors and detect vuln (authentication, injection, and security misconfigurations)

	Provides: 
	
	Attacks: 
	
	Pros:
	
	
	Cons:
	
		Ranked last for open-source tools in detecting low severity vulnerabilities
	
	Additional Info:
	
		Java-based
		
	

<br>

<a id="qoc"></a>
**Quality of Crawling (Tool Assessment Parameter)**

	Def: process that identifies pages of a web application that is vulnerable to a certain attack

	Determined by: number of pages crawled
	
<br>

<a id="qof"></a>
**Quality of Fuzzing (Tool Assessment Parameter)**

	Depends on: number of inputs a fuzzer enters to find certain vulnerability
	
	Inputs capable to exploit application vulnerabilities
	
<br> 

<a id="knowledgebase"></a>
**Knowledgebase (SAU Subsection)**

	Def: AI (Artificial Intelligence) based analysis engine

	Use: Identify security trends, Information leakage and highlight compromised critical data of scanned organizations.

<br>
----

## Other Documents Referenced


	
