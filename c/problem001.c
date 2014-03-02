#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int summe = 0, i;
  
  for (i=1; i<1000; i++)
  {
    if (i%3 == 0 || i%5 == 0)
    {
      summe += i;
    }
  }
  printf ("Summe: %d\n", summe);
  
  EXIT_SUCCESS;
}
