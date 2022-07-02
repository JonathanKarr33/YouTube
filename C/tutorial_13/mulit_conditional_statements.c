#include <stdio.h>
int main(){
    int total = 745;
    int people = 350;
    if((total > 1000) && (people > 250)){
        printf("The number is high and there are a lot of people\n");
    }
    if((total > 1000) || (people > 250)){
        printf("The number is high or there are a lot of people\n");
    }
    return 0;
}