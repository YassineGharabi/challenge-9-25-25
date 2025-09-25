# Associer chaque prix avec son prix
def associer(produits,prix):
    return list(zip(produits,prix))

# filtre les produit avec prix sup o egal 30
def filter_sup_30(produits_prix):

    def fun_logique_filter(produit):
        if produit[1] >= 30:
            return True
        else:
            return False
        
    return list(filter(fun_logique_filter,produits_prix))

# to string like "Produit coute 00 DH"
def to_string(produits_prix):
    def fun_logique(produit):
        if produit[1] > 1000:
            return f"{produit[0]} coute {produit[1]} DH (LUXE)"
        else:
            return f"{produit[0]} coute {produit[1]} DH"

    return list(map(fun_logique,produits_prix))

# trier la liste par order croissante des prix
def sort_prix(produits_prix):
    # this function to acces price of each product
    def fun_logique(item):
        return item[1]

    produits_prix.sort(key=fun_logique) # the key in sort like map pass for each element
    return produits_prix


# from list to tuple
def to_tuple(produits_prix):
    return tuple(produits_prix)


# le produite le plus cher
def produit_max_price(produits_prix):

    produite_with_max_price = ( "produit" , 0 )

    for produit in produits_prix:
        if produit[1] >= produite_with_max_price[1]:
            produite_with_max_price = produit

    return produite_with_max_price

# le produite le mois cher
def produit_min_price(produits_prix):

    produite_with_min_price = produits_prix[0]

    for produit in produits_prix:
        if produit[1] <= produite_with_min_price[1]:
            produite_with_min_price = produit

    return produite_with_min_price