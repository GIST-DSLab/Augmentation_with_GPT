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


## Result Table
|Kinds of problems|Total available|The number of augmentated data|The number of valid augmentated data|Ratio(valid/augmentation)|
|:---:|:---:|:---:|:---:|:---:|
|Above Below|58|158|34|21.52%|
|Center|65|236|35|14.83%|
|Clean Up|106|183|83|45.36%|
|Complete Shape|58|147|37|25.17%|
|Copy|27|153|4|2.61%|
|Count|56|202|29|14.36%|
|Extend To Boundary|37|167|8|4.79%|
|Extract Objects|44|176|21|11.93%|
|Filled Not Filled|58|203|29|14.29%|
|Horizontal Vertical|32|114|7|6.14%|
|Inside Outside|52|191|24|12.57%|
|Move To  Boundary|36|165|12|7.27%|
|Order|47|162|26|16.05%|
|Same Different|107|246|76|30.89%|
|Top Bottom 2D|92|255|59|23.14%|
|Top Bottom 3D|55|215|25|11.63%|
|Total|930|2913|509|17.12%|

<img width="275" alt="스크린샷 2023-11-20 145812" src="https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/e61b6abd-4244-460a-b5b7-c18722d26ee8">
      * You may got this result if you use my prompt.
      
   v. hand_filter.py
   
   this python file is that I've used to filter inadequate data.
