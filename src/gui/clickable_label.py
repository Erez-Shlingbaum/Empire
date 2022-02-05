import pyglet

from utils.math import Rectangle


class ClickableLabel(pyglet.text.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def rect(self) -> Rectangle:
        """
        Get Rectangle for label. (x,y) starts at bottom left
        """
        match self.anchor_x:
            case 'left':
                x_offset = 0
            case 'right':
                x_offset = -self.content_width
            case 'center':
                x_offset = -(self.content_width // 2)
        match self.anchor_y:
            case 'top' | 'baseline':
                raise NotImplementedError()
            case 'bottom':
                y_offset = 0
            case 'center':
                y_offset = -(self.content_height // 2)
        return Rectangle(self.x + x_offset, self.y + y_offset, self.content_width,
                         self.content_height)
