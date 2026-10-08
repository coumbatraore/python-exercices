ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]


ca_par_produit = {}

for vente in ventes:
    produit = vente["produit"]
    ca = vente["prix"] * vente["quantite"]
    ca_par_produit[produit] = ca

print(ca_par_produit)

total = sum(ca_par_produit.values())

print("Total :", total, "euros")


meilleur_produit = max(ca_par_produit, key=ca_par_produit.get)

print("Meilleur produit :", meilleur_produit)





























