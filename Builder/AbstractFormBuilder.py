import abc

class AbstractFormBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_title(self,title):
        self.title = title

    @abc.abstractclassmethod
    def form(self):
        pass

    @abc.abstractclassmethod
    def add_lable(self,text,row,column,**kwargs):
        pass