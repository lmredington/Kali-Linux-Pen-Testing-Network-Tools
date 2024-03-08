# Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

| Resources	|
|----------|
| [Database](https://doi-org.ezproxy.semo.edu:2443/10.1109/IDAACS58523.2023.10348918) |
| DOI: 10.1109/IDAACS58523.2023.10348918 |
| [PDF](https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=10348918) 	|

----

### Goal: analyze existing algorithms and software capable of automatically scanning web applications

**Goal 1:** Analysis of algorithms and software tools for scanning web applications with the aim of detecting vulnerabilities according to OWASP top 10

**Goal 2:** Overview of existing vulnerabilities in web applications

**Goal 3:** main approaches and methods used for their detection

<br>

### Additional Notes

**Exploitable:**
- incorrect/insecure programming


<br>

----

<br>

<a id="approach"></a>
## Approach

**Vulnerability Scanner Types:**
- [Static scanners](#static-scanner)
-  [Dynamic scanners](#dynamic-scanner)
	


<a id="tools"></a>
## Tools

**Dictionary Search Tools:**
- [SQLMap](#sqlmap): SQL injection vulnerability automated detection
- [Blisqy](#blisqy): Find and exploiting Time-based Blind SQL injection vulnerabilities in HTTP headers
- [jSQL Injection](#jsql-injection): Detect and exploit SQL injection vulnerabilities in web applications that use SQL databases

**Insecure Design Tool**
- [Checkov](#checkov): 
- [Trivy](#trivy): 
- [Snyk](#snyk): 
- [Nmap](#nmap): 
- [Metasploit Framework](#metasploit-framework): 


<br>

<a id="equipment"></a>
## Equipment (ex: Raspberry Pi)  





<br>

<a id="methods"></a>
## Methods

**Attacks:**
- XSS-attacks
- SQL injections 
- NoSQL injections
- Blind SQL injections
- LDAP injections

<br>

**Vulnerability Search Schemes (Code Injection):**
- [Dictionary](#dictionary-scheme)
	- [Error-based](#error-based)
	- [Union-based](#union-based)


<br> 

<a id="terminology"></a>
## Terminology



<br>

----

## Misc

<a id="dynamic-scanner"></a>
**Dynamic Scanners (Vulnerability Scanner Type):**
	- where access to the application or infrastructure source code is not available
	- Example: network scanner (Nmap suggested)

<br>

<a id="static-scanner"></a>
**Static scanners (Vulnerability Scanner Type):**
	- use if infrastructure built using infrastructure as code (IaC) tools
	- Examples: Checkov, Trivy, and Snyk

<br>

<a id="dictionary-scheme"></a>
**Dictionary** (Code Injection Vuln. Search Scheme):
	
	Purpose: identify typical vulnerabilities in web applications and databases that lack proper protection or sanitization
	
	Exploits by: attempting to inject known malicious code or payloads from a predefined dictionary into the target application or database to identify if there is a vulnerability
	
	Methods:
		- Error-based
		- Time-based injection
		- Union-based
		- Boolean-based
		
<br>

<a id="error-based"></a>
**Error-Based (Dictionary Scheme Method):**

	Definition: injecting specially crafted input (Ex: specific characters or SQL statements)
	
	Goal: trigger an error response from the database
	
	Provides: additional information that can be useful for further attacks or understanding the structure of the database. 

<br>

<a id="union-based"></a>
**Union-based (Dictionary Scheme Method):**

	Definition: leveraging the UNION operator in SQL queries to combine the results of multiple SELECT statements

	Goal: accessing unauthorized data or bypassing authentication mechanisms

	Provides: additional information from the database

<br>

<a id="sqlmap"></a>
**SQLMap (Dictionary Search Tool):**

	Reference Page: https://sqlmap.org
	
	Purpose: detection of SQL injection vulnerabilities
	
	Pros: 
		- Automated
		- Most popular compared to counterparts
		- Does not require attacker to have in-depth knowledge
	
	Additional Notes:
		
		Types of Vulnerabilities Detected:
			- Error-Based Injection
			- Time-Based Injection
			- Boolean-Based Injection
			- Union-Based Injection
			- Command Injection
		
<br>

<a id="blisqy"></a>
**Blisqy (Dictionary Search Tool):**

	Reference Page: https://www.hackingloops.com/penetration-testing-forblind-sql-injection-using-bbqsql)
	
	Purpose: finding and exploiting Time-based Blind SQL injection vulnerabilities in HTTP headers
		
	Pros: 
		- Customizable 
		
	Cons:
		- Only supports MySQL/MariaDB
	
	Additional Notes:
		- Modules provided can be imported into other Python-based scripts, allowing users to create their own scripts for specific penetration testing tasks
		- Uses blind SQL injection
		- Exploits by: slow extraction of data from a database
		
<br>

<a id="jsql-injection"></a>
**jSQL Injection (Dictionary Search Tool):**

	Reference Page: https://www.kali.org/tools/jsql
	
	Purpose: Detecting and exploiting SQL injection vulnerabilities in web applications that use SQL databases
		
	Pros: 
		- Open-source 
		- Automate injection attacks and exploits
		- Features:
			- Automated Enumeration and Cloning Attacks
			- Scanning Subnets and IP Lists
			- Password Cracking
			- JavaScript Injection Techniques
			- Timing-Based Attacks
	
	Additional Notes:
		- Range of features to automate injection attacks and exploit default configuration weaknesses in databases.
		- exploits time delays in responses to infer the success or failure of injected code

<br>


<a id="checkov"></a>
**Checkov (Insecure Design Tool):**

	Reference Page:  https://www.checkov.io/1.Welcome/Quick%20Start.html
	
	Purpose: Identify and prevent security misconfigurations in cloud environments
		
	Pros: 
		- Open-source
		- Built-in support for popular integrated development environments (IDEs) (Ex: Visual Studio Code and JetBrains IDEs)
		- Provides support for CI/CD (for free systems & proprietary resources)
		- Supports AWS CodePipeline and AWS CodeBuild
	
	Additional Notes:
		- Static analysis tool 
		
		Main focus: scanning IaC templates written in popular formats such as Terraform, AWS CloudFormation, and Kubernetes YAML files
		
		Designed for: infrastructure as code (IaC) security
<br>

<a id="trivy"></a>
**Trivy (Insecure Design Tool):**

	Reference Page:  https://aquasecurity.github.io/trivy/v0.19.2
	
	Purpose: 
		
	Pros: 
		- 
		
	Cons:
	
	Additional Notes:
		
		
<br>

<a id="snyk"></a>
**Snyk (Insecure Design Tool):**

	Reference Page: https://security.snyk.io
	
	Purpose: 
		
	Pros: 
		- 
		
	Cons:
		- 
	
	Additional Notes:
		
		
<br>

<a id="nmap"></a>
**Nmap (Insecure Design Tool):**

	Reference Page: https://nmap.org
	
	Purpose: 
		
	Pros: 
		- 
		
	Cons:
		- 
	
	Additional Notes:
		
		
<br>

<a id="metasploit-framework"></a>
**Metasploit Framework (Insecure Design Tool):**

	Reference Page: https://www.metasploit.com
	
	Purpose: 
		
	Pros: 
		- 
		
	Cons:
		- 
	
	Additional Notes:
		
		
<br>

----

## Other Documents Referenced

**Architecture and model of neural network based service for choice of the penetration testing tools, International Journal of Computing (2021)** 

	A. Tetskyi, V. Kharchenko, D. Uzun, A. Nechausov,
	
