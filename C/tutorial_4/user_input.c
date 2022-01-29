#include <stdio.h>

int main(){
    int num;
    float decimal;
    char character;
    char name[15];
    printf("Enter a number: ");
    scanf(" %d",&num);
    printf("Enter a decimal: ");
    scanf(" %f",&decimal);
    printf("You entered %d and %f\n", num, decimal);
    printf("Enter a character: ");
    scanf(" %c",&character);
    printf("Enter your name: ");
    scanf(" %s",name);
    printf("You entered %c\n",character);
    printf("Your name is %s\n",name);
    return 0;
}