from contextlib import contextmanager

class FileLogger:
    def __init__(self, filename, mode='a'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False
    
@contextmanager
def my_context_manager():
    print("Entering the context...")
    yield 
    print("Exiting the context...")

with my_context_manager():
    print("Inside the block!")
    
if __name__ == "__main__":
    with FileLogger("log.txt") as log:
        log.write("Log entry: System started... \n")
        print("Writing to file...")

    print("Execution finished.")

"""
    EXPECTED OUTPUT:
    Entering the context...
    Inside the block!
    Exiting the context...
    Writing to file...
    Execution finished.
"""
    