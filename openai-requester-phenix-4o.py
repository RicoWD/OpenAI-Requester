import openai
import csv
from dotenv import load_dotenv
import os
from rich.console import Console
from openai import OpenAI
import requests
from PIL import Image
from IPython.display import display


load_dotenv()
console = Console()
client = OpenAI()

# Charger les variables d'environnement à partir du fichier .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# def (py) = function (js)
# (prompt) détermine l'arguement (ce qu'on envoie à la fonction lorsqu'on l'appelle)


########################################################################################
#                                                                                      #
#                                    STORY PROMPTS                                     #
#                                                                                      #
########################################################################################

##################################### CHARACTERS #######################################

Marie = """
Elle s'appelle Marie.\
Marie est la cheffe du groupe..\
Marie est notre guide suprême\
Marie est trés gentille.\
Marie aime son travail et le fait très bien.\
"""

Zina = """
Elle s'appelle Zina.\
Qui mange du Gluten free.\
Zina travail Aubervilliers.\
Zina est trés pointilleuse.\
Zina aime le nétoyant à base de vinaigre.\
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
Maurice travail souvent avec ```{Patrick}```\
"""

Ibrahim = """
Ibrahim s'appelle Ibrahim \
Ibrahim est passionné par l'IA et la trotinette éléctrique.\
Ibrahim n'a plus de voiture en ce moment ni de son scooter en ce moment.\
Ibrahim vient tous les jours en trotinette élélectique.\
Ibrahim est très curieux et aime rechercher \
Ibrahim aime faire un travail minitieux et à l'esthétique impécable.\
"""

Sylvain = """
Il s'appelle Sylvain \
Sylvain est le petit chef de l'équipe.\
C'est un petit tyran communément appelé Dictasylvain.\
Sylvain est très fort et est celui qui connait le plus son métier. \
Sylvain est introverti et mange de toutes petites portions.\
"""

Billal = """
Il s'appelle Billal \
Billal le dernier venu de la bande.\
Billal se fait appellé Bito.\
Billal aime beaucoup cuisiner et est le concurrent cuisine d'{Eric}\
Billal s'est bien intégré dans l'équipe.\
"""

Yordan = """
Il s'appelle Yordan \
Yordan est en train d'apprendre beaucoup de chose\
Yordan est cool.\
"""

Eric = """
Il s'appelle Eric \
Eric est passionné par l'IA\
Eric aime beaucoup cuisiner et faire de la pâtisserie.\
Eric est très déconneur.\
Eric est le concurrent de {Billal}\
"""


##################################### COMBINED #######################################

combined_user_prompt = f"""
Les personnages sont les suivants :
Marie : {Marie}
Zina : {Zina}
Patrick : {Patrick}
Maurice : {Maurice}
Ibrahim : {Ibrahim}
Sylvain : {Sylvain}
Billal : {Billal}
Yordan : {Yordan}
Eric : {Eric}
Écrivez une histoire courte et complète.\
Les protagonistes sont Marie Zina, Patrick, Maurice, Ibrahim, Sylvain, Billal, Yordan, Eric.\
Il doit y avoir de l'action et des combats dans l'histoire.\
Tes histoires doivent être cohérentes et les personnages et leurs personnalité prise en compte\
Il faut que l'histoire se termine en catharsis généralisée.\
Tu dois formater le text en paragraphe.\
"""
# Parmis les protagonistes il y a un seul traitre qui est déterminé de façon aléatoire.\
# Le nom du traitre et la raison de la traitrise doit être connu à la fin de l'histoire.\

system_prompt = """
Tu es un conteur d'histoire courte et passionante.\
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
            "content": "Ecris un prompt précis et concis qui servira à DALL-E pour générer une belle image illustrant l'histoire que tu viens de générer. L'image doit être réaliste.",
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
image_url = response.data[0].url

console.print(f"Generated image URL: {image_url}", style="bold red")

# # set a directory to save DALL·E images to
# image_dir_name = "images"
# image_dir = os.path.join(os.curdir, image_dir_name)

# # create the directory if it doesn't yet exist
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)

# # print the directory to save to
# print(f"{image_dir=}")

# # save the image
# generated_image_name = (
#     "generated_image.png"  # any name you like; the filetype should be .png
# )
# generated_image_filepath = os.path.join(image_dir, generated_image_name)
# generated_image_url = response.data[0].url  # extract image URL from response
# generated_image = requests.get(generated_image_url).content  # download the image


# with open(generated_image_filepath, "wb") as image_file:
#     image_file.write(generated_image)  # write the image to the file

# print(generated_image_filepath)
# display(Image.open(generated_image_filepath))

# # console.print(f"Generated image URL: {image_url}", style="bold green")
