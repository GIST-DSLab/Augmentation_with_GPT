#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI
import json


client = AzureOpenAI(
  azure_endpoint = "https://temp-arc.openai.azure.com/", 
  api_key="",
  api_version="2024-02-15-preview"
)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return None

def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model = "arc_gpt_turbo",
            messages=[{"role":"system","content":"You have to choose Proper ARC(Abstraction Reasoning and Corpus) Problem."},
                      {"role": "user", "content": prompt}],
            temperature = 1.0,
            max_tokens = 1200,
            top_p = 0.95,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = None
        )
        return response.choices[0].message.content.strip() if response.choices else "No response."
    except KeyError as e:
        # 콘텐츠 관리 정책에 걸려서 응답이 없는 경우 처리
        print(f"Error generating text: {e}")
        return "No response due to content management policy."
    
def save_json_file(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON file saved successfully: {file_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

prompt_folder_path = 'Prompt_Data'
prompt_file_names = os.listdir(prompt_folder_path)

# ===================== N3 =====================

candidate_folder_path = 'Research_2024_GEN/Generate_with_Prompt/Gen_With_Normal_Prompt/GPT3-5'
selected_folder_path = 'Research_2024_FILTER/Selected_Data/Selected_N3'

# 폴더 내의 모든 파일 목록을 가져오기
candidate_file__names = os.listdir(candidate_folder_path)
selected_file__names = os.listdir(selected_folder_path)

prompt_question = "Please choose between Positive or Negative from the given options. Simply choose one of the two options. If it seems slightly off, say 'Negative'. You Mustn't explain the reason."

# JSON 파일마다 반복
did = 0
input_n3_str = ''
output_n3_str = ''
for file_name in prompt_file_names:
    # 파일 확장자가 JSON인지 확인
    if file_name.endswith('.json'):
        # JSON 파일의 전체 경로
        prompt_file_path = os.path.join(prompt_folder_path, file_name)
        candidate_file_path = os.path.join(candidate_folder_path, file_name)
        selected_file_path = os.path.join(selected_folder_path, file_name)
        
        example = read_json_file(prompt_file_path)
        candidate = read_json_file(candidate_file_path)
        selected = read_json_file(selected_file_path)

        for i in range(len(candidate['train'])):
            input_n3_str += example + str(candidate['train'][i]) + prompt_question
            temp = generate_text(example + str(candidate['train'][i]) + prompt_question)
            output_n3_str += temp
            if temp == 'Positive':
                if not candidate['train'][i] in selected['train']:
                    selected['train'].append(candidate['train'][i])
        save_json_file(selected, selected_file_path)
    print(f"Progress: {100 * (did + 1) / 160:.2f}%")
    did += 1
    


save_json_file(input_n3_str, f'input_n3.json')
save_json_file(output_n3_str, f'output_n3.json')
