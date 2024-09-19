# Simple GPT-2 Text Generation API

## Description

The Simple GPT-2 Text Generation API is a basic web API that uses the GPT-2 model to generate text based on a provided prompt. This API is built using FastAPI and allows users to send text prompts and receive generated responses.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/simple-gpt2-text-generation-api.git
   cd simple-gpt2-text-generation-api

2. **Create and Activate Virtual Environment**

   ```python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **pip install -r requirements.txt**   

   ```bash
   pip install -r requirements.txt

4. **Download the Model**
   
   ```bash
   python download_model.py

## Usage

Start the API server:
```bash
uvicorn app:app --reload
```
The API will be available at http://127.0.0.1:8000

## Parameters

The API supports the following parameters:

prompt: The textual prompt used to generate text. (Required)
max_length: The maximum length of the generated text. (Default: 100)
temperature: Controls the creativity (lower values result in less creative responses). (Default: 1.0)
top_k: Number of most likely tokens to consider during generation. (Default: 50)
top_p: Controls the diversity in generation. (Default: 0.95)

## Examples

POST Request
Send a POST request to /generate/ with the JSON body:
```json
{
  "prompt": "What is the weather like today?",
  "max_length": 50,
  "temperature": 0.7
}
```

Response
```json
{
  "generated_text": "Today is sunny with a chance of light rain in the afternoon."
}
```
## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes and test them.
Submit a Pull Request.
If you have any questions or suggestions, feel free to open an issue or send an email.

Thank you for using the Simple GPT-2 Text Generation API!

### Notes

- **Replace the URL** in the cloning command with your GitHub repository URL.
- **Adjust the content** according to the specifics of your project, such as additional dependencies or specific instructions.

If you need further modifications or have other questions, just let me know!
