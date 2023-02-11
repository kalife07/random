import pygame
import os

WIDTH, HEIGHT = 1300, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 60
grey = (125,125,125)
smiley_IMAGE = pygame.image.load(os.path.join("game3\images\smiley.png"))
smiley = pygame.transform.scale(smiley_IMAGE, (1568/3, 328))
fist = pygame.image.load(os.path.join("game3\images\yock.png"))
sprite_list = [smiley]

def draw_window(r):
    WIN.fill(grey)
    try:
        WIN.blit(sprite_list[0], (r.x,r.y))
    except:
        pass
    pygame.display.update()

def face_mov(key, r):
    if key[pygame.K_UP] and r.y>0:
        r.y -= 5
    elif key[pygame.K_DOWN] and r.y<HEIGHT-r.height:
        r.y += 5
    elif key[pygame.K_LEFT] and r.x>0:
        r.x -= 5
    elif key[pygame.K_RIGHT] and r.x<WIDTH-r.width:
        r.x += 5

def main():
    r_face = pygame.Rect(0,0,smiley.get_width(),smiley.get_height())
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    try:
                        sprite_list.pop(0)
                    except:
                        pass
                elif event.key==pygame.K_2 and len(sprite_list)==0:
                    sprite_list.append(smiley)
        
        keys_pressed = pygame.key.get_pressed()
        face_mov(keys_pressed, r_face)
        draw_window(r_face)
 
    pygame.quit()

if __name__ == "__main__":
    main()