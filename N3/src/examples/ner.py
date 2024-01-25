from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsNERTagger,
    Doc
)

segmenter = Segmenter()

emb = NewsEmbedding()

text = "Программу назвали «Yandex», название придумали Илья Сегалович, директор «Яндекса» по технологиям, и генеральный директор компании — Аркадий Волож."
doc = Doc(text)

doc.segment(segmenter)

ner_tagger = NewsNERTagger(emb)
doc.tag_ner(ner_tagger)
doc.ner.print()

