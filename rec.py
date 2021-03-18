class Rec:

    def __init__(self):
        self.current_pos = 0
        self.step_size = 1
        self.seen = set([0])
        self.step_delta = 1

    def can_go_back(self):

        back_pos = self.current_pos - self.step_size

        if back_pos < 0:
            return False, back_pos

        if self.already_seen(back_pos):
            return False, back_pos

        return True, back_pos

    def already_seen(self, pos):
        if pos in self.seen:
            return True

        return False

    def get_current(self):
        return self.current_pos

    def reset(self):
        self.current_pos = 0
        self.seen = set()

    def generate_next(self):

        go_back, back_pos = self.can_go_back()

        if go_back:
            self.current_pos = back_pos
            self.seen.add(self.current_pos)
            self.step_size += self.step_delta
            return self.current_pos

        self.current_pos += self.step_size
        self.seen.add(self.current_pos)
        self.step_size += self.step_delta
        return self.current_pos

        