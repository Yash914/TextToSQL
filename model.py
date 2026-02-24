import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, input_size, embed_size, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(input_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)

    def forward(self, x):
        embedded = self.embedding(x)
        outputs, (hidden, cell) = self.lstm(embedded)
        return hidden, cell


class Decoder(nn.Module):
    def __init__(self, output_size, embed_size, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(output_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden, cell):
        embedded = self.embedding(x.unsqueeze(1))
        output, (hidden, cell) = self.lstm(embedded, (hidden, cell))
        prediction = self.fc(output.squeeze(1))
        return prediction, hidden, cell


class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, src, trg):
        batch_size = src.size(0)
        trg_len = trg.size(1)
        output_dim = self.decoder.fc.out_features

        outputs = torch.zeros(batch_size, trg_len, output_dim)

        hidden, cell = self.encoder(src)

        input = trg[:, 0]

        for t in range(1, trg_len):
            output, hidden, cell = self.decoder(input, hidden, cell)
            outputs[:, t] = output
            input = trg[:, t]

        return outputs