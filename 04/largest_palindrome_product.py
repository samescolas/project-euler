import sys

def is_palindrome(n):
    num = str(n)
    for ix,ch in enumerate(num):
        if ch != num[len(num) - ix - 1]:
            return False
    return True

largest_number = int("9"*int(sys.argv[1]))

offset = 0

palindromes = [x for x in range(pow(largest_number,2),1,-1) if is_palindrome(x)]
for num in palindromes:
    for i in range(largest_number,1,-1):
        if num % i == 0 and len(str(int(num/i))) == int(sys.argv[1]):
            print '{} * {} = {}'.format(
                str(num/i),
                str(i),
                num)
            sys.exit(0)
