DATA_DIR=data-bin
TOTAL_UPDATES=125000    # Total number of training steps
WARMUP_UPDATES=1000    # Warmup the learning rate over this many updates
PEAK_LR=0.00005          # Peak learning rate, adjust as needed
TOKENS_PER_SAMPLE=1025   # Max sequence length
MAX_POSITIONS=1025       # Num. positional embeddings (usually same as above)
MAX_SENTENCES=8         # Number of sequences per batch (batch size)
UPDATE_FREQ=128
echo $1 $2 $3
fairseq-train --memory-efficient-fp16 $DATA_DIR \
--task language_modeling --criterion label_smoothed_cross_entropy \
--arch hf_gpt2 --sample-break-mode eos --tokens-per-sample $TOKENS_PER_SAMPLE \
--optimizer adam --adam-betas '(0.9,0.98)' --adam-eps 1e-6 --clip-norm 0.0 \
--lr-scheduler polynomial_decay --lr $PEAK_LR --warmup-updates $WARMUP_UPDATES --total-num-update $TOTAL_UPDATES \
--dropout 0.1 --attention-dropout 0.1 --weight-decay 0.01 \
--batch-size $MAX_SENTENCES --update-freq $UPDATE_FREQ \
--max-update $TOTAL_UPDATES --log-format simple --log-interval 1 \
--tensorboard-logdir tb-save-hf --skip-invalid-size-inputs-valid-test \
--num-workers 0 \
--save-interval-updates 1 --save-dir checkpoints-save-hf --user-dir ./../custom_model --save-hf-cp --train-subset valid