from gi.repository import Gtk


class CellBtn(Gtk.Button):

    cell = None
    
    def __init__(self, cell):
        Gtk.Button.__init__(self)
        self.cell = cell
        self.connect('click', self._on_click)
        
    def _on_click(self, btn):
        self.set_sensitive(False)
        if !cell.isMine:
            self.label = cell.value
        
