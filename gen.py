from rec import Rec
from fib import Fib
from music import Music


def gen():

    r = Rec()
    m = Music()

    #print (m.get_all_notes())
    #exit(0)

    prev_pos = 0
    for i in range(0, 1000):
        
        cur_pos = r.get_current()
        print (cur_pos)
        m.play(prev_pos, cur_pos)
        _ = r.generate_next()
        prev_pos = cur_pos

if __name__ == "__main__":
    gen()
