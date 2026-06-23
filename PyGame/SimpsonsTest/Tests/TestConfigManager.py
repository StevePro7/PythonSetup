def test_dump_config(baseManager, configManager):
    baseManager.Initialize()

    configManager.Initialize()
    configManager.LoadContent()
    configManager.DumpConfig()

    assert configManager.ConfigData is not None
    assert configManager.ConfigData.FPS == 50
