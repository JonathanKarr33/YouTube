#include <stdio.h>
int main(){
    int items;
    printf("Enter the number of items: ");
    scanf("%d",&items);
    switch (items)
    {
    case 0 ... 5:
        printf("You have between 0 and 5 items\n");
        break;
    default:
        printf("You have more than five items\n");
        break;
    }
    return 0;
}