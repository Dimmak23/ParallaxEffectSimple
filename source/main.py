import os
from consts.consts import *
import pygame


def load_images() -> list:
    
    result: list = []
    
    for index in range(1, 6):
        image = pygame.image.load(f"assets/background_0{index}.png").convert_alpha()
        result.append(image)
    
    return result

#? blit to screen list of images
def draw_images(images: list, surface: pygame.Surface, width: int, scroll: int) -> None:
    
    for slide in range(0, SLIDES_COUNT - 1):
        for image in images:
            speed = LAYERS_SPEEDS[images.index(image)]
            surface.blit(image, ((slide * width) - scroll *  speed, 0))

def draw_image(image: pygame.Surface, surface: pygame.Surface, size: dict, scroll: int, speed: float) -> None:
    
	for slide in range(0, (SURFACES_COUNT - 1)):
		surface.blit(image, ((slide * size["width"]) - scroll *  speed, SCREEN_HEIGHT - size["height"]))


if __name__ == "__main__":
    
    #?  Clean this pygame message
    os.system("CLS")
    
    #? initialize here
    pygame.init()
    
    #? clock variable
    clock = pygame.time.Clock()
    
    #? get screen to render
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.set_caption(NAME)
    
    #? prepare images
    backgroundImages: list = load_images()
    
    #? now set surface to walk on
    surfaceImage = pygame.image.load("assets/surface.png").convert_alpha()
    surfaceSize: dict = {"width": surfaceImage.get_width(), "height": surfaceImage.get_height()}
    
    #? scroll position
    scroll: int = 0
    
    #? essential const, background image width
    SLIDE_WIDTH: int = backgroundImages[0].get_width()

    #? run game
    isRunning: bool = True
    
    while isRunning:
        
        #? set tick
        clock.tick(FPS)
        
        #? render
        draw_images(backgroundImages, screen, SLIDE_WIDTH, scroll)
        draw_image(surfaceImage, screen, surfaceSize, scroll, LAYERS_SPEEDS[4]+0.5)
        
        #? keyboard handler
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and scroll > 0:
            scroll -= 5
        if key[pygame.K_RIGHT] and scroll < ((SLIDES_COUNT - 2) * SLIDE_WIDTH - (SCREEN_WIDTH - SLIDE_WIDTH)):
            scroll += 5
        
        #? event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isRunning = False
        
        #? show
        pygame.display.update()
        
    #? release resources
    pygame.quit()
