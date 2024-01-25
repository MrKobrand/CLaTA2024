import argparse
from natasha import (
    MorphVocab,
    AddrExtractor,
)


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Countries, cities and settlements extractor')
    parser.add_argument('-f', '--filename')
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    with open(args.filename, 'r') as f:
        text = f.read()

    morph_vocab = MorphVocab()
    addr_extractor = AddrExtractor(morph_vocab)

    extracted_addresses = [
        {
            'value': extracted_addr.fact.value,
            'type': extracted_addr.fact.type,
        }
        for extracted_addr in list(addr_extractor(text))
    ]

    print(extracted_addresses)
