Yumei Huo:

* computational complexity
* publications on website

Algorithms used in almost all areas.

The entire PhD class is in this course.  

Ask if they want to do a Cohort slack?

Assessment - 'simple' from data structures.

'This class is very hard.'

Need algorithms & discrete math as prerequists

# Preassessment

## Part One

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

### Question One

What is the value returned if the fuction zoc is called with parameter m=3 and n=2?

15

### Question Two

Give the mathematical recurrence function of zoc(m, n):

zoc[m, n] = zoc[m-1, n] + zoc[m, n-1]

### Question Three

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

### Question One

In the above program segment, how many times has comparison of (`theArray[i]<theArray[j]`) been executed?

$$ n^{2} $$ times.

### Question Two

What is the asymptotic complexity of the above algorithm?

$$ O(n^{2}) $$

# Lecture One

Growth of Functions

* Asymptotic Notation
* Recurrence Equation

Divide-and-Conquer:

* Sorting
* Heapsort
* Median and other Order Statistics

Greedy Algorithms:

* Activity Selection
* Minimum Spanning Tree: Prim, Kruskal, Borvka
* Matroids
* Knapsack
* Set Covering

Randomized Algorithms:

* Quicksort
	* the constant counts, which is why randomized quicksort is fast.
	* use a random pivot to make the algorithm fast.
	* 
* Satisability

Iterative Algorithms:

* Page Rank
* K-means
* Steepest Descent

Dynamic Programming:

* Longest Common Subsequence
* Knapsack
	* we will see this a couple times.
* Independent Set
	* we will see this a couple times.
* Dijkstra Algorithm for Shortest Paths
	* contraversal as dynamic programming.
	* greedy is typical case.
		* locally optimal, but may not be globally optimal.
		* pick and then update dynamically.
		* Not really dynamic.
		* if you can see only one pair - you need to go through all others.
		* only consider one pair of vertices, single shortest path for all vertices.
		* you must choose all points and then pick one solution.  This is dynamic program.
	* data is updated dynamically.
	
Data Structures:

* Heaps
* Binary Search Trees
	* 0,1 tree
	* red/black tree
	* avl tree
	* we will choose one.
* Hash Tables
* Disjoint Sets

Aside: we may need another course on algorithms if we want to do research.

Network Flows:

* Ford-Fulkerson
* Bipartite Matching
* Maximum Flow and Minimum Cut

Linear Programming (and Integer Programming):

* Standard and Other Forms
* Simplex
* Duality


Aside: This will happen often.
Very important topic.

Write objective and constraint.  Scheduling some best solutions.  Mixed linear programming.  Software to solve such problems if you have the functions.

Computability and Complexity:

* Halting Problem
* Polynomial Time
* Complexity Classes P and NP
* NP-Completeness

Aside:
Some stuff will be covered here.  How do you prove a problem is NP complete?  

Traveling salesmen - lots of variants of this problem.

If you have breakthrough in this field, you can always publish the top journals.  Even slightly better solutions.  

How do we reduce from 1 NP-complete problem to another problem.  NP-completeness is a decision problem.  If you have an optimization problem: what is the shortest distance - this is an optimization problem.  Decision problem - do you have a path traversing all the cities, such that traversing is less than some equal value.  This changes this to a decision problem.  For any given solutions, you can say yes or no.  Any solution, gives you yes or no.

Aside: we will be recording lectures.

Assessment: 35 percent of final grade.

Homework:

Sometimes industry interview questions as homework.  Sometimes from textbook.

Programming as well.

Make sure to say version and compiler.

Project - huffman encoding

Introduction to algorithms.

Algorithm Design - Kleinberg and Tardos as supplemental.  

The art of programming by Donald Knuth.

Administrivia:

* office hours: by appointment
* email: yumei.huo@csi.cuny.edu
* Zoom meeting 20-30 minutes before class, 30 minutes after class.

Why study Algorithms and performance?

* performance often drwas the line between what is feasible and what is impossible.
* algorithmic mathematics provides a language for talking about program behavior. (e.g. by using big-O-notation)
* in real life, many algorithms, though different from each other, fall into one of several paradigms (discussed shortly).  These paradigms can be discussed

Why these particular algorithms?

1) main
	* greedy
	* divide and conquer
	* dynamic programming
	* branch and bound
		* mostly in AI
		* https://www.geeksforgeeks.org/branch-and-bound-algorithm/
2) Other reasons:
	* relevance to many areas:
		* networking
		* internet
		* search engines

Lots of problems can be modeled as classical data structures.  

Topics:
* recursive equations
* divide and conquer method
* dynamic programming
* basic and advanced data structures
* graph algorithms
* approximation algorithms
* NP-Complete theory
* randomized algorithms

There will be some variance with other courses on algorithms because of the professors research interests.

Algorithms is very broad.

Hou's interests:
* Discrete geometry
* Sequencing / scheduling problems
* Graph Theory

Consider reading Huo's papers to get a sense of what she'll be interested in teaching the most.

Goals of algorithm design

* correct (proof)
	* how do we know if an algorithm is correct?
		* give a proof
	* How do you show this?
		* proof by contradiction
		* proof by induction 
* efficiency
	* time - running time
	* space
		* take mergesort as an example - you need N size memory, so you can get running time n log n.
		* some folks have figured out how to do inplace mergesort.
	* randomized algorithms also matter but may not be covered.
* simple & easy to understand
	* good structure, good documentation, etc.
		* clean code
		* recursive solution is usually more concise.
		* theoretically - you can always write a recursive solution iteratively.
		* divide and conquer and dynamic programming based on recursion.
		* algorithm is divorced from iteration or recursion.  Both are just two implementations for the same algorithm.
		Algorithm:
			* what is a step?
			* what is your running time?
			* How do you go into the next step? - this is implementation detail.

Analyzing Algorithms
* Von Neumon structure - https://en.wikipedia.org/wiki/Von_Neumann_architecture
* RAM: Random access machine
	It takes one step for accessing memory once.
	The instructions are executed one by one

Analysis (Techniques) of computing time (time complexity)

definition: time complexity of a particular algorithm is the running time as a function of problem sizze and expressed in terms of basic operations.

Matrix multiplication:

dimensions of M x N (matrix operations).

basic operations:
	* multiplications
	* additions

We always talk about how many multiplications and how many additions?

N^2? N^3?

Normally N^3.
Divide and conquer for N^2.

Sorting:

you want the algorithm to sort N numbers.

Input of problem size: size of the array.
Total bits to represent these N numbers.
	* talk about this during NP-completeness

fundamental algorithms:
	* comparison
	* swaps

when we evaluate - how many comparisons? how many swaps?

Time is out of n log n - n * log n.

n log n comparisons.

The problem of sorting

Input: sequence (a1, a2, .., aN) of numbers.
Output: permutation of the input numbers

Running time
* parameterize the running time by the size of the input n
* seek upper bounds on the running time T(n) for the input size n, because everybody likes a guarantee.

Kinds of analyses
* worse-case (usually)
	* T(n) - maximum time of algorithm on any input size n.

Average-case: (sometimes)
	* T(n) - expected time of algorithm over all inputs of size n.
	* need assumption of statistical distribution fo inputs.

Best-case: (bogus)
* cheat with a slow algorithm that works fast on some input.

Worst case for quicksort:
O(n^2)

Average case for quicksort: O(n log n)

You need some assumption for the distribution of inputs.  Usually assume a uniform distribution assumption.

Machine-independent time

What is insertion sort's worst-case time?
* it depends on the speed of our computer:
	* relative speed (on the same machine)
	* absolute speed (on different machines)

Big idea:
	* ignore machine-dependent constants
	* look at growth of T(n) as n-> inf
	* asymptotic analysis

We only care about computers for parallel algorithms because we consider number of threads.

But typically we ignore hardware and only consider the theoretical running time.

Bubble sort algorithm:

```
for i <- l to length[A]
	do for j <- length[A] downto i+1
		do if A[j] < a[j-1]
			then exchange A[j] <-> A[j-1]
```

Running time?

worst case: O(n^2)

This is the same algorithm as the preassessment test.

i -> [1, n]
j -> [n, i+1]

for each i, n-(i+1)+1 = n-2
therefore for each i, O(n) comparisons.  Therefore `O(n*n)` comparisons.

$$ \sum n-i = n(n+1)/2 $$

Cover this in next class:
big O - worst case
big omega - best case
little o
little omega
theta - average case

Half of class.

Reading assignment: Read chapter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.  

* Master theorem: master recurrence running time
* recurrence function.
* Merge sort.
	* Use tree structure to analyze recurrence structure.
	* Prove by induction
	* repeated substitution
	* formula - master theorem

Aside - link and slides will be posted.

Homeworks on blackboard. - first homework comes from textbook.

Qualifying exam:  

Unclear, might be seperate, might be this class.

Post the homework this week.

