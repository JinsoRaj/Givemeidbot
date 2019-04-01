#include<stdio.h>
int fibo(int num);
int main()
{
  int num,result;
  printf("enter the nth value:");
  scanf("%d",&num);
  if(num<0)
   {
    printf("please enter a positive number");
   }
  else
   {
    result=fibo(num);
    printf("the result is:%d",result);
   }
return 0;
}
int fibo(int num)
{
   if(num==0)
    {
      return 0;
    }
   else if(num==1)
    {
      return 1;
    }
   else
   {
     return (fibo(num-1))+(fibo(num-2));
   }
return 0;
}
