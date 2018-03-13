import pyglet
import os

#Import other objects too 
import player, finish, blocks

#Size of the window screen
window = pyglet.window.Window(800,600)

#Collection of sprites to be populated and drawn later
main_batch = pyglet.graphics.Batch()

key = pyglet.window.key

#Initializing the event stack size
event_stack_size = 0



# This is where all the objects you want to initialize can get called
def init():
    # Global variables, make sure all objects are global
    # pl, fin, blo are the player, finishing point and blocks
    # More about the properties of each object can be found in respective .py files
    global p1, fin, blo, game_objects, event_stack_size

    #Iterates through the stack size and makes sure there aren't any handlers leftover
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    #Where objects get initiated
    p1 = player.Player(x=400, y=300, batch=main_batch)
    fin = finish.Finish(x=100, y=200, batch=main_batch)
    blo = blocks.Blocks(x=500, y=200, batch=main_batch)

    #Add other objects here to
    game_objects = [p1,fin,blo]

    for obj in game_objects:
        for handler in obj.event_handlers:
            window.push_handlers(handler)
            event_stack_size += 1


# Draws the sprites. Dont really need to change this
@window.event
def on_draw():
    window.clear()  
    main_batch.draw()


#The function called
def update(dt):

    #checks if it collides, with the object
    #Optimized to avoid double checking collisions of objects
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if obj_1.collision(obj_2):
                if((type(obj_1) == finish.Finish or type(obj_1) == player.Player) and
                   (type(obj_2) == finish.Finish or type(obj_2) == player.Player)):
                    
                    #This goes to the next level/game it closes the current window and opens
                    # the file of the next person/groups game.
                    #Change according to the type of operating system that it will be hosted on
                    # Currently this is for Windows OS
                    # For Linux distribution change the string into: os.system("python FILEPATH_NAME/game.py")
                    window.close()
                    os.system("py ./version5/game.py")
                obj_1.handle_collision(obj_2)
    
    #Updates every object from the initialized list
    for obj in game_objects:
        obj.update(dt)


  
if __name__ == "__main__":
    # Initializing Player and other objects
    init()
    # Update the game 120 times per second (fps)
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    # Tell pyglet to do its thing
    pyglet.app.run()




