from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes = []
notes_invalides = 0

for texte in notes_brutes:
    note = convertir_note(texte)

    if note is None:
        notes_invalides += 1
    else:
        notes.append(note)

resultat_moyenne = moyenne(notes)
resultat_mention = mention(resultat_moyenne)

print("Notes ignorées :", notes_invalides)
print("Moyenne :", round(resultat_moyenne, 2))
print("Mention :", resultat_mention)












