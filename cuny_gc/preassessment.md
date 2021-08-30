# Part One

Given the following code segment:

```
int zoc(int m, int n){
	int x, y;
	if (m == 0 | n == 0) 
		return (m+n);
	x = zoc(m-1, n);
	y = zoc(m, n-1);
	return (x+y)
}
```

## Question One

What is the value returned if the fuction zoc is called with parameter m=3 and n=2?

15

## Question Two

Give the mathematical recurrence function of zoc(m, n):

zoc[m, n] = zoc[m-1, n] + zoc[m, n-1]

## Question Three

Describe the procedure (recursive calls) of deriving zoc(3, 2):

So the recursion base case stops at 1, because at that point n and m respectively will be zero.  Then we recurse up the call stack, such that the following call stack returns:

```
x=1, y=1
x=2, y=2
x=1, y=1
x=2, y=2
x=4, y=4
x=1, y=1
x=2, y=2
x=4, y=3
x=8, y=7
15
```

Here I have elected to indicate the first term, as in the code above with x and the second term with y.

## Part Two

Answer the questions based on the following program segment:

```
for(j=1; j<=n; ++j)
{
	i=j+1;
	do
	{
		if (theArray[i]<theArray[j])
			swap(theArray[i], theArray[j])
			++i;
	}while(i <= n);
	}
}
```

## Question One

In the above program segment, how many times has comparison of (`theArray[i]<theArray[j]`) been executed?

$$ n^{2} $$ times.

## Question Two

What is the asymptotic complexity of the above algorithm?

$$ O(n^{2}) $$

