#include <stdio.h>
int main(){
    int number = 25;
    int number2 = 50;
    printf("Number: %d is at address %p\n",number,&number);
    printf("Number2: %d is at address %p\n",number2,&number2);
    int favorite_number;
    printf("Enter your favorite number: ");
    scanf("%d",&favorite_number);
    int reassign = 1;
    for(int i = 0; i < 5; i++){
        reassign = reassign + 1;
        printf("Reassign: %d is at address %p\n",reassign,&reassign);
    }
    int *ptr = &reassign;
    printf("%p is the number %d\n",ptr,*ptr);
    return 0;
}