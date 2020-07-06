import sys, random, math
import pygame

#graphs
'''
import matplotlib.pyplot as plt

plt.xlabel("x axis")
plt.title("title")
'''

#Want to learn more about pygame? Here is a good link:
URL = "http://kidscancode.org/lessons/"
flip = 0
GRAY = (50, 50, 50)

# Pygame template - skeleton for a new pygame project
# set up asset
 
WIDTH = 800
HEIGHT = 600
FPS = 30
checkingdelete = False
X = 0
Y = 0
xcheck = 0
ycheck = 0
alive = False
neighbors = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
step_size = 10
COLORS = [RED, GREEN, BLUE, BLACK]
'''
def draw_grid():
  for x in range(0, WIDTH, step_size):
    pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
  for y in range(0, HEIGHT, step_size):
    pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
'''
def _debug(msg):
  print(msg)

def draw_grid():
  for x in range(0, WIDTH, step_size):
    pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
  for y in range(0, HEIGHT, step_size):
    pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def findplace(pos):
  x, y = pos
  return (x // step_size + 1, y // step_size + 1)

def place(pos):
  x, y = pos
  return ((x - 1) * step_size, (y - 1) * step_size)

class Player(pygame.sprite.Sprite):
  def __init__(self, name, x, y):
    global xcheck, ycheck, alive, neighbors
    pygame.sprite.Sprite.__init__(self)
    lif  = pygame.image.load(name).convert_alpha()
    self.image = pygame.transform.scale(lif, (step_size, step_size))
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)
    self.rect.x = x
    self.rect.y = y

  def update(self):
    pass

  def checkdelete(self, x, y):
    if x == self.rect.x:
      if y == self.rect.y:
        return True
    return False

  def check(self, alive, neighbors):
    global step_size
    _debug('check:' + str(self.rect.x) + ', ' + str(self.rect.y))
    for ycheck in range(0, 36, 1):
      for xcheck in range(0, 49, 1):
        xcheck *= step_size
        ycheck *= step_size
        if xcheck == self.rect.x:
          if ycheck == self.rect.y:
            alive = True

        elif xcheck - step_size == self.rect.x:
          if ycheck - step_size == self.rect.y:
            neighbors += 1
        
        elif xcheck - step_size == self.rect.x:
          if ycheck == self.rect.y:
            neighbors += 1
        
        elif xcheck - step_size == self.rect.x:
          if ycheck + step_size == self.rect.y:
            neighbors += 1

        elif xcheck == self.rect.x:
          if ycheck - step_size == self.rect.y:
            neighbors += 1

        elif xcheck == self.rect.x:
          if ycheck + step_size == self.rect.y:
            neighbors += 1
        
        elif xcheck + step_size == self.rect.x:
          if ycheck - step_size == self.rect.y:
            neighbors += 1
        
        elif xcheck + step_size == self.rect.x:
          if ycheck == self.rect.y:
            neighbors += 1

        elif xcheck + step_size == self.rect.x:
          if ycheck + step_size == self.rect.y:
            neighbors += 1

        if alive == True:
          if neighbors < 2 or neighbors > 3:
            self.kill()
        
        elif alive == False:
          if neighbors == 3:
            life = Player('life.jpg', lifex, lifey)
            all_sprites.add(life)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LayeredComputer")
#add more layers :)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

running = True
while running:
  # keep loop running at the right 
  clock.tick(FPS)
  # Process input (events)
  for event in pygame.event.get():
      # check for closing window
      if event.type == pygame.QUIT:
        running = False

      elif event.type == pygame.MOUSEBUTTONDOWN: 
        lifex, lifey = place(findplace(event.pos))

        for x in all_sprites:
          checkingdelete = x.checkdelete(lifex, lifey)
          if checkingdelete == True:
            _debug('remove:' + str(lifex) + ', ' + str(lifey))
            x.kill()
            break

        if checkingdelete == False:
          life = Player('life.jpg', lifex, lifey)
          all_sprites.add(life)
          _debug('adde:' + str(lifex) + ', ' + str(lifey))

        checkingdelete = False

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          for gamelife in all_sprites:
            gamelife.check(False, 0)
          #start

          '''
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              while event.key != pygame.K_RIGHT:
                print('hi')
          '''

  # Update
  all_sprites.update()
  screen.fill(BLACK)
  draw_grid()

  # Draw / render
  all_sprites.draw(screen)
 

  #player image dot get recked
  # *after* drawing everything, flip the display
  pygame.display.flip()
  pygame.time.delay(1)
pygame.quit()

