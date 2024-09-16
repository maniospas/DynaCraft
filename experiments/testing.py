import torch
from experiments.learning.testing import load, predict
from sklearn.metrics import accuracy_score


def read_snippets(path):
    with open(path, 'r') as file:
        return file.read().replace("\n", "").strip().split('-----')


if __name__ == "__main__":
    # load trained model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model, token2idx = load("model/model.pth", "model/vocab.pickle", device=device)
    idx2token = {v: k for k, v in token2idx.items()}

    # load testing data
    valid = read_snippets('synthetic_data/valid.txt')
    invalid = read_snippets('synthetic_data/invalid.txt')
    if len(invalid) > len(valid):
        invalid = invalid[:len(valid)]
    print(f"Valid snippets {len(valid)}/{len(valid) + len(invalid)}")
    snippets = valid + invalid
    labels = [0] * len(valid) + [1] * len(invalid)
    y_pred = [predict(model, token2idx, snippet, device=device) for snippet in snippets]
    accuracy = accuracy_score(labels, y_pred)
    print(f"Test accuracy {accuracy:.3f}")
