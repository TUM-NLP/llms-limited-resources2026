# Ukrainian data

This folder contains the Ukrainian (ukr) dataset (Ukrainian track).
We compiled the datasets for the Ukrainian language from various open-source resources that kindly allowed us to use the data for the shared task.

## Machine Translation (MT)

We use the same development datasets (en–uk and cs–uk) as in the WMT2025 edition.  
All development sets are in the final JSONL format.

Columns:
- `dataset_id`: dataset ID
- `sent_id`: sentence pair ID
- `{lang_1}`: sentence in language 1, identified with the language code (e.g., `en`)
- `{lang_2}`: sentence in language 2, identified with the language code (e.g., `uk`)

| language pair | N_sentence |
|---|---|
| English–Ukrainian (en–uk) | 5,108 |
| Czech–Ukrainian (cs–uk) | 6,263 |

## Question Answering (QA)

For Question Answering, we use the same dataset as in the WMT2025 edition from the Ukrainian External independent testing (ZNO; `ukr_qa_*`).  
Additionally, we provide the Ukrainian MMLU dataset (`ukr_mmlu_qa_*`).
Both use the same column format and are in JSONL. They also feature a training and a development split.

Columns:
- `dataset_id`: dataset ID
- `question`: the question to answer (part of the model *input*)
- `possible_answers`: all the possible answers, each with a number and the actual answer (e.g., `{'0': '...', '1': '...'}`). This is also part of the model *input*.
- `correct_answer_num`: the number of the correct answer (expected *output*)
- `subject`: the subject area of the question (e.g., `history-of-ukraine`, `abstract_algebra`)

| dataset | split | N_instances |
|---|---|---|
| ZNO (`ukr_qa_dev.jsonl`) | dev | 613 |
| ZNO (`ukr_qa_train.jsonl`) | train | 2,450 |
| Ukrainian MMLU (`ukr_mmlu_qa_dev.jsonl`) | dev | 285 |
| Ukrainian MMLU (`ukr_mmlu_qa_train.jsonl`) | train | 1,531 |

## Spell Checking (SC)

The Spell Checking task aims to identify a spelling mistake (e.g., typo).
There is **up to** one error in a sentence. If there is no error, the model is expected to return `CORRECT`.
There should be two outputs: one to find the wrong word (detection) and its correction (correction).

Columns:
- `dataset_id`: dataset ID
- `id`: sentence ID
- `input_sentence`: sentence with a potential error (model *input*)
- `original_sentence`: reference sentence (no error) for reference
- `incorrect_word`: the word with a spelling error, or `"CORRECT"` if there is no error (expected *output* nº1 for *detection*)
- `correct_word`: the corrected word, or `"CORRECT"` if there was no error (expected *output* nº2 for *correction*)

| language | N_instances |
|---|---|
| ukr | 2,000 |

## Grammar Checking (GC)

The Grammar Checking task follows the spell-checking task in format. There is **up to** one error in a sentence.
There should be two outputs: one to find the wrong word (detection) and its correction (correction).

Columns:
- `dataset_id`: dataset ID
- `id`: sentence ID
- `input_sentence`: sentence with a potential error (model *input*)
- `original_sentence`: reference sentence (no error) for reference
- `incorrect_word`: the word with a grammatical error, or `"CORRECT"` if there is no error (expected *output* nº1 for *detection*)
- `correct_word`: the corrected word, or `"CORRECT"` if there was no error (expected *output* nº2 for *correction*)

| language | N_instances |
|---|---|
| ukr | 2,000 |

## Maths Reasoning (MR)

The problems for the Maths Reasoning task are of low and medium difficulty levels.

Columns:
- `dataset_id`: dataset ID
- `id`: question ID. The prefix indicates the problem difficulty (low or medium)
- `question`: maths problem (model *input*)
- `answer`: answer (expected *output*)

| language | low | medium | total |
|---|---|---|---|
| ukr | 12 | 12 | 24 |

## Licence

We release the datasets with the following licences (from their respective dataset sources):
- MT: Apache-2.0
- QA (ZNO): MIT
- GC: Apache-2.0
- SC: Apache-2.0
- MR: Apache-2.0 
