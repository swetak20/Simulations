# Simulations
Repository to maintain simulation codes over a range of setting.


## Table of Content
  1. Number of Collision
  2. Galaxy
  3. Drunkard Walk


## Number of Collision

### Objects:
  1. Block 1 - mass = 1 unit
  2. Block 2 - mass = 100<sup>(d)</sup>
  3. Wall - mass = inf

![Initial State](https://github.com/swetak20/Simulations/blob/main/utilities/collsion_20.png)

*Initial State* :  Block 1 remains at rest with no contact with the wall. Block 2 moves with velocity in the direction towards block 1. The first collision happens between the two blocks.<br />

*State of affairs* : All the collisions are perfectly elastic. The subsequent collisions are goverened by the laws of linear momentum conservation, total energy conservation. <br />

*Aim* : To calculate the total number of collisions between the two blocks and block 1 and wall. The collisions stop when Block 2 attains velocity with magnitude greater than magnitude of velocity of block 1 and its direction is away from block 1.

It is observed that the total number of collisions comes to be equal to the **first (d-1) digits of π.**



## Galaxy Collision

*Initial State* : This is a Simulation of collision of two galaxies. These galaxies are **hypothetical and do no follow the real shape or mass distribution of original galaxies** .
The galaxies are in the shape of a circle. There are n particle in each of the galaxies. The mass of each particle decreases by the Cosine function, where angle
is normalised to (0,π/2) from magnitude the distance from the centre of the galaxy. These particles are at rest initially.<br />

*State of affairs* : The particles of the two galaxies interact according to the **Gravitational Laws**. The forces of each particle is calculated and henceforth motion is carried out.<br />

*Aim* : To visualise the simulation using **Seaborn Library** and plot them.



## Drunkard Walk

### Obbjects:
  1. Drunkard
  2. House
  3. 1-D path (x-axis)
  4. Coin

*Initial State* : The drunkard is initially at x = 0.<br />

*State of affairs* : The drunkard takes one step at a time. He/She/They always move to x = 1 when currently at x = 0. At x !=0 the drunkard can take a step to right or left with an equal peobability.
An unbaised coin is tossed at each step to decide the direction of next step. The process continues till the drunkard reaches his/her/their house at x = n.

*Aim* :  To analyse the nature of result, we perform the simulation large number of times(100 here) for the same house position and take the average of the individual results. 

It is observed that the average steps is equal to the **square of house position, n<sup>2</sup>**.


