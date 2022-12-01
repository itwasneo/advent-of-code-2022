package solutions;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Day1Problem1 {

	private static final Logger logger = LoggerFactory.getLogger(Day1Problem1.class);

	public static int solve(String filePath) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filePath)), StandardCharsets.UTF_8))) {

			int max = 0;
			int current_elves_calories = 0;
			while (true) {
				String line = br.readLine();
				if (line == null) {
					break;
				}
				if (line.length() == 0) {
					if (current_elves_calories > max) {
						max = current_elves_calories;
					}
					current_elves_calories = 0;
				} else {
					current_elves_calories += Integer.parseInt(line);
				}
			}
			return max;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
