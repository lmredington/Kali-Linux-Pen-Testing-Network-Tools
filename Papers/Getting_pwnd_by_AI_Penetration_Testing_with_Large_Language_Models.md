## Getting pwn’d by AI: Penetration Testing with Large Language Models (Dec. 2023)

| [Database:](https://dl-acm-org.ezproxy.semo.edu:2443/doi/10.1145/3611643.3613083) | DOI: [10.1145/3611643.3613083](https://dl.acm.org/doi/10.1145/3611643.3613083) | [PDF](https://dl-acm-org.ezproxy.semo.edu:2443/doi/pdf/10.1145/3611643.3613083) |
|----------|----------|----------|

### Goal: This paper explores the potential use of large-language models, such as GPT3.5, to augment penetration testers with AI sparring partners. 

We explore two distinct use cases: high-level task planning for security testing assignments and low level vulnerability hunting within a vulnerable virtual machine
	
	
## Main Topics: (State of the Art)

### Approach

### Solutions
Issue: lack of personnel

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

### Other Documents Referenced

#### [Mitre att&ck: Design and philosophy (2018)](https://www.mitre.org/news-insights/publication/mitre-attck-design-and-philosophy)

Citation: Blake E Strom, Andy Applebaum, Doug P Miller, Kathryn C Nickels, Adam G
Pennington, and Cody B Thomas. 2018. Mitre att&ck: Design and philosophy. In
Technical report. The MITRE Corporation

[PDF](https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf) 

