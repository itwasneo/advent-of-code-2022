class Blueprint:
    def __init__(self, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost):
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost

    def __repr__(self) -> str:
        return f"ore_robot_cost: {self.ore_robot_cost}, clay_robot_cost: {self.clay_robot_cost}, obsidian_robot_cost: {self.obsidian_robot_cost}, geode_robot_cost: {self.geode_robot_cost}"


def calculate(time_left, robot_counts, element_status, blueprint):
    if time_left == 0:
        return element_status[3]

    element_status = [x + y for x, y in zip(element_status, robot_counts)]

    p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
    if element_status[0] >= blueprint.geode_robot_cost[0] and element_status[2] >= blueprint.geode_robot_cost[1]:
        robot_counts[3] += 1
        element_status[0] -= blueprint.geode_robot_cost[0]
        element_status[2] -= blueprint.geode_robot_cost[1]
        time_left -= 1
        p1 = calculate(time_left, robot_counts, element_status, blueprint)
    if element_status[0] >= blueprint.obsidian_robot_cost[0] and element_status[1] >= blueprint.obsidian_robot_cost[1]:
        robot_counts[2] += 1
        element_status[0] -= blueprint.obsidian_robot_cost[0]
        element_status[1] -= blueprint.obsidian_robot_cost[1]
        time_left -= 1
        p4 = calculate(time_left, robot_counts, element_status, blueprint)
    if element_status[0] >= blueprint.clay_robot_cost:
        robot_counts[1] += 1
        element_status[0] -= blueprint.clay_robot_cost
        time_left -= 1
        p3 = calculate(time_left, robot_counts, element_status, blueprint)
    if element_status[0] >= blueprint.ore_robot_cost:
        robot_counts[0] += 1
        element_status[0] -= blueprint.ore_robot_cost
        time_left -= 1
        p2 = calculate(time_left, robot_counts, element_status, blueprint)

    p5 = calculate(time_left-1, robot_counts, element_status, blueprint)

    return max(p1, p2, p3, p4, p5)


bs = {}
with open("../../input/input_19_test.txt") as fp:
    for l in fp.readlines():
        bid = l.split(":")[0].split(" ")[-1]
        cost_s = l.split(":")[1].split(".")
        bs[bid] = Blueprint(int(cost_s[0].split("costs")[-1].split(" ")[-2]), int(cost_s[1].split("costs")
                            [-1].split(" ")[-2]), [int(x.strip().split(" ")[0]) for x in cost_s[2].split("costs")[-1].split("and")], [int(x.strip().split(" ")[0]) for x in cost_s[3].split("costs")[-1].split("and")])

        print(calculate(24, [1, 0, 0, 0], [0, 0, 0, 0], bs[bid]))
