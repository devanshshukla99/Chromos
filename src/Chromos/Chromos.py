#!/usr/bin/python3
from sys import stdout

"""
Package for getting colored text output in Python terminal
"""

class InvalidColor(Exception):
    """
    Exception Raised when Invalid Color is entered.
    """
    def __init__(self, message="Invalid Color"):
        self.message = message
        super().__init__(self.message)

    pass

class InvalidBGColor(Exception):
    """
    Exception Raised when Invalid Background Color is entered.
    """
    def __init__(self, message="Invalid Background Color"):
        self.message = message
        super().__init__(self.message)

    pass

class InvalidDelimiter(Exception):
    """
    Exception Raised when the Delimiter is Invalid
    """
    def __init__(self, message=''.join(["Invalid Delimiter\n\n", "\033[1;31m[\033[0m", "\033[1;34m!\033[0m", "\033[1;31m]\033[0m", " Use ' ' as the delimiter\n"])):
        self.message = message
        super().__init__(self.message)

    pass

class InvalidAttribute(Exception):
    """
    Exception Raised when Invalid Attribute is entered.
    """
    def __init__(self, message="Invalid Attribute"):
        self.message = message
        super().__init__(self.message)

    pass

class Chromos():
    """
    Chromos provides colored-text terminal output.

    Colors:
        Black    --    black
        Red      --    red
        Green    --    green
        Yellow   --    yellow
        Blue     --    blue
        Purple   --    purple
        Cyan     --    cyan
        White    --    white

    Background Colors:
        Black    --    bgblack
        Red      --    bgred
        Yellow   --    bgyellow
        Blue     --    bgblue
        Purple   --    bgpurple
        Cyan     --    bgcyan
        White    --    bg white

    Styles:
        (bf)   Bold
        (it)   Itallic         (may not be supported)
        (u)    Underline
        (blk)  Blink           (may not be supported)
        (st)   Strikethrough
    
    Functions:
        cstr('<color> <bgcolor, optional> <attributes>', '<string>')
        blue('<color>', '<string>')
        info('<string>')
        info_y('<string>')
        error_info('<string>')
        error_info_b('<string>')
    """

    base_attr = '\033['
    attr = base_attr
    default_bgcolor = 'bgblack'
    no_style = False
    bold = True
    itallic = False
    underline = False
    blink = False
    strikethrough = False
    colors = {
            "black":"30",
            "red":"31",
            "green":"32",
            "yellow":"33",
            "blue":"34",
            "purple":"35",
            "cyan":"36",
            "white":"37",
            "bgblack":"40",
            "bgred":"41",
            "bggreen":"42",
            "bgyellow":"43",
            "bgblue":"44",
            "bgpurple":"45",
            "bgcyan":"46",
            "bgwhite":"47"
        }

    style = {
            "no_style":"0",
            "bold":"1",
            "itallic": "3",
            "underline":"4",
            "blink": "5",
            "strikethrough": "9"
        }

    attrinter = {
            "bf": "bold",
            "it": "itallic",
            "u": "underline",
            "blk": "blink",
            "st": "strikethrough"
        }

    def get_attr(self):
        self.attr = self.base_attr

        if(self.no_style==False):
            if(self.bold==True):
                self.attr = ''.join([self.attr, "1;"])
            if(self.itallic==True):
                self.attr = ''.join([self.attr, "3;"])
            if(self.underline==True):
                self.attr = ''.join([self.attr, "4;"])
            if(self.blink==True):
                self.attr = ''.join([self.attr, "5;"])
            if(self.strikethrough==True):
                self.attr = ''.join([self.attr, "9;"])
        else:
            self.attr = ''.join([self.attr, "0;"])

        return

    def attribute_interpretor(self, args):
        """
        bl  --  blink
        it  --  itallic
        u   --  underline
        blk --  blink
        st  --  strikethrough
        """

        attr = self.base_attr

        for arg in args:
            if(len(arg.lower()) > 3):
                attr = ''.join([attr, self.style[arg.lower()], ";"])
            else:
                attr = ''.join([attr, self.style[self.attrinter[arg.lower()]], ";"])

        return attr

    def cstr(self, args:'Arguments (str)', string:'Text (str)'):
        """
        cstr('<color> <bgcolor, optional> <attributes>', '<string>')

        Parameters:
            args[0]: color (str): Color.
            args[1]: bgcolor (optional) (str): Background Color.
            args[1:-1]: (optional) Attributes.
            args[-1]: string (str): Text.

        Returns:
            str: Text with Appropiate Prefix and Suffix.
        """

        if(type(args) is str): args = args.split(' ')
        
        color = args[0].lower()
        bgcolor = self.default_bgcolor
        color_attr = ""

        if(len(args)>1):
            if(args[1][0:2]=="bg"):
                bgcolor = args[1].lower()
                args.pop(1)
                try:
                    color_attr = ''.join([self.colors[bgcolor], ";"])
                except KeyError:
                    raise InvalidBGColor

        args.pop(0)

        try:
            color_attr = ''.join([color_attr, self.colors[color]])
        except KeyError:
            raise InvalidColor

        if(args):
            try:
                self.attr = self.attribute_interpretor(args)
            except KeyError:
                raise InvalidAttribute
        else:
            self.get_attr()

        return ''.join([self.attr, color_attr, "m", string, "\033[0m"])

    def help(self):
        stdout.write("""
        Chromos provides colored-text terminal output.

        Colors:
            Black    --    black
            Red      --    red
            Green    --    green
            Yellow   --    yellow
            Blue     --    blue
            Purple   --    purple
            Cyan     --    cyan
            White    --    white

        Background Colors:
            Black    --    bgblack
            Red      --    bgred
            Yellow   --    bgyellow
            Blue     --    bgblue
            Purple   --    bgpurple
            Cyan     --    bgcyan
            White    --    bg white

        Styles:
            (bf)   Bold
            (it)   Itallic         (may not be supported)
            (u)    Underline
            (blk)  Blink           (may not be supported)
            (st)   Strikethrough
        
        Functions:
            cstr('<color> <bgcolor, optional> <attributes>', '<string>')
            blue('<color>', '<string>')
            info('<string>')
            info_y('<string>')
            error_info('<string>')
            error_info_b('<string>')
        """)
        stdout.flush()
        
        return

    def black(self, string:str)->str:
        """
        black('<color>', '<string>')
        """
        self.get_attr()

        return ''.join([self.attr, self.colors["black"], "m", string, "\033[0m"])

    def blue(self, string:str)->str:
        """
        blue('<color>', '<string>')
        """
        self.get_attr()

        return ''.join([self.attr, self.colors["blue"], "m", string, "\033[0m"])

    def red(self, string:str)->str:
        """
        red('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["red"], "m", string, "\033[0m"])

    def green(self, string:str)->str:
        """
        green('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["green"], "m", string, "\033[0m"])

    def yellow(self, string:str)->str:
        """
        yellow('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["yellow"], "m", string, "\033[0m"])

    def purple(self, string:str)->str:
        """
        purple('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["purple"], "m", string, "\033[0m"])

    def cyan(self, string:str)->str:
        """
        cyan('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["cyan"], "m", string, "\033[0m"])

    def white(self, string:str)->str:
        """
        white('<color>', '<string>')
        """
        self.get_attr()
        
        return ''.join([self.attr, self.colors["white"], "m", string, "\033[0m"])

    def info(self, string:str)->None:
        """
        info('<string>')
        """
        stdout.write(''.join([self.red("["), self.blue("*"), self.red("]"), " ", self.red(string)]))
        stdout.flush()
        
        return

    def info_y(self, string:str)->None:
        """
        info_y('<string>')
        """
        stdout.write(''.join([self.blue("["), self.red("*"), self.blue("]"), " ", self.yellow(string)]))
        stdout.flush()

        return

    def error_info(self, string:str)->None:
        """
        error_info('<string>')
        """
        stdout.write(''.join([self.blue("["), self.red("!"), self.blue("]"), " ", self.red(string)]))
        stdout.flush()

        return

    def error_info_b(self, string:str)->None:
        """
        error_info_b('<string>')
        """
        stdout.write(''.join([self.blue("["), self.red("!"), self.blue("]"), " ", self.blue(string)]))
        stdout.flush()
        
        return

    pass

