#╔

def print_section(lines, data, index):
    header_found = False
    for line in lines:
        if header_found:
            if data[index+1] in line:
                break
            print(line)
        elif data[index] in line:
            header_found = True
            print(previous_line)
            print(line)
        previous_line = line
    print()

## Run a Command
def run_command(command):
    print("\nRunning ", command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        # Command was successful
        #print("Output:", output.decode())
        print("Command executed successfully\n")
        
    else:
        # Command failed
        print("Error output:", error.decode())
        print(f"Error executing command. Return code: {return_code}")
        
    return return_code, output.decode()    
    
#---------------------------------------------------------------

RUNNING_COMMAND=0


if RUNNING_COMMAND==1:
    run_command("sudo ./linpeas.sh")

# Open the input file for reading
with open('linpeas-result.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the index of the first occurrence of the phrase
index = content.find("Do you like PEASS")

# If the phrase is found, remove everything before it
if index != -1:
    content = content[index:]

# Replace all occurrences of "" with "^"
content = content.replace("", "^")
content = content.replace("▄", "")

content = content.replace("^[1;4m", "")

content = content.replace("^[1;31;103m", "")
content = content.replace("^[1;31m", "")
content = content.replace("^[1;32m", "")
content = content.replace("^[1;33m", "")
content = content.replace("^[1;34m", "")
content = content.replace("^[1;37m", "")

content = content.replace("^[1;90m", "")
content = content.replace("^[1;95m", "")
content = content.replace("^[1;96m", "")

content = content.replace("^[0m", "")

lines = content.split("\n")

section = ""

# Initialize the list to hold header data
header_data = []
section_data = []
header_subsection_data = []

# Print the rest of each line until it hits "╠" or the end of the line
lines = content.split("\n")
for line in lines:
    index = line.find("╣")
    if index != -1:
        rest_of_line = line[index+1:]
        end_index = rest_of_line.find("╠")
        if end_index != -1:
            header = rest_of_line[:end_index].strip()
            header_data.append(header)
            section_data.append(header)
            #print(header)
        else:
            header = rest_of_line.strip()
            section_data.append(header)
            #print(header)
            

            
for i in range(len(header_data)):
    print("["+str(i)+"] "+header_data[i])

header_index = int(input("Enter the integer representing the header: ")) 

print()

section_header_found = False

for section in section_data:
    if section_header_found:
        if section in header_data:
            break
        print("["+str(section_data.index(section))+"] "+section)
        #header_subsection_data.append(section)
    elif section == header_data[header_index]:
        section_header_found = True
        print("["+str(section_data.index(section))+"] "+section)
        #header_subsection_data.append(section)

section_index = int(input("Enter the integer representing the section: ")) 

print()

lines = content.split("\n")
if section_data[section_index] in header_data:
    print_section(lines, header_data, header_index)
else:
    print_section(lines, section_data, section_index)

    
# Write the modified content back to the file
with open('linpeas-filtered.txt', 'w', encoding='utf-8') as f:
    f.write(content)
