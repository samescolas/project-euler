#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int		is_prime(long long n);

int		main(int ac, char **av) 
{
	if (ac == 2)
	{
		if (is_prime(atoll(av[1])))
			printf("%lld is prime!\n", atoll(av[1]));
		else
			printf("%lld isn't prime!\n", atoll(av[1]));
	}
	return (0);
}

int		is_prime(long long n)
{
	long long search = 1;
	long long ubound = (long long)sqrtl(n) + 1;

	while (++search < ubound)
		if (n %  search == 0)
			return (0);
	return (1);
}
