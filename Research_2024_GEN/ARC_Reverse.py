import os
import json


def collect_data(dataset):
    inputs = [example['train'] for example in dataset]
    return inputs

def read_data_from_json(json_file_path, task):
    try:
        # JSON 파일을 열고 읽기 모드로 엽니다.
        with open(json_file_path, "r") as json_file:
            # JSON 데이터를 읽습니다.
            data = json.load(json_file)

            train_data = data[task]

            return train_data
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return None
    except KeyError:
        print(f"Key 'train' not found in the JSON data.")
        return None

def save_json_file(string_data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(string_data, json_file)


folder_path = 'Concept_Data'
file_names = os.listdir(folder_path)

for file_name in file_names:
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            Reverse = json_data
            for i in range(len(json_data['train'])):
                input = json_data['train'][i]['input']
                output = json_data['train'][i]['output']
                Reverse['train'][i]['input'] = output
                Reverse['train'][i]['output'] = input
            
            loc = str(file_name)
            prompt_file_path = 'Reverse_Concept_Data/' + loc
            save_json_file(Reverse, prompt_file_path)