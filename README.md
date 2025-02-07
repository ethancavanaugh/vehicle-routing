# Vehicle Routing
This application is a school project that attempts to minimize the distance travelled by a fleet of delivery vehicles. 

## 2-Opt Algorithm
The 2-opt algorithm is a local search algorithm that considers each pair of vertices, swapping them if doing so reduces the length of the tour. While this algorithm can theoretically take exponential time in certain specially crafted cases, in practice it will generally reach a local minimum in polynomial time. Since each iteration improves the tour length, it can also be stopped at an arbitrary time and will still provide an improvement over the starting tour. It provides better tours on average than constructive algorithms such as nearest neighbor and Christofides, averaging less than 5% over the Karp-Held lower bound on optimal tour length.[[1]](https://www.cs.ubc.ca/~hutter/previous-earg/EmpAlgReadingGroup/TSP-JohMcg97.pdf)

## Custom Hash Map
As part of this project a custom hash map was implemented (for educational purposes, not performance). It uses a simple version of open addressing where any collisions are handled by saving the value in the next open index. It overrides Python's __getitem__(), __setitem__(), __delitem__(), and __len__() methods, so it can be accessed/manipulated using the same syntax as Python dictionaries. A KeyError Exception will be raised if an invalid key is used.
