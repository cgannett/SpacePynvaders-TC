import pygame
#Game Attributes
windowHeight = 600
windowWidth = 400
windowName = "Space PYnvaders"

pygame.init()

#init gameDisplay
window = pygame.display
window.set_caption(windowName)
gameDisplay = window.set_mode((windowHeight,windowWidth))

class Player:
  def __init__(self, x, y, image, speed):
    self.is_alive = True
    self.locX = x
    self.locY = y
    self.speed = speed
    self.image = image
    self.width = image.get_width()
    self.height = image.get_height()  
  def show(self):
      gameDisplay.blit(self.image, (self.locX, self.locY))
#woo

clock = pygame.time.Clock()

loadImage = pygame.image.load("assets/si-player.gif")

player1 = Player(200, 200, loadImage, 5)


while player1.is_alive:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      player1.is_alive = False  
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player1.locX -= player1.speed
      elif event.key == pygame.K_RIGHT:
        player1.locX += player1.speed
        
  player1.show()
  gameDisplay.update()
  clock.tick(60)


pygame.quit()