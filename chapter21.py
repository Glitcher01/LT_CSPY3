class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        totalsecs = hours * 3600 + minutes * 60 + seconds
        self.hours = totalsecs // 3600
        leftsecs = totalsecs - hours * 3600
        self.minutes, self.seconds = leftsecs // 60, leftsecs % 60

    def __add__(self, other):
        return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __str__(self):
        return '{0}:{1}:{2}'.format(self.hours, self.minutes, self.seconds)

    def increment(self, secs):
        final_time = self.__add__(MyTime(0, 0, secs))
        self.hours, self.minutes, self.seconds = final_time.hours, final_time.minutes, final_time.seconds

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def between(self, time1, time2):
        return time1.to_seconds() <= self.to_seconds() < time2.to_seconds()

