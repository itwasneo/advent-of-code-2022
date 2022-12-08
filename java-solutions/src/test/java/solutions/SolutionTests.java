package solutions;

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SolutionTests {

	private static final Logger logger = LoggerFactory.getLogger(SolutionTests.class);

	@Test
	public void day1problem1() {
		int result = Day1Problem1.solve("../input/input_1_1.txt");
		logger.info("day_1_1_solution: {}", result);
		assertEquals(69883, result);
	}

	@Test
	public void day1problem2() {
		int result = Day1Problem2.solve("../input/input_1_1.txt");
		logger.info("day_1_2_solution: {}", result);
		assertEquals(207576, result);
	}

	@Test
	public void day2problem1() {
		int result = Day2Problem1.solve("../input/input_2_1.txt");
		logger.info("day_2_1_solution: {}", result);
		assertEquals(12156, result);
	}

	@Test
	public void day2problem2() {
		int result = Day2Problem2.solve("../input/input_2_1.txt");
		logger.info("day_2_2_solution: {}", result);
		assertEquals(10835, result);
	}

	@Test
	public void day4problem1() {
		int result = Day4Problem1.solve("../input/input_4_1.txt");
		logger.info("day_4_1_solution: {}", result);
		assertEquals(477, result);
	}

	@Test
	public void day4problem2() {
		int result = Day4Problem2.solve("../input/input_4_1.txt");
		logger.info("day_4_2_solution: {}", result);
		assertEquals(830, result);
	}

	@Test
	public void day5problem5and2() {
		String result1 = Day5Problem1And2.solve("../input/input_5_1.txt", 1);
		String result2 = Day5Problem1And2.solve("../input/input_5_1.txt", 2);
		logger.info("day_5_1_solution: {}", result1);
		logger.info("day_5_2_solution: {}", result2);
		assertEquals("VJSFHWGFT", result1);
		assertEquals("LCTQFBVZV", result2);
	}
}
