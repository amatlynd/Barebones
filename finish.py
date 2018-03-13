import pyglet
import os
from pyglet.window import key
import physicalobject




class Finish(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
         # In the quotations under image specify the file. Make sure the picture format is accurate
         super(Finish, self).__init__(img=pyglet.resource.image("redsquare.png"), *args, **kwargs)

        #Event Handlers. Key Presses if you want to add some
         self.key_handler = key.KeyStateHandler()
         self.event_handlers = [self, self.key_handler]

    
    def update(self, dt):
        
        super(Finish, self).update(dt)


    
    def collision(self, other):
        super(Finish, self).collision(other)
