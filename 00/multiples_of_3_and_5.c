#include <stdlib.h>
#include <stdio.h>

int		mults_3_5(int lim)
{
	int		i;
	int		ret;

	ret = 0;
	i = -1;
	while (++i < lim)
		if (i % 3 == 0 || i % 5 == 0)
			ret += i;
	return (ret);
}

int		main(int ac, char **av)
{
	if (ac == 2)
		printf("%d\n", mults_3_5(atoi(av[1])));
	return (0);
}
