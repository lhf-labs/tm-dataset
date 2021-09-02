import os
import json

PATH = '../output/images'
if __name__ == '__main__':
    data = None
    with open(os.path.join(PATH, 'results.json'), 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    files = set(os.listdir(PATH))
    data = set(map(lambda x: x['file'], data))
    to_remove = list(data.difference(files))
    for rm in to_remove:
        os.remove(os.path.join(PATH, rm))

    print(len(to_remove), "removed")
