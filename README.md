# Augmentation_with_GPT

What I did: Augmenting Concept ARC Problem

How to augment
1. Guessing input data by some characteristics in ARC Problem

<img width="334" alt="스크린샷 2023-10-13 171703" src="https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/4f312bd3-0cec-4331-a0ee-9751b13805d0">

2. Augmentation Process

<img width="1033" alt="스크린샷 2023-10-30 165149" src="https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/6869b0cb-2777-419b-80b4-2d7480276b75">

Prompt(역변환 방법 프롬프트) is written for each Task (Concept ARC has 16 Tasks)

* dotted input(pink and green one) is augmentation target.
* Chat GPT makes other inputs which is suitable to given output

  i. Make prompt file(Prompt.json) with GPT_prompt.py
  
  ii. Use GPT API (GPT3.5_prompt.py / GPT4.0_prompt.py) to make Augmented DATA
  
  iii. I have chosen appropriate input by hand_filter.py


If you want to use this method with other prompt, you may change prompt in GPT_prompt.py

3. Code File(GPT_DATA) to augment Concept ARC

   i. GPT3.5_prompt.py

     This file is using GPT-3.5 API to make ARC Demonstration

   ii. GPT4.0_prompt.py

     This file is using GPT-4.0 API to make ARC Demonstration

   iii. GPT_prompt.py

     This code is making prompt json file

      * You should change this file if you would like to change prompt.

   iv. Prompt.json

     This json file is that I have used to augment concept.

     This json file is composed of input, output, task(Concept ARC Task e.g. AboveBelow, Center,...), result, test_input and test_output.
   
       1) input: input data from concept ARC(train)

       2) output: output data from concept ARC(train)
   
       3) task: task name from concept ARC
   
       4) result: this array is for complement from chat-GPT, which means it is okay to be empty.

       5) test_input: this array is just for deliver to Result file(to adapt ARC interface) <- this array is not so important

       6) test_output: this array is just for deliver to Result file(to adapt ARC interface) <- this array is not so important
      
<img width="275" alt="스크린샷 2023-11-20 145812" src="https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/e61b6abd-4244-460a-b5b7-c18722d26ee8">
      * You may got this result if you use my prompt.
      
   v. hand_filter.py
   
     this python file is that I've used to filter inadequate data.
