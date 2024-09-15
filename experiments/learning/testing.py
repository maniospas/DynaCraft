import pickle
import torch
from experiments.learning.classifier import LSTMClassifier
from experiments.learning.tokenizer import dynacraft_tokenizer


def load(model_file,
         vocab_file,
         device="cpu"):
    with open(vocab_file, 'rb') as f:  # Ensure this path matches the path used in the training script
        token2idx = pickle.load(f)
    model = LSTMClassifier(len(token2idx), embedding_dim=16, hidden_dim=16, num_layers=2).to(device)
    model.load_state_dict(torch.load(model_file, map_location=device))
    model = model.to(device)
    return model, token2idx


def predict(model,
             token2idx,
             input_str,
             device="cpu",
             tokenizer=dynacraft_tokenizer):
    model.eval()
    tokens = tokenizer(input_str)
    token_indices = [token2idx[token] for token in tokens if token in token2idx]
    if len(token_indices) == 0:
        return 1
    seq = torch.tensor(token_indices, dtype=torch.long).unsqueeze(0).to(device) # unsqueeze adds an extra dimension at the beginning to represent the batch size
    with torch.no_grad():
        output, _ = model(seq)
        _, predicted = torch.max(output.data, 1)
    return int(predicted.item())
