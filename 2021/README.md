# 2021

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

### Day 5 Hydrothermal Venture

Simulation, just some basic notes to have more elegant code:
- Convert 2D array index, `[x,y]` into 1D `x * n + y`, where `n` is the length of row.
- `|x1-x2| == |y1-y2|` to check two points 45-degree diagonal. 
- Use while-loop is cleaner to check which direction goes from one direction
to another. 

### Day 6 Lanternfish

Use a hash map to track the number of occurrences of each timer, update each 
timer by decreasing one of each day. For instance, today there are 8 fish with 
timer 3, then tomorrow there will be 8 fish with timer 2. Lastly, be aware 
when timer is 0. 

Brute-force will only _work_ for part 1, not recommend for part 2. 