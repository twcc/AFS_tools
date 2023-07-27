import os
import json
import re
import argparse

os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bigscience/tokenizer')



def get_token(inputs, targets):
    tokens = tokenizer.tokenize(inputs+targets)
    print(len(tokens), " tokens.")


def do_token_calculate(filename):
    error_list = []
    # load file
    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            try:
                data = json.loads(line)
                inputs = data['inputs']
                targets = data['targets']
                get_token(inputs, targets)
            except:
                # print(f'line:{index+1}, not match json format')
                error_list.append(str(index+1))
                matches = re.findall(
                    r'\s*"inputs"\s*:\s*"(.+)",\s*"targets"\s*:\s*"(.+)\s*"', line)
                for match in matches:
                    inputs = match[0]
                    targets = match[1]
                    get_token(inputs, targets)
    if error_list != []:
        print(f"Please check data!!! lines: [{','.join(error_list)}] format are not correct")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='the name of the file to operate on')
    args = parser.parse_args()

    if args.filename:
        print(f'Operating on file: {args.filename}')
    else:
        args.filename = './jsonl/get_token_inputs.jsonl'
        
    do_token_calculate(args.filename)

