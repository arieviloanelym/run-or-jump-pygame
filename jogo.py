import pygame
import sys

# Inicialização
pygame.init()
pygame.mixer.init()

LARGURA, ALTURA = 800, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Run or Jump - DEMO")
CLOCK = pygame.time.Clock()

# Cores
BRANCO, PRETO, VERMELHO, LARANJA, AZUL = (255, 255, 255), (0, 0, 0), (255, 0, 0), (255, 165, 0), (0, 100, 255)

# Variáveis Globais
score = 0
start_t = 0
status = "MENU"
musica_on = True

# Carregamento de Áudio
try:
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)
except: 
    pass

# Carregamento de Fundo
try:
    fundo = pygame.image.load("fundo.png").convert()
except:
    try: 
        fundo = pygame.image.load("fundo.jpg").convert()
    except: 
        fundo = pygame.Surface((LARGURA, ALTURA))
        fundo.fill((135, 206, 235))
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        try:
            sheet = pygame.image.load("sprite_jogador.png").convert_alpha()
            w, h = 168, sheet.get_height() // 2
            for r in range(2):
                for c in range(5):
                    img = sheet.subsurface((c*w, r*h, w-2, h))
                    self.frames.append(pygame.transform.scale(img, (80, 120)))
        except:
            img = pygame.Surface((80, 120)); img.fill(AZUL)
            self.frames.append(img)
        self.idx, self.count = 0, 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(50, ALTURA-120))
        self.mask = pygame.mask.from_surface(self.image)
        self.vel_y, self.grav, self.no_chao = 0, 0.8, True

    def update(self):
        self.vel_y += self.grav
        self.rect.y += self.vel_y
        if self.rect.y >= ALTURA - 120:
            self.rect.y, self.no_chao, self.vel_y = ALTURA-120, True, 0
        if self.no_chao:
            self.count += 1
            if self.count >= 5:
                self.count, self.idx = 0, (self.idx + 1) % len(self.frames)
                self.image = self.frames[self.idx]
        else: 
            self.image = self.frames[0]

class BolaFogo(pygame.sprite.Sprite):
    def __init__(self, v):
        super().__init__()
        try:
            img = pygame.image.load("bola_fogo.png").convert_alpha()
            self.image = pygame.transform.scale(img, (60, 60))
        except:
            self.image = pygame.Surface((50,50), pygame.SRCALPHA)
            pygame.draw.circle(self.image, LARANJA, (25, 25), 25)
        self.rect = self.image.get_rect(topleft=(LARGURA, ALTURA-80))
        self.mask = pygame.mask.from_surface(self.image)
        self.v = v
    def update(self):
        self.rect.x -= self.v
        if self.rect.x < -100: self.kill()

# Grupos e Funções
player = Jogador()
sprites = pygame.sprite.Group(player)
obs_group = pygame.sprite.Group()

def reiniciar():
    global player, sprites, obs_group, status, score, start_t
    player = Jogador()
    sprites = pygame.sprite.Group(player)
    obs_group = pygame.sprite.Group()
    status = "JOGANDO"
    score = 0
    start_t = pygame.time.get_ticks()

pygame.time.set_timer(pygame.USEREVENT+1, 1500)
f_m = pygame.font.SysFont("arial", 22)
f_g = pygame.font.SysFont("arial", 60, bold=True)

# Loop Principal
while True:
    v_jogo = 8 + (score // 10) * 2
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_m:
                musica_on = not musica_on
                pygame.mixer.music.pause() if not musica_on else pygame.mixer.music.unpause()
            if e.key == pygame.K_SPACE:
                if status != "JOGANDO": 
                    reiniciar()
                else: 
                    if player.no_chao:
                        player.vel_y = -16
                        player.no_chao = False
        if e.type == pygame.USEREVENT+1 and status == "JOGANDO":
            b = BolaFogo(v_jogo)
            sprites.add(b)
            obs_group.add(b)

    TELA.blit(fundo, (0,0))
    
    if status == "JOGANDO":
        sprites.update()
        score = (pygame.time.get_ticks() - start_t) // 1000
        
        # DEMO reduzida para 30 segundos
        if score >= 30: 
            status = "VITORIA"
        
        if pygame.sprite.spritecollide(player, obs_group, False, pygame.sprite.collide_mask):
            status = "GAMEOVER"
            
        sprites.draw(TELA)
        txt = f_m.render(f"Score: {score}s | Speed: {v_jogo}", True, PRETO)
        TELA.blit(txt, (15, 15))
        
    elif status == "MENU":
        t1 = f_g.render("RUN OR JUMP", True, PRETO)
        t2 = f_m.render("SPACE to Start Demo | M to Mute", True, PRETO)
        t3 = f_m.render("Developer: Mylena Oliveira", True, PRETO)
        TELA.blit(t1, (LARGURA//2-t1.get_width()//2, 120))
        TELA.blit(t2, (LARGURA//2-t2.get_width()//2, 210))
        TELA.blit(t3, (LARGURA//2-t3.get_width()//2, 250))
        
    elif status == "VITORIA":
        t1 = f_g.render("DEMO COMPLETA", True, (0, 120, 0))
        t2 = f_m.render(f"Você sobreviveu os {score}s da Demo!", True, PRETO)
        t3 = f_m.render("Pressione ESPAÇO para jogar novamente", True, PRETO)
        TELA.blit(t1, (LARGURA//2-t1.get_width()//2, 100))
        TELA.blit(t2, (LARGURA//2-t2.get_width()//2, 180))
        TELA.blit(t3, (LARGURA//2-t3.get_width()//2, 250))
        
    elif status == "GAMEOVER":
        t1 = f_g.render("GAME OVER", True, VERMELHO)
        t2 = f_m.render(f"Sobreviveu por: {score}s", True, PRETO)
        t3 = f_m.render("Pressione ESPAÇO para tentar de novo", True, PRETO)
        TELA.blit(t1, (LARGURA//2-t1.get_width()//2, 100))
        TELA.blit(t2, (LARGURA//2-t2.get_width()//2, 180))
        TELA.blit(t3, (LARGURA//2-t3.get_width()//2, 250))

    pygame.display.flip()
    CLOCK.tick(60)