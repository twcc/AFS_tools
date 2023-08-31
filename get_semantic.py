import requests as rq
import json
import argparse

# set your own enviroments
# ========================
API_ENDPOINT = ''		# copy from your AFS Cloud
API_KEY      = '' 		# copy from your AFS Cloud
# ========================

MODEL_ID = 'ffm-7b'  # keep this, default model_id
INFERENCE_SERVER = f"{API_ENDPOINT}/text-generation/api/models/generate"


def load_inputs(filename):
    inputs_list = []
    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            inputs_list.append(json.loads(line)['inputs'])
    return inputs_list


def inference(text):
    headers = {
        "X-API-KEY": API_KEY,
        "content-type": "application/json"
    }
    data = {
        "inputs": text + "\n\nA:",
        "model": f"{MODEL_ID}"
    }

    ans = rq.post(INFERENCE_SERVER, headers=headers, json=data)
    return ans


def main(filename):
    inputs = load_inputs(filename)
    for text in inputs:
        print(inference(text).json())
        response = inference(text).json()['generated_text']
        print(f"[INPUT]\n{text}\n\n[Response]\n{response}")
        print("="*20)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='the name of the file to operate on')
    args = parser.parse_args()

    if API_ENDPOINT == '' or API_KEY == '':
        print(f'Please set your own API_ENDPOINT and API_KEY in get_semantic.py')
        exit(0)
    if args.filename:
        print(f'Operating on file: {args.filename}')
    else:
        args.filename = './jsonl/TWS_AFS_CLOUD_EVAL.jsonl'

    main(args.filename)
