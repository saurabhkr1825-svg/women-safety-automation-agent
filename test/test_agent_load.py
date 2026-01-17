from droidrun import DroidAgent

def test_agent_initialization():
    agent = DroidAgent(config="agent.yaml")
    assert agent is not None
