import argparse
import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


def _parse_args():
    parser = argparse.ArgumentParser(description='Chat bot')
    parser.add_argument('-if', '--intents-filename')
    parser.add_argument('-mf', '--model-filename')
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open(args.intents_filename, 'r') as json_data:
        intents = json.load(json_data)

    FILE = args.model_filename
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot_name = 'Sam'
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input('You: ')
        if sentence == 'quit':
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f'{bot_name}: I do not understand...')
