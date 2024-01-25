import argparse
from natasha import (
    MorphVocab,
    MoneyExtractor,
)


def _parse_args():
    parser = argparse.ArgumentParser(description='Money extractor')
    parser.add_argument('-f', '--filename')
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    with open(args.filename, 'r') as f:
        text = f.read()

    morph_vocab = MorphVocab()
    money_extractor = MoneyExtractor(morph_vocab)

    extracted_money = [
        {
            'amount': extracted_money.fact.amount,
            'currency': extracted_money.fact.currency,
        }
        for extracted_money in list(money_extractor(text))
    ]

    print(extracted_money)
