def split_and_join(line):
    # write your code here
    a = line.split()
    result_string = '-'.join(a)
    return result_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
