def decorate_function(function):
    """Cette fonction va générer le décorateur."""
 
    def wrapper():
        """Le "vrai" décorateur."""
        print("Do something at the start")
        result = function()
        print("Do something at the end")
        return result
 
    return wrapper
 
 
@decorate_function  # c'est ici que ça se passe !
def travelling_through_the_stars():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")
 
 
# la fonction est directement décorée, et s'utilise comme telle, comme si rien
# comme si rien n'avait changé ! ;)
travelling_through_the_stars()