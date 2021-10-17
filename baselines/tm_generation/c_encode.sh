python encode.py --checkpoint models/2021-10-08-1638/model_3.pt  --batch-size 64 --hidden-size 1024 --k 8192 \
       --data-folder ../output_vqvae/images > logs.txt

python encode.py --checkpoint models/2021-10-14-1406/model_9.pt  --batch-size 64 --hidden-size 512 --k 4096 \
       --data-folder ../output_vqvae/images > logs.txt