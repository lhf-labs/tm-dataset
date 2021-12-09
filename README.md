# The Large Labelled Logo Dataset (L3D): A Multipurpose and Hand-Labelled Continuously Growing Dataset 

**Website:** https://lhf-labs.github.io/tm-dataset
 
## Dataset 🗂️

You can download the dataset either using our scripts or downloading them from Zenodo.

### Using the scripts
Make sure you have ```Python3.8``` or greater as well as ```tqdm``` and ```PIL``` libraries installed.

1. Clone our repository:
```
git clone https://github.com/lhf-labs/tm-dataset
```

2. Download the dataset:
```
python a_download_data.py
```

3. Prepare the dataset using multiprocessing. Depending on the compute capacity (CPU and Disk read/write speed) you might want to change https://github.com/lhf-labs/tm-dataset/blob/main/b_build_dataset_multiproc.py#L92:
```
python b_build_dataset_multiproc.py
```

4. (optional) Compute statistics:
```
python c_dataset_size_stats.py
```
5. Remove too small images as we consider them outliers:
```
python d_filter_dataset.py
```

## Citing 📣
If you get inspiration from this work, please, cite it: TBA
```
TBA
```

## Contact 📧
For additional details contact Asier Gutiérrez-Fandiño <asier.gutierrez@bsc.es>.
