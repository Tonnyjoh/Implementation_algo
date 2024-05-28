def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = round(len(lst) / 2)  # len(lst)//2

    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Fusionner les listes
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Ajouter les éléments restants
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


liste_a_trier = [9, 5, 1, 4, 3, 7, 6, 8, 2, 45, 4, 5, 45, 4, 48, 4787, 87, 4, 4, 5, 78, 64, 97, 45, 97, 546, 123, 89, 1,
                 48, 64, 79, 45, 46, 9, 789, 64, 64, 54, 21, 84, 12, 7, 54, 7, 45, 7, 54, 12, 0, 15, 0, 1, -58, 15, 45,
                 54, 54, 87, 5, 8, 45, 7, 47, 87, 45, 45, 7, 8, 5, 4, 6, 9, 8, 5, 4, 1, 2, 6, 5, 7, 5, 7, 48, 45, 48, 8,
                 7, 5, 87, 16, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 49, 321, 7, 26,
                 15, 26, 36, 48, 89, 78, 59, 98, 36, 26, 36, 54, 15, 98, 78, 258, 258, 14, 798, 478]
triée = merge_sort(liste_a_trier)
print(triée)
