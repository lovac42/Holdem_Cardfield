# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/Holdem_Cardfield
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


import aqt.addcards
from anki.hooks import wrap


history = []
def addHistory(addCards, note, _old):
    addCards.history = history
    return _old(addCards, note)


def __init__(addCards, mw, _old):
    ret = _old(addCards, mw)
    if history:
        addCards.history = history
        addCards.historyButton.setEnabled(True)
    return ret

aqt.addcards.AddCards.addHistory = wrap(aqt.addcards.AddCards.addHistory,addHistory,"around")
aqt.addcards.AddCards.__init__ = wrap(aqt.addcards.AddCards.__init__,__init__,"around")
