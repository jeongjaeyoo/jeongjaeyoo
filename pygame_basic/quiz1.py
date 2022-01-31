from random import randint
import pygame


# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정 
screen_width = 480 # 가로 크기 
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정 
pygame.display.set_caption("JEONGJAE GAME") #게임 이름 

# FPS 
clock = pygame.time.Clock()


# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지(캐릭터), 좌표, 폰트 등 설정)
background = pygame.image.load("C:/Users/wjdwo/OneDrive/바탕 화면/Python/pygame_basic/background.png")

character = pygame.image.load("C:/Users/wjdwo/OneDrive/바탕 화면/Python/pygame_basic/character.png")
character_size =  character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width/2) 
character_y_pos = screen_height - character_height

to_x = 0


# 이동 속도 (5 millisecond는 너무 큼)
character_speed = 10

# 적 enemy 캐릭터 

enemy = pygame.image.load("C:/Users/wjdwo/OneDrive/바탕 화면/Python/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴 
enemy_width = enemy_size[0] # 캐릭터의 가로 크기 
enemy_height = enemy_size[1] # 캐릭터의 세로 크기 
enemy_x_pos = randint(0, int(screen_width) - enemy_width)  # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터를 위치시킴 (가로 위치)
enemy_y_pos = 0 # 화면 세로 크기 가장 아래에  해당하는 곳에 위치 (세로 위치)

running = True  
while running:

    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정 


    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 그렇다면 창이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인 
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로 
                to_x += character_speed 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x 
    
    
    enemy_y_pos += 0.3 * dt

    # 가로 경계값 처리 (세로 경계값은 할 필요 없음; 어차피 세로로 안 움직임 )
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    
    # 똥 그림 출력 처리 
    if enemy_y_pos > screen_height:
        enemy_x_pos = randint(0, int(screen_width) - enemy_width)
        enemy_y_pos = 0
        



    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기   

    screen.blit(background, (0,0))

    screen.blit(character,(character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    
    pygame.display.update() # 게임화면을 계속 그리기

pygame.quit()