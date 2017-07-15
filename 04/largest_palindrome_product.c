#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int		is_palindrome(long n);
long	largest_palindrome(long  upper_bound);
long	find_palindrome(int product_digits);

int		main(int ac, char **av)
{
	if (ac == 2)
	{
		find_palindrome(atoi(av[1]));
	}
	return (0);
}

long	find_palindrome(int product_digits)
{
	long	lower_bound;
	long	upper_bound;
	long	search_val;
	long	f1;
	int		palindrome_found;

	lower_bound = pow(10, product_digits - 1);
	upper_bound = pow(10, product_digits) - 1;

	search_val = largest_palindrome(pow(upper_bound, 2) + 1);
	palindrome_found = 0;
	while (!palindrome_found)
	{
		if (is_palindrome(search_val))
		{
			for (long factor=upper_bound; factor >= lower_bound && search_val / factor > lower_bound; factor--)
			{
				if (search_val % factor == 0 && search_val / factor >= lower_bound && search_val / factor <= upper_bound)
				{
					palindrome_found = 1;
					f1 = factor;
					break ;
				}

			}
		}
		if (!palindrome_found)
			search_val = largest_palindrome(search_val);
	}
	printf("%lu is the product of %lu and %lu!\n", search_val, f1, search_val / f1);
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
