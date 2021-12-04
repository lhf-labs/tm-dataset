import os
import json

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoTokenizer, GPT2Config

PATH = './models'
OUTPUT_PATH = './output/'

if __name__ == '__main__':
    #tokenizer = AutoTokenizer.from_pretrained("./models")

    # add the EOS token as PAD token to avoid warnings
    #tokenizer = GPT2Tokenizer(config=GPT2Config(**json.load(open(os.path.join(PATH, 'config.json')))))
    model = GPT2LMHeadModel(config=GPT2Config(**json.load(open(os.path.join(PATH, 'config.json')))))

    #input_ids = tokenizer.encode('', return_tensors='tf')

    greedy_output = model.generate(torch.zeros((10, 1), dtype=torch.int), max_length=1024+1, min_length=1024+1)
    print(list(greedy_output.data[0].numpy()))

    for file in ('train', 'valid', 'test'):
        with open(os.path.join(OUTPUT_PATH, f'{file}.txt'), 'w') as fout:
            data = greedy_output.data
            for i in range(len(data)):
                elements = list(data[i].numpy())[1:]
                for idx, element in enumerate(elements):
                    fout.write(str(int(element)))
                    if idx < len(elements):
                        fout.write(" ")
                fout.write('\n')
