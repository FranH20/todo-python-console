from datetime import datetime
from typing import Dict

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
    
    def add_to_database(self) -> None:
        model_dicct = {
            "title":self._title, 
            "description": self._description,
            "time": self._time,
            "date": self._date,
            "status": self._status
        }
        return model_dicct

    def find_and_get(self, all_data: Dict, todo_search: int) -> bool:
        #find the object
        collection = {}
        if todo_search >= 0 and todo_search < len(all_data):
            collection = all_data[todo_search]
        else:
            return False
        #get the object
        self._title = collection["title"] 
        self._description = collection["description"]
        self._status = collection["status"]
        self._date = collection["date"]
        self._time = collection["time"]
        return True
    
    def show_all(self):
        message = f'Title: [primary]{self.title}[/primary] \n' + \
            f'Description: [primary]{self.description}[/primary] \n'
        if self.status == True:
            message = message + 'Status: [primary]Todo finished[/primary]  :white_check_mark: \n'
        else:
            message = message + 'Status: [primary]Todo unfinished[/primary] :x: \n'
        message = message +  f'Date: [primary]{self.date}[/primary] \n' + \
            f'Time: [primary]{self.time}[/primary]'
        return message