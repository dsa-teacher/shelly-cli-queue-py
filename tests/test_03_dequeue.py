import sys
sys.path.insert(0, 'src')
from queue import Queue

def test_dequeue():
    """Test removing and returning front element"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() is None

def test_dequeue_empty():
    """Test dequeue on empty queue"""
    queue = Queue()
    assert queue.dequeue() is None
