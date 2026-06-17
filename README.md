# Multitask LLMs with Limited Resources

The GitHub repo for the Shared Task on Multitask LLMs with Limited Resources @ WMT2026.
This edition is the *successor* of the [WMT 2025 Shared Task LLMs with Limited Resources for Slavic Languages](https://www2.statmt.org/wmt25/limited-resources-slavic-llm.html).

## Overview
We present a shared task to train LLMs under **limited data and compute resources** for three Slavic languages: Ukrainian (uk), Upper Sorbian (hsb) and Lower Sorbian (dsb).

The objective of this Shared Task is to develop and improve LLMs for these languages. 
For this edition, we consider **five** tasks that are to be evaluated jointly: **Machine Translation** (MT), **Multiple-Choice Question Answering** (QA), **Spell Checking** (SC), **Grammar Checking** (GC), and **Maths Reasoning** (MR).

Ukrainian has roughly 40 million first-language (L1) speakers spread all over the world and is a mid-resource language in NLP.
Upper and Lower Sorbian are very low-resource, Slavic minority languages, spoken in the eastern part of Germany, with 30k and 7k L1 speakers, respectively.
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
Datasets and details (field schemas, sources, licenses) for both Upper Sorbian and Lower Sorbian can be found in the [`Sorbian/`](Sorbian/README.md) folder.

Datasets and details for Ukrainian can be found in the [`Ukrainian/`](Ukrainian/README.md) folder.

Notes: 
- The licences in both subfolders differ; see the per-folder READMEs for details.
- External datasets can be used on top of the provided corpora. For fairness and reproducibility, they should, however, be **publicly available**.

## Task description
MT and QA have minor changes from last year's edition. The three new tasks (SC, GC, and MR) are described below in more details.

### Machine Translation (MT)
For Ukrainian, we focus on the following language direction (as in the 2025 edition):
- English to Ukrainian (en->uk)
- Czech to Ukrainian (cs->uk)

For the Sorbian track, we will consider the **six translation directions** for the following three language pairs:
- German–Upper Sorbian (de <-> hsb)
- German–Lower Sorbian (de <-> dsb)
- Upper Sorbian–Lower Sorbian (hsb <-> dsb)

### Question Answering (QA)
For Ukrainian, we use the UNLP2024 Shared Task data as in the 2025 edition. Additionally, we also consider the **MMLU dataset** for Ukrainian.

For the Sorbian track, we reuse the WMT2025 edition data, which came from language certificates. This year, we will have a **hidden** dataset during the test phase that will not be released but will be used to test the system's capabilities.

### 🆕 Spell Checking (SC)
The goal of the task is to identify a spelling mistake in a sentence (e.g., a typo). Each sentence can have **up to two mistakes** in **one word only**. There can be no mistake in the sentence, in which case the model should leave the sentence as it is. If there is a mistake, the word should be identified and the correct form given.

Below is the standardised format for all three languages:
- Input sentence: 30.000 opozicionelnych bcuhu zajeći a do lěhwow dowjezeni, statysacy ćeknychu do wukraja.
- Expected outputs (two outputs): 
  - Wrong word (detection): bcuhu
  - Correct word (correction): buchu

### 🆕 Grammar Checking (GC)
The goal of this task is to identify a grammatical mistake in a sentence (e.g., wrong tense agreement). Each sentence can have **up to one mistake** in **one word only**. There can be no mistake in the sentence, in which case the model should leave the sentence as it is. If there is a mistake, the word should be identified and the correct form given.

Below is the standardised format for all three languages:
- Input sentence: Я втомився від консервативних партій та урядів, які прикриваються маскою сприяння підприємців.
- Expected outputs (two outputs): 
  - Wrong word (detection): підприємців
  - Correct word (correction): підприємцям

### 🆕 Maths Reasoning (MR)
This task aims to assess the LLM's capability in solving maths problems of two difficulty levels: low and medium. Our evaluation dataset is a translated and manually verified version of the Qwen PolyMath benchmark (https://huggingface.co/datasets/Qwen/PolyMath).

### Important note
For fair evaluation of the models' performance in our shared task, we kindly ask participants to *avoid* using the original, modified, or translated versions of the benchmarks used for our evaluation (for training or inference).
This includes: 
- the *test* splits of the UNLP2024 Shared Task data and of the MMLU dataset (Ukrainian QA)
- any version (i.e., original or translation) of the PolyMath benchmark (MR)
- Sorbian language certificate questions (Sorbian track QA)
- the test sets of the 2025 edition of this Shared Task

## Evaluation Methods
We will use **chrF++** to evaluate machine translation. For consistency with the previous WMT 2022 Shared Task, we also report BLEU for MT.
For the question-answering and maths-reasoning tasks, we use the standard **accuracy**. 
Finally, for spell checking and grammar checking, we use the ~~F1-score~~ **accuracy** to assess both detection (finding the incorrect word) and correction (outputting the correct word).

The final ranking in the leaderboard will consider the scores from **all five tasks equally**.

We provide this [repository](https://github.com/TUM-NLP/llms-lim-res-eval-2026/) to help with the evaluation. It is a fork of [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) and can be used to reproduce the baseline results and run the evaluation script.

## Baseline results
The baseline results on the *dev* set is in the `baseline_dev` folder.

## Contact / Organisers
Please join our Google group for further information: https://groups.google.com/g/llms-with-limited-resources-2026.

All names are sorted in alphabetical order. 

TUM Heilbronn:
- Daryna Dementieva
- Marion di Marco
- Lukas Edman
- Alexander Fraser
- Kathy Hämmerl
- Shu Okabe

WITAJ-Sprachzentrum (for both Upper and Lower Sorbian):
- Beate Brězan 
- Anita Hendrichowa 
- Marko Měškank
- Kryštof Peršín (maths reasoning dataset annotation)
- Tomaš Šołta (language certificate)


## Acknowledgements
We thank the UNLP 2024 Shared Task 2024 team
- Roman Kyslyi
- Mariana Romanyshyn
- Oleksiy Syvokon

for kindly sharing the Ukrainian QA resources. 
Please acknowledge their work by citing the following paper:

Mariana Romanyshyn, Oleksiy Syvokon, and Roman Kyslyi. 2024. [The UNLP 2024 Shared Task on Fine-Tuning Large Language Models for Ukrainian](https://aclanthology.org/2024.unlp-1.9/). In *Proceedings of the Third Ukrainian Natural Language Processing Workshop (UNLP) @ LREC-COLING 2024*, pages 67–74, Torino, Italia. ELRA and ICCL.

We also thank the INSAIT-institute team---especially, Hanna Yukhymenko---that works on technologies for underrepresented languages, including Ukrainian.
Please cite the following work that introduced MMLU_UKR:
Hanna Yukhymenko, Anton Alexandrov, and Martin Vechev. 2026. [Recovered in Translation: Efficient Pipeline for Automated Translation of Benchmarks and Datasets](https://arxiv.org/pdf/2602.22207). In ACL 2026.

This work was partly funded by the European Union (ERC, EPICAL, 101141712). 
Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. 
Neither the European Union nor the granting authority can be held responsible for them.
