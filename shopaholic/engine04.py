# -*- coding: utf-8 -*-
# engine04.py

from .widgets04 import Widgets

class Engine(Widgets):
    def __init__(self):
        super(Engine, self).__init__()
        self.title = "Shopaholic"
        self.version = 0.1
        platform = "Shopaholic Release 1 (stretch)"
        s = "%s ver %s\nwritten by\nCouch Janus \nMilky Way Galaxy\nSolar System\nThird planet(Earth) \nNAU Ukraine(Kyiv)\ncouchjanus@gmail.com\n%s"
        msg = (s % (self.title,self.version,platform))
        self.about = msg
