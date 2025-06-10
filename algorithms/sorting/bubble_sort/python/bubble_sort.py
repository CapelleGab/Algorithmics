"""
-----------------------------------------------------------------------------
Nom du fichier : bubble_sort.py
Auteur        : CAPELLE Gabin (https://github.com/CapelleGab)
Créé le      : 10-06-2025 20:39
Dernière MAJ : 10-06-2025 20:39

Description   : Implémentation de l'algorithme de tri à bulles (Bubble Sort).
-----------------------------------------------------------------------------
"""

# Jeu de données varié pour tester l'algorithme de tri à bulles
data = [123, 456, 789, 234, 567, 890, 345, 
        678, 901, 432, 765, 198, 543, 876, 
        321, 654, 987, 234, 567, 890, 12, 
        45, 78, 23, 56, 89, 34, 67, 
        90, 43, 76, 19, 54, 87, 32, 65, 
        23, 56, 89, 12, 99, 0, 99]


def bubble_sort(data: list) -> list:
  length = len(data)  
  for i in range(length):
    for j in range(length - i - 1):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
  return data


print(bubble_sort(data))