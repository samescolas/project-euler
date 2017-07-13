#include <stdlib.h>
#include <stdio.h>
#include <math.h>

long long	largest_prime_factor(long long x);

int		main(int ac, char **av)
{
	if (ac == 2)
		printf("%lu\n", largest_prime_factor((long long)atoll(av[1])));
	return (0);
}

long long	min_factor(long long x)
{
	long long	i;
	long long	range_max;

	i = 1;
	range_max = (long long)ceill(sqrtl((long double)x)) + 1;
	while (++i < range_max)
	{
		if (x % i == 0)
			return (i);
	}
	return (1);
}

int			is_prime(long long x)
{
	return (min_factor(x) == 1);
}

long long	largest_prime_factor(long long x)
{
	long long	guess;

	guess = x / min_factor(x);
	while (1)
	{
		if (is_prime(guess))
			return (guess);
		guess = guess / min_factor(guess);
	}
	return (x);
}
