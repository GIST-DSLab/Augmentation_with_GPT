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
    
def save_json_file(string_data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(string_data, json_file)

Normal_folder_path = 'Research_2024_GEN/Generate_with_Prompt/Gen_With_Normal_Prompt/GPT4'
Specific_folder_path = 'Research_2024_GEN/Generate_with_Prompt/Gen_With_Specific_Prompt/GPT4'

concept_folder_path = 'Concept_Data'
file_names = os.listdir(concept_folder_path)


normal_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
specific_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
concept_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}

for file_name in file_names:
    for i in range(0, 16):
        if file_name.endswith('.json') and list(concept_count.keys())[i] in file_name:
            Normal_file_path = os.path.join(Normal_folder_path, file_name)
            Specific_file_path = os.path.join(Specific_folder_path, file_name)
            concept_file_path = os.path.join(concept_folder_path, file_name)
            
            normal = read_json_file(Normal_file_path)['train']
            specific = read_json_file(Specific_file_path)['train']
            temp_normal = read_json_file(concept_file_path)
            temp_specific = read_json_file(concept_file_path)

            for n in normal:
                if not n in temp_normal['train']:
                    temp_normal['train'].append(n)
                                        
            for s in specific:
                if not s in temp_specific['train']:
                    temp_specific['train'].append(s)
                    
            #save_json_file(temp_normal, 'Research_2024_GEN/Not_Redundancy/GPT4/Normal/' + file_name)
            #save_json_file(temp_specific, 'Research_2024_GEN/Not_Redundancy/GPT4/Specific/' + file_name)

            normal_count[list(normal_count.keys())[i]] += len(temp_normal['train'])
            specific_count[list(specific_count.keys())[i]] += len(temp_specific['train'])
            concept_count[list(concept_count.keys())[i]] += len(read_json_file(concept_file_path)['train'])

print('concept', concept_count)
print()
print('normal', normal_count)
print()
print('specific',specific_count)