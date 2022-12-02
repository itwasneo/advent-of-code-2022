package solutions;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class Day2Problem2 {

	private static final HashMap<String, Integer> SCORES;
	static {
		SCORES = new HashMap<>();
		SCORES.put("A X", 3);
		SCORES.put("A Y", 4);
		SCORES.put("A Z", 8);
		SCORES.put("B X", 1);
		SCORES.put("B Y", 5);
		SCORES.put("B Z", 9);
		SCORES.put("C X", 2);
		SCORES.put("C Y", 6);
		SCORES.put("C Z", 7);
	}

	public static int solve(String filePath) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filePath)), StandardCharsets.UTF_8))) {

			int total_score = 0;
			while (true) {
				String line = br.readLine();
				if (line == null) {
					break;
				}

				total_score += SCORES.get(line);
			}
			return total_score;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
