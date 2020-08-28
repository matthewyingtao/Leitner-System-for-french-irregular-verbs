import random

stack_a_verb = []
stack_a_stem = []
stack_b_verb = []
stack_b_stem = []
stack_c = []

stacks = [
    stack_a_verb, stack_a_stem, stack_b_verb, stack_b_stem
]

future_verb = [
    "avoir", "être", "aller", "faire", "devoir", "savoir", "pouvoir",
    "vouloir", "voir", "envoyer", "venir", "recevoir", "courir", "boire",
    "lire", "écrire", "dire"
]
future_stem = [
    "aur", "ser", "ir", "fer", "devr", "saur", "pourr", "voudr", "verr",
    "enverr", "viendr", "recevr", "courr", "boir", "lir", "écrir", "dir"
]

common_past_verb = [
    "être", "faire", "dire", "écrire", "conduire", "mettre", "prendre",
    "suivre", "rire", "dormir", "ouvrir", "avoir", "voir", "devoir", "savoir",
    "pouvoir", "vouloir", "recevoir", "vivre", "boire", "courir", "connaître"
]
common_past_stem = [
    "été", "fait", "dit", "écrit", "conduit", "mis", "pris", "suivi", "ri",
    "dormi", "ouvert", "eu", "vu", "dû", "su", "pu", "voulu", "reçu", "vécu",
    "bu", "couru", "connu"
]
etre_past_verb = [
    "monter", "rester", "sortir", "revenir", "devenir", "venir", "aller",
    "naître", "descendre", "entrer", "rentrer", "tomber", "retourner",
    "arriver", "mourir", "partir"
]
etre_past_pp = [
    "monté", "resté", "sorti", "revenu", "devenu", "venu", "allé", "né",
    "descendu", "entré", "rentré", "tombé", "retourné", "arrivé", "mort",
    "parti"
]
question_number = 0
option_name = ""

def shuffle():
	global stack_c
	global stack_a_stem
	global stack_a_verb
	global choose_list
	global option_name
	if choose_list == "1":
		stack_a_verb = future_verb
		stack_a_stem = future_stem
		option_name = "future stem "
	elif choose_list == "2":
		stack_a_verb = common_past_verb
		stack_a_stem = common_past_stem
		option_name = "past participle "
	elif choose_list == "3":
		stack_a_verb = etre_past_verb
		stack_a_stem = etre_past_pp
		option_name = "past participle "
	stack_c = list(zip(stack_a_stem, stack_a_verb))
	random.shuffle(stack_c)
	stack_a_stem, stack_a_verb = zip(*stack_c)
	stack_a_stem = list(stack_a_stem)
	stack_a_verb = list(stack_a_verb)


choose_list = input("Which list would you like to practice? \n" +
                    "-1- Future Tense \n" + "-2- Common Past Tense \n" +
                    "-3- Past with Etre \n")


shuffle()


while len(stack_a_verb) > 0:
    for verb in stack_a_verb:
        answer = input("What is the " + option_name + "of " + verb + "? \n")
        if answer.lower() == stack_a_stem[question_number]:
            print("correct!")
            stack_b_verb.append(verb)
            stack_b_stem.append(stack_a_stem[question_number])
            stack_a_verb.remove(verb)
            stack_a_stem.remove(stack_a_stem[question_number])
        elif answer == "exit":
            exit()
        else:
            print("wrong!")
        question_number += 1
    question_number = 0

shuffle()

while len(stack_b_verb) > 0:
    for verb in stack_b_verb:
        answer = input("What is the future tense stem of " + verb + "? \n")
        if answer == stack_b_stem[question_number]:
            print("correct!")
            stack_b_verb.remove(verb)
            stack_b_stem.remove(stack_b_stem[question_number])
        elif answer == "exit":
            exit()
        else:
            print("wrong!")
        question_number += 1
    question_number = 0
