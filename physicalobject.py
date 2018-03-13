import pyglet

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # Velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Previous Location for detection
        self.prev_x, self.prev_y = 0.0, 0.0
        
    #updates the object
    def update(self,dt):
        #Updates position from velocity
        self.prev_x = self.x
        self.x += self.velocity_x * dt
        print(self.x)

        self.prev_y = self.y
        self.y += self.velocity_y * dt
        print(self.y)
        #Border
        self.check_bounds()
        
    #the border of the whole screen checker
    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = 800 - self.image.width #Make sure to change this constant according to the window 
        max_y = 600 - self.image.height #Make sure to change this constant according to the window 
        if self.x < min_x:
            self.velocity_x = 0
            self.x = min_x
        if self.y < min_y:
            self.velocity_y = 0
            self.y = min_y
        if self.x > max_x:
            self.velocity_x = 0
            self.x = max_x
        if self.y > max_y:
            self.velocity_y = 0
            self.y = max_y

    #checks if object collides with another object
    def collision(self, other):
        # Checks of there is a collision
        # More specifically if there is an overlap of rectangles
        if (self.x < other.x + other.image.width and
            self.x + self.image.width > other.x and
            self.y < other.y + other.image.height and
            self.y + self.image.height > other.y):
                self.velocity_x, self.velocity_y = 0.0, 0.0
                print('touch')
                return True
        return False
            
        

    def handle_collision(self,other):
        wy = (self.image.width + other.image.width) * (self.y - other.y)
        hx = (self.image.height + self.image.height) * (self.x - other.x)

        if (wy > hx):
            if (wy > -hx):
                #top
                self.y = other.y + other.image.height
            else:
                #left
                self.x = other.x - self.image.width
        else:
            if (wy > -hx):
                #right
                self.x = other.x + other.image.width
            else:
                #bottom
                self.y = other.y - self.image.width
        

