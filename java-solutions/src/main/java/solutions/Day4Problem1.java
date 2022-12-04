package solutions;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.StringTokenizer;

public class Day4Problem1 {

	/**
	 * Read line by line, tokenize with String Tokenizer, no mumbo jumbo
	 * @param filename String
	 * @return int
	 */
	public static int solve(String filename) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filename)), StandardCharsets.UTF_8))) {

			int result = 0;
			while (true) {
				String line = br.readLine();
				if (line == null) {
					break;
				}

				// Splitting first and second group
				StringTokenizer groupExtractor = new StringTokenizer(line, ",");

				String firstGroup = groupExtractor.nextToken();
				String secondGroup = groupExtractor.nextToken();

				StringTokenizer firstExtractor = new StringTokenizer(firstGroup, "-");
				int firstStart = Integer.parseInt(firstExtractor.nextToken());
				int firstEnd = Integer.parseInt(firstExtractor.nextToken());

				StringTokenizer secondExtractor = new StringTokenizer(secondGroup, "-");
				int secondStart = Integer.parseInt(secondExtractor.nextToken());
				int secondEnd = Integer.parseInt(secondExtractor.nextToken());

				if (firstStart >= secondStart && firstEnd <= secondEnd || firstEnd >= secondEnd && firstStart <= secondStart) {
					result += 1;
				}
			}

			return result;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
