import json
import os

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def score(selected, hf_file):
    point = 0
    total = len(selected['train'])
    for i in selected['train']:
        if i in hf_file['train']:
             point += 1
    return point, total
    
selected_folder_path = 'Research_2024_FILTER/Selected_Data/KSC'
HF_folder_path = 'HF_Data/KSC'
concept_folder_path = 'Concept_Data'

selected_file_names = os.listdir(selected_folder_path)


point_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
total_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
concept_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}

for file_name in selected_file_names:
    for i in range(0, 16):
        if file_name.endswith('.json') and list(point_count.keys())[i] in file_name:
            selected_file_path = os.path.join(selected_folder_path, file_name)
            HF_file_path = os.path.join(HF_folder_path, file_name)
            concept_file_path = os.path.join(concept_folder_path, file_name)
            
            point, total = score(read_json_file(selected_file_path), read_json_file(HF_file_path))
            point_count[list(point_count.keys())[i]] += point
            total_count[list(point_count.keys())[i]] += total
            concept_count[list(point_count.keys())[i]] += len(read_json_file(concept_file_path)['train'])

for k in point_count.keys():
    total_count[k] = total_count[k] - concept_count[k]
    point_count[k] = point_count[k] - concept_count[k]

print(total_count)
print()
print(point_count)