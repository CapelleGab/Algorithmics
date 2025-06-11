/*
-----------------------------------------------------------------------------
Nom du fichier : bubble_sort.java
Auteur        : CAPELLE Gabin (https://github.com/CapelleGab)
Créé le      : 10-06-2025 20:39
Dernière MAJ : 10-06-2025 20:39

Description   : Implémentation de l'algorithme de tri à bulles (Bubble Sort) en Java.
-----------------------------------------------------------------------------
*/

import java.util.Arrays;

class BubbleSort {
  public static void main(String[] args) {
    int[] data = {123, 456, 789, 234, 567, 890, 345, 678, 901, 432, 765, 198, 543, 876, 321, 654, 987, 234, 567, 890, 12, 45, 78, 23, 56, 89, 34, 67, 90, 43, 76, 19, 54, 87, 32, 65, 23, 56, 89, 12, 99, 0, 99};

    int[]sortedList = bubbleSort(data);

    Arrays.stream(sortedList).forEach(System.out::println);
  }

  public static int[] bubbleSort(int[] data) {
    int length = data.length;

    for (int i = 0; i < length; i++) {
      for (int j = 0; j < length - i - 1; j++) {
        if (data[j] > data[j + 1]) {
          int temp = data[j];
          data[j] = data[j + 1];
          data[j + 1] = temp;
        }
      }
    }
    return data;
  }
}