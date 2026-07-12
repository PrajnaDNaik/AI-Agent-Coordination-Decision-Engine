from workflows.decision_flow import DecisionFlow
def test_decision_flow():

    workflow = DecisionFlow()

    result = workflow.process_request(
        "Should the company expand to a new city and hire 20 employees?"
    )

    assert "analysis" in result
    assert "plan" in result
    assert "execution" in result
    assert "decision" in result