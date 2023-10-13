from actions.base_actions import BaseActions
from utils.logger import Logger
from utils.recorder_helper import RecorderHelper


class TestSomeActions:

    def test_take_record(self):
        try:
            recorder = RecorderHelper("abc")
            recorder.start_record()
        except Exception as e:
            Logger.take_screenshot("test_do_something")
            print(f"Error : {str(e)}")

    def test_run_specific(self):
        try:
            recorder = RecorderHelper("base")
            recorder.run_record()
        except Exception as e:
            Logger.take_screenshot("test_do_something")
            print(f"Error : {str(e)}")

    def test_rerun_abc(self):
        try:
            actions = BaseActions()
            actions.rerun_abc()
        except Exception as e:
            Logger.take_screenshot("test_do_something")
            print(f"Error : {str(e)}")