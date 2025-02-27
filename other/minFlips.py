"""A password string, pwd, consists of binary characters (0s and 1s).
A cyber security expert is trying to determine the minimum number
of changes required to make the password secure.

To do so, it must be divided into substrings of non-overlapping,
even length substrings. Each substring can only contain 1s or 0s,
not a mix. This helps to ensure that the password is'strong and less 
vulnerable to hacking attacks.

Find the minimum number of characters that must be
flipped in the password string, i.e. changed from 0 to 1 or 1
to 0 to allow the string to be divided as described.

Note: A substring is a contiguous sequence of characters in
a string.

Ex. Given pwd = 1110011000

1110011000 -> 1111111100 -> 11111111
                         -> 00

The 2 substrings have lengths 8 and 2 respectively.
Since both are even, the division is valid and the answer is 3.

getMinFlip:

@param pwd (str): binary string

@return int: min number of flips to make the division

Constrains:

2 <= pwd <= 10^5 
Length of pwd is even
pwd only contains 0s and 1s
"""

def getMinFlip(pwd: str) -> int:
    flip = 0
    pwd_length = len(pwd)
    substr = ""

    pwd = list(pwd)

    for i in range(0, pwd_length-1):
        
        substr += pwd[i]

        if pwd[i] == pwd[i+1]:
            continue

        if len(substr) % 2 == 0:
            substr = ""
        else:
            flip += 1
            pwd[i+1] = pwd[i]


    if pwd[pwd_length -1] not in substr:
        flip += 1

    return flip

if __name__ == "__main__":
    pwd = "000001000001110100"

    print(getMinFlip(pwd))