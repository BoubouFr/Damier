import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((315,315),)
fenetre_2 = pygame.display.set_caption("Damier")

gameIcon = pygame.image.load("jeton.png")
pygame.display.set_icon(gameIcon)


fond = pygame.image.load("fond.jpg").convert()

fenetre.blit(fond, (0,0))

perso = pygame.image.load("objet.png").convert_alpha()
perso = pygame.transform.scale(perso,(40,40))

fenetre.blit(perso, (-1,-1))

pygame.display.flip()

position_perso=0
position_perso_y=0
position_perso_y2=0

son = pygame.mixer.Sound("timer cut.wav")

son.play()


print("N'appuyez pas sur aucun bouton ! Le Jeu va commençer dans 10 secondes. Pour jouer il suffit d'utiliser les touches directionnelles droites et gauche afin de déplaçer le jeton. Le but est d'atteindre la fin du damier. vous pouvez quand même revenir en arrière ! Bonne chance.")

pygame.time.wait(10000)

son = pygame.mixer.Sound("legend-of-zelda-nes-intro.wav")

son.play(loops=-1, maxtime=0, fade_ms=0)

print("Partez")


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=0
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                if position_perso<7:
                    position_perso = position_perso + 1
                    print(position_perso)

                else:

                    if position_perso==7:
                        position_perso=0
                        position_perso_y=position_perso_y+1
                        pygame.key.get_repeat()
                        print(position_perso)

                    if position_perso_y==8:
                        position_perso_y=0
                        position_perso=0
                        print("Bien joué, Tu as accompli la mission")




            if event.key==K_LEFT:
                if position_perso>0:
                    position_perso=position_perso-1
                    print(position_perso)
                else:
                    if position_perso==0:
                        position_perso=7
                        position_perso_y=position_perso_y-1




    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (position_perso*40,position_perso_y*40))
    pygame.display.flip()
pygame.quit()

