from src.classifier import classify

def test_classifier():

    category, score = classify(
        "This lecture discusses quantum mechanics and wave functions."
    )

    assert isinstance(category, str)
    assert score > 0