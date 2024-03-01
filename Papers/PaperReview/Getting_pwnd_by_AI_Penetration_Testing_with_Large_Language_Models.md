## Getting pwn’d by AI: Penetration Testing with Large Language Models (Dec. 2023)

| Resources	|
|----------|
| [Database](https://dl-acm-org.ezproxy.semo.edu:2443/doi/10.1145/3611643.3613083) |
| DOI: 10.1145/3611643.3613083) |
| [PDF](https://dl-acm-org.ezproxy.semo.edu:2443/doi/pdf/10.1145/3611643.3613083) |

### Goal: This paper explores the potential use of large-language models, such as GPT3.5, to augment penetration testers with AI sparring partners. 

We explore two distinct use cases: high-level task planning for security testing assignments and low level vulnerability hunting within a vulnerable virtual machine
	
	
## Main Topics: (State of the Art)

### Approach

Use Cases:
(1) typical questions asked by pen-testers (“what is a good attack methodology”, e.g., “how to attack Active Directory”)
(2) low level search for techniques and corresponding procedures

Asked AgentGPT to “Become domain admin in an Active Directory” --> generated document contained highly realistic attack vectors such as password spraying, Kerberoasting, AS-REP roasting, exploiting Active Directory Certificate Services, abusing unconstrained delegation or exploiting group policies

Next, tasked AutoGPT to devise an external penetration testing plan for that company --> standard methods such as performing a network vulnerability scan, performing OSINT/user enumeration, and performing phishing against identified users

Next, further inquire -->  AutoGPT was able to crawl the
company’s web page and identify potential phishing targets (users and their email addresses) but declined to perform any “real” network security scan or perform phishing operations due to its ethical filters

### Solutions
Issue: lack of personnel

Solution: AI

#### Large language models (LLMs) - ChatCPT or GPT3.5

Experimented asking LLM to help design penetration tests for both generic scenarios and concrete target organization

* Use: help design penetration tests, generate phishing or vishing messages, automated report generation (for pen-test and red teaming)
* should be able to cover the whole TTP spectrum 
	* select suitable tactics and corresponding techniques
	* given an employed tactic, derive feasible techniques and procedures

### Tools

AI
* GPT3.5
* ChatGPT (uses prompts)
* llama.cpp
* AutoGPT (creates prompts - requires less user engineering)
* BabyAGI (task generation, planning, and execution)


#### MITRE ATT&CK: curated database of knowledge about threat actors in the cybersecurity domain
* covers different tactics, techniques, and procedures

**T** - Tactics
* describes high-level objectives an adversary intends to achieve (e.g. reconnaissance, privilege escalation or collection)
**T** - Techniques
* each is a way to achieve a tactic (e.g. Abuse Elevation Control Mechanism: Sudo and Sudo Caching)
**P** - Procedures
* specific details of how an adversary executes a technique

* Training a new LLM is prohibitively expensive for most researchers, but existing LLMs can be refined or fine-tuned to specific use cases for feasible costs
*  Prompts have to be carefully prepared

	
### Methods (ex: Raspberry Pi)
To showcase low-level guidance, we integrated GPT3.5 with a vulnerable virtual machine and allowed it to analyze the machine for vulnerabilities and suggest attack vectors

### Misc

#### (Tools) llama.cpp
* makes use of small-scale models (up to 13b parameters) feasible on consumer-grade hardware.
* models can be run without any cloud/API costs
* are not subject to any server-side moderation or censorship.

#### (Tools) [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT)  
* auto-generating sequences of instructions by leveraging LLMs to create the prompt that is subsequently used to query the LLM
* allows users to provide concise initial questions -- less of a need for manual prompt engineering
* issue: can invent facts that seem statistically plausible
* integrates web-based queries and optional human-provided feedback during its operation

#### (Tools) BabyAGI

[Website](https://github.com/yoheinakajima/babyagi)

* focused on automated task generation, planning, and execution
* provides a “pareddown” version of 

Autonomous Task Execution Agents 
* take tasks from the task queue, execute them, and add new information to a memory store
* identifies new subsequent tasks that are pushed upon the task queue and are eventually executed

#### (Tools) hackingBuddyGPT

[github](https://github.com/ipa-lab/hackingBuddyGPT)

Purpose: allow for realistic evaluation

* Python script that uses SSH to connect to a deliberately vulnerable lin.security Linux virtual machine
* Uses GPT3.5-turbo
* uses command output to identify potential security vulnerabilities (and provide exploitation example)
* suggested system commands were based upon pattern-matching and not on a deeper understanding of the Linux system or on model building
* The ethics filter was infrequently triggered (triggered more when asking "detail additional vulnerabilities")

Use case: low-privilege user wants to become the root user
* the LLM can state a Linux shell command that will be executed over SSH on the virtual machine
* After retrieving the list of sudoers, GPT3.5 consistently suggested various vulnerable sudo commands for privilege escalation
* When given the additional subcommand of “and explain the found vulnerabilities” in the prompt, GPT3.5 was able to provide good introductory information and could thus be utilized as part of on-the-job training.

Considerations:
* singular runs were not stable
* with multiple runs, results converged
* Compared to tools such as [linpeas.sh](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS), LLMs seem to be less deterministic
* switching from OpenAI to one of the locally running LLMs would remove all server-side ethics checks
* Using LLMs to generate and optimize the prompts themselves, similar to AutoGPT, might improve their effectiveness (current is static and manual)


### Other Documents Referenced

#### [Mitre att&ck: Design and philosophy (2018)](https://www.mitre.org/news-insights/publication/mitre-attck-design-and-philosophy)

Citation: Blake E Strom, Andy Applebaum, Doug P Miller, Kathryn C Nickels, Adam G
Pennington, and Cody B Thomas. 2018. Mitre att&ck: Design and philosophy. In
Technical report. The MITRE Corporation

[PDF](https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf) 
