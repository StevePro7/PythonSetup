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




GameManger.cs
public interface IGameManager
{
	IBarManager BarManager { get; }
	IFooManager FooManager { get; }
	ILogger Logger { get; }
}


public class GameManager : IGameManager
{
	public GameManager
	(
		IBarManager barManager,
		IFooManager fooManager,		
		ILogger logger
	)
	{
		BarManager = barManager;
		FooManager = fooManager;
		Logger = logger;
	}

	public IBarManager BarManager { get; private set; }
	public IFooManager FooManager { get; private set; }
	public ILogger Logger { get; private set; }
}	



Program.cs
from an_game import AnGame


def main():
    game = AnGame()
    game.run()


if __name__ == "__main__":
    main()