import os
import json

PATH = '../output'
if __name__ == '__main__':
    data = None
    with open(os.path.join(PATH, 'results.json'), 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    files = set(os.listdir(os.path.join(PATH, 'images')))
    data = set(map(lambda x: x['file'], data))
    to_remove = list(files.difference(data))
    for rm in to_remove:
        os.remove(os.path.join(PATH, 'images', rm))

    print(len(to_remove), "removed")
