from collections.abc import Iterator
from dataclasses import dataclass

from game.commander.tasks.primitive.oca import PlanOcaStrike
from game.commander.theaterstate import TheaterState
from game.htn import CompoundTask, Method


@dataclass(frozen=True)
class AttackAirInfrastructure(CompoundTask[TheaterState]):
    aircraft_cold_start: bool

    def each_valid_method(self, state: TheaterState) -> Iterator[Method[TheaterState]]:
        for garrison in state.oca_targets:
            yield [PlanOcaStrike(garrison, self.aircraft_cold_start)]
