# 1. 게임 초기화
pygame.init()

# 2. 게임 내 설정
clock = pygame.time.Clock()
k = 0

# rocket 이미지 생성 및 불러오기        
rocket = obj()         
rocket.load_img('rocket.png')
rocket.change_size(30,50)
# 이미지가 가로 중앙에 위치하도록 좌표 변경
rocket.x = size[0]//2 - rocket.sx//2
rocket.y = size[1] - rocket.sy - 15
rocket.move = 10 # 움직임, 속도 지정

# 미사일,외계인 생성리스트
m_list = []
a_list = []

# 키 동작 default 설정
left_key = right_key = space_key = up_key = down_key = False

# score 메시지
score = 0
heart = 3

# 4-0. 게임 시작 대기 화면
readyGame()

# 4. 메인 이벤트

start_time = datetime.now() # 시간 측정
Running = False
GO = False
while Running == False:

    # 4-1. FPS 설정
    clock.tick(60) # 1초에 60번

    # 4-2. 각종 입력 감지 

    for event in pygame.event.get(): # 여러버튼 동시 작동 가능하도록 반복문
        if event.type == pygame.QUIT:
            Running = True 
        if event.type == pygame.KEYDOWN: # 어떤 키가 눌렸는지
            if event.key == pygame.K_LEFT: # 눌린 키가 왼쪽 방향키면
                left_key = True # 좌표를 왼쪽으로
            elif event.key == pygame.K_RIGHT:
                right_key = True
            elif event.key == pygame.K_SPACE:
                space_key = True
                k = 0
                
            # 상하 이동도 추가
            elif event.key == pygame.K_UP: 
                up_key = True
            elif event.key == pygame.K_DOWN: 
                down_key = True            
                
        elif event.type == pygame.KEYUP: # 키를 뗐을 때의 동작
            if event.key == pygame.K_LEFT: 
                left_key = False 
            elif event.key == pygame.K_RIGHT:
                right_key = False
            elif event.key == pygame.K_SPACE:
                space_key = False
            elif event.key == pygame.K_UP:  
                up_key = False
            elif event.key == pygame.K_DOWN: 
                down_key = False   
                
    
    # 4-3. 입력, 시간에 따른 변화 
    now_time = datetime.now() # 시간 측정
    delta_time = int((now_time - start_time).total_seconds())
    if left_key == True:
        rocket.x -= rocket.move
        if rocket.x <= 0: # 창을 벗어나지 못하게 제한
            rocket.x = 0
    
    elif right_key == True:
        rocket.x += rocket.move
        if rocket.x >= size[0] - rocket.sx:
            rocket.x = size[0] - rocket.sx
            
    elif up_key == True:
        rocket.y -= rocket.move
        if rocket.y <= size[1]//3 * 2:
            rocket.y = size[1]//3 * 2
    elif down_key == True:
        rocket.y += rocket.move
        if rocket.y >= size[1] - rocket.sy - 15:
            rocket.y = size[1] - rocket.sy - 15
            
    # 미사일의 작동 : 입력(space) 발생 시 발사, 시간에 따라(while) 위로 이동   
    
    # 미사일 생성
    if space_key == True and k % 12 == 0: # k: 미사일 
        missile = obj() 
        missile.load_img('bullet.png')
        missile.change_size(10,15)
        # 위치 지정 (비행선 위에서 시작)
        missile.x = rocket.x +  missile.sx # 미사일 사이즈 반영
        missile.y = rocket.y - missile.sy # 미사일 사이즈 반영
        
        missile.move = 20 # 움직임, 속도 지정
        m_list.append(missile) # 여러개의 미사일 생성
    
    k += 1 # 미사일 생생 조건 관련
        
    # 미사일 이동
    d_list = []
    for m in m_list:
        m.y -= m.move # 위로 이동
        if m.y <= -m.sy: # 미사일이 화면 상단으로 사라지면
            d_list.append(m)
            
    for d in d_list:
        m_list.remove(d)
        
    # 외계인 발생
    if random.random() > 0.98:
        alien = obj() 
        alien.load_img('alien.png')
        alien.change_size(30,45)
        # 위치 지정 (비행선 위에서 시작)
        alien.x = random.randrange(0,size[0] - alien.sx - rocket.sx//2) # 외계인 사이즈 반영, 로켓 사이즈 반영(로켓의 중앙에서 미사일 발사)
        alien.y = 10 # 미사일 사이즈 반영
        alien.move = 1 # 움직임, 속도 지정
        a_list.append(alien) # 여러개의 외계인 생성
        
    # 외계인 이동
    d_list = []
    for a in a_list:
        a.y += a.move # 아래로 이동
        if a.y >= size[1]: # 화면에서 사라지면
            d_list.append(a)
    for d in d_list:
        a_list.remove(d)
        
    # 충돌 발생
    dm_list = []
    da_list = []
    for m in m_list:
        for a in a_list:
            if crash(m,a) == True:
                dm_list.append(m)
                da_list.append(a)
                score += 1
    dm_list = list(set(dm_list))
    da_list = list(set(da_list))
    
    for dm in dm_list:
        m_list.remove(dm)
    for da in da_list:
        a_list.remove(da)
        
    for alien in a_list:
        if crash(alien,rocket) == True: # 충돌
            Running = True
            GO = True
            
    # 4-4. 그리기
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    screen.blit(background2,(0,background_sy))
    rocket.show()
    for m in m_list:
        m.show()   
    for a in a_list:
        a.show()  
        
    font = pygame.font.Font('C:/Windows/Fonts/Arial.ttf', 20) # address, size
    text = font.render(f'score:{score} heart: {heart} time: {delta_time}',True,(255,255,255)) # text, anti-aliasing, RGB code
    screen.blit(text,(10,5))
    
    
    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료
gameOver()

pygame.quit()
