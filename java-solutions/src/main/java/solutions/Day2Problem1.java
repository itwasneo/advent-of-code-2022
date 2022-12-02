package solutions;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class Day2Problem1 {

	private static final Logger logger = LoggerFactory.getLogger(Day2Problem1.class);

	private static final HashMap<String, Integer> SCORES;
	static {
		SCORES = new HashMap<>();
		SCORES.put("A X", 4);
		SCORES.put("A Y", 8);
		SCORES.put("A Z", 3);
		SCORES.put("B X", 1);
		SCORES.put("B Y", 5);
		SCORES.put("B Z", 9);
		SCORES.put("C X", 7);
		SCORES.put("C Y", 2);
		SCORES.put("C Z", 6);
	}


	public static int solve(String filePath) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filePath)), StandardCharsets.UTF_8))) {

			int totalScore = 0;
			while (true) {
				String line = br.readLine();
				if (line == null) {
					break;
				}

				totalScore += SCORES.get(line);

			}
			return totalScore;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
