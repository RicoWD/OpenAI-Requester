import openai
from dotenv import load_dotenv, find_dotenv

# Charger les variables d'environnement depuis un fichier .env
_ = load_dotenv(find_dotenv())

# Définir votre clé API OpenAI
openai.api_key = "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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# Texte d'exemple pour la complétion
text = """
C'est l'histoire d'un homme.
Il est australien.
Il habite en France.
Il travaille dans la finance.
"""

# Prompt pour obtenir une description courte du texte
prompt = f"""
Écrivez une histoire dans lequel le méchant est l'homme décrit entre les triples backticks \
en une seule phrase.
```{text}```
"""

# Obtenir une complétion
response = get_completion(prompt)

print(response)
