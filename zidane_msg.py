import random

zidane_quotes = [
    "Les performances individuelles, ce n'est pas le plus important. On gagne et on perd en équipe.",
    "Je suis fier que l'on me compare à Michel Platini.",
    "Parfait, je les prends.",
    "La vie est pleine de regrets, mais ça ne paie pas de regarder en arrière.",
    "C'est mon père qui nous a appris qu'un immigrant doit travailler deux fois plus que n'importe qui d'autre, qu'il ne doit jamais abandonner.",
    "Le Real Madrid est la chose la plus importante qui m'est arrivée, à la fois en tant que footballeur et en tant que personne.",
    "Je suis censé donner l'exemple aux jeunes joueurs.",
    "Mon père est Algérien, fier de qui il est et je suis fier que mon père soit algérien.",
    "Peu importe combien de fois vous gagnez un prix, c'est toujours très spécial.",
    "J'ai peut-être eu beaucoup de chance dans ma vie, mais j'ai encore besoin de trouver un défi dans le jeu.",
    "J'ai l'impression de faire ce que je veux. Et ce sera toujours comme ça.",
    "J'ai gagné de nombreux prix et j'en suis très content, mais je ne suis pas le meilleur joueur au monde.",
    "Je pense que Marseille est probablement un endroit comme Liverpool, très dynamique et très dur.",
    "Être reconnu par tout un pays, c'est incroyable.",
    "Quand vos propres fans sifflent et se moquent, alors vous avez un gros problème.",
    "Je suis d'abord de La Castellane et Marseille.",
    "De toute évidence, la mode est un monde complètement différent du football."
]



def get_random_quote():
    return random.choice(zidane_quotes)
