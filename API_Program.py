import openai

def ask(text):
    openai.api_key='API-KEY'
    

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=120,
    )
    return response.choices[0].text


def main():
    while True:
        text=input("Question: ")
        if 'hi' in text or 'hello' in text or 'hey' in text:
            print("Hello, I am a chatbot. I can answer your very questions.")
            continue
        print(ask(text))
        if text.endswith("None"):
            text.replace("None","")
main()
