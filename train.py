import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from preprocessing import load_data, build_vocab
from dataset import TextToSQLDataset
from model import Encoder, Decoder, Seq2Seq

device = torch.device("cpu")

pairs = load_data()

questions = [p[0] for p in pairs]
sqls = [p[1] for p in pairs]

input_vocab = build_vocab(questions)
output_vocab = build_vocab(sqls)

dataset = TextToSQLDataset(pairs, input_vocab, output_vocab)
loader = DataLoader(dataset, batch_size=8, shuffle=True)

encoder = Encoder(len(input_vocab), 256, 512)
decoder = Decoder(len(output_vocab), 256, 512)

model = Seq2Seq(encoder, decoder)

criterion = nn.CrossEntropyLoss(ignore_index=output_vocab["<PAD>"])
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(50):
    total_loss = 0

    for src, trg in loader:
        optimizer.zero_grad()
        output = model(src, trg)

        output = output[:, 1:].reshape(-1, output.shape[-1])
        trg = trg[:, 1:].reshape(-1)

        loss = criterion(output, trg)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss/len(loader)}")

torch.save({
    "model": model.state_dict(),
    "input_vocab": input_vocab,
    "output_vocab": output_vocab
}, "model.pth")