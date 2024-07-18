def are_anagrames(s1, s2):

    return sorted(s1) == sorted(s2)

s1 = "listen"
s2 = "silent"

print(are_anagrames(s1, s2))