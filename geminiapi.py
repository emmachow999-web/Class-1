from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

systemPrompt = ("You are a grandmother in your eighties who has no knowledge of math, science, or technology whatsoever and steers the conversation towards baking, gardening, and other typical grandmother-ly hobbies.")

history = []

while True:
    userMessage = input("you: ")
    
    if userMessage == "":
        continue

    if userMessage.lower() in ["quit", "exit", "bye", "goodbye", "stop"]:
        print("Bye!")
        break

    parts = []

    for message in history:
        if message["role"] == "user":
            parts.append("You: " + message["text"])
        
        else:
            parts.append("AI: " + message["text"])

    parts.append("You: " + userMessage)
    parts.append("AI:")
    fullPrompt = "\n".join(parts)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=fullPrompt,
        config={"system_instruction": systemPrompt}
    )

    aiReply = response.candidates[0].content.parts[0].text

    print (aiReply)

    history.append({"role": "user", "text": userMessage})
    history.append({"role": "ai",   "text": aiReply})
