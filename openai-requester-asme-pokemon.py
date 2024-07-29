import openai
import csv
from dotenv import load_dotenv
import os
from rich.console import Console

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
console = Console()

# ATTENTION ! Doit normalement être dans un fichier ".env" qui doit rester secret.
# C'est avec la clé API que l'on s'identifie auprès de chatGPT et que l'on est débité


openai.api_key = os.getenv("OPENAI_API_KEY")

# def (py) = function (js)
# (prompt) détermine l'arguement (ce qu'on envoie à la fonction lorsqu'on l'appelle)


def get_completion(prompt):

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=3000
    )

    with open("output-openai-asme.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([response.choices[0].text])

    return response.choices[0].text


# Prompts (secondaires) que l'on réutilisera dans l'envoie à la fonction

# Prompts for characters
Soukhi = """
Elle s'appelle Soukhi.\
Souhki est une femme.\
Soukhi est très gentille et organisée .\
Soukhi est la guide suprême du groupe.\
Soukhi n'a pas confiance en elle.\
Soukhi est susceptible.\
Soukhi est introvertie.\
Souhki est autoritaire.\
"""

Sarah = """ 
Elle s'appelle Sarah.\
Sarah est une femme.\
Sarah est enthousiaste.\
Sarah est très gentille.\
Sarah fait de très bon cup cakes.\
Sarah est la fiancée de Mehdy.\
Sarah est hypersensible.\
Sarah est chiante.\
Sarah est très conne.\
"""

Mehdy = """
Il s'appelle Mehdy.\
Mehdy est un homme.\
Mehdy s'en bas les couilles de tout.\
Mehdy est serviable.\
Mehdy est très gourmand.\
Mehdy est le fiancé de Sarah.\
Mehdy est un petit malin.\
Mehdy est un bon ami.\
Mehdy est vulgaire.\
Mehdy est un putain de raciste.\
"""

Eric = """
Il s'appelle Eric.\
Eric est un homme.\
Eric est très serviable.\
Eric est éloquent.\
Eric est jovial.\
Eric adore apprendre des choses.\
Eric aime la cuisine.\
Eric est attentionné.\
Eric est coquin.\
Eric a un début de calvitie qu'il n'assume pas.\
"""


# Ce qui est envoyé à l'API
# Prompt faisant le lien entre tous les autres prompts

prompt = f"""
Écrivez une histoire courte et complète.\
Les protagonistes ```{Soukhi} ```, ```{Sarah} ```, ```{Mehdy} ```, ```{Eric} ``` sont des dresseurs Pokémon. U
Un Pokémon doit leur être attibué en accord avec leur personnalité. \
Le nom de ce Pokemon doit être connu. \
Parmis ```{Soukhi} ```, ```{Sarah} ```, ```{Mehdy} ```, ```{Eric} ```, il y a un seul traitre qui est déterminé de façon aléatoire. \
Il doit y avoir de l'action et des combats dans l'histoire.
Le nom du traitre et la raison de la traitrise doit être connu à la fin de l'histoire.
"""

# On lance la fonction déclarée en haut et on lui envoie comme prompt le contenu entre les """ """
response = get_completion(prompt)


# print() [py] = console.log() [js]
console.print(response, style="bold green")
