package solutions;

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SolutionTests {

	private static final Logger logger = LoggerFactory.getLogger(SolutionTests.class);

	@Test
	public void day1problem1() {
		logger.info("day_1_1_solution: {}", Day1Problem1.solve("../input/input_1_1.txt"));
	}
}
