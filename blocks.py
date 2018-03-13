import pyglet, physicalobject
from pyglet.window import key


class Blocks(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        #Give me properties
        # Basic block with collision detection
        super(Blocks, self).__init__(img=pyglet.resource.image("yellowsquare.png"), *args, **kwargs)

        #Event Handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        super(Blocks, self).update(dt)

    def collision(self, other):
        super(Blocks, self).collision(other)

    
