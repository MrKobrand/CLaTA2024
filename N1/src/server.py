import os
import argparse
from typing import List

import torch
import nemo.collections.asr as nemo_asr

import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
TEMP_DIRECTORY = './temp'


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Run inference using NeMo checkpoint')
    parser.add_argument(
        'asr_ckpt', help='Path to ASR NeMo checkpoint file (.nemo)')
    return parser.parse_args()


def infer_greedy(files, asr_model):
    return asr_model.transcribe(files, batch_size=20)


@app.post("/audio-transcription")
def transcribe_audio(files: List[UploadFile]):
    filenames = []

    for file in files:
        try:
            contents = file.file.read()
            os.makedirs(TEMP_DIRECTORY, exist_ok=True)
            uploaded_filename = f'{TEMP_DIRECTORY}/{file.filename}'
            with open(uploaded_filename, 'wb') as f:
                f.write(contents)
            filenames.append(uploaded_filename)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    hyps = infer_greedy(filenames, asr_model)

    for filename in filenames:
        os.remove(filename)

    transcriptions = list(zip(filenames, hyps))

    return {
        "message": f"Successfuly uploaded {[file.filename for file in files]}",
        "result": [
            {
                "filename": transcription[0],
                "transcription": transcription[1]
            }
            for transcription in transcriptions
        ]
    }


if __name__ == '__main__':
    args = _parse_args()
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from(args.asr_ckpt)
    uvicorn.run(app, host="127.0.0.1", port=8000)
