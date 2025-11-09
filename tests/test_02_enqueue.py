import sys
sys.path.insert(0, 'src')
from queue import Queue

def test_enqueue():
    """Test adding elements to the queue"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
