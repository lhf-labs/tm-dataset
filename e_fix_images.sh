find . -name \*.TIF -exec mogrify -format jpg '{}' \;
find . -name \*.jpg -exec rename -f 's/.jpg/.JPG/' '{}' \;
find . -name \*.JPG -exec mogrify -resize 800x800 -background white -gravity center -extent 800x800 '{}' \;

