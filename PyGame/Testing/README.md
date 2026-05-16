Testing
16-May-2026

cd D:\GitHub\StevePro9\PythonSetup\PyGame
mkdir Testing

uv init --python 3.11
uv venv --python 3.11

.venv\Scripts\activate

https://github.com/Mekire/pygame-delta-time/blob/master/dt_example.py



Key Press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if actor_index > MIN_ACTOR_INDEX:
                        actor_index -= 1

                if event.key == pygame.K_RIGHT:
                    if actor_index < MAX_ACTOR_INDEX:
                        actor_index += 1