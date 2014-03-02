#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int sum = 2; // Gleich mit 2 Starten um sonderfall auslassen zu können
    int old = 1;
    int new = 2;

    while (new < 4000000)
    {
        new = old + new;
        old = new - old;

        if (new % 2 == 0)
        {
            sum += new;
        }
    }
    printf("Summe: %i\n", sum);

    EXIT_SUCCESS;
}
