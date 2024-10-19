import pygame,sys
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("MATCH THE FOLLOWING GAMES")
screen.fill("white")

subway=pygame.image.load("aut.png")
ludo=pygame.image.load("lbg.png")
candycrush=pygame.image.load("hbg.png")
temple_run=pygame.image.load("pgsmash.png")
screen.blit(subway,(100,150))
screen.blit(ludo,(100,250))
screen.blit(temple_run,(100,350))
screen.blit(candycrush,(100,450))
font=pygame.font.SysFont("Times New Roman",36)
t1=font.render("Heroes Battleground",True,(0,0,0))
t2=font.render("Legends Battleground",True,(0,0,0))
t3=font.render("A Universal Time",True,(0,0,0))
t4=font.render("Project Smash",True,(0,0,0))
screen.blit(t1,(400,150))
screen.blit(t2,(400,250))
screen.blit(t3,(400,350))
screen.blit(t4,(400,450))
pygame.display.update()
while True:
    event=pygame.event.poll()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,255),(pos),10,width=0)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),(pos),(pos2),5)
        pygame.draw.circle(screen,(0,0,255),(pos2),10,width=0)
        pygame.display.update()
