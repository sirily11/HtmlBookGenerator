from datetime import datetime, timedelta
from tqdm import tqdm

class SRT:
    def __init__(self, sentences, time):
        self.sentences = sentences
        self.time = time
        self.linenum = len(sentences)

    def to_srt(self):
        returnStr = ""
        print("Start making a srt object")
        for i in tqdm(range(self.linenum)):
            currentline = self.sentences[i]
            starttime = self.__generate_timestamp(self.time[i]['starttime'])
            endtime = self.__generate_timestamp(self.time[i]['endtime'])
            returnStr += "{} --> {}\n{}\n\n".format(i+1,starttime,endtime,currentline)
        print("Finished making a srt object")
        return returnStr

    def __generate_timestamp(self, time):
        millionSec = int((time - int(time)) * 1000)
        sec = timedelta(seconds=time)
        d = datetime(1, 1, 1) + sec
        sec = d.second
        min = d.minute
        hr = d.hour

        if sec < 10:
            sec = "0{}".format(sec)

        if min < 10:
            min = "0{}".format(min)

        if hr < 10:
            hr = "0{}".format(hr)

        return "{}:{}:{}.{}".format(hr, min, sec, millionSec)
