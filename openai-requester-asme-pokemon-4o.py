import openai
import csv
from dotenv import load_dotenv
import os
from rich.console import Console
from openai import OpenAI
import requests
from PIL import Image
from IPython.display import display


# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
console = Console()
client = OpenAI()

openai.api_key = os.getenv("OPENAI_API_KEY")

# def (py) = function (js)
# (prompt) détermine l'arguement (ce qu'on envoie à la fonction lorsqu'on l'appelle)


########################################################################################
#                                                                                      #
#                                    STORY PROMPTS                                     #
#                                                                                      #
########################################################################################

##################################### CHARACTERS #######################################
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


##################################### COMBINED #######################################

combined_user_prompt = f"""
Les personnages sont les suivants :
Soukhi : {Soukhi}
Sarah : {Sarah}
Mehdy : {Mehdy}
Eric : {Eric}
Écrivez une histoire courte et complète. 
Les protagonistes Soukhi, Sarah, Mehdy, et Eric sont des dresseurs Pokémon. 
Un Pokémon doit leur être attribué en accord avec leur personnalité. 
Le nom de ce Pokémon doit être connu. Parmi Soukhi, Sarah, Mehdy, et Eric, il y a un seul traître qui est déterminé de façon aléatoire. 
Il doit y avoir de l'action et des combats dans l'histoire. 
Le nom du traître et la raison de la traîtrise doivent être connus à la fin de l'histoire.
Rajoutez des dialogues crus et vulgaires.
"""

system_prompt = """
Tu es un conteur d'histoire courte et passionante.\
Tu dois formater le text en paragraphe.\
Tes histoires doivent être cohérentes et les personnages et leurs personnalité prise en compte\
"""

########################################################################################
#                                                                                      #
#                                      GENERATIONS                                     #
#                                                                                      #
########################################################################################

######################################### STORY ########################################

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": combined_user_prompt},
    ],
)

generated_story = completion.choices[0].message.content

console.print(generated_story, style="bold yellow")


######################################## RESUME ########################################

completion_resume = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Ecris un prompt précis et concis qui servira à DALL-E pour générer une belle image illustrant l'histoire que tu viens de générer.",
        },
        {"role": "user", "content": generated_story},
    ],
)

generated_resume = completion_resume.choices[0].message.content

console.print(generated_resume, style="bold blue")


######################################### IMAGE ########################################


response = client.images.generate(
    model="dall-e-3",
    prompt=generated_resume,
    size="1024x1024",
    quality="standard",
    n=1,
)
# image_url = response.data[0].url

# set a directory to save DALL·E images to
image_dir_name = "images"
image_dir = os.path.join(os.curdir, image_dir_name)

# create the directory if it doesn't yet exist
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# print the directory to save to
print(f"{image_dir=}")

# save the image
generated_image_name = (
    "generated_image.png"  # any name you like; the filetype should be .png
)
generated_image_filepath = os.path.join(image_dir, generated_image_name)
generated_image_url = response.data[0].url  # extract image URL from response
generated_image = requests.get(generated_image_url).content  # download the image


with open(generated_image_filepath, "wb") as image_file:
    image_file.write(generated_image)  # write the image to the file

print(generated_image_filepath)
display(Image.open(generated_image_filepath))

# console.print(f"Generated image URL: {image_url}", style="bold green")
