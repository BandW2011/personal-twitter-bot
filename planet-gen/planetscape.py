import World

def main():
    WIDTH  = 720 // 4
    HEIGHT = 1280 // 4

    world = World.World()
    world.createImage(WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
