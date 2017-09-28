/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   permutations.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sescolas <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/02/05 14:31:00 by sescolas          #+#    #+#             */
/*   Updated: 2017/09/28 11:43:14 by sescolas         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int		*get_next_permutation(int *arr, int size)
{
	int		i;
	int		j;
	int		tmp;

	i = size - 1;
	while (i > 0 && arr[i - 1] >= arr[i])
		i--;
	if (i <= 0)
		return ((void *)0);
	j = size - 1;
	while (arr[j] <= arr[i - 1])
		j--;
	tmp = arr[i - 1];
	arr[i - 1] = arr[j];
	arr[j] = tmp;
	j = size - 1;
	while (i < j)
	{
		tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
		i++;
		j--;
	}
	return (arr);
}

int		main(void)
{
	int		arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int		*result;
	int		iterations = 0;
	int		total_iterations = 1000000;

	while (++iterations < total_iterations)
		result = get_next_permutation((int *)arr, 10);
	for (int i=0; i<10; ++i)
		printf("%d", result[i]);
	printf("\n");
	return (0);
}
