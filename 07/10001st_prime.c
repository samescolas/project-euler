#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int			is_prime(long long n);
long long	get_prime(int nth);

int		main(int ac, char **av) 
{
	int		bound;

	if (ac == 2)
		printf("%lld\n", get_prime(atoi(av[1])));
	return (0);
}

long long	get_prime(int nth)
{
	long long	prime = 2;
	int			count = 0;

	while (count < nth)
	{
		if (is_prime(prime))
			++count;
		if (count == nth)
			return (prime);
		++prime;
	}
	return (0);
}

int		is_prime(long long n)
{
	long long search = 1;
	long long ubound = (long long)sqrtl(n) + 1;

	while (++search < ubound)
		if (n % search == 0)
			return (0);
	return (1);
}
