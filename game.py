import sdl3
import ctypes

def run():
    # 1. Init
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO):
        print(f"Error: {sdl3.SDL_GetError().decode()}")
        return

    # 2. Create Window and Renderer (Raw SDL3 style)
    window = sdl3.SDL_CreateWindow(b"STREMA - Zander the Liar", 1280, 720, 0)
    renderer = sdl3.SDL_CreateRenderer(window, None)
    test = sdl3.IMG_Load(b"c.png")
    texture = sdl3.SDL_CreateTextureFromSurface(renderer, test)
    sdl3.SDL_DestroySurface(test)
    tex_w = ctypes.c_float()
    tex_h = ctypes.c_float()
    sdl3.SDL_GetTextureSize(texture, ctypes.byref(tex_w), ctypes.byref(tex_h))
    hunger_mass = 1.0
    running = True
    event = sdl3.SDL_Event()
    rect = sdl3.SDL_FRect(100, 100, 200, 100)
  
    
    sdl3.SDL_SetRenderDrawColor(renderer, 200, 0, 0, 255)
    
    sdl3.SDL_RenderFillRect(renderer, rect)
    
    


    while running:
        # 3. Poll Events
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl3.SDL_EVENT_QUIT:
                running = False
            
            if event.type == sdl3.SDL_EVENT_KEY_DOWN:
                if event.key.key == sdl3.SDLK_M: # Munch
                    hunger_mass += 0.15
                    sdl3.SDL_RenderLine(renderer, 10.23 * hunger_mass, 30.4 * hunger_mass, 22.4 * hunger_mass, 300.4 * hunger_mass)

                    print(f"MUNCH: Hunger Mass now {hunger_mass:.2f}")
                if event.key.key == sdl3.SDL_ClickTrayEntry
      
        draw_w = int(tex_w.value * hunger_mass)
        draw_h = int(tex_h.value * hunger_mass)

        dst_rect = sdl3.SDL_FRect(
            (1280 - draw_w) / 2,
            (720 - draw_h) / 2, 
            float(draw_w),
            float(draw_h)
        )
        # 4. The Void
        points = sdl3.LP_SDL_FPoint(sdl3.SDL_FPoint(draw_h, draw_w))
        sdl3.SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255)
        sdl3.SDL_RenderLines(renderer, points, 30)
        sdl3.SDL_RenderRect(renderer, rect)
        sdl3.SDL_RenderPresent(renderer)
    
        


        # Draw logic will go here
        
        sdl3.SDL_RenderPresent(renderer)
    
    sdl3.SDL_DestroyRenderer(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()

if __name__ == "__main__":
    run()