import pygame, socket
import time, pickle

"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SIZE = (1366/2, 768/2)

pygame.__init__('This is fun')
screen = pygame.display.set_mode(SIZE)

startFlag = False
while startFlag == False and False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            print "Detected keydown", event.key, pygame.K_d
            startFlag = True


while True and False:
    screen.fill(WHITE)
    pygame.display.flip()
    time.sleep(0.3)
    screen.fill(BLACK)
    pygame.display.flip()
    time.sleep(0.3)
    """

class FlashClient(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SIZE = (1366, 768)

    SMALL = 0x1
    BIG = 0x2
    def __init__(self, serverURL, serverPort, mode):
        self.server = serverURL
        self.port = serverPort
        pygame.__init__("DDD Client")
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.toggle_fullscreen()

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server, self.port))
        sizedata = ""
        while '|' not in sizedata:
            sizedata += s.recv(64)
        size = int(sizedata.split('|')[0])
        print size
        data = sizedata.split('|')[1]
        while len(data) < size:
            data += s.recv(4096)
        data = pickle.loads(data)
        print data
        self.data = data
        self.s = s
        self.trigger()

    def trigger(self):
        print "Trigger Start"
        #x = self.s.recv(20)
        x = ""
        #if len(x) > 0:
        while len(x) < 10:
            x += self.s.recv(11)
            print x
        x = int(x)
        while time.time() < x:
            pass
        self.run(self.data)
        print "Trigger End"
        self.quit()

    def run(self, colorData):
        for i in colorData:
            self.screen.fill(i[0])
            pygame.display.flip()
            time.sleep(i[1])

    def quit(self):
        pygame.display.quit()

FC = FlashClient("192.168.0.109", 4646, FlashClient.SMALL)
FC.start()
