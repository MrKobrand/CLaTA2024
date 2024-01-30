import os
import json

from yargy import interpretation as interp
from yargy.interpretation import (
    fact,
    attribute
)

from yargy.pipelines import (
    caseless_pipeline,
    morph_pipeline
)

from yargy.predicates import (
    caseless, type, gram, normalized,
    in_, in_caseless, dictionary
)

from yargy import (
    Parser,
    rule, or_, and_, not_,
)

from razdel import sentenize
from ipymarkup import show_span_ascii_markup as show_markup

from common.database_providers.mongo_provider import MongoProvider
from common.database import Database


def test(rule, *tests):
    parser = Parser(rule)
    for line, etalon in tests:
        match = parser.match(line)
        assert match, line
        guess = match.fact
        assert etalon == guess, guess


def show_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


class Match(object):
    def __init__(self, fact, spans):
        self.fact = fact
        self.spans = spans


Problem = fact(
    'Problem',
    ['problem', 'solution']
)


DEBUG = or_(
    PROBLEM
)


class Extractor(object):
    def __init__(self):
        self.debug = Parser(DEBUG)

    def __call__(self, line):
        matches = self.debug.findall(line)
        spans = [_.span for _ in matches]

        fact = None
        if matches:
            fact = matches[0].fact.item

        return Match(fact, spans)


def main():
    database_provider = MongoProvider(os.environ['MONGO_CONNECTION_STRING'])
    database = Database(database_provider)
    patents = database.get_patents()
    for patent in patents:
        problems = []
        extractor = Extractor()
        description_sentences = list(sentenize(patent.description))

        for description_sentence in description_sentences:
            match = extractor(description_sentence)
            # show_markup(description_sentence, match.spans)

            # if match.fact:
            #     show_json(match.fact.as_json)

            if match.fact:
                problems.append({
                    'sentence': description_sentence,
                    'problem': match.fact.problem,
                    'solution': match.fact.solution
                })

        database.insert_problems(patent.patent_id, problems)


if __name__ == '__main__':
    main()
