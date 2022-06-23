#exemple_interface

from pymel.core import *
win = window(title="My Window")
layout = columnLayout()
chkBox = checkBox(label = "My Checkbox", value=True, parent=layout)
btn = button(label="My Button", parent=layout)
def buttonPressed(*args):
    if chkBox.getValue():
        print "Check box is CHECKED!"
        btn.setLabel("Uncheck")
    else:
        print "Check box is UNCHECKED!"
        btn.setLabel("Check")
btn.setCommand(buttonPressed)
win.show()