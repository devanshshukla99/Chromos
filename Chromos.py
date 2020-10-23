#!/usr/bin/python3
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
    """

    def __init__(self):
        super(Chromos, self).__init__()

        self.base_attr = "\033["

        self.default_bgcolor = "bgblack"
        
        self.no_style = False
        self.bold = True
        self.itallic = False
        self.underline = False
        self.blink = False
        self.strikethrough = False
        self.attr = self.base_attr

        # self.txt_colors = {
        #     "black":"30",
        #     "red":"31",
        #     "green":"32",
        #     "yellow":"33",
        #     "blue":"34",
        #     "purple":"35",
        #     "cyan":"36",
        #     "white":"37"
        # }

        # self.bg_colors = {
        #     "black":"40",
        #     "red":"41",
        #     "green":"42",
        #     "yellow":"43",
        #     "blue":"44",
        #     "purple":"45",
        #     "cyan":"46",
        #     "white":"47"
        # }

        self.colors = {
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

        self.style = {
            "no_style":"0",
            "bold":"1",
            "itallic": "3",
            "underline":"4",
            "blink": "5",
            "strikethrough": "9"
        }
        
        self.attrinter = {
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

    def cstr(self, args, string):
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

        if(type(args) is str):
            args = args.split(" ")
        
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
        print("""
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

        cstr('<color> <bgcolor, optional> <attributes>', '<string>')
        blue('<color>', '<string>')
        info('<string'>)
        info_y('<string'>)
        error_info('<string>')
        error_info_b('<string>')
        """)
        
        return

    def blue(self, string):
        """
        blue('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["blue"], "m", string, "\033[0m"])

    def red(self, string):
        """
        red('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["red"], "m", string, "\033[0m"])

    def green(self, string):
        """
        green('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["green"], "m", string, "\033[0m"])

    def yellow(self, string):
        """
        yellow('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["yellow"], "m", string, "\033[0m"])

    def purple(self, string):
        """
        purple('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["purple"], "m", string, "\033[0m"])

    def cyan(self, string):
        """
        cyan('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["cyan"], "m", string, "\033[0m"])

    def white(self, string):
        """
        white('<color>', '<string>')
        """

        self.get_attr()
        
        return ''.join([self.attr, self.colors["while"], "m", string, "\033[0m"])

    def info(self, string):
        """
        info('<string'>)
        """

        print(''.join([self.red("["), self.blue("*"), self.red("]"), " ", self.red(string)]))
        
        return

    def info_y(self, string):
        """
        info_y('<string'>)
        """

        print(''.join([self.blue("["), self.red("*"), self.blue("]"), " ", self.yellow(string)]))

        return

    def error_info(self, string):
        """
        error_info('<string>')
        """

        print(''.join([self.blue("["), self.red("!"), self.blue("]"), " ", self.red(string)]))

        return

    def error_info_b(self, string):
        """
        error_info_b('<string>')
        """

        print(''.join([self.blue("["), self.red("!"), self.blue("]"), " ", self.blue(string)]))

        return

    pass

