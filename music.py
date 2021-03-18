import musicalbeeps

class Music:
    def __init__(self):
        self.player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

        self.notes = [
            "C",
            "D",
            "E",
            "F",
            "G",
            "A",
            "B",
        ]

        self.notes_with_format = [
            "C{oct}",
            "C{oct}#",
            "D{oct}",
            "D{oct}#",
            "E{oct}",
            "F{oct}",
            "F{oct}#",
            "G{oct}",
            "G{oct}#",
            "A{oct}",
            "A{oct}#",
            "B{oct}",
        ]

        self.octaves_count = 8
        self.max_note_play_time = 3
        self.note_count = len(self.notes) - 1
        self.current_note = None
        self.all_notes = []
        self.get_all_notes()

    def get_all_notes(self):

        for oct in range(1,9):
            for note in self.notes_with_format:
                self.all_notes.append(
                    note.format(
                        oct = str(oct)
                    )
                )

    def gen_func_1(self, prev_pos, curr_pos):
        """ normal progression

            if current pos is more than prev pos, go to higher note
            else go to lower note. Octave is same. Note play time is
            constant
        """

        if self.current_note == None:
            self.current_note = 0
            return self.current_note, 4, 0.2

        if curr_pos > prev_pos:
            self.current_note = min(self.current_note + 1, self.note_count)
        else:
            self.current_note = max(self.current_note - 1, 0)

        return self.notes[self.current_note], 4, 0.1

    def gen_func_2(self, prev_pos, curr_pos):
        """ modulo 7 progression

            current note is current position % 7. Octave is same.
            Note play time is constant
        """

        self.current_note = curr_pos % 7

        return self.notes[self.current_note], 4, 0.1

    def gen_func_3(self, prev_pos, curr_pos):
        """ all notes
        """

        self.current_note = curr_pos % 96
        print (self.current_note)

        return self.all_notes[self.current_note], "", 0.05

    def gen_params(self, prev_pos, curr_pos):

        return self.gen_func_3(prev_pos, curr_pos)

    def play(self, prev_pos, curr_pos):
        print (prev_pos, curr_pos)

        note_params = self.gen_params(prev_pos, curr_pos)

        #note = "{note_letter}{octave}#".format(
            #note_letter=note_params[0],
            #octave=str(note_params[1])
        #)

        note = note_params[0]

        play_time = note_params[2]

        self.player.play_note(note, play_time)
