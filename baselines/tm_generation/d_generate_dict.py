from tqdm import tqdm

if __name__ == '__main__':
    different = set()
    with open('train.txt', 'r') as fin:
        for line in tqdm(fin):
            line = line.replace('\n', '')
            line = line.split(" ")
            different.update(line)
    print("different", len(different))

    different = sorted(list(map(int, list(different))))

    with open('dict.txt', 'w', encoding='utf-8') as fout:
        for token in different:
            fout.write(f'{token} 100\n')
