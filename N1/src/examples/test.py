import argparse
import torch
import nemo.collections.asr as nemo_asr


def infer_greedy(files, asr_model):
    return asr_model.transcribe(files, batch_size=20)


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Run inference using NeMo checkpoint')
    parser.add_argument(
        'asr_ckpt', help='Path to ASR NeMo checkpoint file (.nemo)')
    parser.add_argument('-f', '--filenames', nargs='+', default=[])
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from(args.asr_ckpt)
    files = args.filenames
    hyps = infer_greedy(files, asr_model)
    print(hyps)
