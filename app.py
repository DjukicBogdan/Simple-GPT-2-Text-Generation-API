# app.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = FastAPI()

# Učitavanje pretreniranog modela i tokenizera
model = GPT2LMHeadModel.from_pretrained("./model")
tokenizer = GPT2Tokenizer.from_pretrained("./model")

class TextPrompt(BaseModel):
    prompt: str

@app.post("/generate/")
async def generate_text(prompt: TextPrompt):
    inputs = tokenizer.encode(prompt.prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": generated_text}
