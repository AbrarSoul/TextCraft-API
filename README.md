# TextCraft API

This project provides a REST API for generating text using a Large Language Model (LLM). The API leverages a pre-trained model from Hugging Face's Transformers library and serves it via a Flask-based web server.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Text Generation:** Generate text based on a prompt using a state-of-the-art LLM (e.g., GPT-2).
- **Customizable Output:** Specify the maximum length of the generated text.
- **Scalable API:** Easily deployable in various environments, including local, cloud, or containerized setups.

## Requirements

- Python 3.8+
- `pip` (Python package manager)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/TextCraft-API.git
    cd TextCraft-API
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python app.py
    ```

    The API will be available at `http://127.0.0.1:5000`.

## Usage

### Testing the API

You can test the API using tools like `curl`, Postman, or any HTTP client.

#### Example Request

```bash
curl -X POST http://127.0.0.1:5000/generate \
-H "Content-Type: application/json" \
-d '{"prompt": "Once upon a time", "max_length": 100}'
