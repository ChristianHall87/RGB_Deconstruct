import pygame, sys, numpy
from PIL import Image

pygame.init()
'''
def Menu():
	while True: 
		sel = input('Hello! Experience Magic!\n 1. Convert Image\n 2. Expose Image')
		sel = int(sel)
		if sel == 1:
			Convert()
			Menu()
		if sel == 2:
			R()
			G()
			B()
			Menu()
		if sel != 1 or sel != 2:
			print('Whoops, try again!')
			Menu()
'''
width, height = 275,183
speed1 = [1,0]


def Convert():
	
	img = Image.open("/Users/christianhall/Desktop/icon.JPG") # Open image

	for x in range(img.size[0]):					# X range pixels
		for y in range(img.size[1]):				# Y range Pixels
			r, g, b = img.getpixel((x,y))			# Get RGB data
			img.putpixel((x,y),(r,0,0))				# Place RED
	#img.show()
	img.save("/Users/christianhall/Desktop/iconR.JPG") #Save New Image


	img = Image.open("/Users/christianhall/Desktop/icon.JPG")	#GREEN
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			r, g, b = img.getpixel((x,y))
			img.putpixel((x,y),(0,g,0))
	#img.show()
	img.save("/Users/christianhall/Desktop/iconG.JPG")

	img = Image.open("/Users/christianhall/Desktop/icon.JPG")	#BLUE
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			r, g, b = img.getpixel((x,y))
			img.putpixel((x,y),(0,0,b))
	#img.show()
	img.save("/Users/christianhall/Desktop/iconB.JPG")






def R():
	beams = 0
	#width, height = 1280, 1024					#SET THIS FOR CAMERA
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption('RGB Magic')
	background1 = pygame.image.load("/Users/christianhall/Desktop/iconR.JPG")
	background2 = pygame.image.load("/Users/christianhall/Desktop/iconG.JPG")
	background3 = pygame.image.load("/Users/christianhall/Desktop/iconB.JPG")
	screen.blit(background1, (0,0) )

	#load image
	target1 = pygame.image.load('black.png')
	target1 = pygame.transform.scale(target1, (width * 2 ,height))
	targetpos1 = target1.get_rect()
	screen.blit(target1, targetpos1)



	#running
	while True:
		targetpos1.move_ip(speed1)
		screen.blit(background1, (0,0))
		screen.blit(target1, targetpos1)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		if targetpos1[0] > 0 or targetpos1[0]<-width:
			speed1[0] = -speed1[0]
			beams = beams + 1
			if beams == 3:
				break
#______________________________________________________________________'
def G():
	beams = 0
	#width, height = 1280, 1024
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption('RGB Magic')
	background2 = pygame.image.load("/Users/christianhall/Desktop/iconG.JPG")
	screen.blit(background2, (0,0) )

	#load image
	target1 = pygame.image.load('black.png')
	target1 = pygame.transform.scale(target1, (width * 2 ,height))
	targetpos1 = target1.get_rect()
	screen.blit(target1, targetpos1)

	




	#running
	while True:
		targetpos1.move_ip(speed1)
		screen.blit(background2, (0,0))
		screen.blit(target1, targetpos1)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		if targetpos1[0] > 0 or targetpos1[0]<-width:
			speed1[0] = -speed1[0]
			beams = beams + 1
			if beams == 3:
				break


#______________________________________________________________________'
def B():
	beams = 0
	#width, height = 1280, 1024
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption('RGB Magic')
	background3 = pygame.image.load("/Users/christianhall/Desktop/iconB.JPG")
	screen.blit(background3, (0,0) )

	#load image
	target1 = pygame.image.load('black.png')
	target1 = pygame.transform.scale(target1, (width * 2 ,height))
	targetpos1 = target1.get_rect()
	screen.blit(target1, targetpos1)






	#running
	while True:
		targetpos1.move_ip(speed1)
		screen.blit(background3, (0,0))
		screen.blit(target1, targetpos1)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		if targetpos1[0] > 0 or targetpos1[0]<-width:
			speed1[0] = -speed1[0]
			beams = beams + 1
			if beams == 3:
				break



if __name__ == '__main__':
	#Menu()
	Convert()
	R()
	G()
	B()
	exit()

