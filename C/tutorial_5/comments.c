/*****************************************************
Program: comments.c
Author: Jonathan Karr
This program introduces comments
This program asks the user for 3 numbers and sums them
******************************************************/
#include <stdio.h>

int main(){
    double num1, num2;
    printf("Enter two numbers to add: ");
    scanf(" %lf %lf", &num1, &num2);//takes in 2 numbers as doubles
    double sum = num1 + num2; //sum 2 numbers as a double
    printf("%g + %g = %g\n", num1, num2, sum); //prints out the answer 1 + 3 = 4
    return 0;
}