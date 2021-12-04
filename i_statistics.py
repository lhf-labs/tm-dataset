import json
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain
from collections import defaultdict


def get_base(data):
    vienna_codes = chain.from_iterable([d['vienna_codes'] for d in data])
    vienna_codes = sorted([vc.replace('.', '') for vc in vienna_codes])
    vc_obj = {}
    for depth in [2, 4, 6]:
        vcs = [vc[0:depth] for vc in vienna_codes]
        vc_obj.update(Counter(vcs))

    return vc_obj


if __name__ == '__main__':
    with open('../results.json') as fin:
        data = json.load(fin)

    print("Total images", len(data))


    vc_obj = get_base(data)
    with open('../stats.json', 'w') as fout:
        json.dump(vc_obj, fout)

    data = {
        'type': 'sunburst',
        'labels': [],
        'parents': [],
        'values': [],
        'leaf': {'opacity': 0.4},
        'marker': {'line': {'width': 2}},
        'branchvalues': 'total'
    }

    for element_k, element_v in vc_obj.items():
        if len(element_k) == 6:
            element_k = element_k[0:2] + "." + element_k[2:4] + "." + element_k[4:]
        elif len(element_k) == 4:
            element_k = element_k[0:2] + "." + element_k[2:]
        data['labels'].append(element_k)
        data['values'].append(element_v)
        if len(element_k) > 2:
            data['parents'].append(element_k[:-3])
        else:
            data['parents'].append('')
    with open('../plotly_chart.json', 'w') as fin:
        json.dump([data], fin)
