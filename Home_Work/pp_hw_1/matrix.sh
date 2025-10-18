#!/bin/bash

read -p "Enter the number of matrix rows: " rows_matrix
read -p "Enter the number of matrix columns: " cols_matrix

count=1
declare -A matrix

for ((i=0; i<rows_matrix; i++)); do
  for ((j=0; j<cols_matrix; j++)); do
    matrix[$i,$j]=$count
    ((count++))
  done
done

echo "Matrix $rows_matrix x $cols_matrix:"
for ((i=0; i<rows_matrix; i++)); do
  for ((j=0; j<cols_matrix; j++)); do
    printf "%4d " "${matrix[$i,$j]}"
  done
  echo
done
