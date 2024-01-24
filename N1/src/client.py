import argparse
import requests
import json

URL = 'http://127.0.0.1:8000/audio-transcription'


def _parse_args():
    parser = argparse.ArgumentParser(description='Audio translator')
    parser.add_argument('-f', '--filenames', nargs='+', default=[])
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    files = [('files', open(f, 'rb')) for f in args.filenames]
    response = requests.post(URL, files=files)
    response_json = json.dumps(response.json(), indent=4)

    print(response_json)
