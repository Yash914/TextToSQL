import torch
import re


def generate_sql(model, question, input_vocab, output_vocab, max_len=80):
    model.eval()

    # Extract numbers in order
    numbers = re.findall(r"\d+", question)

    # Extract quoted names or proper names (after "student")
    name_match = re.search(r"student\s+([A-Za-z]+)", question)
    names = [name_match.group(1)] if name_match else []

    processed_question = question.lower()

    # Replace numbers sequentially
    processed_question = re.sub(r"\d+", "<NUM>", processed_question)

    # Replace name if exists
    if names:
        processed_question = processed_question.replace(names[0].lower(), "<STR>")

    processed_question = re.sub(r"[^\w\s><=]", "", processed_question)

    tokens = processed_question.split()
    ids = [input_vocab.get(t, input_vocab["<UNK>"]) for t in tokens]
    ids += [input_vocab["<PAD>"]] * (max_len - len(ids))

    src = torch.tensor(ids).unsqueeze(0)

    hidden, cell = model.encoder(src)

    input_token = torch.tensor([output_vocab["<START>"]])
    result = []

    idx2word = {v: k for k, v in output_vocab.items()}

    for _ in range(max_len):
        output, hidden, cell = model.decoder(input_token, hidden, cell)
        top1 = output.argmax(1)

        word = idx2word[top1.item()]

        if word == "<END>":
            break

        result.append(word)
        input_token = top1

    generated_sql = " ".join(result)

    # Restore numbers in order
    for num in numbers:
        generated_sql = generated_sql.replace("<NUM>", num, 1)

    # Restore string
    if names:
        generated_sql = generated_sql.replace("<STR>", f"'{names[0]}'")

    return generated_sql