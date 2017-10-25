#!/usr/bin/env python2
# {{@@ env['dotdrop_warning'] @@}}
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#

import gtk
import gobject
import sys
import threading
import os


class TrayIcon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.icon = gtk.StatusIcon()
        self.icon.set_visible(False)
        self.current_icon = None
        self.icon.connect("popup-menu", self.right_click_event)
        # self.icon.connect("button-press-event", self.left_click_event)
        self.icon.connect('activate', self.left_click_event)
        self.shutdownstatus = True

    def left_click_event(self, icon, button):
        print "yes"

    def right_click_event(self, icon, button, time):
        menu = gtk.Menu()

        if self.shutdownstatus:
            noshut = gtk.MenuItem("No shutdown")
            noshut.connect("activate", self.noshutdown)
            menu.append(noshut)
        else:
            noshut = gtk.MenuItem("Shutdown when finished")
            noshut.connect("activate", self.noshutdown)
            menu.append(noshut)

        cancel = gtk.MenuItem("Cancel")
        cancel.connect("activate", self.exodos)
        menu.append(cancel)

        menu.show_all()

        menu.popup(None, None, gtk.status_icon_position_menu, button, time,
                   self.icon)

    def noshutdown(self, dummy):
        if self.shutdownstatus:
            pyfile = open((sys.path[0]) + "/.pyoutput", "wb")
            pyfile.write("noshut")
            pyfile.close()
            self.shutdownstatus = False
        else:
            pyfile = open((sys.path[0]) + "/.pyoutput", "wb")
            pyfile.write("turnoff")
            pyfile.close()
            self.shutdownstatus = True

    def exodos(self, dummy):
        pyfile = open((sys.path[0]) + "/.pyoutput", "wb")
        pyfile.write("quit")
        pyfile.close()

    def run(self):
        while True:
            l = sys.stdin.readline()
            if not l:
                break
            else:
                fields = l.strip().split()
                if not fields:
                    continue
                if fields[0] == "icon":
                    gobject.idle_add(self.update_icon, fields[1])
                elif fields[0] == "reload":
                    gobject.idle_add(self.reload_icon)
                elif fields[0] == "tooltip":
                    gobject.idle_add(self.update_tooltip, " ".join(fields[1:]))
                elif fields[0] == "hide":
                    gobject.idle_add(self.hide)
        os._exit(0)

    def update_icon(self, fname):
        if fname != self.current_icon:
            self.icon.set_from_file(fname)
            self.current_icon = fname
        self.icon.set_visible(True)

    def update_tooltip(self, tooltip):
        self.icon.set_tooltip_text(tooltip)

    def hide(self):
        self.icon.set_visible(False)

    def reload_icon(self):
        self.icon.set_from_file(self.current_icon)
        self.icon.set_visible(True)

if __name__ == "__main__":
    gobject.threads_init()
    TrayIcon().start()
    try:
        gtk.main()
    except KeyboardInterrupt:
        os._exit(0)
