import sys
sys.path.insert(0, 'src')
from queue import Queue

def test_size():
    """Test returning the number of elements"""
    queue = Queue()
    assert queue.size() == 0
    queue.enqueue(10)
    assert queue.size() == 1
    queue.enqueue(20)
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1

