import pygame
from utils.colors import Colors
from pages.page import Page

class Menu(Page):
    modebtn_radius = 10
    buttons_distance = 50
    base_qbr = qbr = 40
    rotate_title = 0.1
    rotate_bg = -0.1
    rotate = pygame.USEREVENT + 1
    base_modebtn_dim = modebtn_dim = modebtn1_dim = modebtn2_dim = (220, 140)
    
    def on_start(self:any)->None:
        pygame.time.set_timer(self.rotate, 500)

    def draw(self:any)->None:
        self.game.screen.fill(Colors.beige)

        title_fs = round(min(180, self.game.dim[0] / 5.147, self.game.dim[1] / 4.583))
        self.modebtn_dim = tuple([val*title_fs/120 for val in self.base_modebtn_dim])
        self.base_qbr = 40 * title_fs / 120
        self.buttons_distance = self.modebtn_dim[0] / 5
        title_padding_top = 30
        title = self.game.text_surface('ScribblAI', 'Ink Free', title_fs, Colors.purple)
        title_bg = self.game.text_surface('ScribblAI', 'Ink Free', title_fs, Colors.pink)
        title_x = self.game.dim[0] // 2 - title.get_width() // 2

        subtitle = self.game.text_surface('Bist du besser als die KI?', 'Ink Free', title_fs / 4, Colors.purple)
        subtitle_x = self.game.dim[0] // 2 - subtitle.get_width() // 2
        subtitle_y = title.get_height() + title_padding_top

        self.game.draw(subtitle, (subtitle_x, subtitle_y))
        self.game.draw(pygame.transform.rotate(title_bg, self.rotate_bg / 120 * title_fs), (title_x, title_padding_top + title_fs/12))
        self.game.draw(pygame.transform.rotate(title, self.rotate_title / 120 * title_fs), (title_x, title_padding_top))

        modebtn_y = self.game.dim[1]/2 - self.modebtn_dim[1]/2
        modebtn1_x = self.game.dim[0]/2 - self.modebtn_dim[0] - self.buttons_distance/2 + self.modebtn_dim[0]/2 - self.modebtn1_dim[0]/2
        modebtn1_y = modebtn_y + self.modebtn_dim[1]/2 - self.modebtn1_dim[1]/2
        self.modebtn1 = self.game.create_btn((modebtn1_x, modebtn1_y), self.modebtn1_dim, Colors.purple, self.modebtn_radius, 'Mehrspieler', 'Arial', title_fs / 4, Colors.salmon)
        
        modebtn2_x = self.game.dim[0]/2 + self.buttons_distance/2 + self.modebtn_dim[0]/2 - self.modebtn2_dim[0]/2
        modebtn2_y = modebtn_y + self.modebtn_dim[1]/2 - self.modebtn2_dim[1]/2
        self.modebtn2 = self.game.create_btn((modebtn2_x, modebtn2_y), self.modebtn2_dim, Colors.salmon, self.modebtn_radius, 'Sandkiste', 'Arial', title_fs / 4, Colors.purple)

        self.qbtn = pygame.Rect(self.game.dim[0] // 2 - self.qbr, self.game.dim[1] - (140 * title_fs / 120) - self.qbr, 2 * self.qbr, 2 * self.qbr)
        pygame.draw.circle(self.game.screen, Colors.pink, (self.qbtn.center), self.qbr)
        q_surface = self.game.text_surface('?', 'Arial', title_fs / 2, Colors.beige)
        self.game.draw(q_surface, (self.qbtn.center[0] - q_surface.get_width() // 2, self.qbtn.center[1] - q_surface.get_height() // 2))

        credits = self.game.text_surface('Ennio Binder 2024', 'Ink Free', title_fs / 6, Colors.purple)
        credits_x = self.game.dim[0] // 2 - credits.get_width() // 2
        self.game.draw(credits, (credits_x, self.game.dim[1] - credits.get_height() - 10))

    def event_check(self:any, event:pygame.event)->None:
        if event.type == self.rotate:
            self.rotate_title *= -1
            self.rotate_bg *= -1

        # Handle mouse clicks
        if self.modebtn1.collidepoint(self.mouse_pos):
            self.modebtn1_dim = tuple([val * 1.05 for val in self.modebtn_dim])
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.goto_page('Lobby')
        else:
            self.modebtn1_dim = self.modebtn_dim

        if self.modebtn2.collidepoint(self.mouse_pos):
            self.modebtn2_dim = tuple([val * 1.05 for val in self.modebtn_dim])
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.goto_page('Sandbox')
        else:
            self.modebtn2_dim = self.modebtn_dim

        if self.qbtn.collidepoint(self.mouse_pos):
            self.qbr = self.base_qbr * 1.1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.goto_page('Info')
        else:
            self.qbr = self.base_qbr
