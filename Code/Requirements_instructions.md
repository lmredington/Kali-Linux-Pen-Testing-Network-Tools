# Download OpenAI (Linux) https://platform.openai.com/docs/quickstart?context=python

(1)

	python3 -m venv openai-env
	
(2)

	source openai-env/bin/activate

(3) 

	pip install --upgrade openai
	
(4) Create secret key and save it

(5) Verify API is working

	curl https://api.openai.com/v1/models \  -H "Authorization: Bearer $your-secret-key" \  -H "OpenAI-Organization: org-CWpFAZh2MUaue9Q6q05opzmj"
	
	
# Download HackingBuddyGPT

# Clone the repository

	git clone https://github.com/andreashappe/hackingBuddyGPT.git && cd hackingBuddyGPT

# setup virtual python environment

	python3 -m venv venv
	
	source ./venv/bin/activate

# install python requirements

	pip install -r requirements.txt

# copy default .env.example

	cp .env.example .env

# IMPORTANT: setup your OpenAI API key, the VM's IP and credentials within .env

	vi .env

# if you start wintermute without parameters, it will list all available use cases

	python3 wintermute.py
	
usage: wintermute.py [-h] {linux_privesc,windows privesc} ...
wintermute.py: error: the following arguments are required: {linux_privesc,windows privesc}

# start wintermute, i.e., attack the configured virtual machine

	python wintermute.py linux_privesc --enable_explanation true --enable_update_state true

## If you run into issues with this last command, you may need to update the ssh port (22 or 2222)
