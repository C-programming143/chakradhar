#include<stdio.h>
int find_factors(int num)//fun def
{
	int fc=0,i;
	if(num==0 || num==1)
	{
		return 1;
	}
	for(i=2;i<=num/2;i++)
	{
		if(num%i==0)
		{
			fc++;
			break;
		}
	}
	return fc;	
}

void main()
{
	int num,i,fc,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&num);
		fc=find_factors(num);//function call
		if (fc==0)
		{
			printf("Prime");
		}
		else
		{
			printf("Not a Prime");
		}
	}	
}
