from functions import filter_sup_30 , associer , to_string , sort_prix , to_tuple , produit_max_price , produit_min_price

from data import produits , prix

produits_prix = associer(produits,prix)

# q1
print(associer(produits,prix))

# q2
print(filter_sup_30(produits_prix))

# q3 - q8
print(to_string(produits_prix))

# q4
print(sort_prix(produits_prix))

# q5 - q6
print(to_tuple(produits_prix))

# q7
print(produit_max_price(produits_prix))
print(produit_min_price(produits_prix))