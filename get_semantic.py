import requests as rq
import json
import argparse

# set your own enviroments
# ========================
API_ENDPOINT = ''		# copy from your AFS Cloud
API_KEY      = '' 		# copy from your AFS Cloud
# ========================

MODEL_ID = '00000000'  # keep this, default model_id
API_SERVER = API_ENDPOINT+"/text-generation"
INFERENCE_SERVER = f"{API_SERVER}/api/models/{MODEL_ID}"


def load_inputs(filename):
    inputs_list = []
    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            inputs_list.append(json.loads(line)['inputs'])
    return inputs_list


def inference(text):
    url = "{}/generate".format(INFERENCE_SERVER)
    headers = {
        "X-API-KEY": API_KEY,
        "content-type": "application/json"
    }
    data = {
        "inputs": text + "\n\nA:"
    }

    ans = rq.post(url, headers=headers, json=data)
    return ans


def main(filename):
    inputs = load_inputs(filename)
    for text in inputs:
        response = inference(text).json()['generated_text']
        print(f"INPUT: {text}\n\tResponse:{response}")


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
