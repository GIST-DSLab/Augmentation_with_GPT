# Augmentation_with_GPT

What I did: Augmenting Concept ARC Problem

How to augment
1. Guessing input data by some characteristics in ARC Problem

![다대일](https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/1f496c54-a712-4937-a465-4f4f7d89d545)

2. Augmentation Process
 (1) Category Prompt
Prompt(역변환 방법 프롬프트) is written for each Task (Concept ARC has 16 Tasks)
  * If you want to use this method with other prompt, you may change prompt in GPT_prompt.py

 (2) Prompt Concretization
The prompts in (1) are prompts specific to each category rather than to individual problems. However, since each category contains problems with diverse logical relationships, we aimed to increase accuracy by adding prompts that describe each problem in detail.

![스크린샷 2024-05-01 오후 9 12 27](https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/88162a17-0c2a-4ce7-824a-4299d35d5260)

 (3) Data Generation
![스크린샷 2024-05-01 오후 9 12 51](https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/a9711d10-7a25-4668-8faa-389852fa9cf7)

 (4) Data Filtering
Despite utilizing negative prompts, many of the generated data from the large language model did not meet the criteria. Therefore, an additional filtering process was necessary, and in this study, we filtered using the large language model.
![스크린샷 2024-05-01 오후 9 20 04](https://github.com/GIST-DSLab/Augmentation_with_GPT/assets/126467193/4071d0c2-1182-480b-b89c-dd230184d6f1)


3. Code File(GPT_DATA) to augment Concept ARC

  i. Generate ARC File with Research_2024_Gen
  
    The file in Research_2024_GEN is for generating ARC. (2.(1) - (3))
    
     1) ARC_Reverse.py will make inverse ARC Problem which will be in Reverse_Concept_Data
     
     2) Generate_with_Prompt/Generate.py will make ARC Problem.
     
     3) Remove_Redundancy.py will get rid of overlapped data.

  ii. Filter the inadequate ARC File with Research_2024_FILTER
  
    The file in Research_2024_FILTER is for Filtering unsuitable ARC. (2.(4))
    
     1) Prompt.py will make prompt file to help filtering.
    
     2) File in Decision Folder is filtering code.

       - n3 means generated with gpt 3.5 without prompt concretization

       - s3 means generated with gpt 3.5 with prompt concretization
       
       - n4 means generated with gpt 4.0 without prompt concretization
       
       - s4 means generated with gpt 4.0 with prompt concretization


## Result Table
|Problem Category|Total available|The number of generated data|The number of valid augmentated data|Ratio(valid/generated)|
|:---:|:---:|:---:|:---:|:---:|
|[Above Below](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/AboveBelow.pdf)|58|158|34|21.52%|
|[Center](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/Center.pdf)|65|236|35|14.83%|
|[Clean Up](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/CleanUp.pdf)|106|183|83|45.36%|
|[Complete Shape](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/CompleteShape.pdf)|58|147|37|25.17%|
|[Copy](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/Copy.pdf)|27|153|4|2.61%|
|[Count](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/Count.pdf)|56|202|29|14.36%|
|[Extend To Boundary](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/ExtendToBoundary.pdf)|37|167|8|4.79%|
|[Extract Objects](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/ExtractObjects.pdf)|44|176|21|11.93%|
|[Filled Not Filled](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/FilledNotFilled.pdf)|58|203|29|14.29%|
|[Horizontal Vertical](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/HorizontalVertical.pdf)|32|114|7|6.14%|
|[Inside Outside](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/InsideOutside.pdf)|52|191|24|12.57%|
|[Move To  Boundary](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/MoveToBoundary.pdf)|36|165|12|7.27%|
|[Order](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/Order.pdf)|47|162|26|16.05%|
|[Same Different](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/SameDifferent.pdf)|107|246|76|30.89%|
|[Top Bottom 2D](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/TopBottom2D.pdf)|92|255|59|23.14%|
|[Top Bottom 3D](https://github.com/GIST-DSLab/Augmentation_with_GPT/blob/main/visualization/TopBottom3D.pdf)|55|215|25|11.63%|
|Total|930|2913|509|17.12%|

      
   v. hand_filter.py
   
   this python file is that I've used to filter inadequate data.
