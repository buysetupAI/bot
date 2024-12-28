from src.ai_decision import AIDecision

def test_get_recommendations():
    ai_decision = AIDecision({"enable": True})
    assert ai_decision.get_recommendations() == []
