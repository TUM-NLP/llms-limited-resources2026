# Results

## Overall results
Below are the results for each team's *primary* submission.

For the final rank per track (i.e., for Ukrainian or Sorbian), points are given according to the rank of the submission *per task* (computed as the average per sub-task).
The best output gets the maximum number of points. 
In the case of ties, we ranked according to the MT results.

The winning team per track and the best submission per task are in bold.

### Ukrainian track

|              | MT (chrF++) | points | QA        | points | SC        | points | GC        | points | MR        | points | final points | final rank |
|--------------|-------------|--------|-----------|--------|-----------|--------|-----------|--------|-----------|--------|--------------|--------|
| **Zolint**   | **49.86**   | 4      | 41.15     | 3      | **66.43** | 4      | **45.18** | 4      | **21.60** | 4      | 19           | 1 |
| koshi        | 16.80       | 1      | **46.99** | 4      | 52.50     | 3      | 30.55     | 3      | 0.40      | 1      | 12           | 2 |
| baseline     | 18.46       | 3      | 36.33     | 1      | 8.38      | 1      | 2.18      | 1      | 20.00     | 3      | 9            | 4 |
| TUMHN        | 16.08       | 1      | 40.13     | 2      | 16.50     | 2      | 6.80      | 2      | 4.40      | 2      | 9            | 4 |

### Sorbian track

|              | MT (chrF++) | points | QA        | points | SC        | points | GC        | points | MR        | points | final points | final rank |
|--------------|-------------|--------|-----------|--------|-----------|--------|-----------|--------|-----------|--------|--------------|-------|
| **HeyBusan** | **72.75**   | 5      | 55.92     | 3      | **78.03** | 5      | **79.52** | 5      | 29.00     | 4      | 22           | 1 |
| **LT3**          | 69.57       | 4      | **65.05** | 5      | 76.11     | 4      | 78.32     | 4      | **30.40** | 5      | 22           | 1 |
| Hitsz        | 63.12       | 3      | 57.33     | 4      | 73.13     | 3      | 62.11     | 3      | 18.60     | 3      | 16           | 3 |
| HSE          | 61.50       | 2      | 46.77     | 2      | 63.63     | 2      | 50.02     | 2      | 5.00      | 1      | 9            | 4 |
| baseline     | 21.68       | 1      | 43.39     | 1      | 6.66      | 1      | 1.34      | 1      | 5.40      | 1      | 5            | 5 |


## Detailed results
We report below the detailed scores per track.
The aggregated score per *task* is in **bold** in the tables.

### Ukrainian results

| Task | Subset | Metric | TUMHN | baseline | koshi | Zolint |
|------|--------|--------|-------|----------|-------|--------|
| MT | all | chrF++ | **16.08** | **18.46** | **16.80** | **49.86** |
|    | ces-ukr | BLEU | 3.93 | 5.38 | 6.01 | 23.66 |
|    | ces-ukr | chrF++ | 19.77 | 25.44 | 23.05 | 51.53 |
|    | eng-ukr | BLEU | 1.01 | 0.55 | 0.70 | 15.43 |
|    | eng-ukr | chrF++ | 12.39 | 11.47 | 10.55 | 48.18 |
| QA | all | Exact Match | **40.13** | **36.33** | **46.99** | **41.15** |
|    | ukrqa | Exact Match | 35.82 | 30.76 | 45.01 | 37.42 |
|    | ukrmmlu | Exact Match | 44.44 | 41.90 | 48.97 | 44.88 |
| SC | all | Exact Match | **16.50** | **8.38** | **52.50** | **66.43** |
|    | ukrsc | Exact Match (Wrong) | 22.20 | 8.55 | 60.10 | 71.70 |
|    |       | Exact Match (Corrected) | 10.80 | 8.20 | 44.90 | 61.15 |
| GC | all | Exact Match | **6.80** | **2.18** | **30.55** | **45.18** |
|    | ukrgc | Exact Match (Wrong) | 10.35 | 2.70 | 36.55 | 45.25 |
|    |       | Exact Match (Corrected) | 3.25 | 1.65 | 24.55 | 45.10 |
| MR | ukrmr | Exact Match | **4.40** | **20.00** | **0.40** | **21.60** |

### Sorbian results 

| Task | Subset | Metric | baseline | HSE | Hitsz | LT3 | HeyBusan |
|------|--------|--------|--------------|-----|-------|-----|----------|
| MT | all | chrF++ | **21.68** | **61.50** | **63.12** | **69.57** | **72.75** |
|    | deu-hsb | BLEU | 0.96 | 30.48 | 35.32 | 42.07 | 48.61 |
|    | deu-hsb | chrF++ | 13.67 | 56.27 | 60.04 | 64.55 | 70.26 |
|    | hsb-deu | BLEU | 6.08 | 27.14 | 37.42 | 44.11 | 46.62 |
|    | hsb-deu | chrF++ | 27.05 | 52.70 | 62.42 | 67.19 | 69.43 |
|    | deu-dsb | BLEU | 0.95 | 27.14 | 26.87 | 34.56 | 39.36 |
|    | deu-dsb | chrF++ | 10.42 | 52.72 | 52.37 | 58.90 | 63.06 |
|    | dsb-deu | BLEU | 3.73 | 29.90 | 36.30 | 44.05 | 47.87 |
|    | dsb-deu | chrF++ | 23.18 | 54.61 | 60.92 | 66.56 | 69.42 |
|    | dsb-hsb | BLEU | 5.81 | 55.78 | 49.42 | 63.18 | 66.67 |
|    | dsb-hsb | chrF++ | 28.66 | 75.50 | 70.62 | 80.09 | 82.38 |
|    | hsb-dsb | BLEU | 4.88 | 57.32 | 50.50 | 62.12 | 64.82 |
|    | hsb-dsb | chrF++ | 27.10 | 77.19 | 72.35 | 80.12 | 81.96 |
| QA | all | Exact Match | **43.39** | **46.77** | **57.33** | **65.05** | **55.92** |
|    | hsbqa | Exact Match | 42.38 | 44.76 | 58.57 | 66.19 | 54.76 |
|    | dsbqa | Exact Match | 44.39 | 48.78 | 56.10 | 63.90 | 57.07 |
| SC | all | Exact Match | **6.66** | **63.63** | **73.13** | **76.11** | **78.03** |
|    | hsbsc | Exact Match (Wrong) | 6.95 | 72.40 | 81.55 | 81.90 | 84.25 |
|    |       | Exact Match (Corrected) | 6.80 | 52.85 | 66.95 | 69.65 | 73.50 |
|    | dsbsc | Exact Match (Wrong) | 6.60 | 72.70 | 78.05 | 81.55 | 82.35 |
|    |       | Exact Match (Corrected) | 6.30 | 56.55 | 65.95 | 71.35 | 72.00 |
| GC | all | Exact Match | **1.34** | **50.02** | **62.11** | **78.32** | **79.52** |
|    | hsbgc | Exact Match (Wrong) | 1.90 | 50.25 | 64.70 | 79.20 | 79.30 |
|    |       | Exact Match (Corrected) | 0.35 | 50.00 | 60.80 | 73.30 | 73.85 |
|    | dsbgc | Exact Match (Wrong) | 2.67 | 49.94 | 63.09 | 83.02 | 85.05 |
|    |       | Exact Match (Corrected) | 0.46 | 49.88 | 59.85 | 77.75 | 79.90 |
| MR | all | Exact Match | **5.40** | **5.00** | **18.60** | **30.40** | **29.00** |
|    | hsbmr | Exact Match | 6.00 | 5.20 | 19.20 | 32.00 | 29.20 |
|    | dsbmr | Exact Match | 4.80 | 4.80 | 18.00 | 28.80 | 28.80 |


