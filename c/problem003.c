#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    long long int input = 600851475143;
    while (input % 2 == 0)
    {
        input /= 2;
    }
    for (long long int factor = 3; factor <= sqrt(input); factor += 2)
    {
        if (input % factor == 0)
        {
            input /= factor;
        }
    }
    printf("%i\n", input);
    return 0;
}
