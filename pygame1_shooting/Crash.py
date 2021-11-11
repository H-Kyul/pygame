# 충돌 감지 함수

def crash(a,b):         
    if (a.x - b.sx <= b.x) & (b.x <= a.x + a.sx):
        if (a.y - b.sy <= b.y) & (b.y <= a.y + a.sy):
            return True
        else:
            return False
    return False
