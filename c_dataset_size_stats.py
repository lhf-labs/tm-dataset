import os
from PIL import Image
from tqdm import tqdm
from statistics import mean, stdev

PATH = '../output/images'
if __name__ == '__main__':
    widths = list()
    heights = list()
    fails = 0
    for file in tqdm(os.listdir(PATH)):
        try:
            width, height = Image.open(os.path.join(PATH, file)).size
            widths.append(width)
            heights.append(height)
        except:
            fails = fails + 1

    print(f'Width -  min: {min(widths)}, max: {max(widths)}, mean: {mean(widths)}, std: {stdev(widths)}')
    print(f'Height -  min: {min(heights)}, max: {max(heights)}, mean: {mean(heights)}, std: {stdev(heights)}')
    print(fails)
