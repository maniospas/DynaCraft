import torch
from torch.utils.data import random_split
from experiments.learning.dataset import CodeDataset
from experiments.learning.classifier import LSTMClassifier
from experiments.learning.training import trainer
from experiments.learning.tokenizer import python_tokenizer

def read_snippets(path):
    with open(path, 'r') as file:
        return file.read().replace("\n", "").strip().split('-----')


# Example Usage
if __name__ == "__main__":
    valid = read_snippets('synthetic_dataPythonGenerator/valid.txt')
    invalid = read_snippets('synthetic_dataPythonGenerator/invalid.txt')
    if len(invalid) > len(valid):
        invalid = invalid[:len(valid)]
    print(f"Valid snippets {len(valid)}/{len(valid)+len(invalid)}")

    dataset = CodeDataset(valid + invalid,  [0]*len(valid) + [1]*len(invalid), tokenizer=python_tokenizer)
    train_dataset, val_dataset = random_split(dataset, [0.8, 0.2])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(F"Experimenting on device: {device}")

    model = LSTMClassifier(dataset.vocab_size, embedding_dim=16, hidden_dim=16, num_layers=2).to(device)
    trainer(train_dataset, val_dataset, model, device=device, epochs=50, keep_best=False, batch_size=64)
