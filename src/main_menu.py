import pyglet
import glooey


class MyLabel(glooey.Label):
    custom_color = '#babdb6'
    custom_font_size = 10
    custom_alignment = 'center'

class MyButton(glooey.Button):
    Foreground = MyLabel
    custom_alignment = 'fill'

    class Base(glooey.Background):
        custom_color = '#204a87'

    class Over(glooey.Background):
        custom_color = '#3465a4'

    class Down(glooey.Background):
        custom_color = '#729fcff'

    def __init__(self, text, response):
        super().__init__(text)
        self.response = response

    def on_click(self, widget):
        print(widget)
        print(self.response)


class MainMenu(glooey.Bin):
    """
    """
    def __init__(self, deck):
        super().__init__()
        vbox = glooey.VBox()

        continue_button = MyButton("continue", "continue")
        exit_button = MyButton("exit", "exit")
        exit_button.push_handlers(on_click=lambda w: self.parent.set_state("gameplay"))

        vbox.add(continue_button)
        vbox.add(exit_button)

        self.add(vbox)
