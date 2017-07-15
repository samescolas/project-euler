#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int		is_palindrome(char *num);

int		main(int ac, char **av)
{
	if (ac == 2)
	{
		if (is_palindrome(av[1]))
			printf("%s is a palindrome!\n", av[1]);
		else
			printf("%s is not a palindrome!\n", av[1]);
	}
	return (0);
}

int		is_palindrome(char *num)
{
	int		i;
	int		len;

	len = strlen(num);
	i = -1;
	while (num[++i] != '\0')
	{
		if (num[i] != num[len - i - 1])
			return (0);
	}
	return (1);
}
