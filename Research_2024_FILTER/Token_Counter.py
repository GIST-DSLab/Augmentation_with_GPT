import tiktoken
import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

encoder = tiktoken.get_encoding("cl100k_base") #cl100k_base include GPT-3.5 and GPT-4.0


input = read_json_file('input_s4.json')
output = read_json_file('output_s4.json')
input_token = encoder.encode(input)
output_token = encoder.encode(output)

print("input:",len(input_token))
print("output:",len(output_token))