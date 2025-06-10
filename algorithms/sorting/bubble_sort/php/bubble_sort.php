<?php

$DATA = [123, 456, 789, 234, 567, 890, 345, 678, 901, 432, 765, 198, 543, 876, 321, 654, 987, 234, 567, 890, 12, 45, 78, 23, 56, 89, 34, 67, 90, 43, 76, 19, 54, 87, 32, 65, 23, 56, 89, 12, 99, 0, 99];

function bubbleSort(array $data): array
{
  $length = count($data);

  for ($i = 0; $i < $length; $i++) {
    for ($j = 0; $j < $length - $i - 1; $j++) {
      if ($data[$j] > $data[$j + 1]) {
        [$data[$j], $data[$j + 1]] = [$data[$j + 1], $data[$j]];
      }
    }
  }

  return $data;
}

$sortedData = bubbleSort($DATA);

echo implode(', ', $sortedData);