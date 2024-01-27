import os
import re
import time
import argparse
from datetime import datetime

from common.database_providers.mongo_provider import MongoProvider
from common.parsers.google_patent_parser import GooglePatentParser
from common.web_drivers.google_patent_webdriver import GooglePatentWebDriver
from common.database import Database
from common.patent import Patent
from models.patent_model import PatentModel


def _parse_args():
    parser = argparse.ArgumentParser(description='Web patent parser')
    parser.add_argument(
        '-f',
        '--filename',
        help='Path to file with patent links'
    )
    return parser.parse_args()


def main():
    args = _parse_args()
    database_provider = MongoProvider(os.environ['MONGO_CONNECTION_STRING'])
    database = Database(database_provider)
    database.ensure_db_and_table_created()

    google_driver = GooglePatentWebDriver()
    google_parser = GooglePatentParser(google_driver)

    patent_id_pattern = re.compile(r'^[A-Z]{2}[0-9]{6,7}[A-Z][0-9]$')

    with open(args.filename, 'r') as f:
        patent_links = [
            patent_link.strip() for patent_link in f.read().split('\n')
        ]

    patent_links_len = len(patent_links)

    for idx, patent_link in enumerate(patent_links):
        # if idx < 58:
        #     continue
        now = datetime.now().strftime('%H:%M:%S')
        print(f'{now} - [{idx + 1}/{patent_links_len}] - {patent_link}')

        patent = Patent(patent_link, google_parser)

        patent_id = patent.get_id()

        if patent_id_pattern.match(patent_id):
            if not database.check_if_patent_exists(patent_id):
                patent_model = PatentModel()
                patent_model.patent_id = patent_id
                patent_model.title = patent.get_title()
                patent_model.url = patent_link
                patent_model.abstract = patent.get_abstract()
                patent_model.description = patent.get_description()
                patent_model.claims = patent.get_claims()

                database.insert_patent(patent_model)

        # Задержка, чтобы избежать бана 429 Too Many Requests
        time.sleep(15)


if __name__ == '__main__':
    main()
