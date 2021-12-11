# 2021

Here are some brief intuitions of each day's problem. 

### Day 1: Sonar Sweep

Straightforward

### Day 2: Dive!

Straightforward


### Day 3: Binary Diagnostic
- __part 1__: Use XOR with 1 to flip a bit, i.e., `1 XOR 1 = 0`, `O XOR 1 = 1`, 
  or `1011 XOR 1111 = 0100`. Thus, we only have to get one rate and then just 
  flip it to get another one. 
- __part 2__: Basically simulation. Note that we could use `zip` to group 
columns together.
  
### Day 4: Giant Squid 
Replace the current number with zero in the grid, so if any row or column has a sum of zero, 
then we have a bingo. 

- __part 1__: Immediately print the first win.
- __part 2__: Track all won games to avoid repeat check, then the last one will 
naturally be our answer. 

There is an obvious bug with this algorithm, for instance, 
after we replace the fourth number in a row, and the fifth number in that row 
is originally zero, thus, the `bingo` function will still return true.
Anyways, this is just not an OJ :). 

### Day 5: Hydrothermal Venture

Simulation, just some basic notes to have more elegant code:
- Convert 2D array index, `[x,y]` into 1D `x * n + y`, where `n` is the length of row.
- `|x1-x2| == |y1-y2|` to check two points 45-degree diagonal. 
- Use while-loop is cleaner to check which direction goes from one direction
to another. 

### Day 6: Lanternfish

Use a hash map to track the number of occurrences of each timer, update each 
timer by decreasing one of each day. For instance, today there are 8 fish with 
timer 3, then tomorrow there will be 8 fish with timer 2. Lastly, be aware 
when timer is 0. 

Brute-force will only _work_ for part 1, not recommend for part 2. 


### Day 7: The Treachery of Whales
Brute-force. Exam period, no time to think something smarter, like binary search maybe :stuck_out_tongue:.

### Day 8: Seven Segment Search
- __part 1:__ straightforward
- __part 2:__ Use set operators to determine the letter of each segment. Take each number as a set of letters. From the very top example in the problem description, consider 1 and 7, we can confirm the top segment must be `a`, because all elements in 7 also in 1 except `a`. Repeat this kind of logic until we get the letter for each segment confirmed. Finally, we just get all the segments need for each number. 

### Day 9: Smoke Basin
- __part 2:__ DFS. Track the previous location's height. Then we only keep searching if the current height is greater than the previous height. Others are just traditional DFS, i.e., remember where already visited, and boundaries check. 

### Day 10: Syntax Scoring
Classic stack parentheses problem. Two conditions need to be checked for matching parentheses, first is close parentheses unmatch the top of the stack, and second is the stack should empty at the end. Thus, that part 1 and part 2, respectively. 

### Day 11: Dumbo Octopus
We could use backtracking to resolve the second condition for flashes. Two notes
- flash first then increase by 1, because we could
- use -1 to mark the current-step flashed octopus, so then increase by 1
will become 0. 
