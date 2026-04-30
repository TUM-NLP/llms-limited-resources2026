# Multitask LLMs with Limited Resources

The GitHub repo for the Shared Task on Multitask LLMs with Limited Resources @ WMT2026.
This edition is the *successor* of the [WMT 2025 Shared Task LLMs with Limited Resources for Slavic Languages](https://www2.statmt.org/wmt25/limited-resources-slavic-llm.html).

## Overview
We present a shared task to train LLMs under **limited data and compute resources** for three Slavic languages: Ukrainian (uk), Upper Sorbian (hsb) and Lower Sorbian (dsb).

The objective of this Shared Task is to develop and improve LLMs for these languages. 
For this edition, we consider **five** tasks that are to be evaluated jointly: **Machine Translation** (MT), **Multiple-Choice Question Answering** (QA), **Spell Checking** (SC), **Grammar Checking** (GC), and **Maths Reasoning** (MR).

Ukrainian has roughly 40 million first-language (L1) speakers spread all over the world and is a mid-resource language in NLP.
Upper and Lower Sorbian are very low-resource, Slavic minority languages, spoken in the Eastern part of Germany, with 30k and 7k L1 speakers, respectively.
In this task, we aim to test and improve the performance of LLMs on these languages.

More practical details on the Shared Task can be found on the official webpage [here](https://www2.statmt.org/wmt26/limited-resources-llm.html).

## Summary of the changes

The novelties are as follows:
- More tasks to perform **jointly**: Machine Translation, Question Answering, **Spell Checking**, **Grammar Checking**, and **Maths Reasoning**
- Spell checking: finding the spelling error in a sentence (i.e., typo) and correcting it (there might also be no error in the sentence)
- Grammar checking: finding the grammatical error in a sentence and correcting it (there might also be no error in the sentence)
- Maths Reasoning: finding the correct answer to maths problems from two difficulty levels of Qwen PolyMath
- Sorbian MT specific: **one** model for **all six** translation directions of the **three** language pairs: Upper Sorbian–German, Lower Sorbian–German, and Upper Sorbian–Lower Sorbian
- **Merging the two Sorbian language tracks** for a unified model for both languages
- Upper Sorbian QA specific: **new hidden QA** dataset for the test phase
- Ukrainian QA specific: additionally considering the Massive Multitask Language Understanding (MMLU) in Ukrainian
- **Updated model** from the Qwen family: we restrict the model to **Qwen3.5 2B** to remain below the 3B threshold
- Submission of the model: either publicly on HuggingFace (recommended, when possible) or privately to us (we will *not* publish it) for hidden evaluation datasets.

## Datasets
Datasets and details about both Upper Sorbian and Lower Sorbian can be found in the `Sorbian` folder. 

Datasets and details about Ukrainian can be found in the `Ukrainian` folder. 

Notes: 
- The licences in both subfolders differ.
- External datasets can be used on top of the provided corpora. For fairness and reproducibility, they should, however, be **publicly available**.




## Contact / Organisers
Please join our Google group for further information: https://groups.google.com/g/llms-with-limited-resources-2026.

