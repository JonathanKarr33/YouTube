/*********************************
Program: if_statements.c
Author: Jonathan Karr
This program introduces the if statement
print out the largest number
*********************************/

#include <stdio.h>

int main(){
    double num1, num2;
    printf("Enter 2 numbers to see which is bigger: ");
    scanf("%lf %lf", &num1, &num2);
    if(num1 > num2){
        printf("%g is the largest number\n", num1);
    }
    else if( num1 == num2 ){
        printf("The numbers are the same. They are both %g\n", num1);
    }
    else{
        printf("%g is the largest number\n", num2);
    }
    return 0;
}