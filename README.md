# AI Newsletter Generator

An AI-powered tool that transforms a Markdown market digest into a fully formatted HTML newsletter and sends it via email.  


## 🚀 Features

- **LLM-powered analysis**: Converts Markdown text into structured JSON.
- **Automatic HTML generation**: Produces a clean, modern email-style layout.
- **Email delivery**: Sends the final newsletter via SMTP.
- **Separation of concerns**: Transformer → HTML generator → Mailer.
- **Environment-based configuration**: No secrets in code.
- **Anonymized example included**: Safe for public demos or tutorials.


### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Newsletter-Generator.git
cd AI-Newsletter-Generator
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

---

## 🔐 Configuration

Copy the environment template:

```bash
cp .env.example .env
```

Then fill in your credentials:

```env
GOOGLE_API_KEY="your_google_api_key_here"

EMAIL_SENDER="your_email@example.com"
EMAIL_PASSWORD="your_app_password_here"
EMAIL_RECEIVER="recipient1@example.com,recipient2@example.com"
```

### Notes:
- Gmail requires an **App Password**, not your normal password.
- Multiple recipients must be comma-separated.
- Never commit your personal `.env` file.

---

## 🧠 How the System Works

### 1️⃣ Transformation Agent  
Reads a Markdown digest and asks an LLM to extract:

- top news  
- key players  
- competitive landscape  
- risk radar  
- strategic insights  
- closing reflection  

### 2️⃣ HTML Generator  
Takes the structured JSON and injects it into a lightweight, customizable HTML layout.

### 3️⃣ Mailer  
Connects to your SMTP server and sends the newsletter.

---


## 🧪 Example Digest

You can modify the provided anonymized example:

```
examples/input_digest_example.md
```

Or replace it with your own Markdown content.

---

## 🛠️ Customization

You can easily adjust:

- **Color palette / layout** → `html_generator.py`
- **JSON schema & prompt** → `transformer_agent.py`
- **SMTP subject & settings** → `mailer.py`

Everything is intentionally simple and transparent.

---
## 🧩 Combining All Modules into a Single Script (Optional)

This project follows a clean, modular architecture:
- **each responsibility — analysis, HTML generation, email delivery, orchestration — lives in its own file.**
This makes the code easier to maintain, extend, and reuse.

However, if you prefer a **single-file script** (e.g., for small deployments or personal workflows), 
you can merge all modules into a unified file such as newsletter_agent.py.

Here is how to do it:

### 1️⃣ Copy the contents of each module

In this order:

- transformer_agent.py
- html_generator.py
- mailer.py
- main.py (renamed as if __name__ == "__main__": block)

### 2️⃣ Remove the import paths

Replace:
- from src.transformer_agent import run_transformation_agent
with a direct call to the function (since it’s now defined above).

Do the same for:
- from src.html_generator import generate_html_email
- from src.mailer import send_email

### 3️⃣ Keep the functions exactly as they are

They are self-contained and do not depend on hidden state.

### 4️⃣4️ Final structure of the merged script

Your unified script would look like this:


```
newsletter_agent.py
├── run_transformation_agent()
├── generate_html_email()
├── send_email()
└── main() and execution block
```

### 5️⃣Environment variables remain the same

The .env file, configuration, and usage instructions do not change.

📌 Optional: Quick Start for a Unified Script

If users want a “one file only” version, they would:

```
cp src/transformer_agent.py newsletter_agent.py
cat src/html_generator.py >> newsletter_agent.py
cat src/mailer.py >> newsletter_agent.py
cat src/main.py >> newsletter_agent.py
```

(Or simply paste the content manually in the order described above.)

---

## 🤝 Contributing

Contributions, discussions, and feature proposals are welcome!  
You may open an Issue or submit a Pull Request.

---

## 📄 MIT License

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER  
DEALINGS IN THE SOFTWARE.
```

---