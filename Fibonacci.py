#importons le module argparse qui va nous permettre d'interpréter les arguments passés sur la ligne de commande.

from argparse import ArgumentParser

def fibonacci(n) :
    
    if n <= 1 :
        return n
    else :
        f_0 , f_1 = 0 , 1
        for i in range(2, n+1) :
            f_0 , f_1 = f_1 , f_0 + f_1
            
        return f_1

parser = ArgumentParser()
parser.add_argument(dest="entier", type=int,
                    help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier


# de cette façon on peut utiliser la fonction fibonacci(n) en lui passant la valeur 10 en argument en utilisant le script suivant dans un terminal
# python fibonacci.py 10