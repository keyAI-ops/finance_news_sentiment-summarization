import torch
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import pandas as pd
import numpy as np
import random

def set_seed(random_seed):
    torch.random.manual_seed(random_seed)
    torch.manual_seed(random_seed)
    torch.cuda.manual_seed(random_seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(random_seed)
    random.seed(random_seed)

def summaryModel(text):
    tokenizer = AutoTokenizer.from_pretrained("noahkim/KoT5_news_summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("noahkim/KoT5_news_summarization")
    
    set_seed(777)


    input_ids = tokenizer.encode(text)
    gen_ids = model.generate(torch.tensor([input_ids]),
                           max_length=1000,repetition_penalty=1.4,
                           top_k=6,
                           temperature=1.0,                          
                           pad_token_id=tokenizer.pad_token_id,
                           eos_token_id=tokenizer.eos_token_id,
                           bos_token_id=tokenizer.bos_token_id)
    
    generated = tokenizer.decode(gen_ids[0,:].tolist(),skip_special_tokens=True)

    return generated