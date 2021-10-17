python train_vqvae.py --batch-size 32 --lr 3e-4 --num-workers 4 --hidden-size 1024 --k 8192 \
       --data-folder /home/oracle/tm_euipo/output_vqvae/images --device cuda:0

python train_vqvae.py --batch-size 16 --lr 3e-4 --num-workers 4 --hidden-size 512 --k 4096 \
       --data-folder /home/oracle/tm_euipo/output_vqvae/images --device cuda:0