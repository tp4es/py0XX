from typing import Any


class StrategyError(Exception):
    pass


class CreatureStrategyError(StrategyError):
    def __init__(self, args: Any) -> None:
        super().__init__(
            f"{args} Can't use strategy."
            "Only Well formed Creatures can participate."
        )


class DefensiveStrategyError(StrategyError):
    def __init__(self, args: Any) -> None:
        super().__init__(
            f"{args} Can't use the Defensive-Strategy."
            "Only Creatures with healing capability might execute that."
        )


class AgressiveStrategyError(StrategyError):
    def __init__(self, args: Any) -> None:
        super().__init__(
            f"{args} Can't use the Agressive-Strategy."
            "Only Creatures with transform capability might execute that."
        )
