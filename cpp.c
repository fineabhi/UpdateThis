#include<stdio.h>
#include <math.h>
int main(){
    float Principle,Rate,Time,si,ci;
    int Choice;
printf("this is programme to find out the simple interest and compound interest\n");
printf("Press 1 to find out Simple Interest and Press 2 to find out Compound Interest\n");
scanf("%d",&Choice);
if (Choice==1){
    printf("enter Principle,Rate and Time for calculating Simple Interest\n");

    scanf("%f%f%f",&Principle,&Rate,&Time);
    si=(Principle*Rate*Time)/100;
    printf("The Simple Interest is %f\n",si);
}
else{
    printf("enter values for calculating Compound Interest\n");
    scanf("%f%f%f",&Principle,&Rate,&Time);
    ci=((Principle*(1+Rate/100))*2)-Principle;

    printf("The Compound Interest is %f\n",ci);

}
return 0;
}