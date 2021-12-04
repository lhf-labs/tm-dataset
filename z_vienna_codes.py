import csv
import json


def normalize(id):
    id = '.'.join([element if len(element) == 2 else '0' + element for element in id.split('.')])
    return id


if __name__ == '__main__':
    data = {}
    with open('../categories.tsv') as fin:
        reader = csv.reader(fin, delimiter='\t')
        for row in reader:
            data[normalize(row[0])] = row[1].lower()

    with open('../categories.json', 'w') as fout:
        json.dump(data, fout)
