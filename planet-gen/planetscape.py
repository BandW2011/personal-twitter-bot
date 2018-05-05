from World import World

class Planetscape:
    def __init__(self):
        # make configurable
        self.WIDTH  = 720 // 4
        self.HEIGHT = 1280 // 4

    def main(self):
        world = World()
        world.createImage(self.WIDTH, self.HEIGHT)

if __name__ == "__main__":
    Main.main()
