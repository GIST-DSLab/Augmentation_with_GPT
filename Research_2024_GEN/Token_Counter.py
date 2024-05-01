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

input3 = read_json_file('Generate_with_Specific_Prompt/input_GPT3-5.json')
output3 = read_json_file('Generate_with_Specific_Prompt/output_GPT3-5.json')
input_token = encoder.encode(input3)
output_token = encoder.encode(output3)

print("input3:",len(input_token))
print("output3:",len(output_token))


input4 = read_json_file('Generate_with_Specific_Prompt/input_GPT4.json')
output4 = read_json_file('Generate_with_Specific_Prompt/output_GPT4.json')
input_token = encoder.encode(input4)
output_token = encoder.encode(output4)

print("input4:",len(input_token))
print("output4:",len(output_token))