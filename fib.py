class Fib:

    def __init__(self):
        self.current = 1
        self.previous = 0

    def get_current(self):
        return self.current
    
    def generate_next(self):
        next_num = self.current + self.previous
        self.previous = self.current
        self.current = next_num
        return next_num

    def reset(self):
        self.current = 1
        self.previous = 0

