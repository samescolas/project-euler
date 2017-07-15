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



'''
while True:
    print 'testing {} and {}...'.format(largest_number, (largest_number - offset))
    if is_palindrome(largest_number * (largest_number - offset)):
        print 'palindrome {} is a product of {} and {}'.format(
            largest_number * (largest_number - offset),
            largest_number - offset,
            largest_number)
        break
    elif largest_number * (largest_number - offset - 1) < (largest_number - 1) * largest_number:
        offset = 0
        largest_number -= 1
    else:
        offset += 1
'''
