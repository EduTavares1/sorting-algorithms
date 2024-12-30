import time

def selection_sort(arr):
    """Selection Sort Algorithm based on provided pseudocode."""
    n = len(arr)
    for i in range(n - 1):  
        i_min = i  
        for j in range(i + 1, n): 
            if arr[j] < arr[i_min]:  
                i_min = j  
        if i != i_min:  
            temp = arr[i] 
            arr[i] = arr[i_min]  
            arr[i_min] = temp  
    return arr  


# Caminho relativo ao arquivo de entrada
input_path = 'input/num.100000.1.in'  # Ajuste o nome do arquivo conforme necessário

# Ler os números do arquivo de entrada
with open(input_path, 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# Ordenar os números usando Selection Sort
start_time = time.time()
sorted_numbers = selection_sort(numbers)
end_time = time.time()

execution_time = end_time - start_time

# Imprimir os números ordenados no terminal de forma organizada
print("Números ordenados :\n")
for number in sorted_numbers:
    print(number)


print(f"\n\nTempo de execução selection sort: {execution_time:.6f} segundos")        
