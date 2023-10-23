#!/usr/bin/env python
# coding: utf-8

# In[6]:


#source : https://www.w3schools.com/python/python_functions.asp
# Parcourir chaque mot avec des conditions if-elif-else aurait généré un code très longue, c'est pourquoi j'ai choisi d'intégrer des fonctions définies

# 1. Demande à l’utilisateur le nom d’un fichier à analyser ;
# 2. Ouvre le fichier en mode lecture, lit chaque ligne du fichier et la découpe en mots ;
# 3. Pour chaque mot de longueur supérieure ou égale à 6, effectue une analyse morpho-syntaxique minimale 
# afin d’identifier les noms, les adjectifs et les adverbes en fonction des suffixes de longueur supérieure ou égale à 3.

import re

# Analyse pos pour identifier nom, adjectif ou adverbe
# Longueur des suffixes supérieure ou égale à 3 donné dans les définitions
def analyse_pos(word):
    result = ""
    # Initialisation de la variable result pour les retours.
    # Avec les conditions if on parcourt toutes les possibilités pour trouver des cas ambiguës.
    # result += ' NOM' (p. ex.) ajoute donc le pos nom si ambiguiëté. 
    # Adjectifs
    if re.search(r'((\w*ain\b)|(\w*i?aire\b)|(\w*ée?\b)|(\w*i?el\b)|(\w*u?el\b)|(\w*i?al\b)|(\w*i?er\b)|(\w*esque\b)|(\w*eur\b)|(\w*i?eux\b)|(\w*i?euses?\b)|(\w*u?eux\b)|(\w*if\b)|(\w*ive\b)|(\w*in\b)|(\w*ique\b)|(\w*ue?\b)|(\w*issime\b)|(\w*able\b)|(\w*ible\b)|(\w*uble\b)|(\w*ième\b)|(\w*u?ple\b))', word):
        result = 'ADJ'
    # Noms
    if re.search(r'((\w*ades?\b)|(\w*ages?\b)|(\w*ailles?\b)|(\w*a?o?isons?\b)|(\w*a?i?tions?\b)|(\w*s?sions?\b)|(\w*xions?\b)|(\w*isations?\b)|(\w*e?ments?\b)|(\w*eries?\b)|(\w*ures?\b)|(\w*a?tures?\b)|(\w*is\b)|(\w*a?e?nces?\b)|(\w*escences?\b)|(\w*ats?\b)|(\w*i?e?tés?\b)|(\w*(er)?ies?\b)|(\w*esses?\b)|(\w*ises?\b)|(\w*eurs?\b)|(\w*ismes?\b)|(\w*istes?\b)|(\w*(is)?seurs?\b)|(\w*(is)?ateurs?\b)|(\w*euses?\b)|(\w*(is)?seuses?\b)|(\w*atrices?\b)|(\w*iers?\b)|(\w*ières?\b)|(\w*aires?\b)|(\w*iens?\b)|(\w*iennes?\b)|(\w*istes?\b)|(\w*ers?\b)|(\w*erons?\b)|(\w*eronnes?\b)|(\w*os?\b)|(\w*ots?\b)|(\w*eurs?\b)|(\w*euses?\b)|(\w*a?trices?\b)|(\w*oire?s?\b)|(\w*t?iers?\b)|(\w*t?ières?\b)|(\w*eries?\b)|(\w*anderies?\b)|(\w*oirs?\b)|(\w*és?\b)|(\w*r?aies?\b)|(\w*aine?s?\b)|(\w*ailles?\b)|(\w*ées?\b)|(\w*ards?\b)|(\w*asses?\b)|(\w*assiers?\b)|(\w*âtres?\b)|(\w*auts?\b)|(\w*c?eaus?\b)|(\w*e(r|t)eaus?\b)|(\w*e?i?lles?\b)|(\w*ets?\b)|(\w*elets?\b)|(\w*ins?\b)|(\w*otins?\b)|(\w*ines?\b)|(\w*ots?\b)|(\w*ott?es?\b)|(\w*(er)?ons?\b)|(\w*illons?\b)|(\w*(er)?oles?\b)|(\w*i?c?ules?\b)|(\w*iches?\b)|(\w*ai?n?s?\b)|(\w*ois\b)|(\w*ie?ns?\b)|(\w*istes?\b)|(\w*aires?\b)|(\w*a?e?ux\b))', word):
        result += ' NOM'
    # Adverbes
    if re.search(r'\w*ment\b', word):
        result += ' ADV'
    # Pour les cas non-analysés (et pour éviter le retour "NONE")
    return result

    
# Analyse pos pour identifer les classes fermées
def analyse_pos1(word):
    result = ""
    # Déterminant
    if re.search(r'((\bla?e?s?\b)|(\bune?\b)|(\bdes\b))', word):
        result = 'DET'
    # Conjonctions
    if re.search(r'((et\b)|(mais\b)|(car\b)|(donc\b)|(ou\b)|(or\b)|(ni\b)|((\w)?que?\b)|(quand\b)|(comme\b)|(quoique\b)|(si\b)|(lorsque\b))', word):
        result += ' CONJ'
    # Prépositions
    if re.search(r'((à)|(\baux?)|(après)|(avant)|(dans)|(\bde?\b)|(depuis)|(dès)|(\ben\b)|(jusque?)|(pendant)|(chez)|(\bcontre)|(derrière)|(hors)|(loin)|(par\b)|(\bprès)|(sous)|(sur)|(vers)|(avec)|(\bcontre\b)|(entre)|(sauf)|(grâce)|(malgré)|(parmi)|(pour)|(sans)|(selon))', word):
        result += ' PREP'
    # Pronoms
    if re.search(r'((je)|(\btu\b)|(ils?)|(elles?)|(\bon\b)|(nous)|(vous)|(\bme?s?)|(\bte?s?)|(\bse?s?\b)|(nou?s)|(vou?s)|(ses?)|(moi)|(\btoi\b)|(lui)|(\bc?eux\b)|(\bles?)|(\bla?\b)|(leurs?)|(\by\b)|(\ben\b)|(\bque?)|(qui)|(quoi)|(où)|(dont)|((d|a)uquel)|(lequel)|(\btou(t|s)\b)|(toutes)|(plusieurs)|(aucune?)|(chacune)|(quelque chose)|(quelqu\'un)|(celui(-ci)?)|(celles?)|(ça)|(cela)|(miens?)|(tiens?)|(siens?)|(nôtres?)|(vôtres?)|(miennes?)|(tiennes?)|(siennes?))', word):
        result += ' PRON'
    # Pour les cas non-analysés (et pour éviter le retour "NONE")
    return result

# D'abord on demande à l'utilisateur le nom d'un fichier à analyser et on l'ouvre ensuite
file = input("Entrez le nom d'un fichier de texte à analyser : ")

with open(file, 'r', encoding='utf8') as file:
    for line in file:
        words = re.findall(r"[\w]+|[.,!?;\']", line.lower().rstrip())
            # Pour le découpage de la phrase, une regex est employée afin de retrouver tous les lettres alphanumériques repétées
            # et les signes de ponctuations. line.lower() est utilisé pour que la case n'importe pas et pour que les regex captent tout.
            # Pour chaque mot de longueur supérieure ou égale à 6, on effectue la (première) analyse pos.
            # Si non, les classes fermées sont parcourues (la deuxième analyse pos).
        for word in words:
            if len(word) >= 6:
                pos = analyse_pos(word)
                print(f'{word} {pos}')
            elif len(word) <= 6:
                pos = analyse_pos1(word)
                print(f'{word}  {pos}')  

