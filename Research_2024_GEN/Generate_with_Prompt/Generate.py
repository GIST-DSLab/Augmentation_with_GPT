import os
from openai import AzureOpenAI
import json

MODE = 'GPT3-5'

client = AzureOpenAI(
  azure_endpoint = "https://desicionllm.openai.azure.com/", 
  api_key="a50ef2cb5f494575b9af9d04e419bbb4",
  api_version="2024-02-15-preview"
) if MODE == 'GPT4' else AzureOpenAI(
  azure_endpoint = "https://canada-arc.openai.azure.com/", 
  api_key="b7bfb05d77214413a968e896511a608b",
  api_version="2024-02-15-preview"
)

def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model = "generating_gpt32k" if MODE == 'GPT4' else "generating_gpt35_turbo_16k",
            messages=[{"role":"system","content":"You have to explain how to solve ARC(Abstraction Reasoning and Corpus) Problem."},
                      {"role": "user", "content": prompt}],
            temperature = 1.0,
            max_tokens = 72,
            top_p = 0.95,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = None
        )
        return response.choices[0].message.content.strip() if response.choices else "No response."
    except Exception as e:
        # 콘텐츠 관리 정책에 걸려서 응답이 없는 경우 처리
        print(f"Error generating text: {e}")
        return "No response due to content management policy."

def generate_arc(prompt):
    try:
        response = client.chat.completions.create(
            model = "generating_gpt32k" if MODE == 'GPT4' else "generating_gpt35_turbo_16k",
            messages=[{"role":"system","content":"You have to solve ARC(Abstraction Reasoning and Corpus) Problem."},
                      {"role": "user", "content": prompt}],
            temperature = 1.0,
            max_tokens = 800,
            top_p = 0.95,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = None
        )
        return response.choices[0].message.content.strip() if response.choices else "No response."
    except Exception as e:
        # 콘텐츠 관리 정책에 걸려서 응답이 없는 경우 처리
        print(f"Error generating text: {e}")
        return "No response due to content management policy."


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
        
def extract_2d_arrays(input_str):
    extracted_arrays = []
    bracket_count = 0
    start_index = None
    end_index = None

    for i, char in enumerate(input_str):
        if char == '[':
            bracket_count += 1
            if bracket_count == 1:
                start_index = i
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_index = i
                potential_array = input_str[start_index:end_index+1]
                try:
                    current_array = eval(potential_array)
                    if isinstance(current_array, list) and all(isinstance(sublist, list) for sublist in current_array):
                        extracted_arrays.append(current_array)
                except:
                    pass

    return extracted_arrays


relation_prompt = {'AboveBelow': 'Focus on the horizontal criteria, you may have to modify some regein by that line. such as removing, moving, filling region by color. element. See the provided example to how to modify',
                   'Center': ' Fix the array issue by addressing the center, potentially moving or removing the central element. See the provided example for clarity. ',
                   'CleanUp': ' Distort the shapes in areas where they are polygonal or completely filled, adding noise or disturbances to disrupt the complete shapes. ', 
                   'CompleteShape': ' Distort the perfectly shaped objects identified in the input image. Introduce noise to these identified objects to easily generate diverse outputs. ', 
                   'Copy': ' Delete one identical object from the output. Refer to the example to identify which one to remove. Consider deleting the object located in a position-indicating space. ', 
                   'Count': ' Create an input image based on the provided count-related problem. Focus on details like object or color count, as shown in the example. ', 
                   'ExtendToBoundary': ' In the input image, find lines connected to boundaries with different colors. Transform these lines into a different shape. The example illustrates how to make this transformation. ', 
                   'ExtractObjects': ' Generate an output image with objects from the given input. Refer to examples for guidance. Hint: Extract objects when inferring input from output. ', 
                   'FilledNotFilled': ' When inferring the input from the output, focus on situations where the inner part of an object contains empty space or another object. Examples provide guidance for creating the output image. ', 
                   'HorizontalVertical': ' Focus on horizontal and vertical relations, representing them with colors or preserving one direction while eliminating the other. Examples illustrate the approach. ', 
                   'InsideOutside': ' Address the inside-outside relationship, either by selecting items inside or outside in the input or determining quantities. Use the boundary as a reference. Examples offer guidance. ', 
                   'MoveToBoundary': ' Objects in the input may be shifted from some side, and in the output, they are displaced either horizontally or vertically. Infer the direction from examples and choose the displacement freely. ', 
                   'Order': ' This is about randomly rearranging initially ordered objects while representing their original positions through a specific rule. Examine the examples to understand how to achieve this. ', 
                   'SameDifferent': ' You will notice that only specific-shaped objects are extracted in the input image. Create additional objects in the zero-represented space. Examples provide guidance on how to proceed. ', 
                   'TopBottom2D': ' Objects are in a 2D space. Check changes in the top and bottom. The input may have shifted or require removing top/bottom indicators. Look at examples for specifics. ', 
                   'TopBottom3D': ' Objects are in 3D space. Consider front-back relationships; bring objects forward or move them backward in the input. Look at examples for specific methods. '
                   }

folder_path = 'Reverse_Concept_Data'
file_names = os.listdir(folder_path)

inputt = ''
outputt = ''
inputn = ''
outputn = ''
inputs = ''
outputs = ''

Hello = "Try solving the ARC problem and do not say sensitive word. generate the output accordingly. I will give you Hint, "

prompt_question = 'Input output pair and a prompt to explain it, but what additional prompt should I write to make it easier to understand the relationship between input and output?'
general_question = 'Provide two-dimensional array that are not identical to the input array or a direct copy of the example. Each element is an integer between 0 and 9. Would you give me 2 answer? No need to explain how you solved.'

for file_name in file_names:
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
                
            new_explain = ''
            for key in relation_prompt.keys():
                if key in file_name:
                    new_explain = relation_prompt[key]
                        
            for i in range(len(json_data['train'])):
                ia = json_data['train'][i]['input']
                oa = json_data['train'][i]['output']
                json_data['train'][i]['input'] = oa
                json_data['train'][i]['output'] = ia
                
            nor_gen_total = json_data.copy()

            for i in range(len(json_data['train'])):
                sample_demo = ''
                for j in range(len(json_data['train'])):
                    if j != i:
                        sample_demo += str(json_data['train'][j])
                target = 'input: ' + str(json_data['train'][i]['output'])
                gen_with_nor = generate_arc(Hello + new_explain + sample_demo + target + general_question)
                                
                inputn = inputn + sample_demo + Hello + new_explain + general_question + target
                outputn += gen_with_nor

                nor_temp = {'input': '','output': ''}
                new_nor_input = extract_2d_arrays(gen_with_nor)
                for new in new_nor_input:
                    if new:
                        nor_temp['input'] = new
                        nor_temp['output'] = json_data['train'][i]['output']
                        nor_gen_total['train'].append(nor_temp)
                        
            loc = str(file_name)
            if not os.path.exists(f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Normal_Prompt/{MODE}'):
                os.makedirs(f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Normal_Prompt/{MODE}')
            nor_prompt_file_path = f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Normal_Prompt/{MODE}/' + loc

            save_json_file(nor_gen_total, nor_prompt_file_path)

for file_name in file_names:
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            sample = ''
            for i in range(len(json_data['train'])):
                sample += str(json_data['train'][i])
                
            prompt = sample
            new_explain = ''
            for key in relation_prompt.keys():
                if key in file_name:
                    prompt += relation_prompt[key]
                    new_explain = relation_prompt[key]
            specific = generate_text(prompt + prompt_question)
            
            inputt = inputt + prompt + prompt_question
            outputt += specific
            
            for i in range(len(json_data['train'])):
                ia = json_data['train'][i]['input']
                oa = json_data['train'][i]['output']
                json_data['train'][i]['input'] = oa
                json_data['train'][i]['output'] = ia
                
            spe_gen_total = json_data.copy()

            for i in range(len(json_data['train'])):
                sample_demo = ''
                for j in range(len(json_data['train'])):
                    if j != i:
                        sample_demo += str(json_data['train'][j])
                target = 'input: ' + str(json_data['train'][i]['output'])
                gen_with_spe = generate_arc(Hello + new_explain + sample_demo +  specific + target + general_question)
                                
                inputs = input + sample_demo + Hello + new_explain + specific + general_question + target
                outputs += gen_with_spe
            
                spe_temp = {'input': '','output': ''}
                new_spe_input = extract_2d_arrays(gen_with_spe)
                for new in new_spe_input:
                    if new_spe_input:
                        spe_temp['input'] = new
                        spe_temp['output'] = json_data['train'][i]['output']
                        spe_gen_total['train'].append(spe_temp)

            loc = str(file_name)
            if not os.path.exists(f'Research_2024_GEN/Generate_with_Prompt/Prompt_Data/{MODE}'):
                os.makedirs(f'Research_2024_GEN/Generate_with_Prompt/Prompt_Data/{MODE}')
            if not os.path.exists(f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Specific_Prompt/{MODE}'):
                os.makedirs(f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Specific_Prompt/{MODE}')

            prompt_file_path = f'Research_2024_GEN/Generate_with_Prompt/Prompt_Data/{MODE}/' + loc
            spe_prompt_file_path = f'Research_2024_GEN/Generate_with_Prompt/Gen_With_Specific_Prompt/{MODE}/' + loc

            save_json_file(specific, prompt_file_path)
            save_json_file(spe_gen_total, spe_prompt_file_path)
            
save_json_file(inputt, f'Research_2024_GEN/Generate_with_Prompt/input_text_{MODE}.json')
save_json_file(outputt, f'Research_2024_GEN/Generate_with_Prompt/output_text_{MODE}.json')
save_json_file(inputn, f'Research_2024_GEN/Generate_with_Prompt/input_normal_{MODE}.json')
save_json_file(outputn, f'Research_2024_GEN/Generate_with_Prompt/output_normal_{MODE}.json')
save_json_file(inputs, f'Research_2024_GEN/Generate_with_Prompt/input_specific_{MODE}.json')
save_json_file(outputs, f'Research_2024_GEN/Generate_with_Prompt/output_specific_{MODE}.json')