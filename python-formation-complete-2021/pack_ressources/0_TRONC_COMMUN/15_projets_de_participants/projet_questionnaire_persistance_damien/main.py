import time

try:

    def reponse(question):
        global score

        print(f"\n{question[0]}")
        for c in range(len(question[1])):
            print(f"{c + 1} - {question[1][c]}")
        answer = input("-> ")
        if answer == ":exit":
            return
        try:
            condition = int(answer) == question[1].index(question[2]) + 1
            if int(answer) > len(question[1]) or int(answer) < 1:
                print(f"ERREUR: Veuillez entrer un nombre entre 1 et {len(question[1])}")
                return reponse(question)
        except ValueError:
            condition = None
        if answer.lower() == question[2].lower() or condition:
            score += 1
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")


    def ajouter_question():
        global questionnaire
        question = [input("\nÉcrivez votre question\n-> "), []]
        if question[0] == ":exit":
            return
        print("Entrez les choix de votre question (Au moins 2 choix). Appuyer sur ENTRER pour terminer")
        while True:
            choix = input("-> ")
            if choix == ":exit":
                return
            if not choix:
                if len(question[1]) > 1:
                    question[1] = tuple(question[1])
                    break
                print("ERREUR: Entrez au moins 2 choix")
            elif choix[0] == "c" and choix[1] == "e" and choix[2] == "n" and choix[3] == "d":
                print("ERREUR: Vous ne pouvez pas entré ce mot")
            else:
                question[1].append(choix)
        print("Entrez la réponse de votre question")
        while True:
            reponse = input("-> ")
            if reponse == ":exit":
                return
            for q in question[1]:
                if reponse == q:
                    question.append(reponse)
                    questionnaire.append(tuple(question))
                    print("Questionnaire ajouté !\n")
                    return
            print("ERREUR: La reponse doit être dans les choix de votre question")


    def lancer_questionnaire():
        global nb_question, score

        score = 0
        if not questionnaire:
            print(
                "ERREUR: Questionnaire vide, utilisez la commande ':ajouter' dans le terminal pour ajouter un nouvelle question.\n")
            return
        for nb_question, q in enumerate(questionnaire):
            reponse(q)
        print(f"TEST TERMINÉ\nVous avez un score de {score}/{nb_question + 1} !\n")


    def supprimer_question():
        if not questionnaire:
            print(
                "ERREUR: Questionnaire vide, utilisez la commande ':ajouter' dans le terminal pour ajouter une nouvelle question.\n")
            return
        for i, question in enumerate(questionnaire):
            print(f"-- Questionnaire n°{i + 1} --\n   Question: {question[0]}\n     Choix: ", end="")
            for x in question[1]:
                char = ","
                if x == question[1][-1]:
                    char = ""
                print(f"{x}{char} ", end="")
            print()
            print(f"     Réponse: {question[2]}\n")
        print("\nQuel Questionnaire voulez-vous supprimer (n°) ?")
        while True:
            choix = input("-> ")
            if choix == ":exit":
                return
            try:
                if int(choix) != 0:
                    del questionnaire[int(choix) - 1]
                    print(f"Questionnaire n°{int(choix)} supprimé!\n")
                    return
                print("ERREUR: Ce questionnaire n'existe pas!")
            except ValueError:
                print("ERREUR: Veuillez entrer un numéro de questionnaire")
            except IndexError:
                print("ERREUR: Ce questionnaire n'existe pas!")


    def sauvegarder_question():
        fname = input("Nom du fichier\n-> ")
        if fname == ':exit':
            return
        print()
        try:
            with open(f"{fname}.txt", "r"):
                pass
        except:
            print(f"Fichier {fname}.txt créé")
        with open(f"{fname}.txt", "w") as fichier:
            for question in questionnaire:
                for element in range(len(question)):
                    if element == 0:
                        fichier.write(f"q{question[element]}\n")
                    if element == 1:
                        fichier.write("c\n")
                        for e in question[element]:
                            fichier.write(f"{e}\n")
                        fichier.write("cend\n")
                    if element == 2:
                        fichier.write(f"r{question[element]}\nend\n")

        time.sleep(0.5)
        print(f"Questionnaires sauvegardés dans {fname}.txt")


    def charger_question():
        global questionnaire
        fname = input("Nom du fichier (sans .txt)\n-> ")
        if fname == ":exit" or not fname:
            return
        try:
            with open(f"{fname}.txt", "r") as fichier:
                ligne = 'a'
                questionnaire = []
                while ligne:
                    choix_liste, question, reponse = [], '', ''
                    ligne = fichier.readline().rstrip()
                    c_bool = False
                    end = False
                    if not ligne and not c_bool:
                        return
                    while not end:
                        # Question lu
                        if ligne[0] == 'q' and not c_bool:
                            question = ""
                            print(f"Question récupérée: {ligne[1:]}")
                            for i in range(len(ligne)):
                                if not i == 0:
                                    question += ligne[i]
                        # Fin de la lecture des choix
                        if ligne.rstrip() == 'cend':
                            c_bool = False
                        # Lecture en cours des choix
                        if c_bool:
                            print(f"Ajout de choix: {ligne}")
                            choix_liste.append(ligne)
                        # Choix lus
                        if ligne.rstrip() == 'c':
                            c_bool = True
                        # Réponse lu
                        if ligne[0] == 'r':
                            reponse = ''
                            print(f"Réponse récupérée: {ligne[1:]}")
                            for i in range(len(ligne)):
                                if not i == 0:
                                    reponse += ligne[i]
                        if ligne.rstrip() == "end":
                            end = True
                        else:
                            ligne = fichier.readline().rstrip()
                    questionnaire.append((question, tuple(choix_liste), reponse))
        except FileNotFoundError:
            print("ERREUR: Fichier introuvable")
            return charger_question()
        return


    """ 
    Sous la forme (QUESTION, (CHOIX, CHOIX, CHOIX, ...), REPONSE)
    """
    questionnaire = []


    # Terminal
    while True:
        print("\nCommandes:\n  :lancer\n  :ajouter\n  :exit\n  :supprimer\n  :sauvegarder\n  :charger\n")
        cmd = input("-> ")
        if cmd == ":lancer":
            lancer_questionnaire()
        elif cmd == ":ajouter":
            ajouter_question()
        elif cmd == ":exit":
            exit()
        elif cmd == ":supprimer":
            supprimer_question()
        elif cmd == ":sauvegarder":
            sauvegarder_question()
        elif cmd == ":charger":
            charger_question()
        else:
            print("ERREUR: Commande inconnue")
            print()

except KeyboardInterrupt:
    exit()