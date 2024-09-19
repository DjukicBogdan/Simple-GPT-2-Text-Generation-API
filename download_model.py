# download_model.py
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Preuzimanje pretreniranog modela i tokenizera
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Čuvanje modela i tokenizera u lokalni direktorijum
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")
