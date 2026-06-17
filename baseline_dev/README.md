# Baseline evaluation on the dev set

This folder presents the baseline results for Qwen3.5-2B obtained on the dev set for both the Ukrainian and Sorbian tracks.
We also share one set of outputs from the evaluation [repository](https://github.com/TUM-NLP/llms-lim-res-eval-2026/). 
We converted the outputs, which can be found in their respective sub-folders.

As noted in the evaluation repository, QA is computed **separately** (but with the same model).

Note: we compute *one* aggregated score per *task* (average chrF++ for MT, average accuracy otherwise), in **bold** in the tables.  
We will use those scores to compute the final ranking.

## Ukrainian results (dev)

| Task | Subset | Metric | Score |
|------|--------|--------|-------|
| MT | all | chrF++ | **32.4680** |
|    | ces-ukr | BLEU | 11.8923 |
|    | ces-ukr | chrF++ | 34.1566 |
|    | eng-ukr | BLEU | 9.8272 |
|    | eng-ukr | chrF++ | 30.7793 |
| QA | all | Exact Match | **0.3773** |
|    | ukrqa | Exact Match | 0.2985 |
|    | ukrmmlu | Exact Match | 0.4561 |
| SC | all | Exact Match | **0.1735** |
|    | ukrsc | Exact Match (Wrong) | 0.1745 |
|    |       | Exact Match (Corrected) | 0.1725 |
| GC | all | Exact Match | **0.0340** |
|    | ukrgc | Exact Match (Wrong) | 0.0425 |
|    |       | Exact Match (Corrected) | 0.0255 |
| MR | ukrmr | Exact Match | **0.1250** |

## Sorbian results (dev)

| Task | Subset | Metric | Score |
|------|--------|--------|-------|
| MT | all | chrF++ | **22.1937** |
|    | deu-hsb | BLEU | 1.2793 |
|    | deu-hsb | chrF++ | 13.9922 |
|    | hsb-deu | BLEU | 5.8788 |
|    | hsb-deu | chrF++ | 26.3793 |
|    | deu-dsb | BLEU | 1.0492 |
|    | deu-dsb | chrF++ | 10.7518 |
|    | dsb-deu | BLEU | 4.9170 |
|    | dsb-deu | chrF++ | 23.5764 |
|    | dsb-hsb | BLEU | 5.8252 |
|    | dsb-hsb | chrF++ | 30.1090 |
|    | hsb-dsb | BLEU | 5.2676 |
|    | hsb-dsb | chrF++ | 28.3536 |
| QA | all | Exact Match | **0.4937** |
|    | hsbqa | Exact Match | 0.5174 |
|    | dsbqa | Exact Match | 0.4700 |
| SC | all | Exact Match | **0.0920** |
|    | hsbsc | Exact Match (Wrong) | 0.0970 |
|    |       | Exact Match (Corrected) | 0.0935 |
|    | dsbsc | Exact Match (Wrong) | 0.0875 |
|    |       | Exact Match (Corrected) | 0.0900 |
| GC | all | Exact Match | **0.0194** |
|    | hsbgc | Exact Match (Wrong) | 0.0305 |
|    |       | Exact Match (Corrected) | 0.0045 |
|    | dsbgc | Exact Match (Wrong) | 0.0336 |
|    |       | Exact Match (Corrected) | 0.0088 |
| MR | all | Exact Match | **0.0417** |
|    | hsbmr | Exact Match | 0.0417 |
|    | dsbmr | Exact Match | 0.0417 |
