
"""
Chapitre 4 - Fonctions
Activite 1 : Ecrire des fonctions simples
"""

# --- Fonction sans parametre ni sortie ---

def affiche_table_de_7():
    """Affiche la table de multiplication par 7."""
    for i in range(1, 11):
        print(i, "* 7 =", i * 7)

def affiche_bonjour():
    """Demande le prenom et affiche un bonjour personnalise."""
    prenom = input("Veuillez entrer votre prenom : ")
    print("Bonjour", prenom)


# --- Fonction avec parametre et sans sortie ---

def affiche_une_table(n):
    """Affiche la table de multiplication par n."""
    for i in range(1, 11):
        print(i, "*", n, "=", i * n)

def affiche_salutation(formule):
    """Affiche une salutation personnalisee selon la formule donnee."""
    prenom = input("Veuillez entrer votre prenom : ")
    print(formule, prenom)


# --- Fonction sans parametre et avec sortie ---

def demande_prenom_nom():
    """Demande prenom et nom, renvoie l'identite complete (nom en majuscule)."""
    prenom = input("Veuillez entrer votre prenom : ")
    nom = input("Veuillez entrer votre nom : ")
    return nom.upper() + " " + prenom


# --- Tests1 ---
#affiche_table_de_7()
#affiche_bonjour()
#affiche_une_table(5)
#affiche_salutation("Coucou !")
#print(demande_prenom_nom())

"""
Activite 2 : Construire des fonctions avec différents types d'entrée et de sortie
"""
from math import pi


# 1. Trinômes

def trinome_1(x):
    """Renvoie la valeur du trinôme 3x² - 7x + 4."""
    return 3*x**2 - 7*x + 4

def trinome_2(a, b, c, x):
    """Renvoie la valeur du trinôme ax² + bx + c."""
    return a*x**2 + b*x + c


# 2. Devises

def conversion_euros_vers_dollars(montant):
    """Convertit un montant en euros vers les dollars (1€ = 1.15$)."""
    return montant * 1.15

def conversion_euros(montant, devise):
    """Convertit un montant en euros vers la devise choisie."""
    if devise == "dollars":
        return montant * 1.15
    elif devise == "livre":
        return montant * 0.81
    elif devise == "yens":
        return montant * 130
    elif devise == "fcfa":
        return montant * 655


# 3. Volumes

def volume_cube(a):
    """Renvoie le volume d'un cube de côté a."""
    return a**3

def volume_boule(r):
    """Renvoie le volume d'une boule de rayon r."""
    return (4/3) * pi * r**3

def volume_cylindre(r, h):
    """Renvoie le volume d'un cylindre de rayon r et hauteur h."""
    return pi * r**2 * h

def volume_boite(L, l, h):
    """Renvoie le volume d'une boîte de dimensions L, l, h."""
    return L * l * h


# 4. Périmètres et aires

def perimetre_aire_rectangle(a, b):
    """Renvoie le périmètre et l'aire d'un rectangle de dimensions a et b."""
    return 2 * (a + b), a * b

def perimetre_aire_disque(r):
    """Renvoie le périmètre et l'aire d'un disque de rayon r."""
    return 2 * pi * r, pi * r**2

# Trouver à partir de quel rayon l'aire dépasse le périmètre
for rayon in range(0, 30):
    P, A = perimetre_aire_disque(rayon / 10)
    if A > P:
        print("À partir du rayon", rayon / 10, "l'aire est plus grande que le périmètre.")
        break
    
# --- Tests2 ---
print(trinome_1(7))           # doit afficher 102
print(trinome_2(2, -1, 0, 6)) # doit afficher 66
print(conversion_euros_vers_dollars(100))  # doit afficher 115.0
print(conversion_euros(100, "livre"))      # doit afficher 81.0
print(volume_cube(3))         # doit afficher 27
print(volume_boule(3))        # doit afficher ~113.1
print(perimetre_aire_rectangle(5, 10))     # doit afficher (30, 50)
print(perimetre_aire_disque(5))            # doit afficher (~31.4, ~78.5)