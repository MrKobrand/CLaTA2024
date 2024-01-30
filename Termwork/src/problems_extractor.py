import os
import argparse
from typing import List

from yargy import Parser, rule
from yargy.interpretation import fact
from yargy.pipelines import caseless_pipeline, morph_pipeline
from razdel import sentenize

from common.database_providers.mongo_provider import MongoProvider
from common.database import Database


class PatentProblemAnalyzer:
    __PROBLEM = fact(
        'Problem',
        ['target', 'add_word', 'second_word']
    )

    __TARGET = morph_pipeline([
        'цель',
        'способ',
        'изобретение',
        'модель',
        'задача',
        'использование',
        'технический',
    ])

    __ADD_WORD = caseless_pipeline([
        'предполагаемого',
        'настоящего',
        'данного',
        'решаемая'
    ])

    __SECOND_WORD = morph_pipeline([
        'изобретения',
        'предназначено',
        'позволяет',
        'решения',
        'способа',
        'достигается',
        'результат',
        'решает',
        'направлено',
        'модели'
    ])

    def __init__(self) -> None:
        self.__ORG = rule(
            self.__TARGET.interpretation(self.__PROBLEM.target),
            self.__ADD_WORD.interpretation(self.__PROBLEM.add_word).optional(),
            self.__SECOND_WORD.interpretation(self.__PROBLEM.second_word)
        )

        self.__parser = Parser(self.__ORG)

    def get_problem_sentences(self, text) -> List[str]:
        sentences = [sentence.text for sentence in sentenize(text)]

        sentences_with_problems = []

        for sentence in sentences:
            matches = self.__parser.findall(sentence)

            for _ in matches:
                sentences_with_problems.append(sentence)
                break

        return sentences_with_problems


def _parse_args():
    parser = argparse.ArgumentParser(description='Problems extractor')
    parser.add_argument(
        '-f',
        '--filename',
        help='Path to save file with problems'
    )
    return parser.parse_args()


def main():
    args = _parse_args()
    database_provider = MongoProvider(os.environ['MONGO_CONNECTION_STRING'])
    database = Database(database_provider)
    patents = database.get_patents()

    patent_problem_analyzer = PatentProblemAnalyzer()
    patents_problems = []

    for patent in patents:
        patents_problems.extend(patent_problem_analyzer.get_problem_sentences(
            patent.description
        ))

    with open(args.filename, 'w+') as f:
        f.write('\n'.join(patents_problems))


if __name__ == '__main__':
    main()
