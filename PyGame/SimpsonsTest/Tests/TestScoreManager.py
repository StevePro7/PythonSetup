def test_score_value(scoreManager):
    scoreManager.Initialize()
    scoreManager.LoadContent()

    assert scoreManager.ScoreValu == 0
    scoreManager.Increment()
    assert scoreManager.ScoreValu == 1
