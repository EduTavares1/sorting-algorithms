import time

def insertion_sort(arr):
    """Insertion Sort Algorithm."""
    for i in range(1, len(arr)):
        pivo = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivo:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivo
    return arr


# Caminho relativo ao arquivo de entrada
input_path = 'input/num.100000.1.in'  # troca o input

# Ler os números do arquivo de entrada
with open(input_path, 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# Ordenar os números
start_time = time.time() 
sorted_numbers = insertion_sort(numbers)
end_time = time.time() 

execution_time = end_time - start_time

# Imprimir os números ordenados no terminal
print("Números ordenados:")
for number in sorted_numbers:
    print(number)

print(f"\n\nTempo de execução insertion sort: {execution_time:.6f} segundos")    
