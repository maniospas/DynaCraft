import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import pickle
from matplotlib import pyplot as plt


def trainer(train_dataset,
                val_dataset,
                model,
                epochs=100,
                batch_size=64,
                lr=0.001,
                device="cpu",
                model_path="model/model.pth",
                vocab_path="model/vocab.pickle",
                keep_best=True):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    os.makedirs(os.path.dirname(vocab_path), exist_ok=True)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    train_losses = list()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    best_val_accuracy = 0.0

    # Save vocab
    with open(vocab_path, 'wb') as f:
        pickle.dump(train_dataset.dataset.token2idx, f)  # Access the underlying dataset's token2idx

    for epoch in range(epochs):
        model.train()
        epoch_loss = 0
        for seq, labels in train_loader:
            seq, labels = seq.to(device), labels.to(device)
            optimizer.zero_grad()
            output, _ = model(seq)
            loss = criterion(output, labels)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=5)
            optimizer.step()
            epoch_loss += loss.item()
            _, predicted = torch.max(output.data, 1)

        epoch_loss /= len(train_loader)
        train_losses.append(epoch_loss)

        model.eval()
        val_loss = 0
        correct = 0
        total = 0
        val_losses = list()
        with torch.no_grad():
            for seq, labels in val_loader:
                seq, labels = seq.to(device), labels.to(device)
                output, _ = model(seq)
                loss = criterion(output, labels)
                val_loss += loss.item()
                _, predicted = torch.max(output.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        val_loss /= len(val_loader)
        val_losses.append(val_loss)
        accuracy = 100 * correct / total

        # Save the model if the validation accuracy is the best we've seen so far.
        if accuracy > best_val_accuracy:
            best_val_accuracy = accuracy
            if keep_best:
                torch.save(model.state_dict(), model_path)
        print(f'Epoch  {epoch + 1}/{epochs}: Train loss {epoch_loss:.3f}\t Val loss {val_loss:.3f}\t Val acc {accuracy:.3f}\t Best val acc {best_val_accuracy:.3f}')

    # Plot and save the losses
    plt.figure(figsize=(10, 5))
    plt.plot(train_losses, label='Training Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Losses')
    plt.savefig(os.path.join(os.path.dirname(model_path), 'loss_plot.png'))

    # Save model
    if not keep_best:
        torch.save(model.state_dict(), model_path)