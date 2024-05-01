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

relation_prompt = {'AboveBelow': 'Take a close look at the changes above and below a specific object or line.',
                   'Center': 'Choose something to place at the center and observe the changes it brings about. Pay close attention to what it is.',
                   'CleanUp': 'You should get rid of something that is asymmetrically placed, whether it will a point or a shape. Focus on the background as you observe.', 
                   'CompleteShape': 'You should complete the shape. Try combining the input and output to complete it.', 
                   'Copy': 'Copy the objects and place them elsewhere. You may get hint to position them if you think carefully', 
                   'Count': 'Try counting the number of objects, points, or lines carefully.', 
                   'ExtendToBoundary': 'Extend certain points or shapes to the edge of a specific area.', 
                   'ExtractObjects': 'Extract objects that follow a distinct pattern compared to others.', 
                   'FilledNotFilled': 'Focus on extracting objects that are either incompletely filled or filled in a peculiar manner.', 
                   'HorizontalVertical': 'There are rules related to vertical and horizontal aspects. It could involve indicating vertical and horizontal elements, or comparing vertical and horizontal aspects to make a representation.', 
                   'InsideOutside': 'There are rules based on the inside and outside. Take a closer look to identify them.', 
                   'MoveToBoundary': 'Move objects to the end of a specific area. Focus on the direction and position.', 
                   'Order': 'Sorting based on size or the number of objects, among other criteria. The sorted result could be represented in terms of position.', 
                   'SameDifferent': 'There is a rule to select objects with the same color or shape.', 
                   'TopBottom2D': 'Take a closer look at things on the 2D plane, focusing on the top and bottom.', 
                   'TopBottom3D': 'Examine the objects in three-dimensional space, paying attention to what is in front and what is behind.'}

des_prompt = ' These are the ARC problem which has logical relationship I said.'

folder_path = 'concept_data'
file_names = os.listdir(folder_path)

for file_name in file_names:
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            sample = ''
            for i in range(len(json_data['train'])):
                sample += str(json_data['train'][i])
            prompt = sample
            
            for key in relation_prompt.keys():
                if key in file_name:
                    prompt += relation_prompt[key]

            prompt += des_prompt

            loc = str(file_name)
            prompt_file_path = 'Prompt_Data/' + loc
            save_json_file(prompt, prompt_file_path)