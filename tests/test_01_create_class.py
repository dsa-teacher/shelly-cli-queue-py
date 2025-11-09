import sys
sys.path.insert(0, 'src')
from queue import Queue

def test_create_queue():
    """Test creating a new queue instance"""
    queue = Queue()
    assert queue is not None
