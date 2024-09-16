#from tokenizerFile import tokenizer
import torch
from torch.utils.data import Dataset
from experiments.learning.tokenizer import dynacraft_tokenizer


class CodeDataset(Dataset):
    def __init__(self,
                 snippets,
                 labels,
                 seq_length=60,
                 tokenizer=dynacraft_tokenizer):
        self.tokenized_snippets = [tokenizer(snippet) for snippet in snippets]
        self.tokens = sorted(list(set(token for snippet in self.tokenized_snippets for token in snippet)))
        self.token2idx = {token: idx for idx, token in enumerate(self.tokens)}
        self.idx2token = {idx: token for token, idx in self.token2idx.items()}
        self.vocab_size = len(self.tokens)
        self.snippets = snippets
        self.labels = labels
        self.seq_length = seq_length
        self.data = self._prepare_data(self.tokenized_snippets, labels, seq_length)

    def _prepare_data(self, tokenized_snippets, labels, seq_length):
        sequences = []
        for snippet, label in zip(tokenized_snippets, labels):
            for i in range(0, len(snippet) - seq_length):
                seq = snippet[i:i + seq_length]
                sequences.append((seq, label))
        return sequences

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        seq, label = self.data[index]
        seq_idx = torch.tensor([self.token2idx[token] for token in seq], dtype=torch.long)
        label_idx = torch.tensor(label, dtype=torch.long)
        return seq_idx, label_idx
