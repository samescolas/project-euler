#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int		main(int argc, char **argv)
{
	long long	ix;
	long long	sum;
	long long	input_val;
	
	if (argc == 2)
	{
		ix = -1;
		input_val = atoll(argv[1]) + 1;
		while (++ix < input_val)
			sum += (powl(ix, 2) * (ix - 1));
		printf("%lld\n", sum);
	}
	return (0);
}
