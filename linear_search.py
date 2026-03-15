def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i  # Mengembalikan indeks jika ditemukan
    return -1  # Mengembalikan -1 jika tidak ditemukan

# Contoh penggunaan
data = [3, 8, 2, 5, 9, 1]
target = 5

result = linear_search(data, target)
if result != -1:
    print("Target ditemukan di indeks", result)
else:
    print("Target tidak ditemukan")