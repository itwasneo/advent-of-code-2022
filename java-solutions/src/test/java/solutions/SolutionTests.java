package solutions;

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;

public class SolutionTests {

	private static final Logger logger = LoggerFactory.getLogger(SolutionTests.class);

	@Test
	public void day1problem1() {
		logger.info("day_1_1_solution: {}", Day1Problem1.solve("../input/input_1_1.txt"));
	}

	@Test
	public void day1problem2() {
		logger.info("day_1_2_solution: {}", Day1Problem2.solve("../input/input_1_1.txt"));
	}

	@Test
	public void day2problem1() {
		logger.info("day_2_1_solution: {}", Day2Problem1.solve("../input/input_2_1.txt"));
	}
}
