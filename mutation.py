def mutate_string(string, position, character):
    list_of_string = list(s)
    list_of_string[int(i)] = c
    return ''.join(list_of_string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
