frozen_set = frozenset([1, 2, 3, 4, 5])
outro_frozen_set = frozenset([1, 3, 5])

print(type(frozen_set))
print(frozen_set)
print(frozen_set ^ outro_frozen_set)
