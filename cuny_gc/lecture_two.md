First exam Requirements:

For First Exam: Pass four core courses, at least one course from each of the three core areas, Algorithms being one of the four, with an average of A- or above.

This requirement is likely to be approved by all levels by the end of this semester. However just to be cautious, we will have final exam for this course, and it is important for you to perform well for the exam.

This implies you need A's in every class.

30% on final exam.  In person exam.

Question: Can we write code in a language we know?  For psuedo code will you expect C or C++?

We need the primitives to be expressed, but language doesn't matter.

T(n) - the running time of the given algorithm for input size n.

recursive insertion sort -

```python
from typing import List

def insertion_sort(A: List, n: int):
	# base case is implicit
	if n > 1:
		insertion_sort(A, n-1)
		insert(A, n)

def insert(A, n):
	tmp = A[n-1]
	j = n-2
	while j >= 0 and A[n-1] < A[j]:
		A[j+1] = A[j]
		j -= 1
	A[j+1] = tmp
```

For recursion - can your problem always reach the base case?


We maintain state by passing the array each time, but only considering the n-1 positions at each step.

T(n) = 
 * base case - 0 n = 1
 * T(n-1) + O(n) n > 1 

T(n) is always a recursive function.

T(n) will be multiplicative with the 'internal' O(n).  

So T(n) = T(n-1) + O(n) 

is how we get the recursion!!!

Methods of analysis:
* T(n) is a _recurrence relation_
* You might need to use the tree

1. Repeated Substitution

T(n) = T(n-1) + n-1

T(n-1) = T(n-2) + n-2

implies:

T(n) = T(n-2) + n-2 + n-1

therefore:

T(n) = 1 + 2 + .. + n-2 + n-1
$$ T(n) = \sum_{i=1}^{n} n $$

T(n) = n(n-1)/2.

2. Guess and prove by induction

3. Tree structure

Asymptotic complexity:

T[1](n) = 10n
T[2](n) = 2n^2

Linear time eventually grows more slowly than polynomial time.

T(n):

If there exists constants c and n[o] such that if T(n) <= cF(n) for n >= n[0] then we say T(n) is O(F(n)).

We say T(n) is the order of F(n).

O(.) - upperbound.  

Example:

T(n) = 5n + 10

Prove T(n) is order n.

need to find - k, c, n[0].

T(n) = 5n + 10
    <= 5n + 10n for n >= 1
     = 15n

We find c = 15 and n[0] = 1 such that T(n) <= `c*n` for n >= n[0].

By definition, we get T(n) is O(n).

Example:

Polynomial property:

For T(n) = a[k] * n^k + a[k-1] * n^k-1 + .. + a[1] * n + a[0]

we must have that T(n) is O(n^k).

Proof 

T(n) = a[k] * n^k + a[k-1] * n^k-1 + .. + a[1] * n + a[0]

    <= |a[k]| * n^k + |a[k-1]| * n^k-1 + .. + |a[1]| * n + |a[0]|

    <= |a[k]| * n^k + |a[k-1]| * n^k + .. + |a[1]| * n^k + |a[0]|

    $$ = (\sum_{i=0}^{n} |a[i]|) * n^k $$

We find c = \sum_{i=0}^{n} |a[i]|)

n[0] = 1

such that T(n) <= c * n^k for n >= n[0]

Sum Rule for O(.) 

if T[1](n) is O(f(n)) and T[2](n) is O(g(n)), then T[1](n) + T[1](n) is O(f(n) + g(n)).

Proof:

Since T[1](n) is O(f(n)), we have T[1](n) <= c[1] * f(n) for n >= n[1].  

Since T[2](n) is O(g(n)), we have T[2](n) <= c[2] * g(n) for n >= n[2].

T[1](n) + T[2](n)

<= c[1] * f(n) + c[2] * g(n) n >= max(n[1], n[2])

<= max(c[1], c[2]) f(n) + max(c[1], c[2]) * g(n) = max(c[1], c[2]) * f(n) + max(c[1], c[2]) * g(n)

Product Rule

if T[1](n) is O(f(n)) and T[2](n) is O(g(n)), then T[1](n) * T[1](n) is O(f(n) * g(n)).

Omega (.)

Definition

If there exists c and n[0] such that T(n) >= c * f(n) for n >= n[0], then we say T(n) is omega(f(n)).

Example:

T(n) = 5n^2 + 3n + 5
     >= 5n^2 for n >= 0

We find c = 5, n[0] = 0, such that T(n) >= c * n^2 for n >= n[0].  so we say that T(n) is Omega(n^2).

Theta (.)

Definition:

If T(n) is both O(f(n)) and Omega(f(n)), then T(n) is Theta(f(n)). 

Example:

T(n) = 5n^2 + 3n + 5

T(n) is Theta(n^2).

Tight bounds:

o(.) and omega(.)

We care about this 