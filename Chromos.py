#!/usr/bin/python3
#Colored Text Model

class Chromos():

    def __init__(self):
        super(Chromos, self).__init__()

        self.base_attr = "\033["

        self.no_style = False
        self.bold = True
        self.underline = False
        self.negative1 = False
        self.negative2 = False
        self.attr = self.base_attr

        self.txt_colors = {
            "black":"30",
            "red":"31",
            "green":"32",
            "yellow":"33",
            "blue":"34",
            "purple":"35",
            "cyan":"36",
            "white":"37"
        }

        self.bg_colors = {
            "black":"40",
            "red":"41",
            "green":"42",
            "yellow":"43",
            "blue":"44",
            "purple":"45",
            "cyan":"46",
            "white":"47"
        }

        self.style = {
            "no_style":"0",
            "bold":"1",
            "underline":"2",
            "negative1":"3",
            "negative2":"5"

        }
    
    def get_attr(self):

        self.attr = self.base_attr

        if(self.no_style==False):
            if(self.bold==True):
                self.attr += "1;"
            if(self.underline==True):
                self.attr += "2;"
            if(self.negative1==True):
                self.attr += "3;"
            if(self.negative2==True):
                self.attr += "5;"
        else:
            self.attr +=  "0;"

        return

    def blue(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["blue"] + "m" + string

    def red(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["red"] + "m" + string

    def green(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["green"] + "m" + string

    def yellow(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["yellow"] + "m" + string

    def purple(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["purple"] + "m" + string

    def cyan(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["cyan"] + "m" + string

    def white(self, string):

        self.get_attr()
        
        return self.attr + self.txt_colors["white"] + "m" + string

    def error_info(self, string):
        
        print(self.blue("[") + self.red("!") + self.blue("]") + " " + self.blue(string))
        print(self.red("[") + self.blue("!") + self.red("]") + " " + self.red(string))

        return

    pass
