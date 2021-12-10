import json
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain
from collections import defaultdict

plt.rcParams.update({
    "font.family": "CMU Serif",
    "font.size": 10
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


if __name__ == '__main__':
    with open('../results.json') as fin:
        data = json.load(fin)

    print("Total images", len(data))

    plot_by_year(data)
    plot_assign(data)

