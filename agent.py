from __future__ import annotations

import argparse
import json
import re
from typing import Any, Callable, Dict


DEFAULT_ACTIONS = {
    "get_blue": "get_blue",
    "put_blue": "put_blue",
    "get_green": "get_green",
    "put_green": "put_green",
    "get_red": "get_red",
    "penalty1": "penalty1",
    "get_high_red": "get_high_red",
    "get_high_blue": "get_high_blue",
    "car": "car",
    "get_basic_shapes": "get_basic_shapes",
}


def normalize_command(raw: str) -> str:
    text = (raw or "").lower()
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    if not text:
        return ""

    words = text.split()
    if len(words) >= 2 and words[0] in {"get", "put", "penalty"}:
        if words[0] == "penalty":
            return f"penalty{words[1]}"
        return f"{words[0]}_{'_'.join(words[1:])}"

    if len(words) >= 2 and words[0] == "high":
        return f"get_high_{'_'.join(words[1:])}"

    if len(words) >= 2 and words[0] == "turn":
        return f"turn_{'_'.join(words[1:])}"

    return "_".join(words)


def _load_robot_actions() -> Dict[str, Callable[[], Any]]:
    actions: Dict[str, Callable[[], Any]] = {}

    try:
        import code.main as robot_main
    except Exception:
        return actions

    for name in DEFAULT_ACTIONS:
        fn = getattr(robot_main, name, None)
        if callable(fn):
            actions[name] = fn

    return actions


class RobotAgent:
    def __init__(self, action_registry: Dict[str, Callable[[], Any]] | None = None):
        registry = dict(_load_robot_actions())
        if action_registry:
            registry.update(action_registry)

        self._actions = registry or {
            name: self._simulate_action for name in DEFAULT_ACTIONS
        }

    @staticmethod
    def _simulate_action() -> Dict[str, Any]:
        return {"status": "simulated", "message": "Action was accepted but not executed on hardware."}

    def list_actions(self) -> list[str]:
        return sorted(self._actions)

    def dispatch(self, command: str) -> str:
        key = normalize_command(command)
        aliases = {
            "get_high_red": "get_high_red",
            "get_high_blue": "get_high_blue",
            "high_red": "get_high_red",
            "high_blue": "get_high_blue",
            "blue": "get_blue",
            "green": "get_green",
            "red": "get_red",
            "put_blue": "put_blue",
            "put_green": "put_green",
        }

        resolved = aliases.get(key, key)
        if resolved in self._actions:
            return resolved

        matches = [name for name in self._actions if name.startswith(resolved)]
        if len(matches) == 1:
            return matches[0]

        raise ValueError(f"Unknown action: {command!r}. Available actions: {', '.join(self.list_actions())}")

    def execute(self, command: str) -> Dict[str, Any]:
        action_name = self.dispatch(command)
        handler = self._actions[action_name]
        try:
            result = handler()
        except Exception as exc:  # pragma: no cover - guard for missing hardware
            return {"status": "error", "action": action_name, "message": str(exc)}

        if isinstance(result, dict):
            result = {"action": action_name, **result}
        else:
            result = {"action": action_name, "result": result}

        return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Robot command agent for the LEGO control routines.")
    parser.add_argument("command", nargs="?", help="Command to run, such as 'get blue' or 'penalty 1'.")
    parser.add_argument("--list", action="store_true", help="List all available agent actions.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    agent = RobotAgent()

    if args.list:
        print(json.dumps(agent.list_actions(), indent=2))
        return 0

    if not args.command:
        parser.print_help()
        return 1

    try:
        result = agent.execute(args.command)
    except ValueError as exc:
        print(str(exc))
        return 2

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
