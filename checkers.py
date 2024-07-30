import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load("C:\\Users\\nikit\\Downloads\\Checkers_data_game.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // COLS
# rgb
BLUE = (0, 0, 255)

REDKING=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\pics\\redking.png"),(45,45))
REDCHECKER=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\pics\\redchecker.png"),(80,80))
BLACKCHECKER=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\pics\\blackchecker.png"),(80,80))
BOARD=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\board.jpg"),(800,800))
MAIN = pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\main screen.jpg"),(800,800))
INSTRUCTIONS=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\instructions.jpg"),(800,800))
REDKING=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\pics\\redking.png"),(80,80))
BLACKKING=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\pics\\blackking.png"),(80,80))
WINSCREEN=pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\win screen.jpg"),(800,800))
BACK= pygame.transform.scale(pygame.image.load("C:\\Users\\nikit\\OneDrive\\Documents\\back screen.jpg"),(800,800))
FPS=60

turn_count = 0

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x,y=pos
    row=y//SQUARE_SIZE
    col=x//SQUARE_SIZE
    return row,col

def _winnerR():
    while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        WIN.blit(WINSCREEN,(0,0))
        font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",80)
        WON_TEXT = font.render("RED WON", True, "BLACK")
        WIN.blit(WON_TEXT,(150,240))

        WIN.blit(REDKING,(365,400))
        Winning_sound = mixer.Sound("C:\\Users\\nikit\\OneDrive\\Documents\\win sound.mp3")
        Winning_sound.play()
        MAIN_BUTTON = Button(image=None, pos=(250,570), 
                            text_input="BACK", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="BLACK", hovering_color="white")

        QUIT_BUTTON = Button(image=None, pos=(580, 570), 
                            text_input="QUIT", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="black", hovering_color="White")
        for button in [MAIN_BUTTON,  QUIT_BUTTON]:
            button.changeColor(WINNER_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_BUTTON.checkForInput(WINNER_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(WINNER_MOUSE_POS ):
                    pygame.quit()

        pygame.display.update()

def _winnerB():
    while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        WIN.blit(WINSCREEN,(0,0))
        font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",80)
        WON_TEXT = font.render("BLACK WON", True, "BLACK")
        WIN.blit(WON_TEXT, (150,240))

        WIN.blit(BLACKKING,(365,400))
        Winning_sound = mixer.Sound("C:\\Users\\nikit\\OneDrive\\Documents\\win sound.mp3")
        Winning_sound.play()
        MAIN_BUTTON = Button(image=None, pos=(250,570), 
                            text_input="BACK", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="BLACK", hovering_color="white")

        QUIT_BUTTON = Button(image=None, pos=(580, 570), 
                            text_input="QUIT", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="black", hovering_color="White")

        for button in [MAIN_BUTTON, QUIT_BUTTON]:
            button.changeColor(WINNER_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_BUTTON.checkForInput(WINNER_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(WINNER_MOUSE_POS ):
                    pygame.quit()

        pygame.display.update()

class Button():
	def _init_(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class Game:
    def _init_(self,win):
        self._init()
        self.win=win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
       self.selected=None
       self.board=Board()
       self.turn=REDCHECKER
       self.valid_moves={}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self,row,col):
        if self.selected:
            result=self._move(row,col)
            if not result:
                self.selected=None
                self.select(row,col)

        piece=self.board.get_piece(row,col)
        if piece != 0 and piece.color==self.turn:
            self.selected=piece
            self.valid_moves=self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self,row,col):
        piece=self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected,row,col)
            skipped=self.valid_moves[(row,col)]
            if skipped:
                Capture_sound = mixer.Sound("C:\\Users\\nikit\\OneDrive\\Documents\\capturing.mp3")
                Capture_sound.play()
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self,moves):
        for move in moves:
            row,col=move
            pygame.draw.circle(self.win,BLUE,(col * SQUARE_SIZE + SQUARE_SIZE//2,row * SQUARE_SIZE + SQUARE_SIZE//2),15)
        
    def change_turn(self):
        self.valid_moves={}
        if self.turn==REDCHECKER:
            self.turn=BLACKCHECKER
        else:
            self.turn=REDCHECKER

class Board:

    def _init_(self):
        self.board=[]
        self.red_left=self.black_left=12
        self.red_kings=self.black_kings=0
        self.create_board()
        
    def draw_squares(self,win):
        WIN.blit(BOARD, (0, 0))
        
    def move(self,piece,row,col):
        self.board[piece.row][piece.col],self.board[row][col]=self.board[row][col],self.board[piece.row][piece.col]
        Move_sound = mixer.Sound("C:\\Users\\nikit\\Downloads\\Checkers_data_CheckerMove.mp3")
        Move_sound.play()
        piece.move(row,col)

        if row==ROWS-1 or row==0:
            piece.make_king()
            if piece.color==BLACKCHECKER:
                self.black_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self,row,col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2==((row+1)%2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,BLACKCHECKER))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,REDCHECKER))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece=self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self,pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color==REDCHECKER:
                    self.red_left -=1
                else:
                    self.black_left -= 1

    def winner(self):
        if self.red_left <= 0:
            _winnerB()
        elif self.black_left <= 0:
            _winnerR()

        return None

    def get_valid_moves(self,piece):
        moves={}
        left=piece.col - 1
        right=piece.col + 1
        row=piece.row
        if piece.color==REDCHECKER:
            moves.update(self._traverse_left(row - 1,max(row-3,-1),-1,piece.color,left))
            moves.update(self._traverse_right(row - 1,max(row-3,-1),-1,piece.color,right))

        if piece.redking or piece.blackking:
            moves.update(self._traverse_left(row - 1,max(row-3,-1),-1,piece.color,left))
            moves.update(self._traverse_right(row - 1,max(row-3,-1),-1,piece.color,right))
            moves.update(self._traverse_left(row + 1,min(row+3,ROWS),1,piece.color,left))
            moves.update(self._traverse_right(row + 1,min(row+3,ROWS),1,piece.color,right))

        if piece.color==BLACKCHECKER:
            moves.update(self._traverse_left(row + 1,min(row+3,ROWS),1,piece.color,left))
            moves.update(self._traverse_right(row + 1,min(row+3,ROWS),1,piece.color,right))

        return moves

    def _traverse_left(self,start,stop,step,color,left,skipped=[]):
        moves={}
        last=[]
        for r in range(start,stop,step):
            if left<0:
                break

            current=self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break 
                elif skipped:
                    moves[(r,left)]=last + skipped
                else:
                    moves[(r,left)]=last

                if last:
                    if step == -1:
                        row=max(r-3,0)
                    else:
                        row=min(r+3,ROWS)
                    moves.update(self._traverse_left(r+step,row,step,color,left-1,skipped=last))
                    moves.update(self._traverse_right(r+step,row,step,color,left+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]

            left -= 1

        return moves

    def _traverse_right(self,start,stop,step,color,right,skipped=[]):
        moves={}
        last=[]
        for r in range(start,stop,step):
            if right>=COLS:
                break

            current=self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break 
                elif skipped:
                    moves[(r,right)]=last + skipped
                else:
                    moves[(r,right)]=last

                if last:
                    if step == -1:
                        row=max(r-3,0)
                    else:
                        row=min(r+3,ROWS)
                    moves.update(self._traverse_left(r+step,row,step,color,right-1,skipped=last))
                    moves.update(self._traverse_right(r+step,row,step,color,right+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]

            right += 1

        return moves

class Piece:
    PADDING=15
    OUTLINE=2
    def _init_(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.redking=False
        self.blackking=False
        self.x=0
        self.y=0
        self.calc_pos()

    def calc_pos(self):
        self.x=SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row+SQUARE_SIZE//2

    def make_king(self):
        if self.color==REDCHECKER:
            self.redking = True
        else:
            self.blackking = True

    def draw(self,win):
        win.blit(self.color,(self.x-self.color.get_width()//2,self.y-self.color.get_width()//2))
        if self.redking:
            win.blit(REDKING,(self.x-REDKING.get_width()//2,self.y-REDKING.get_height()//2))
        if self.blackking:
            win.blit(BLACKKING,(self.x-BLACKKING.get_width()//2,self.y-BLACKKING.get_height()//2))
        
    def move(self,row,col):
        self.row=row
        self.col=col
        self.calc_pos()

    def repr(self):
        return str(self.color)
def main():
    run=True
    clock=pygame.time.Clock()
    game=Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            break
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                back()

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col=get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()
            
    pygame.quit()

def back():
    while True:
        BACK_MOUSE_POS = pygame.mouse.get_pos()
        WIN.blit(BACK,(0,0))
        font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",28)
        GAME_TEXT = font.render("DO YOU WANT TO QUIT OR GO BACK", True, "BLACK")
        WIN.blit(GAME_TEXT, (90,255))

        MENU_BUTTON = Button(image=None, pos=(230,575), 
                            text_input="MENU", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="black", hovering_color="white")

        QUIT_BUTTON = Button(image=None, pos=(580, 575), 
                            text_input="QUIT", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="black", hovering_color="White")

        for button in [MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(BACK_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON .checkForInput(BACK_MOUSE_POS):
                   main_menu()
                if QUIT_BUTTON.checkForInput(BACK_MOUSE_POS):
                    pygame.quit()
                    exit()
    
        pygame.display.update()
          
def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()
        WIN.blit(INSTRUCTIONS,(0, 0))

        INSTRUCTIONS_BACK = Button(image=None, pos=(208,745), 
                            text_input="BACK", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="BLACK", hovering_color="white")
        PLAY_BUTTON = Button(image=None, pos=(582, 745), 
                            text_input="PLAY", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="black", hovering_color="White")
        
        for button in [PLAY_BUTTON, INSTRUCTIONS_BACK]:
            button.changeColor(INSTRUCTIONS_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()
                if PLAY_BUTTON.checkForInput(INSTRUCTIONS_MOUSE_POS ):
                    main()

        pygame.display.update()
    
def main_menu():
    while True:
        WIN.blit(MAIN, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",85)
        GAME_TEXT = font.render("CHECKERS", True, "black")
        WIN.blit(GAME_TEXT, (132,73.5))

        PLAY_BUTTON = Button(image=None, pos=(395, 315), 
                            text_input="PLAY", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="BLACK", hovering_color="White")
        INSTRUCTIONS_BUTTON = Button(image=None, pos=(396, 485), 
                            text_input="INSTRUCTIONS", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",39), base_color="BLACK", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(396,653), 
                            text_input="QUIT", font = pygame.font.Font("C:\\Users\\nikit\\Downloads\\menufont.ttf",45), base_color="BLACK", hovering_color="white")

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    exit()

        pygame.display.update()
        
main_menu()