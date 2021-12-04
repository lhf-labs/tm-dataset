import json
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain
from collections import defaultdict

plt.rcParams.update({
    "font.family": "CMU Serif"
})


def plot_by_year(data):
    years_counts = Counter(sorted([d['year'] for d in data]))
    years = list(years_counts.keys())
    counts = list(years_counts.values())
    fig, ax = plt.subplots(1)
    plt.bar(range(len(years)), counts)
    ax.set_xticklabels(years, rotation=45)
    ax.set_xticks(range(len(years)))
    ax.set_ylabel("Count")
    ax.set_xlabel("Years")
    ax.set_title("Trademark count by year")
    plt.tight_layout()
    fig.savefig('./analysis/by_year.pdf')
    fig.savefig('./analysis/by_year.svg')


def plot_assign(data):
    ncodes_count = Counter(sorted([len(d['vienna_codes']) for d in data]))
    ncodes = list(ncodes_count.keys())
    counts = list(ncodes_count.values())
    fig, ax = plt.subplots(1)
    plt.bar(range(len(ncodes)), counts)
    ax.set_xticklabels(ncodes, rotation=45)
    ax.set_xticks(range(len(counts)))
    ax.set_ylabel("Count")
    ax.set_xlabel("Assignment")
    ax.set_title("Vienna code assignment by trademark")
    plt.tight_layout()
    fig.savefig('./analysis/by_trademark.pdf')
    fig.savefig('./analysis/by_trademark.svg')


def get_base(data):
    vienna_codes = chain.from_iterable([d['vienna_codes'] for d in data])
    vienna_codes = sorted([vc.replace('.', '') for vc in vienna_codes])
    vc_obj = {}
    for depth in [2, 4, 6]:
        vcs = [vc[0:depth] for vc in vienna_codes]
        vc_obj.update(Counter(vcs))

    return vc_obj


def get_tree(vc_obj, lookup_obj):
    vc_obj_filled = {'id': 'all', 'name': 'all', 'children': []}
    for vck, vcv in vc_obj.items():
        if len(vck) == 2:
            vc_obj_filled['children'].append({'id': vck, 'name': f'{vck}({vcv})', 'value': vcv, 'children': []}) # : {lookup_obj[vck]}

    for vck, vcv in vc_obj.items():
        if len(vck) == 4:
            vck = vck[:2]+'.'+vck[2:]
            for child in vc_obj_filled['children']:
                if child['id'] == vck[:2]:
                    child['children'].append({'id': vck, 'name': f'{vck}({vcv})', 'value': vcv, 'children': []}) # : {lookup_obj[vck]}
                    break

    for vck, vcv in vc_obj.items():
        if len(vck) == 6:
            vck = vck[:2] + '.' + vck[2:4] + '.' + vck[4:]
            for child_1 in vc_obj_filled['children']:
                if child_1['id'] == vck[:2]:
                    for child_2 in child_1['children']:
                        if child_2['id'] == vck[:4]:
                            child_2['children'].append({'id': vck, 'name': f'{vck}({vcv})', 'value': vcv}) # : {lookup_obj[vck]}
                            break
                    break
    return vc_obj_filled


if __name__ == '__main__':
    with open('../results.json') as fin:
        data = json.load(fin)

    print("Total images", len(data))

    plot_by_year(data)
    plot_assign(data)
    exit(0)
    vc_obj = get_base(data)
    with open('../stats.json', 'w') as fout:
        json.dump(vc_obj, fout)

    with open('../categories.json') as fin:
        lookup_obj = defaultdict(str)
        lookup_obj.update(json.load(fin))

    vc_obj_filled = get_tree(vc_obj, lookup_obj)
    with open('../stats_tree.json', 'w') as fout:
        json.dump(vc_obj_filled, fout)

