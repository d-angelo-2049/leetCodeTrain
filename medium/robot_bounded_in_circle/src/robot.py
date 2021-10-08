from medium.robot_bounded_in_circle.src.coordinate import Coordinate
from medium.robot_bounded_in_circle.src.instruction import INSTRUCTION
from medium.robot_bounded_in_circle.src.direction import DIRECTION


class Robot:
    def __init__(self):
        self.direction = DIRECTION.NORTH
        self.coordinate = Coordinate()

    def execute_instruction(self, instruction_code: str):
        for instruction in instruction_code:
            if instruction is INSTRUCTION.GO.value:
                self.__go_straight()
            elif instruction is INSTRUCTION.LEFT.value:
                self.__turn_left()
            else:
                self.__turn_right()

        return self.direction, self.coordinate

    def __go_straight(self):
        if self.direction is DIRECTION.NORTH:
            self.coordinate.incremental(0, 1)

        elif self.direction is DIRECTION.EAST:
            self.coordinate.incremental(1, 0)

        elif self.direction is DIRECTION.SOUTH:
            self.coordinate.incremental(0, -1)

        else:
            self.coordinate.incremental(-1, 0)

    def __turn_left(self):
        if self.direction is DIRECTION.NORTH:
            self.direction = DIRECTION.WEST

        elif self.direction is DIRECTION.EAST:
            self.direction = DIRECTION.NORTH

        elif self.direction is DIRECTION.SOUTH:
            self.direction = DIRECTION.EAST

        else:
            self.direction = DIRECTION.SOUTH

    def __turn_right(self):
        if self.direction is DIRECTION.NORTH:
            self.direction = DIRECTION.EAST

        elif self.direction is DIRECTION.EAST:
            self.direction = DIRECTION.SOUTH

        elif self.direction is DIRECTION.SOUTH:
            self.direction = DIRECTION.WEST

        else:
            self.direction = DIRECTION.NORTH

