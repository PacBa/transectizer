# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TransectizerDialog
                                 A QGIS plugin
 Transectizer plugin
                             -------------------
        begin                : 2013-11-21
        copyright            : (C) 2013 by Jorge Tornero
        email                : jtorlistas@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_transectizer import Ui_transectizer

class transectizerDialog(QtGui.QDockWidget):
    def __init__(self):
        QtGui.QDockWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_transectizer()
        self.ui.setupUi(self)
        
        