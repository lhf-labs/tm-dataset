$TOKENS_PER_SAMPLE = 1024

fairseq-train \
  --only-source \
  -- srcdict dict.txt \
  --arch "hf_gpt2" \
  --task language_modeling --criterion label_smoothed_cross_entropy \
  --sample-break-mode complete_doc --tokens-per-sample $TOKENS_PER_SAMPLE \
  --optimizer adam --adam-betas '(0.9,0.98)' --adam-eps 1e-6 --clip-norm 0.0
  ;
