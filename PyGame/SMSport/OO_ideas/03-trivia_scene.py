class TriviaScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(None, 32)

        self.question = "Who is Bart's dad?"
        self.answers = ["A: Homer", "B: Ned", "C: Moe", "D: Barney"]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.answers)

            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.answers)

            elif event.key == pygame.K_RETURN:
                print("Selected:", self.answers[self.selected])

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        # Draw question
        q = self.font.render(self.question, True, (255, 255, 0))
        screen.blit(q, (50, 50))

        # Draw answers
        for i, answer in enumerate(self.answers):
            color = (0, 255, 0) if i == self.selected else (255, 255, 255)
            text = self.font.render(answer, True, color)
            screen.blit(text, (70, 120 + i * 40))