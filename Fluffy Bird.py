import pygame
import random

pygame.init()

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fluffy Bird")

clock = pygame.time.Clock()
FPS = 60

# Warna
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)  # Latar belakang langit
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

# Konstanta fisika dan game
GRAVITY = 0.5
JUMP_STRENGTH = -8
PIPE_SPEED = 3
PIPE_GAP = 130
PIPE_WIDTH = 70

# --------------------------------------
# Kelas Burung
# --------------------------------------
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.radius = 20
        self.vel = 0

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def jump(self):
        self.vel = JUMP_STRENGTH

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius)

# --------------------------------------
# Kelas Pipa
# --------------------------------------
class Pipe:
    def __init__(self, x):
        self.x = x
        # Tentukan tinggi pipa atas secara acak
        self.top_height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
        self.bottom_y = self.top_height + PIPE_GAP
        self.scored = False  # Untuk menandai apakah skor sudah ditambah

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surface):
        # Gambar pipa atas
        pygame.draw.rect(surface, GREEN, (self.x, 0, PIPE_WIDTH, self.top_height))
        # Gambar pipa bawah
        pygame.draw.rect(surface, GREEN, (self.x, self.bottom_y, PIPE_WIDTH, SCREEN_HEIGHT - self.bottom_y))

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird):
        # Rectangle untuk burung (approx. lingkaran)
        bird_rect = pygame.Rect(bird.x - bird.radius, bird.y - bird.radius,
                                bird.radius*2, bird.radius*2)
        # Rectangle pipa atas & bawah
        top_pipe_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        bottom_pipe_rect = pygame.Rect(self.x, self.bottom_y, PIPE_WIDTH, SCREEN_HEIGHT - self.bottom_y)

        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)

# --------------------------------------
# Fungsi utama game
# --------------------------------------
def main():
    bird = Bird()
    # Buat beberapa pipa awal
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(3)]
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(FPS)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Tekan spasi/atas untuk lompat
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    bird.jump()
            # Tap/click di layar untuk lompat (Pydroid sering kesulitan tangkap keyboard)
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump()

        # Update burung
        bird.update()

        # Update pipa dan cek tabrakan
        for pipe in pipes:
            pipe.update()
            # Cek tabrakan
            if pipe.collide(bird):
                running = False  # Game over
            # Cek skor (burung melewati pipa)
            if pipe.x + PIPE_WIDTH < bird.x and not pipe.scored:
                score += 1
                pipe.scored = True

        # Hapus pipa lama, tambah pipa baru
        if pipes and pipes[0].off_screen():
            pipes.pop(0)
            pipes.append(Pipe(SCREEN_WIDTH))

        # Jika burung jatuh ke tanah atau terbang di luar layar
        if bird.y - bird.radius > SCREEN_HEIGHT or bird.y + bird.radius < 0:
            running = False  # Game over

        # Gambar latar belakang
        screen.fill(BLUE)

        # Gambar pipa
        for pipe in pipes:
            pipe.draw(screen)

        # Gambar burung
        bird.draw(screen)

        # Gambar skor
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    # Ketika loop berhenti, kita hanya quit pygame tanpa sys.exit()
    pygame.quit()

if __name__ == "__main__":
    main()