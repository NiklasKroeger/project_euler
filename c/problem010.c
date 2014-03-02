#include <stdio.h>


int main()
{
	int a, b;			/*untere und obere Grenze*/
	int i = 1;			/*Primzahlzähler*/
	int rest, teiler = 2;		/*Variablen zum testen ob Primzahl*/	
	unsigned long summe = 2;


	printf ("\nPrimzahlbestimmung in 2 Grenzen, Testat 1a, Dag Röttger, Niklas Kröger.\n\n");
	printf ("Bitte untere Grenze eingeben: ");
	scanf ("%d", &a);
	printf ("Bitte obere Grenze eingeben: ");
	scanf ("%d", &b);
	if (a == 0 && b>=2)
	{
		a=2;
		printf ("Primzahl 1: 2\n");
		i++;

	}
	else if (a == 1 && b>=2)		/*1 ist keine Primzahl, erfüllt aber Bedingungen, daher unterdrücken*/
	{	
		a ++;				/*2 ist Primzahl, wird aber vom Programm nicht korrekt erfasst*/
		printf ("Primzahl 1: 2\n");
		i++;
	}
	else if (a == 2)
	{	
		printf ("Primzahl 1: 2\n");
		i++;
	}
	do
	{
		do
		{
			rest = (a % teiler);	/*solange nicht teilbar, rest != 0*/
			teiler ++;
		}
		while (rest != 0 & teiler < (a/2));
		if (rest != 0)			/*Wenn rest nach Durchlauf bis a-1 immernoch null, Primzahl*/
		{
			summe += a;
			
//			printf ("Primzahl %d: %d\n",i, a);
			i ++;
		}
		teiler = 2;			/*teiler zur Neuberechnung auf 2 zurücksetzen*/
		a ++;
	}
	while (a <= b);
//	printf ("\n");
	printf("%lu\n", summe);
	return (0);
}
