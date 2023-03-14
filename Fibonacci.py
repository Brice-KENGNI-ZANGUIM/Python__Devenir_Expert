#importons le module argparse qui va nous permettre d'interpréter les arguments passés sur la ligne de commande.

# Module qui servira à récupérer un argument passé depuis le terminal
from argparse import ArgumentParser

# Définition de la fonction
def fibonacci(n) :
    
    if n <= 1 :
        return n
    else :
        f_0 , f_1 = 0 , 1
        for i in range(2, n+1) :
            f_0 , f_1 = f_1 , f_0 + f_1
            
        return f_1

# Permet de definir un objet Parser qui récupère la valeur donné depuis le terminal lors du lancement de la fonction Python
parser = ArgumentParser()
parser.add_argument(dest="entier", type=int, help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier

print(f"Fibonacci({n}) = {fibonacci(n)}")
# de cette façon on peut utiliser la fonction fibonacci(n) en lui passant la valeur 10 en argument en utilisant le script suivant dans un terminal
# python fibonacci.py 10