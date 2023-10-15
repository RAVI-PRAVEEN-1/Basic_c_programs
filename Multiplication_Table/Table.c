#include<stdio.h>
int main()
{
    int m,n,i;
    printf("Enter the value for table:");
    scanf("%d",&n);
    printf("Enter the limit of table:");
    scanf("%d",&m);
    for(i=1;i<=m;i++)
    {
        printf("%dx%d=%d\n",n,i,n*i);
    }
}
