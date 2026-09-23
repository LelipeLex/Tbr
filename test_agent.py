from agent import RobotAgent, normalize_command


def test_normalize_command():
    assert normalize_command("GET BLUE") == "get_blue"
    assert normalize_command("put green") == "put_green"
    assert normalize_command("penalty 1") == "penalty1"


def test_dispatch_known_action():
    bot = RobotAgent()
    result = bot.dispatch("get blue")
    assert result == "get_blue"
