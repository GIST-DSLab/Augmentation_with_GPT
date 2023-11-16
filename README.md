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
