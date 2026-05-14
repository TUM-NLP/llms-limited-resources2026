# Upper Sorbian and Lower Sorbian data

This folder contains the Upper Sorbian (hsb) and Lower Sorbian (dsb) datasets (Sorbian track). Both languages and tasks should be handled by a **single model**.

## Machine Translation (MT)

We release three dev sets for the development phase, one per language pair. 
We additionally provide *new* training data for all three language pairs (de–hsb, de–dsb, hsb–dsb) and monolingual sentences for Upper and Lower Sorbian.

All development sets are in the final JSONL format, while the additional files are in CSV format.

### Dev sets (`MT/*_mt_dev.jsonl`)

We use the same development dataset for de–hsb and de–dsb as in the WMT2025 edition.
The hsb–dsb development set is *new*. 

Columns:
- `dataset_id`: dataset ID
- `sent_id`: sentence pair ID
- `{lang_1}`: sentence in language 1, identified with the language code (e.g., `de`)
- `{lang_2}`: sentence in language 2, identified with the language code (e.g., `hsb`)

| language pair | N_sentence |
|---|---|
| German–Upper Sorbian (de–hsb) | 4,000 |
| German–Lower Sorbian (de–dsb) | 4,000 |
| Upper Sorbian–Lower Sorbian (hsb–dsb) | 4,000 |

### Parallel training corpora (`MT/train_*_2026.csv`)

We release new parallel sentences for all three language pairs (de–hsb, de–dsb, and hsb–dsb). Each row is a sentence pair.

| language pair | N_sentence |
|---|---|
| German–Upper Sorbian (de–hsb) | 23,116 |
| German–Lower Sorbian (de–dsb) | 30,560 |
| Upper Sorbian–Lower Sorbian (hsb–dsb) | 67,845 |

### Monolingual corpora (`MT/*_monolingual_2026.csv`)

Monolingual sentences have been filtered and merged from monolingual corpora of different sources.

Columns:
- `id`: source of the sentence (e.g., `hsb_witaj_mono_2026`)
- `year`: the year of the edition
- `{hsb|dsb}`: monolingual sentence

| language | N_sentence |
|---|---|
| Upper Sorbian | 512,671 |
| Lower Sorbian | 38,028 |


## Question Answering (QA)

For both languages, the Question Answering datasets come from actual language certification exercises.
We use the same datasets as in the WMT2025 edition. 

Columns:
- `dataset_id`: dataset ID
- `question_id`: the unique ID *per language* (e.g., `A1.1.H3`) composed of the level (e.g., A1), a source identifier (e.g., 1), a question type (e.g., H for listening, L for reading, and S for grammar exercises), and a question number (e.g., 3).
- `question_level`: the CEFR level of the question
- `context`: the context needed to answer the question, e.g., a text for reading comprehension or a dialogue transcription. This is part of the model *input* but may be empty.
- `question`: the question to answer (part of the model *input*)
- `possible_answers`: all the possible answers (each with a numeral and the actual answer; e.g., 1 pšawje 
2 wopak) shown in the exercise; **the number of answers depends on the exercise level and number** (up to 16). This is also part of the model *input*.
- `correct_answer_num`: the numeral corresponding to the correct answer (expected *output*)
- `question_type`: the ID for the question type (e.g., `listening_B2_3`) composed of the exercise type (e.g., listening comprehension), the exercise level (e.g., B2), and the number of the exercise (e.g., 3); this can help to understand the question types.

| language | N_instances |
|---|---|
| hsb, dsb | 158 |

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
| hsb, dsb | 2,000 |

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
| hsb | 2,000 |
| dsb | 1,250 |

## Maths Reasoning (MR)

The problems for the Maths Reasoning task are of low and medium difficulty levels.

Columns:
- `dataset_id`: dataset ID
- `id`: question ID. The prefix indicates the problem difficulty (low or medium)
- `question`: maths problem (model *input*)
- `answer`: answer (expected *output*)


| language | low | medium | total |
|---|---|---|---|
| hsb, dsb | 12 | 12 | 24 |

## Licence

All datasets in this folder are released under a CC BY-NC-SA licence, except for the MT *monolingual* sentences and the Maths Reasoning data which has the Apache-2.0 licence.
