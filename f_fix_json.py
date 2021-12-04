import os
import json
from tqdm import tqdm
from PIL import Image

PATH = '../output/'
if __name__ == '__main__':
    results = list()
    for element in os.listdir(PATH):
        if element.endswith('.json') and 'results' not in element:
            path = os.path.join(PATH, element)
            with open(path, 'r', encoding='utf-8') as fin:
                results.extend(json.load(fin))

    results_keep = list()
    for idx, result in tqdm(enumerate(results)):
        if not isinstance(result['vienna_codes'], list):
            result['vienna_codes'] = [result['vienna_codes']]
        result['file'] = result['file'].replace('.TIFF', '.JPG')
        result['file'] = result['file'].replace('.TIF', '.JPG')
        file = os.path.join(PATH, 'images', result['file'])

        if os.path.isfile(file):
            try:
                img = Image.open(file)
                img.verify()
                width, height = img.size
                if width == 256 and height == 256:
                    results_keep.append(result)
            except:
                pass

    print(len(results_keep), "results")
    with open(os.path.join(PATH, 'results.json'), 'w', encoding='utf-8') as fout:
        json.dump(results_keep, fout)
