def isCryptSolution(crypt, solution):
    index = {}
    for letter, number in solution:
        index[letter] = int(number)

    decoded_crypt = []

    for word in crypt:
        number = 0
        for letter in word:
            number += index[letter]
            number *= 10

        number /= 10

        if len(word)>1 and number < 10**(len(word) - 1):
            return False

        decoded_crypt.append(number)

    a, b, c = decoded_crypt

    return a + b == c


crypt = ["SEND",
         "MORE",
         "MONEY"]

solution = [["O","0"],
            ["M","1"],
            ["Y","2"],
            ["E","5"],
            ["N","6"],
            ["D","7"],
            ["R","8"],
            ["S","9"]]

crypt = ["A",
         "A",
         "A"]

solution = [["A","0"]]

print(isCryptSolution(crypt, solution))
