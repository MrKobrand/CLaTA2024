import argparse

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


def _parse_args():
    parser = argparse.ArgumentParser(description='Problem finder')
    parser.add_argument(
        '-m',
        '--model',
        help='Path to model'
    )
    parser.add_argument(
        '-f',
        '--filename',
        help='Path to file with patent description'
    )
    return parser.parse_args()


def answer(x, **kwargs):
    inputs = tokenizer(x, return_tensors='pt').to(model.device)
    with torch.no_grad():
        hypotheses = model.generate(**inputs, **kwargs)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


if __name__ == '__main__':
    args = _parse_args()

    trained_model = args.model
    model = T5ForConditionalGeneration.from_pretrained(trained_model)
    tokenizer = T5Tokenizer.from_pretrained(trained_model)

    with open(args.filename) as f:
        data = f.read()

    print(answer(data))
