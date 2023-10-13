from utils.logger import Logger
from utils.recorder_helper import RecorderHelper


class BaseActions:
    logger = Logger.log()

    def rerun_abc(self):
        recorder = RecorderHelper("abc")
        recorder.run_record()

    def rerun_base(self):
        recorder = RecorderHelper("base")
        recorder.run_record()