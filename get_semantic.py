import requests as rq
import json

# set your own enviroments
# ========================
API_SERVER = ''
MODEL_ID = ''
API_KEY = ''
# ========================
INFERENCE_SERVER = f"{API_SERVER}/api/models/{MODEL_ID}"


def load_inputs(filename):
    inputs_list = []
    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            inputs_list.append(json.loads(line)['inputs'])
    return inputs_list


def inference(input):
    url = "{}/generate".format(INFERENCE_SERVER)
    headers = {
        "X-API-KEY": API_KEY,
        "content-type": "application/json"
    }
    data = {
        "inputs": input
    }

    return rq.post(url, headers=headers, json=data)


def main():
    inputs = load_inputs('TWS_AFS_CLOUD_EVAL.jsonl')
    for input in inputs:
        response = inference(input)
        print(f"inputs:{input}, response:{response}")


if __name__ == '__main__':
    main()
