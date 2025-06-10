/*
-----------------------------------------------------------------------------
Nom du fichier : bubble_sort.ts
Auteur        : CAPELLE Gabin (https://github.com/CapelleGab)
Créé le      : 10-06-2025 20:39
Dernière MAJ : 10-06-2025 20:39

Description   : Implémentation de l'algorithme de tri à bulles (Bubble Sort) en TypeScript.
-----------------------------------------------------------------------------
*/

const DATA = [
  123, 456, 789, 234, 567, 890, 345, 678, 901, 432, 765, 198, 543, 876, 321,
  654, 987, 234, 567, 890, 12, 45, 78, 23, 56, 89, 34, 67, 90, 43, 76, 19, 54,
  87, 32, 65, 23, 56, 89, 12, 99, 0, 99,
];

const bubbleSort = (data: number[]): number[] => {
  const length = data.length;

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length - i - 1; j++) {
      if (data[j] > data[j + 1]) {
        [data[j], data[j + 1]] = [data[j + 1], data[j]];
      }
    }
  }

  return data;
};

console.log(bubbleSort(DATA));
