#include <stdio.h>
#include <stdlib.h>

long	even_fib_sum(long max);

int		main(int ac, char **av)
{
	if (ac == 2)
	{
		printf("%lu\n", even_fib_sum(atoi(av[1])));
	}
	return (0);
}


long	even_fib_sum(long max)
{
	long		a;
	long		b;
	long		tmp;
	long		sum;

	sum = 0;
	a = 0;
	b = 1;
	while (a < max)
	{
		if (a % 2 == 0)
			sum += a;
		tmp = a + b;
		a = b;
		b = tmp;
	}
	return (sum);
}
