# 캐릭터 생성 클래스

class obj:
    def __init__(self):
        self.x = 0 
        self.y = 0 
        self.move = 0
    def load_img(self, address): 
        if address[-3:] == 'png':
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx,self.sy = self.img.get_size()
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx,self.sy = self.img.get_size() 
    def show(self):
        screen.blit(self.img,(self.x,self.y))
        
        
'''
init() : 초기 설정(좌표, 움직임)
load_img() : 이미지 로드, 이미지 사이즈 생성
change_size() : 이미지 사이즈 변경, 이미지 사이즈 업데이트
show() : 화면 표시, 좌표 지정
'''
