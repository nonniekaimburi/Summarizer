import os
import openai

openai.organization = "org-zr2hzpsw3Lma4hcDkvasgqQu"
openai.api_key = os.getenv("OPENAI_API_KEY")  # Fetch the API key from environment variables for security.

def summarize(text):
    # Use OpenAI to generate a summary. The prompt is crafted to guide the model.
    response = openai.Completion.create(prompt=f"Summarize the following text: {text}", model="gpt-4.0-turbo", max_tokens=100)
    return response.choices[0].text.strip()
