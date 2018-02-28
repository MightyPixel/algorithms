import math

def is_prime(n):
    n_root = math.sqrt(n)
    for x in range(2, round(n_root) + 1):
        if n % x == 0:
            return False

    return True

if __name__ == '__main__':
    p = int(input().strip())
    for a0 in range(p):
        n = int(input().strip())
        if n > 1 and is_prime(n):
            print('Prime')
        else:
            print('Not prime')
