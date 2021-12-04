import json
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain

plt.rcParams.update({
    "font.family": "CMU Serif"
})


def plot_by_year(data):
    years_counts = Counter(sorted([d['year'] for d in data]))
    years = list(years_counts.keys())
    counts = list(years_counts.values())


def plot_assign(data):
    ncodes_count = Counter(sorted([len(d['vienna_codes']) for d in data]))
    ncodes = list(ncodes_count.keys())
    counts = list(ncodes_count.values())


def get_tree(data):
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

    plot_by_year(data)
    plot_assign(data)
    vc_obj = get_tree(data)
    with open('../stats.json', 'w') as fout:
        json.dump(vc_obj, fout)

