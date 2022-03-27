#include <stdio.h>
int main(){
    int i = 1;

    while(i <= 5){
        if (i == 3){
            i++;
            continue;
        }
        printf("%d\n", i);
        i++;
    }
    printf("We are finished with the loop\n");
    return 0;
}