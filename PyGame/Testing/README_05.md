README 05
05-Jun-2026

NOT going to use scale!
but here was the code

DrawActor
        actorPosn: pygame.Vector2 = self.actorVect.copy()
        actorRect: pygame.Rect = self.actorRects[index]
        scale: float = 1.0

        if index == enums.ActorType.Lisa1.value or index == enums.ActorType.Lisa2.value:
            scale = 0.85
            actorPosn.y += 2 * const.FONT_SIZE

        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            actorPosn,
            actorRect,
            scale=scale)
