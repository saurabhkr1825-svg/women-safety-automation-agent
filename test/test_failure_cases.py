from droidrun import DroidAgent

def test_agent_run_without_device(mocker):
    agent = DroidAgent(config="agent.yaml")
    mocker.patch.object(agent, "run", return_value=None)
    agent.run()
