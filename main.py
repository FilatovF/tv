from typing import List
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    cur_ch = 0

    def __init__(self, channels: List):
        self.chs = channels

    def first_channel(self):
        self.cur_ch = 0
        return self.chs[self.cur_ch]

    def last_channel(self):
        self.cur_ch = len(self.chs) - 1
        return self.chs[self.cur_ch]

    def turn_channel(self, num):
        if num - 1 < len(self.chs):
            self.cur_ch = num - 1
            return self.chs[self.cur_ch]
        return self.last_channel()

    def next_channel(self):
        self.cur_ch += 1
        # if self.cur_ch < len(self.chs):
        return self.turn_channel(self.cur_ch + 1)

    def previous_channel(self):
        self.cur_ch -= 1
        if self.cur_ch < 0:
            return self.first_channel()
        return self.turn_channel(self.cur_ch + 1)

    def current_channel(self):
        return self.chs[self.cur_ch]

    def is_exist(self, data) -> str:
        if type(data) == int:
            if data in range(len(self.chs) + 1):
                return "Yes"
            return "No"

        if data in self.chs:
            return "Yes"
        return "No"

controller = TVController(CHANNELS)

