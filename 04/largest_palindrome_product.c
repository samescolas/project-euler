#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int		is_palindrome(long n);
long	largest_palindrome(long  upper_bound);

int		main(int ac, char **av)
{
	if (ac == 2)
	{
		if (is_palindrome(atoll(av[1])))
			printf("%s is a palindrome!\n", av[1]);
		else
			printf("%lu is the largest palindrome!\n", largest_palindrome(atoll(av[1])));
	}
	return (0);
}

long	find_palindrome(int product_digits)
{
	
}

int		is_palindrome(long n)
{
	int		i;
	int		len;
	char	num[24];

	sprintf(num, "%lu", n);
	len = strlen(num);
	i = -1;
	while (num[++i] != '\0')
	{
		if (num[i] != num[len - i - 1])
			return (0);
	}
	return (1);
}

long	largest_palindrome(long upper_bound)
{
	long search_val;

	search_val = upper_bound - 1;
	while (1)
	{
		if (is_palindrome(search_val))
			return (search_val);
		search_val -= 1;
	}
	return (-1);
}
