from medium.robot_bounded_in_circle.src.robot import Robot
from medium.robot_bounded_in_circle.src.direction import DIRECTION
from medium.robot_bounded_in_circle.src.coordinate import Coordinate


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot = Robot()
        final_direction, final_coordinate = robot.execute_instruction(instructions)
        origin = Coordinate()
        return final_direction != DIRECTION.NORTH or (final_coordinate.x == origin.x and final_coordinate.y == origin.y)
