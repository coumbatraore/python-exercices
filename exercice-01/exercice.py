# 1. Variables
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# 2. Calculs
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

# 3. Affichage 
print(f"{quantite} x {produit} : {total_ht:.2f} € HT, soit {total_ttc:.2f} € TTC")

# 4. Le prix arrive sous forme de texte
prix_texte = "19.90"
prix_ht = float(prix_texte) 

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"Après conversion : {total_ht:.2f} € HT, soit {total_ttc:.2f} € TTC")