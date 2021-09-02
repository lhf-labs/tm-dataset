import os
from PIL import Image
from tqdm import tqdm

PATH = '../output/images'
FILTER_WIDTH_HEIGHT = 20
if __name__ == '__main__':
    removal_count = 0
    for file in tqdm(os.listdir(PATH)):
        remove = False
        file = os.path.join(PATH, file)

        try:
            width, height = Image.open(file).size
            remove = (width < FILTER_WIDTH_HEIGHT) or (height < FILTER_WIDTH_HEIGHT)
        except:
            remove = True
        if remove:
            removal_count = removal_count + 1
            os.remove(file)

    print(removal_count, 'removed')



