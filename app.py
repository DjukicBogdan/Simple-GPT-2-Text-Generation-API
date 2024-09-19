from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from fastapi.middleware.cors import CORSMiddleware
import torch

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost:3000",  # React app runs on this port by default
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained("./model")
tokenizer = GPT2Tokenizer.from_pretrained("./model")

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class TextRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.5
    top_k: int = 50
    top_p: float = 0.9

@app.post("/generate/")
async def generate_text(request: TextRequest):
    try:
        # Tokenize and move input to the appropriate device (CPU or GPU)
        inputs = tokenizer.encode(request.prompt, return_tensors="pt").to(device)
        outputs = model.generate(
            inputs,
            max_length=request.max_length,
            temperature=request.temperature,
            top_k=request.top_k,
            top_p=request.top_p,
            num_return_sequences=1
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"generated_text": generated_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the GPT-2 Text Generation API!"}
