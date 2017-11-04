#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

long long factorial(int n)
{
  if (n == 0)
    return (1);
  else
    return (n * factorial(n - 1));
}

int   special(long n)
{
  static int  *factorials = (void *)0;
  int         sum = 0;
  char        num_str[40];

  if (factorials == (void *)0)
  {
    factorials = malloc(10 * sizeof(int));
    for (int i=0; i<10; i++)
      factorials[i] = factorial(i);
  }
  sprintf(num_str, "%ld", n);
  for (int i=0; num_str[i]; i++)
  {
    sum += factorials[num_str[i] - '0'];
  }
  return (sum == n);
}

int   main(void)
{
  int   results[100];
  int   ix;
  int   upper_bound;
  int   sum;

  bzero(results, 100 * sizeof(int));
  upper_bound = 7 * factorial(9);
  ix = 0;
  for (int i=3; i<upper_bound; i++)
  {
    if (special(i))
      results[ix++] = i;
  }
  printf("There are %d values satisfying this condition: ", ix);
  printf("%d", results[0]);
  sum = results[0];
  for (int i=1; results[i] > 0; i++)
  {
    printf(", %d", results[i]);
    sum += results[i];
  }
  printf("\nTheir sum is %d\n", sum);
  return (0);
}
