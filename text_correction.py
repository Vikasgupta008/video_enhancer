# text_correction.py
import openai

def correct_text(text):
    openai.api_type = "azure"
    openai.api_base = "YOUR_AZURE_ENDPOINT"
    openai.api_version = "2023-05-15"
    openai.api_key = "YOUR_API_KEY"

    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that corrects grammar and removes filler words."},
            {"role": "user", "content": f"Please correct this text and remove filler words: {text}"}
        ]
    )
    return response.choices[0].message['content']