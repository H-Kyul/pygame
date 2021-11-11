# Game Over 설정

def gameOver():
    global GO
    
    while GO == True: 
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GO = False
                
        # display setting
        time.sleep(1)
        screen.fill((0,0,0))
        font = pygame.font.Font('C:/Windows/Fonts/Arial.ttf', 20)
        text = font.render(f'GAME OVER',True,(255,0,0))  
        screen.blit(text,(120,size[1]//2-20))
        pygame.display.flip() 
        
        
'''
종료 조건: QUIT 버튼(X) 입력
GO : GameOver 조건(게임 실행 중 충돌 발생 시, GO = True)
font : 텍스트 적용할 폰트, parameter : address, size
text : 텍스트, parameter : string, anti-aliasing, RGB code
screen.blit() : 화면 적용, text, 좌표 
pygame.display.flip() : 화면 업데이트
'''
