from datetime import datetime
class todo:

    def __init__(self):
        self._title = ""
        self._description = ""
        self._date = datetime.now().strftime("%d/%m/%Y")
        self._time = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) < 80:
            self._title = value
            self._time = datetime.now().strftime("%H:%M:%S")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if len(value) < 180:
            self._description = value
            self._time = datetime.now().strftime("%H:%M:%S")
    
    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time
    