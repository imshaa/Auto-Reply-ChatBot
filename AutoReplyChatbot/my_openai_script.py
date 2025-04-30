import openai  


openai.api_key = "OPENAI_API_KEY"


role_instruction = """
You are a person named Imsha who speaks urdu as well as English.
She is from Pakistan and is a software engineering student.
You analyze chat history and respond like imsha, keeping the tone natural and friendly.
"""

chat_history = """
# It will directly copy our selected chat history
"""

latest_message = " /// "

messages = [
    {"role": "system", "content": role_instruction},
    {"role": "user", "content": f"Chat History:\n{chat_history}\n\nUser: {latest_message}\nImsha:"}
]


completion = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=messages
)


print("Imsha:", completion["choices"][0]["message"]["content"])
