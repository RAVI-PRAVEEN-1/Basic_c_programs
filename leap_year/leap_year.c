#include <stdio.h>
int main() {
   int year;
   scanf("%d",&year);
   printf("Enter Year");
   if (((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0))
      printf("%d is a leap year", year);
   else
      printf("%d is not a leap year", year);
return 0;
}
