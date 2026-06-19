import pandas as pd
import sacrebleu

from math_verify import parse, verify


# Read JSONL files
def read_gold_pred_files(gold_file_path, pred_file_path):
    '''Read the gold and prediction JSONL files.'''
    gold_df = pd.read_json(gold_file_path, lines=True, encoding='utf-8')
    pred_df = pd.read_json(pred_file_path, lines=True, encoding='utf-8')
    n = len(gold_df)
    print(f'{n} instances')
    assert n == len(pred_df), f'Not the same number of lines: {n}, {len(pred_df)}'

    return gold_df, pred_df


# Metrics
## MT
def compute_bleu_chrfpp(pred_list, ref_list):
    '''Compute BLEU and chrF++ for MT outputs (list).'''
    sabl_ref_list = [ref_list]
    bleu = sacrebleu.corpus_bleu(pred_list, sabl_ref_list).score
    chrfpp = sacrebleu.corpus_chrf(pred_list, sabl_ref_list, word_order=2).score
    return (bleu, chrfpp)


def evaluate_mt(pred_file_path, gold_file_path, trg_lang):
    '''Evaluate the MT task from the file paths.'''
    gold_df, pred_df = read_gold_pred_files(gold_file_path, pred_file_path)

    print(f'Target language: {trg_lang}')
    gold_translation_list = list(gold_df[trg_lang])
    pred_translation_list = list(pred_df['pred'])

    return compute_bleu_chrfpp(pred_translation_list, gold_translation_list)


## QA, SC & GC: accuracy
def accuracy_score(pred_list, ref_list):
    '''Compute the accuracy score between the predictions and references.'''
    n = len(ref_list)
    assert len(pred_list) == n, f'Different lengths: {len(pred_list)} and {n}.'

    total_match = sum(pred_val == ref_val for pred_val, ref_val in zip(pred_list, ref_list))
    return (total_match / n)


def evaluate_qa(pred_file_path, gold_file_path):
    '''Evaluate the QA task from the file paths.'''
    gold_df, pred_df = read_gold_pred_files(gold_file_path, pred_file_path)

    gold_label_list = list(gold_df['correct_answer_num'])
    pred_label_list = list(pred_df['pred'])

    return accuracy_score(pred_label_list, gold_label_list)

def evaluate_checking(pred_file_path, gold_file_path):
    '''Evaluate the SC and GC tasks from the file paths.'''
    gold_df, pred_df = read_gold_pred_files(gold_file_path, pred_file_path)

    # Error detection
    gold_incorrect_label_list = list(gold_df['incorrect_word'])
    pred_incorrect_label_list = list(pred_df['pred_incorrect'])

    detection_accuracy = accuracy_score(pred_incorrect_label_list, gold_incorrect_label_list)

    # Error correction
    gold_correct_label_list = list(gold_df['correct_word'])
    pred_correct_label_list = list(pred_df['pred_corrected'])

    correction_accuracy = accuracy_score(pred_correct_label_list, gold_correct_label_list)

    print('Error detection accuracy:', detection_accuracy)
    print('Error correction accuracy:', correction_accuracy)

    return (detection_accuracy, correction_accuracy)


## MR
def maths_reasoning_evaluation(gold_list, pred_list):
    '''Compute the maths reasoning score with a dedicated parser.'''
    n = len(gold_list)
    assert len(pred_list) == n, f'Not the same length: {n} {len(pred_list)}'

    match_list = []
    for i in range(n):
        gold = parse(gold_list[i])
        pred = parse(pred_list[i])
        
        match_list.append(verify(gold, pred))

    return sum(match_list) / n


def evaluate_mr(pred_file_path, gold_file_path):
    '''Evaluate the MR task from the file paths.'''
    gold_df, pred_df = read_gold_pred_files(gold_file_path, pred_file_path)

    gold_label_list = list(gold_df['answer'].map(str))
    pred_label_list = list(pred_df['pred'])

    return maths_reasoning_evaluation(gold_label_list, pred_label_list)

