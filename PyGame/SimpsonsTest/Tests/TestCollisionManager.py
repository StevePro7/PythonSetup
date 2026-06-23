from Game.Static import Enumerations as enums

def test_collisions(collisionManager):
    collisionManager.LoadContent()

    fullScreen: bool = collisionManager.FullScreen(560, 20)
    assert fullScreen is True

    cheatMode: bool = collisionManager.CheatMode(430, 260)
    assert cheatMode is True

    character: bool = collisionManager.Character(400, 160)
    assert character is True

    volumeIcon: bool = collisionManager.VolumeIcon(560, 20)
    assert volumeIcon is True


def test_get_option_type(collisionManager):
    collisionManager.LoadContent()

    invalid: enums.OptionType = collisionManager.GetOptionType(589, 188)
    assert invalid == enums.OptionType.Invalid

    a: enums.OptionType = collisionManager.GetOptionType(62, 195)
    assert a == enums.OptionType.A

    b: enums.OptionType = collisionManager.GetOptionType(58, 275)
    assert b == enums.OptionType.B

    c: enums.OptionType = collisionManager.GetOptionType(44, 342)
    assert c == enums.OptionType.C

    d: enums.OptionType = collisionManager.GetOptionType(48, 437)
    assert d == enums.OptionType.D
