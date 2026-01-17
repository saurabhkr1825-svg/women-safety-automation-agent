import os

def test_trigger_file_exists():
    assert os.path.exists("triggers/sos_trigger.yaml")

def test_actions_file_exists():
    assert os.path.exists("actions/emergency_actions.yaml")
