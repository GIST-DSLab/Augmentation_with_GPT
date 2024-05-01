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
        
HF_KSC = 'HF_Data/KSC'
HF_Normal_folder_path_3 = 'HF_Data/GPT3.5/Normal'
HF_Specific_folder_path_3 = 'HF_Data/GPT3.5/Specific'
HF_Normal_folder_path_4 = 'HF_Data/GPT4/Normal'
HF_Specific_folder_path_4 = 'HF_Data/GPT4/Specific'

concept_folder_path = 'Concept_Data'
file_names = os.listdir(HF_Normal_folder_path_3)

concept_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
KSC_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
normal3_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
specific3_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
normal4_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}
specific4_count = {'AboveBelow': 0, 'Center': 0, 'CleanUp': 0, 'CompleteShape': 0, 'Copy': 0, 'Count': 0, 'ExtendToBoundary': 0, 'ExtractObjects': 0, 'FilledNotFilled': 0, 'HorizontalVertical': 0, 'InsideOutside': 0, 'MoveToBoundary': 0, 'Order': 0, 'SameDifferent': 0, 'TopBottom2D': 0, 'TopBottom3D': 0}

for file_name in file_names:
    for i in range(0, 16):
        if file_name.endswith('.json') and list(concept_count.keys())[i] in file_name:
            KSC_file_path = os.path.join(HF_KSC, file_name)
            Normal_file_path_3 = os.path.join(HF_Normal_folder_path_3, file_name)
            Specific_file_path_3 = os.path.join(HF_Specific_folder_path_3, file_name)
            Normal_file_path_4 = os.path.join(HF_Normal_folder_path_4, file_name)
            Specific_file_path_4 = os.path.join(HF_Specific_folder_path_4, file_name)
            concept_file_path = os.path.join(concept_folder_path, file_name)
            
            KSC = read_json_file(KSC_file_path)['train']
            normal_3 = read_json_file(Normal_file_path_3)['train']
            specific_3 = read_json_file(Specific_file_path_3)['train']
            normal_4 = read_json_file(Normal_file_path_4)['train']
            specific_4 = read_json_file(Specific_file_path_4)['train']
            
            KSC_count[list(KSC_count.keys())[i]] += len(KSC)
            normal3_count[list(normal3_count.keys())[i]] += len(normal_3)
            specific3_count[list(specific3_count.keys())[i]] += len(specific_3)
            normal4_count[list(normal4_count.keys())[i]] += len(normal_4)
            specific4_count[list(specific4_count.keys())[i]] += len(specific_4)
            concept_count[list(concept_count.keys())[i]] += len(read_json_file(concept_file_path)['train'])

print('KSC', KSC_count)
print()
print('normal3', normal3_count)
print()
print('specific3',specific3_count)
print()
print('normal4', normal4_count)
print()
print('specific4',specific4_count)