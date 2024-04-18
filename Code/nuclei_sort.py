import json

# Open the JSON file for reading
with open('nuclei.json', 'r') as file:
    data = json.load(file)

# Filter out the desired elements
filtered_data = []
for item in data:
    filtered_item = {
        "template-id": item["template-id"],
        "info": item.get("info", {}),
        "port": item.get("port")
    }
    filtered_data.append(filtered_item)

# Save the filtered data to a new JSON file
with open('output.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
