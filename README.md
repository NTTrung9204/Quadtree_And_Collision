# Applications of quadtree in collision detection problems.

**Demo program for collision of 2000 points:**
![image](https://github.com/NTTrung9204/Quadtree_And_Collision/assets/83105598/a5d72212-69b8-43b6-80ef-13f34df3a0f9)

## Getting started
Clone this repository:
`git clone https://github.com/NTTrung9204/Quadtree_And_Collision.git`

Run the program by typing `py Main.py` or `python3 Main.py` on the command line

## About quadtree
![image](https://github.com/NTTrung9204/Quadtree_And_Collision/assets/83105598/71192845-bea9-4543-9e35-ff98d7ea7389)

### Initialize QuadTree

**Constructor `__init__()`:**

- Takes in two points, TopLeftPoint and BottomRightPoint, representing the top-left and bottom-right corners of the region managed by the QuadTree.
- Capacity is the maximum number of points each node can hold before splitting, defaulting to 4.
- divided is a flag indicating whether the node has been subdivided into four child nodes.
- TopLeftTree, TopRightTree, BottomLeftTree, BottomRightTree represent the four child trees.
- listPoints is the list of points contained within the current region.


### Boundary Check `inBoundary()`

- This method checks whether a point lies within the region managed by the QuadTree.


### Division `divide()`

- Divides the current region into 4 smaller sub-regions:
- TopLeftTree: Manages the top-left region.
- TopRightTree: Manages the top-right region.
- BottomLeftTree: Manages the bottom-left region.
- BottomRightTree: Manages the bottom-right region.
- Sets the flag 'divided' to True after division.

### Inserting Points `insert()`

- Checks if the point lies outside the managed region, then returns False.
- If the number of points in the current node is less than the capacity, inserts the point into the listPoints.
- If the capacity has been exceeded and the node has not been divided yet, performs division.
- Inserts the point into the appropriate child region.

### Searching within a Range `search()`

- Finds points within a specified region defined by TopLeft and BottomRight.
- Checks for intersection between the search region and the current region.
- Iterates through the points in listPoints and adds them to the result if they are within the search region.
- If the node has been divided, continues searching within the child regions and aggregates the results.

### Application
- Every frame, iterate through the points and use the search() method to find neighboring points for the current point. This helps to avoid complexity and optimize performance. In fact, the program is already able to run smoothly and stably with 2000 points.

### Algorithm Complexity
- When building the quadtree with n data points, we have a complexity of `O(nlog(n))`
- In the ideal case, the average complexity of the search method by region is `O(log(n))`, the worst-case scenario is `O(n)` (when the search area equals the entire map), and the best-case scenario remains `O(log(n))`.
- When the search area is smaller, the search becomes faster.
