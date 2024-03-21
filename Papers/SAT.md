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


<br>
----

<br>
<a id="approach"></a>
## Approach


	

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
	
	Definition: web vulnerability checker

	Goal: 

	Provides:
	
	Use: Exploits XSS, SQL injections, Host Header Injection, and over 3000 other web vulnerabilities

	Additional Info:

<br>

<a id="hp-webinspect"></a>
**HP WebInspect (Commerical Scanner):**
	
	Definition: launch attacks on web systems

	Goal: 

	Provides: 
	
	Exploit: 

<br>

<a id="netsparker"></a>
**NetSparker (Commerical Scanner):**
	
	Definition: web scanner to discover web vulnerabilities

	Goal: 

	Provides:
	
	Attacks: XSS and SQLi
	
	Additional Info:

<br>

<a id="appscan"></a>
**AppScan (Commerical Scanner):**
	
	Definition: Provides centralized control several additional functionalities such as advanced application scanning, remediation capabilities, enterprise application security status metrics along seamless integration with AppScan Standard.

	Goal: 

	Provides: user's administration
	
	Attacks: 
	
	Additional Info:

<br>

<a id="nessus"></a>
**Nessus (Commerical Scanner):**
	
	Definition: 

	Goal: detect multiple security vulnerabilities in the OS of targeted hosts [18], software patches, and services.

	Provides:
	
	Attacks: 
	
	Additional Info:
	
		- has hundreds of plugins that can be employed for detailed and customized scans.

<br>
<a id="zap"></a>
**ZAP (Open-Source Scanner):**
	
	Definition: web security assessment tool

	Goal: 

	Provides: 
	
	Attacks: 
	
	Additional Info:

<br>

<a id="nikto"></a>
**Nikto (Open-Source Scanner):**
	
	Definition: 

	Goal: execute and scan for multiple items including malicious files/ programs, and outdated versions in both software libraries and web servers.

	Provides: 
			- scan configuration files of web servers (ex: multiple index files, server fingerprinting, and HTTP calls settings)

	Attacks: 
	
	Additional Info:

<br>

<a id="w3af"></a>
**W3af (Open-Source Scanner):**
	
	Definition: Web Application Attack and Audit Framework

	Goal: detect and exploit web application vulnerabilities

	Provides: 
	
	Attacks: 
	
	Additional Info:
		
		available as command line and graphical interface
		
		aka Metasploit of web
		
		uses black-box technique

<br>

<a id="wapiti"></a>
**Wapiti (Open-Source Scanner):**
	
	Definition: 

	Goal: automates audit process

	Provides: 
	
	Attacks: (detects) Injection, CSS, Command Execution Attacks, CRLF Injection, and File Disclosure
	
	Additional Info:
	
		generic command-line tool
		
		requires minimum user interaction

<br>

<a id="arachni"></a>
**Arachni (Open-Source Scanner):**
	
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

	Goal: verify attack vectors and detect vuln (authentication, injection, and security misconfigurations)

	Provides: 
	
	Attacks: 
	
	Additional Info:
	
		Java-based


<br>
----

## Other Documents Referenced


	
