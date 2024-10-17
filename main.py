import sys
import json
from groq import Groq

sys.stdout.reconfigure(encoding='utf-8')

json_file_path = sys.argv[1]
dubTo = sys.argv[2]
with open(json_file_path, 'r', encoding='utf-8') as json_file:
        script = json.load(json_file)

def function(script, dubTo):
    client = Groq(api_key="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")        
    completion = client.chat.completions.create(
        model="llama-3.2-90b-text-preview",
        messages=[
            {
                "role": "user",
                "content": f"I have a script for a YouTube video and I want translate the text only into {dubTo}. Please ensure that the tone, style, and delivery are preserved exactly as in the original script as well as I want use of English as well as daily sentence words.\nI want give no addition or extra words like 'here is the sentence' or 'feel free to ask' and such more things. I want only script in your response.\nScript:\n {script}",
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

function(script, dubTo)
