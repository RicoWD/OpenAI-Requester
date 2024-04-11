import openai
import csv

# ATTENTION ! Doit normalement être dans un fichier ".env" qui doit rester secret.
# C'est avec la clé API que l'on s'identifie auprès de chatGPT et que l'on est débité

OPENAI_API_KEY = "sk-OkjzlJPKKwecP2qFPm00T3BlbkFJfc8avgmjt8PlmEivx---"

# def (py) = function (js)
# (prompt) détermine l'arguement (ce qu'on envoie à la fonction lorsqu'on l'appelle)


def get_completion(prompt):

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=3000
    )

    with open("output_openai.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([response.choices[0].text])

    return response.choices[0].text


# Prompts (secondaires) que l'on réutilisera dans l'envoie à la fonction

Zina = """
Elle s'appelle Zina.\
Zina est française.\
Qui mange du Gluten free.\
Zina travail Aubervilliers.\
Zina est trés pointilleuse.\
Zina aime le nétoyant à base de vinaigre.\
"""

Clément = """ 
Il s'appelle Clément.\
Clément est marié à Sakura. \
Clément est le petit chef de l'équipe. \
Clément se balade souvent en chaussettes. \
Clément était absent pendant un moment et ```̀{Raouf}``` a pris sa place pendant ce temps.\
Clément va nous quitter bientôt et ``̀{Raouf}``` va lui reprendre sa place. \
"""

Raouf = """
Il s'appelle Raouf \
Raouf était le petit chef pendant que ```{Clément}``` n'était pas là.\
Pendant que Raouf était chef, Raouf était très tyranique.\
Raouf veut reprendre son statut de petit chef\
C'est Raouf qui a le plus de connaissance dans le domaine. \
"""

Patrick = """
Il s'appelle Patrick\
Il est très sportif\
Il aime manger des frites.\
Il boit toujours son Caprisun.\
Il confond toujours Javascript avec Java\
Il travail souvent avec ```{Maurice}```
"""

Maurice = """
Il s'appelle Maurice\
Maurice est notre dernier venu\
Maurice est un nouveau joueur de Pokémon Go\
Maurice est très prometteur\
Maurice a disparu depuis deux jours et personne ne sait ou Maurice se trouve.
Maurice travail souvent avec ```{Patrick}```\
Maurice s'endors souvent partout, même debout, et ronfle énormement. \
"""

Ibrahim = """
Ibrahim s'appelle Ibrahim \
Ibrahim est passionné par l'IA et de véhicules.\
Ibrahim n'a plus de voiture en ce moment ce qui le rend triste, même s'il a toujours son scooter.\
Ibrahim est très curieux et aime rechercher \
Ibrahim aime faire un travail minitieux et à l'esthétique impécable.\
"""

Eric = """
Il s'appelle Eric \
Eric est passionné par l'IA\
Eric aime beaucoup cuisiner et faire de la pâtisserie.\
Eric est traumatisé par son dernier dessert qui n'a pas survécu aux transports. \
"""

data = """ScM"""


# Ce qui est envoyé à l'API
# Prompt faisant le lien entre tous les autres prompts

prompt = f"""
Écrivez une histoire courte et complète.\
Les protagonistes ```{Zina} ```, ```{Clément} ```, ```{Raouf} ```, ```{Patrick} ```, ```{Maurice} ```, ```{Ibrahim} ```, ```{Eric} ``` ont tous la même importance dans l'histoire. \
Parmis ```{Zina} ```, ```{Clément} ```, ```{Raouf} ```, ```{Patrick} ```, ```{Maurice} ```, ```{Ibrahim} ```, ```{Eric} ```, il y a un seul traitre qui est déterminé de façon aléatoire. \
Il doit y avoir de l'action et des combats dans l'histoire.
Le nom du traitre et la raison de la traitrise doit être connu à la fin de l'histoire.
"""

# On lance la fonction déclarée en haut et on lui envoie comme prompt le contenu entre les """ """
response = get_completion(prompt)


# print() [py] = console.log() [js]
print(response)
