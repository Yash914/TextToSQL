import torch
from torch.utils.data import Dataset


class TextToSQLDataset(Dataset):
    def __init__(self, pairs, input_vocab, output_vocab, max_len=40):
        self.pairs = pairs
        self.input_vocab = input_vocab
        self.output_vocab = output_vocab
        self.max_len = max_len

    def encode(self, sentence, vocab):
        tokens = sentence.split()
        ids = [vocab.get(t, vocab["<UNK>"]) for t in tokens]
        ids = ids[:self.max_len]
        ids += [vocab["<PAD>"]] * (self.max_len - len(ids))
        return torch.tensor(ids)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        question, sql = self.pairs[idx]

        input_ids = self.encode(question, self.input_vocab)

        sql_tokens = ["<START>"] + sql.split() + ["<END>"]
        sql_ids = [self.output_vocab.get(t, self.output_vocab["<UNK>"]) for t in sql_tokens]
        sql_ids = sql_ids[:self.max_len]
        sql_ids += [self.output_vocab["<PAD>"]] * (self.max_len - len(sql_ids))

        return input_ids, torch.tensor(sql_ids)