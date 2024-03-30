import argparse
from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc
)


def _parse_args():
    parser = argparse.ArgumentParser(description='Literary authors extractor')
    parser.add_argument('-f', '--filename')
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    with open(args.filename, 'r') as f:
        text = f.read()

    segmenter = Segmenter()
    morph_vocab = MorphVocab()

    emb = NewsEmbedding()
    ner_tagger = NewsNERTagger(emb)

    names_extractor = NamesExtractor(morph_vocab)

    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)

    for span in doc.spans:
        span.normalize(morph_vocab)
        if span.type == PER:
            span.extract_fact(names_extractor)

    extracted_literary_authors = {
        _.normal: _.fact.as_dict for _ in doc.spans if _.type == PER
    }
    print(extracted_literary_authors)
