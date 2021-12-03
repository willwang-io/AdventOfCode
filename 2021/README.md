# 2021

### Day 1

Straightforward

### Day 2

Straightforward


### Day 3
- __part 1__: we can use XOR with 1 to flip a bit, i.e., `1 XOR 1 = 0`, `O XOR 1 = 1`, 
  or `1011 XOR 1111 = 0100`. Thus, we only have to get one rate and then just 
  flip it to get another one. 
- __part 2__: Basically simulation. Note that we could use `zip` to group 
columns together.