import os
from collections import OrderedDict
from transformers import GPT2Config, GPT2LMHeadModel
from fairseq.checkpoint_utils import torch_persistent_save, load_checkpoint_to_cpu
import json
from fairseq_model import hf_gpt2


PATH = "checkpoints-save-hf2"
FQ_CP = "checkpoints/checkpoint_best.pt"
#model = GPT2LMHeadModel.from_pretrained(PATH, local_files_only=True)
cp_fq = load_checkpoint_to_cpu(FQ_CP)
model_fq = cp_fq["model"]
model_to_copy = OrderedDict()
for key in model_fq:
    model_to_copy[key.partition('decoder.model.')[2]] = model_fq[key]
print(model_to_copy.keys())
model_to_copy['transformer.wpe.weight'] = model_to_copy['transformer.wpe.weight'][1:]
model = GPT2LMHeadModel(config=GPT2Config(**json.load(open(os.path.join(PATH, 'config.json')))))
model.load_state_dict(model_to_copy, strict=False)
model.save_pretrained(PATH)
