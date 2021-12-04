find . -name \*.TIF -exec mogrify -format jpg '{}' \;
find . -name \*.jpg -exec rename -f 's/.jpg/.JPG/' '{}' \;
find . -name \*.JPG -exec mogrify -resize 256x256 -background white -gravity center -extent 256x256 '{}' \;

