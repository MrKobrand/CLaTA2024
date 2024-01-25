import argparse
from natasha import (
    MorphVocab,
    DatesExtractor,
)


def _parse_args():
    parser = argparse.ArgumentParser(description='Date and time extractor')
    parser.add_argument('-f', '--filename')
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    with open(args.filename, 'r') as f:
        text = f.read()

    morph_vocab = MorphVocab()
    dates_extractor = DatesExtractor(morph_vocab)

    extracted_dates = [
        f'{extracted_date.fact.day}.{extracted_date.fact.month}.{extracted_date.fact.year}'
        for extracted_date in list(dates_extractor(text))
    ]

    print(extracted_dates)
