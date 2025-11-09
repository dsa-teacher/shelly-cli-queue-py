import sys
sys.path.insert(0, 'src')
from queue import Queue

def test_front():
    """Test returning front element without removing"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.front() == 10
    assert queue.dequeue() == 10
    assert queue.front() == 20

def test_front_empty():
    """Test front on empty queue"""
    queue = Queue()
    assert queue.front() is None
