import pandas as pd
import re
from collections import Counter

SPECIAL_TOKENS = ["<PAD>", "<START>", "<END>", "<UNK>"]
CSV_PATH = "data/student_dataset.csv"


def clean_question(text):
    text = text.lower()

    # Replace numbers
    text = re.sub(r"\d+", "<NUM>", text)

    # Replace quoted strings
    text = re.sub(r"'[a-zA-Z]+'", "<STR>", text)

    text = re.sub(r"[^\w\s><=]", "", text)

    return text


def clean_sql(text):
    text = text.lower()

    text = re.sub(r"\d+", "<NUM>", text)
    text = re.sub(r"'[a-zA-Z]+'", "<STR>", text)

    text = re.sub(r"[^\w\s><=]", "", text)

    return text


def load_data():
    df = pd.read_csv(CSV_PATH)

    pairs = []
    for _, row in df.iterrows():
        question = clean_question(row["question"])
        sql = clean_sql(row["sql"])
        pairs.append((question, sql))

    return pairs


def build_vocab(sentences):
    counter = Counter()
    for sentence in sentences:
        counter.update(sentence.split())

    vocab = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}

    for word in counter:
        if word not in vocab:
            vocab[word] = len(vocab)

    return vocab