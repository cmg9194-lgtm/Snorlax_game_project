import pygame, sys, random
from programming_quiz import *
from fade import Fade
from datetime import datetime
from item import ItemManager
WIDTH, HEIGHT = 1000, 700
WHITE, BLACK, GRAY = (255,255,255), (0,0,0), (70,70,70)
fade=Fade(WIDTH, HEIGHT,speed=8)
pygame.init()
pygame.key.start_text_input()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load("./menu_background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

classroom_background = pygame.image.load("./classroom.png").convert()
classroom_background = pygame.transform.scale(classroom_background, (WIDTH, HEIGHT))
ending_background=pygame.transform.scale(pygame.image.load("./ending_background.png").convert(),(WIDTH, HEIGHT))
snorlax_sleep2 = pygame.transform.scale(pygame.image.load("./snorlax_sleep2.png").convert_alpha(), (150,150))
snorlax_sleep3 = pygame.transform.scale(pygame.image.load("./snorlax_sleep3.png").convert_alpha(), (180,180))
snorlax_awake2 = pygame.transform.scale(pygame.image.load("./snorlax_awake2.png").convert_alpha(), (190,190))

player_image = pygame.transform.scale(pygame.image.load("./player.png").convert_alpha(), (80,80))
notebook_img = pygame.transform.scale(
    pygame.image.load("./notebook.png").convert_alpha(),
    (50,50)
)

item_manager = ItemManager()
button_font = pygame.font.SysFont(None, 50)
game_font = pygame.font.SysFont(None, 80)
korean_font = pygame.font.Font("./CookieRun Black.ttf", 30)
quiz_font = pygame.font.Font("./CookieRun Black.ttf", 23)
submit_font = pygame.font.Font("./CookieRun Black.ttf", 24)
small_font = pygame.font.Font("./CookieRun Black.ttf", 24)
code_font = pygame.font.SysFont("consolas", 26)

def draw_dotted_line(surface, color, start_pos, end_pos, radius=2, gap=14):
    x1, y1 = start_pos
    x2, y2 = end_pos
    for x in range(x1, x2, gap):
        pygame.draw.circle(surface, color, (x, y1), radius)
start_button = pygame.Rect(340,520,300,70)
quit_button = pygame.Rect(340,610,300,70)
easy_button = pygame.Rect(300,260,400,80)
normal_button = pygame.Rect(300,380,400,80)
end_button=pygame.Rect(420,520,160,60)

MENU, DIFFICULTY_SELECT, MODE_SELECT, START_SCREEN, PLAYING, GAME_OVER, RECAP_SCREEN, ENDING, ENDING_FADE = 0,1,2,3,4,5,6,7,8
game_state = MENU
selected_mode = None
current_question = None
selected_difficulty= None
time_limit=None
start_screen_init=False
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (70,70,70)

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,200,0)
YELLOW = (255,255,0)

player_x, player_y = 900, 500
player_speed = 4
base_player_speed=4

start_timer = 0
game_start_time=0

snorlax_state = "sleep"
snorlax_timer = pygame.time.get_ticks()
snorlax_change_time = random.randint(14000,18000)

animation_timer = 0
animation_index = 0

seat_positions = [

    ("A1",(110,240)),
    ("A2",(265,240)),
    ("A3",(425,240)),
    ("A4",(585,240)),
    ("A5",(745,240)),

    ("B1",(110,340)),
    ("B2",(265,340)),
    ("B3",(425,340)),
    ("B4",(585,340)),
    ("B5",(745,340)),

    ("C1",(110,440)),
    ("C2",(265,440)),
    ("C3",(425,440)),
    ("C4",(585,440)),
    ("C5",(745,440))
]

target_seat = random.choice(seat_positions)

mission_clear = False

mission2 = False
mission2_clear = False

mission3 = False
mission3_clear = False

mission4 = False
mission4_clear = False

recap_popup = False
recap_text=""
RECAP_SCREEN=5
recap_start_time=0

input_active = False

mission1_clear_time = 0
coding_popup_open_time=0

question_popup = False
coding_popup = False
answer1_button = pygame.Rect(220,350,250,60)
answer2_button = pygame.Rect(530,350,250,60)
midterm_button = pygame.Rect(250,250,500,80)
final_button = pygame.Rect(250,470,500,80)
quiz_a_button = pygame.Rect(220,470,250,60)
quiz_b_button = pygame.Rect(530,470,250,60)
save_button = pygame.Rect(740,520,80,40)

ending_fade_alpha=0
ending_fade_phase="out"
running = True

while running:

    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if question_popup and event.type == pygame.MOUSEBUTTONDOWN:
            if answer1_button.collidepoint(event.pos):
                question_popup = False
                coding_popup=False
                input_active=False
                mission2_clear = True
                mission3 = True
                fade.start(fade_in=True)
                continue

            elif answer2_button.collidepoint(event.pos):
                game_state = GAME_OVER
                fade.update
                continue
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())

        if game_state == MENU and event.type == pygame.MOUSEBUTTONDOWN:

            if start_button.collidepoint(event.pos):
                game_state = DIFFICULTY_SELECT

            if quit_button.collidepoint(event.pos):
                running = False
        if game_state == DIFFICULTY_SELECT and event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button.collidepoint(event.pos):
                selected_difficulty = "easy"
                time_limit = None
                base_player_speed=6
                player_speed=base_player_speed
                game_state = MODE_SELECT
                snorlax_change_time=30000
                mission_clear = False
                mission2 = False
                mission2_clear = False
                mission3 = False
                mission3_clear = False
                item_manager.reset()
                start_timer=pygame.time.get_ticks()
            elif normal_button.collidepoint(event.pos):
                selected_difficulty = "normal"
                time_limit = 77
                base_player_speed = 3
                player_speed=base_player_speed
                game_state = MODE_SELECT
                snorlax_change_time = random.randint(14000,18000)
                mission_clear = False
                mission2 = False
                mission2_clear = False
                mission3 = False
                mission3_clear = False
                item_manager.reset()
                start_timer=pygame.time.get_ticks()

        if game_state == MODE_SELECT and event.type == pygame.MOUSEBUTTONDOWN:

            if midterm_button.collidepoint(event.pos):
                selected_mode = "midterm"
                current_question = random.choice(midterm_questions)

                game_state = START_SCREEN
                start_screen_init=False
                start_timer = pygame.time.get_ticks()
                fade.start(fade_in=True)

            elif final_button.collidepoint(event.pos):
                selected_mode = "final"
                current_question = random.choice(final_questions)
                game_state = START_SCREEN
                start_screen_init=False
                start_timer = pygame.time.get_ticks()
                fade.start(fade_in=True)
        if  game_state == PLAYING and mission3 and not mission3_clear and coding_popup and event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.time.get_ticks()-coding_popup_open_time < 500:
                continue
            if quiz_a_button.collidepoint(event.pos):

                if current_question["answer"] == 0:
                    coding_popup = False
                    question_popup = False
                    mission3_clear = True
                    game_state = RECAP_SCREEN
                    input_active=True
                    continue
                else:
                    game_state = GAME_OVER
                    continue

            elif quiz_b_button.collidepoint(event.pos):

                if current_question["answer"] == 1:
                    coding_popup = False
                    question_popup = False
                    mission3_clear = True
                    game_state = RECAP_SCREEN
                    input_active=True
                    continue
                else:
                    game_state = GAME_OVER
                    continue
        if game_state == RECAP_SCREEN:
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                 input_rect=pygame.Rect(150,250,700,200)
                 input_active=input_rect.collidepoint(event.pos)
                 if save_button.collidepoint(event.pos):
                    with open("recap.txt","w",encoding="utf-8") as f:
                        today=datetime.now().strftime("%Y년 %m월 %d일")
                        f.write(f"학습일: {today}\n")
                        f.write(("=" * 30) + "\n")
                        f.write(recap_text)
                    mission4_clear=True
                    ending_fade_alpha=0
                    ending_fade_phase="out"
                    game_state=ENDING_FADE
            if input_active:
                if event.type == pygame.TEXTINPUT:
                    recap_text += event.text
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        recap_text = recap_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        recap_text += "\n"
        if game_state == ENDING and event.type==pygame.MOUSEBUTTONDOWN:
            if end_button.collidepoint(event.pos):
                running=False
                   
    if game_state == MENU: #GAME START/QUIT

        screen.blit(background, (0,0))

        start_color = (120,120,120) if start_button.collidepoint(mouse_pos) else GRAY
        quit_color = (120,120,120) if quit_button.collidepoint(mouse_pos) else GRAY

        pygame.draw.rect(screen, start_color, start_button, border_radius=15)
        pygame.draw.rect(screen, quit_color, quit_button, border_radius=15)

        start_text = button_font.render("GAME START!", True, WHITE)
        quit_text = button_font.render("QUIT", True, WHITE)

        screen.blit(start_text, (375,540))
        screen.blit(quit_text, (445,630))
    elif game_state == DIFFICULTY_SELECT: 
        screen.blit(background, (0,0))
        title= korean_font.render("난이도를 선택하세요!", True, BLACK)
        screen.blit(title,(360,150))
        pygame.draw.rect(screen,GRAY,easy_button,border_radius=15)
        pygame.draw.rect(screen,GRAY,normal_button,border_radius=15)
        easy_text = korean_font.render("  easy", True, WHITE)
        normal_text = korean_font.render("  normal", True, WHITE)
        screen.blit(easy_text,(450,285))
        screen.blit(normal_text,(420,405))
    
    elif game_state == MODE_SELECT:

        screen.blit(background,(0,0))
        yellow = pygame.Surface((WIDTH,HEIGHT))
        yellow.set_alpha(100)
        yellow.fill(YELLOW)

        screen.blit(yellow,(0,0))

        title = korean_font.render("플레이어의 시험 범위를 선택하세요!",True,BLACK)

        screen.blit(title,(330,150))

        pygame.draw.rect(screen,GRAY,midterm_button,border_radius=15)

        pygame.draw.rect(screen,GRAY,final_button,border_radius=15)
    

        mid_text = korean_font.render("  중간고사 VER.",True,WHITE)

        final_text = korean_font.render("  기말고사 VER.",True,WHITE)

        screen.blit(mid_text,(380,275))
        screen.blit(final_text,(380,495))
       
    elif game_state == START_SCREEN: #START

        screen.blit(background, (0,0))

        dark = pygame.Surface((WIDTH, HEIGHT))
        dark.set_alpha(120)
        dark.fill((0,0,0))
        screen.blit(dark, (0,0))

        game_text = game_font.render("GAME START!", True, WHITE)
        screen.blit(game_text, (250,300))
        if not start_screen_init:
            start_timer = pygame.time.get_ticks()
            start_screen_init=True

        if start_screen_init and pygame.time.get_ticks() - start_timer >= 1000:
            game_state = PLAYING
            game_start_time=pygame.time.get_ticks()
            fade.start(fade_in=True)
    elif game_state == PLAYING:

        screen.blit(classroom_background, (0,0))
        
        for seat_name, seat_pos in seat_positions:

            pygame.draw.circle(
                screen,
                (255,0,0),
                seat_pos,
                8
            )

            text = korean_font.render(
                seat_name,
                True,
                (255,0,0)
            )

            screen.blit(
                text,
                (seat_pos[0] + 10, seat_pos[1] - 10)
            )
        for seat_name, seat_pos in seat_positions:

            pygame.draw.rect(
                screen,
                (255,0,0),
                (
                    seat_pos[0],
                    seat_pos[1],
                    140,
                    95
                ),
                3
            )
        current_time = pygame.time.get_ticks()

        if current_time - snorlax_timer >= snorlax_change_time:

            if snorlax_state == "sleep":
                snorlax_state = "awake"
                snorlax_change_time = 2000

            else:
                snorlax_state = "sleep"
                if selected_difficulty == "easy":
                    snorlax_change_time = 30000
                else:
                    snorlax_change_time = random.randint(14000,18000)

            snorlax_timer = current_time

        if current_time - animation_timer >= 300:
            animation_timer = current_time
            animation_index += 1

        if snorlax_state == "sleep":

            sleep_frames = [snorlax_sleep2, snorlax_sleep3]
            current_frame = sleep_frames[animation_index % len(sleep_frames)]

        else:
            current_frame = snorlax_awake2
        if selected_difficulty == "normal" and time_limit is not None:
            elapsed=(pygame.time.get_ticks()-game_start_time)//1000
            remain=time_limit-elapsed
            timer_text=korean_font.render(f"남은 시간: {remain} sec",True,BLACK)
            screen.blit(timer_text,(WIDTH-timer_text.get_width()-20,20))
            if remain <= 0:
                game_state=GAME_OVER
        keys = pygame.key.get_pressed()
        player_moving = False

        if keys[pygame.K_a]:
            player_x -= player_speed
            player_moving = True

        if keys[pygame.K_d]:
            player_x += player_speed
            player_moving = True

        if keys[pygame.K_w]:
            player_y -= player_speed
            player_moving = True

        if keys[pygame.K_s]:
            player_y += player_speed
            player_moving = True
        player_rect = pygame.Rect(player_x, player_y, 80, 80)
        player_speed=item_manager.update(player_rect, base_player_speed,pygame.time.get_ticks())
        if snorlax_state == "awake" and player_moving and not item_manager.is_invisible():
            game_state = GAME_OVER

        
        screen.blit(current_frame, (210,45))

        item_manager.draw(screen)
        if item_manager.is_invisible():
            transparent_player = player_image.copy()
            transparent_player.set_alpha(100)
            screen.blit(transparent_player, (player_x, player_y))
        else:
            screen.blit(player_image, (player_x, player_y))

        if snorlax_state == "sleep":

            state_text = button_font.render("Zzz...", True, WHITE)

        else:

            state_text = button_font.render("AWAKE!!", True, (255,0,0))

        screen.blit(state_text, (240,150))

        target_rect = pygame.Rect(
            target_seat[1][0],
            target_seat[1][1],
            20,
            20
        )
        

        if player_rect.colliderect(target_rect) and not mission_clear:
            mission_clear = True
            mission1_clear_time = pygame.time.get_ticks()
            question_popup=False
            coding_popup=False
            input_active=False
        if mission_clear and not mission2:
            if pygame.time.get_ticks() - mission1_clear_time >= 1000:
                fade.start(fade_in=True)
                mission2 = True
        if not mission_clear:

            mission_text = korean_font.render(
                f"Mission 1 : {target_seat[0]}에 앉기",
                True,
                BLACK
            )

            screen.blit(mission_text, (600,90))
        
        elif mission2 and not mission2_clear:

            mission_text = korean_font.render(
                "Mission: 교수님께 과제 제출하기",
                True,
                BLACK   
            )

            screen.blit(mission_text, (450,90))
            screen.blit(
                notebook_img,
                (player_x + 35, player_y + 35)
            )
            question_rect = pygame.Rect(280,175,60,50)
            player_center = (player_x + 40, player_y + 40)

            if question_rect.collidepoint(player_center) and not mission2_clear:
                question_popup = True
           
            
        if question_popup:

            dark = pygame.Surface((WIDTH, HEIGHT))
            dark.set_alpha(180)
            dark.fill((150,150,150))
            screen.blit(dark, (0,0))

            popup_rect = pygame.Rect(180,120,640,400)

            pygame.draw.rect(
                screen,
                WHITE,
                popup_rect,
                border_radius=20
            )
            answer1_button = pygame.Rect(220,350,250,60)
            answer2_button = pygame.Rect(530,350,250,60)
            pygame.draw.rect(
                screen,
                (220,220,220),
                answer1_button,
                border_radius=10
            )
            pygame.draw.rect(
                screen,
                (220,220,220),
                answer2_button,
                border_radius=10
            )
            a_text = korean_font.render( 
                "          (A)",
                True,
                RED
            )

            b_text = korean_font.render(
                "          (B)",
                True,
                RED
            )
            screen.blit(a_text, (answer1_button.x + 18, answer1_button.y + 10))
            screen.blit(b_text, (answer2_button.x + 18, answer2_button.y + 10))
            
            question_text1 = korean_font.render(
                "   과제를 해내느라 고생이 많았구나.",
                True,
                BLACK
            )
            question_text2 = korean_font.render(
                "   이 과제는 자네에게 유익했는가?",
                True,
                BLACK
            )
            screen.blit(question_text1,(250,200))
            screen.blit(question_text2,(250,250))
            
            answer_text1_1= korean_font.render(
                "많은 것을 배우고",
                True,
                BLUE
            )
            answer_text1_2= korean_font.render(
                "성장할 수 있었습니다!",
                True,
                BLUE
            )
            answer_text2_1 = korean_font.render(
                "끔찍했습니다.",
                True,
                BLUE
            )
            answer_text2_2 = korean_font.render(
                "하기 싫었어요.",
                True,
                BLUE
            )
            screen.blit(answer_text1_1, (240,415))
            screen.blit(answer_text1_2, (240,455))
            screen.blit(answer_text2_1, (550,415))
            screen.blit(answer_text2_2, (550,455))
        elif mission3 and mission2_clear and not mission3_clear and not coding_popup:
            mission_text = korean_font.render("Mission: 자리로 돌아가 문제를 푸세요",True,BLACK)

            screen.blit(mission_text, (350,90))
            player_center = (player_x + 40,player_y + 40)

            mission3_rect = pygame.Rect(target_seat[1][0],target_seat[1][1],20,20)
            if player_rect.colliderect(mission3_rect):
                coding_popup = True
                coding_popup_open_time=pygame.time.get_ticks()
                
        if mission3 and not mission3_clear and coding_popup:

            dark = pygame.Surface((WIDTH, HEIGHT))
            dark.set_alpha(180)
            dark.fill((150,150,150))
            screen.blit(dark, (0,0))

            popup_rect = pygame.Rect(120,80,760,500)

            pygame.draw.rect(screen,WHITE,popup_rect,border_radius=20)
            title_text = korean_font.render("잠만보: 얼마 남지 않았어. 문제를 풀어라.", True, BLACK)
            unit_text = korean_font.render(f"단원 : {current_question['unit']}", True, BLUE)

            screen.blit(title_text, (250,120))
            screen.blit(unit_text, (250,180))
            question_lines = current_question["question"].split("\n")
            y=250
            for line in question_lines:
                if line.strip() != "":
                    line_surface= korean_font.render(line, True, BLACK)
                    screen.blit(line_surface, (200,y))
                    y += 35
            choice_a = quiz_font.render(current_question["choices"][0], True, BLUE)
            choice_b = quiz_font.render(current_question["choices"][1], True, BLUE)

            choice_a_rect = choice_a.get_rect(center=quiz_a_button.center)
            choice_b_rect = choice_b.get_rect(center=quiz_b_button.center)

            screen.blit(choice_a, choice_a_rect)
            screen.blit(choice_b, choice_b_rect)
        
    elif game_state == RECAP_SCREEN:
        dark = pygame.Surface((WIDTH, HEIGHT))
        dark.set_alpha(180)
        dark.fill((150,150,150))
        screen.blit(dark, (0,0))

        popup_rect = pygame.Rect(100,100,800,500)

        pygame.draw.rect(screen,WHITE,popup_rect,border_radius=20)

        title_text = korean_font.render("프로그래밍 문제에서 배운 점을 입력하세요.", True, BLACK)
        screen.blit(title_text,(150,150))

        input_rect = pygame.Rect(150,250,700,200)
        pygame.draw.rect(screen,(220,220,220),input_rect,border_radius=10)
        pygame.draw.rect(screen,BLUE if input_active else BLACK,input_rect,2,border_radius=10)
        lines=recap_text.split("\n")
        y=10
        for line in lines:
            text_surface = korean_font.render(line, True, BLACK)
            screen.blit(text_surface, (input_rect.x + 10, input_rect.y + y))
            y += 35
        pygame.draw.rect(screen,GRAY,save_button,border_radius=10)
        save_text = submit_font.render(" 제출", True, WHITE)
        save_text_rect = save_text.get_rect(center=save_button.center)
        screen.blit(save_text, save_text_rect)
    elif game_state == ENDING_FADE:
        if ending_fade_phase=="out":
            screen.fill(BLACK)
            ending_fade_alpha+=2
            if ending_fade_alpha>=255:
                ending_fade_alpha=255
                ending_fade_phase="in"
        elif ending_fade_phase=="in":
            screen.blit(ending_background,(0,0))
            ending_fade_alpha-=2
            if ending_fade_alpha<=0:
                ending_fade_alpha=0
                game_state=ENDING
        fade_surface=pygame.Surface((WIDTH,HEIGHT))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(ending_fade_alpha)
        screen.blit(fade_surface,(0,0))
    elif game_state==ENDING:
        screen.blit(ending_background,(0,0))
        pygame.draw.rect(screen,BLACK,end_button,border_radius=15)
        end_text=button_font.render("END",True,WHITE)
        text_rect=end_text.get_rect(center=end_button.center)
        screen.blit(end_text,text_rect)
    elif game_state == GAME_OVER:

        screen.fill(WHITE)

        over_text = game_font.render("GAME OVER", True, (255,0,0))
        screen.blit(over_text, (280,300))
    
    fade.update(screen)
    pygame.display.update()
pygame.quit()
sys.exit()