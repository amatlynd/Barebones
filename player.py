import pyglet
from pyglet.window import key
import physicalobject, util



class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        #Probably should have a resources page 
         super(Player, self).__init__(img=pyglet.resource.image("greensquare.jpg"), *args, **kwargs)

         #Event Handlers
         self.key_handler = key.KeyStateHandler()
         self.event_handlers = [self, self.key_handler]

    def update(self, dt):


        #Movement speed. Since only the player moves in this level only they get
        if self.key_handler[key.LEFT]:
            self.velocity_x += -100 * dt

        if self.key_handler[key.RIGHT]:
            self.velocity_x += 100 * dt

        if self.key_handler[key.UP]:
            self.velocity_y += 100 * dt

        if self.key_handler[key.DOWN]:
            self.velocity_y += -100 * dt

        super(Player, self).update(dt)
