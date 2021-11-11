# 대기화면, 입력(space key) 감지 전까지 화면 유지

def readyGame():
    k=0
    Pressed = False
    while Pressed == False:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Pressed = True
        if k % 10 == 0:
            screen.fill((0,0,0))
        else:
            screen.fill((0,0,0))
            font = pygame.font.Font('C:/Windows/Fonts/Arial.ttf', 20) # address, size 
            text = font.render(f'PRESS SPACE KEY TO START',True,(255,255,0)) # text, anti-aliasing, RGB code
            screen.blit(text,(30,size[1]//2))
        k+=1
        pygame.display.flip()
        
'''
k : 화면 대기 중 깜박임
'''
