import json

# Step 1: Read the raw content
with open("import - pilotlog_mcc.json", "r", encoding="utf-8") as f:
    raw = f.read()

# Step 2: Decode escape characters (turns \" into ")
unescaped = raw.encode().decode("unicode_escape")

# Step 3: Parse JSON
json_data = json.loads(unescaped)

# Step 4: Pretty-print
# print(json.dumps(json_data, indent=4))

unique_tabels = set()

for entry in json_data:
    # if "table" in entry:
    unique_tabels.add(entry["table"])
for table in unique_tabels:
    print(table)

# with open("cleaned_input.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, indent=4)
