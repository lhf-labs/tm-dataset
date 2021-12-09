# Instructions to build the L3D dataset on your own 📖

Make sure you have ```Python3.8``` or greater as well as ```tqdm``` and ```PIL``` libraries installed.

1- Clone our repository:
```
git clone https://github.com/lhf-labs/tm-dataset
```

2- Download the dataset:
```
python a_download_data.py
```

3- Prepare the dataset using multiprocessing. Depending on the compute capacity (CPU and Disk read/write speed) you might want to change https://github.com/lhf-labs/tm-dataset/blob/main/b_build_dataset_multiproc.py#L92:
```
python b_build_dataset_multiproc.py
```

4- (optional) Compute statistics:
```
python c_dataset_size_stats.py
```
5- Remove too small images as we consider them outliers:
```
python d_filter_dataset.py
```
*After this operation you can run step 4 again*

6- Install [ImageMagick](https://imagemagick.org/index.php). You can use Windows Linux Substystem if you are on Linux. For MacOS users install it
using brew and for Linux users just use apt.

6.1- Normalize the image formats to JPG.
```
cd ../output/images
find . -name \*.TIF -exec mogrify -format jpg '{}' \;
```

6.2- (optional) Change all .jpg to .JPG. For some image processing libraries you might need the images as .jpg, if that is the case, perform the reverse operation.

```
find . -name \*.jpg -exec rename -f 's/.jpg/.JPG/' '{}' \;
```

6.3- Resize the images to 256x256 centering the image, mantaining the original image ratio and adding a white background if necessary. 

```
find . -name \*.JPG -exec mogrify -resize 256x256 -background white -gravity center -extent 256x256 '{}' \;
```

7- Fix the JSONs (image renames), corrupted images, etc.

```
python f_fix_json.py
```

8- Remove the images that are removed.

```
python g_clean_images.py
```

*The rest of the scripts are for analytical purposes only.*
