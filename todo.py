from datetime import datetime
class todo:

    def __init__(self):
        self._title = ""
        self._description = ""
        self._date = datetime.now().strftime("%d/%m/%Y")
        self._time = ""
        self._status = False
    
    #Get title
    @property
    def title(self):
        return self._title

    #Set title
    @title.setter
    def title(self, value):
        if len(value) < 80:
            self._title = value
            self._time = datetime.now().strftime("%H:%M:%S")

    #Get description
    @property
    def description(self):
        return self._description

    #Set description
    @description.setter
    def description(self, value):
        if len(value) < 180:
            self._description = value
            self._time = datetime.now().strftime("%H:%M:%S")
    
    #Get status
    @property
    def status(self):
        return self._status
    
    #Set status
    @status.setter
    def status(self, value):
        if value is True or value is False:
            self._status = value
    
    #Get date
    @property
    def date(self):
        return self._date
    
    #Get time
    @property
    def time(self):
        return self._time
    