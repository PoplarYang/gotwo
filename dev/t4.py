from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import getpass
import sys

current_username = getpass.getuser()

user_info = {}


def gather_ssh_info():
    """
    gather ssh information
    """
    try:
        with open('/Users/yangyanan/.ssh/config') as fd:
            for line in fd:
                line = line.strip()
                if line.startswith('Host ') and '*' not in line:
                    hostname = line.split()[1]
                if line.startswith('HostName') and '*' not in line:
                    host = line.split()[1]
                    if hostname and host:
                        user_info[hostname] = host
                    hostname = host = ''
    except Exception as e:
        print('Error, %s' % e)
        sys.exit()


class ListView(Frame):
    def __init__(self, screen, model):
        super(ListView, self).__init__(screen,
                                       screen.height * 2 // 3,
                                       screen.width * 2 // 3,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Servers List")
        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            add_scroll_bar=True
        )
        self._connect_button = Button("Connect", self._connect)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.fix()
        self._on_pick()

    def _connect(self):
        self._model.current_id = None
        raise NextScene("Edit Contact")

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


def demo(screen, scene):
    scenes = [
        Scene([ListView(screen, contacts)], -1, name="Main"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
