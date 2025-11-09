# Queue Implementation Hints

## General Approach
- A queue follows First-In-First-Out (FIFO) principle
- Elements are added at one end (back) and removed from the other (front)

## Sub-Challenge 1: Create Class
**Hint:** Define your data structure. Consider what storage supports adding to one end and removing from another.

**Common approaches:** Array/List, Circular buffer, or Linked List

## Sub-Challenge 2: Enqueue
**Hint:** Add to the back/end of your storage.

**Think about:** The enqueue operation should be straightforward with most data structures.

## Sub-Challenge 3: Dequeue
**Hint:** Remove from the front/beginning. This is the key difference from a stack!

**Performance note:** Removing from the front can be slow with some structures. That's OK for learning.

**Edge case:** What should happen if the queue is empty?

## Sub-Challenge 4: Front
**Hint:** Access the first element without removing it.

**Think about:** Similar to peek in stack, but at the front end.

**Edge case:** Handle empty queue appropriately.

## Sub-Challenge 5: Size
**Hint:** Return the count of elements currently in the queue.

**Think about:** Track this as you add/remove elements.

## Common Pitfalls
- Mixing up front/back operations (FIFO vs LIFO)
- Handling empty queue edge cases
- Performance considerations with array/list removal

## Test Independence
Each challenge tests only its specific functionality:
- Challenge 1 (Create Class) tests basic instantiation
- Challenge 2 (Enqueue) tests adding elements
- Challenge 3 (Dequeue) tests removing elements and verifies FIFO order
- Challenge 4 (Front) tests peeking without removal
- Challenge 5 (Size) tests element counting

**Recommendation:** Implement in order, as later challenges may use earlier methods.
