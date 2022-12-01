package solutions;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayDeque;

public class Day1Problem2 {

	private static final Logger logger = LoggerFactory.getLogger(Day1Problem2.class);

	private static final int CAPACITY = 3;

	public static int solve(String filePath) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filePath)), StandardCharsets.UTF_8))) {

			ArrayDeque<Integer> top3 = new ArrayDeque<>(CAPACITY);
			int current_elves_calories = 0;
			while (true) {
				String line = br.readLine();
				if (line == null) {
					break;
				}

				if (line.length() == 0) {
					// queue is full
					if (top3.size() == CAPACITY) {
						// push front, pop back
						// bigger than 1st
						if (top3.peekFirst() < current_elves_calories) {
							top3.removeLast();
							top3.addFirst(current_elves_calories);

							// push back
						} else if (top3.peekLast() < current_elves_calories) {
							top3.removeLast();

							// bigger than 2nd
							if (top3.peekLast() < current_elves_calories) {
								int tmp = top3.removeLast();
								top3.addLast(current_elves_calories);
								top3.addLast(tmp);
								// bigger than 3rd
							} else {
								top3.addLast(current_elves_calories);
							}
						}
					} else if (top3.size() < CAPACITY && top3.size() > 0) {
						if (top3.peekFirst() < current_elves_calories) {
							top3.addFirst(current_elves_calories);
						} else if (top3.peekLast() < current_elves_calories) {
							int tmp = top3.removeLast();
							top3.addLast(current_elves_calories);
							top3.addLast(tmp);
						} else {
							top3.addLast(current_elves_calories);
						}
					} else if (top3.isEmpty()) {
						top3.addFirst(current_elves_calories);
					} else {
						logger.error("Unexpected state.");
					}
					current_elves_calories = 0;
				} else {
					current_elves_calories += Integer.parseInt(line);
				}
			}

			return top3.stream().mapToInt(i -> i).sum();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}