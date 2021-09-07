## Chapter 2

I was really stuck on the whole recurrence equation thing until I found [this handout](http://cse.unl.edu/~choueiry/F07-235/files/Recursion-HandoutNoNotes.pdf)

Recurrence equations have two parts:

The recursive part: T(n) 
The subproblem work: everything else

So!  If you are doing O(n) work in each subproblem and T(n) work in the recursive part (aka you are doing n recursive calls), then you are doing O(n^2) work.  This is _because_ the recursion is the same thing as an _outer_ for loop (or while loop).  So if you want to figure out how much work is happening overall, you need to look at the number of recursive calls, and the work being done per recursive call.

That's why, for instance - the running time of recurrsive insertion sort is still O(n^2) even though, we are only doing worst case, O(n) per call!

