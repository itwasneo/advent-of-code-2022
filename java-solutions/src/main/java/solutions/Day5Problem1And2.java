package solutions;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day5Problem1And2 {

	public static String solve(String filepath, int problemNumber) {
		try (BufferedReader br = new BufferedReader(
				new InputStreamReader(
						Files.newInputStream(Paths.get(filepath)), StandardCharsets.UTF_8))) {

			// Creating 9 empty stacks, keeping them in an array list
			ArrayList<LinkedList<Character>> blocks = IntStream.rangeClosed(1, 9)
					.boxed()
					.map(i -> new LinkedList<Character>() {})
					.collect(Collectors.toCollection(ArrayList::new));

			for (int i = 0; i < 8; i++) {
				String line = br.readLine();
				if (line == null) {
					break;
				}

				String[] strings = line.split(" ");
				for (int j = 0; j < strings.length; j++) {
					char c = strings[j].charAt(1);
					if (c != '*') {
						blocks.get(j).addLast(c);
					}
				}
			}

			// Reading redundant lines
			String line = br.readLine();
			line = br.readLine();

			while ((line = br.readLine()) != null) {

				String[] tokens = line.split(" ");
				if (problemNumber == 1) {
					for (int i = 0; i < Integer.parseInt(tokens[1]); i++) {
						blocks.get(Integer.parseInt(tokens[5])-1)
								.push(blocks.get(
										Integer.parseInt(tokens[3])-1).pop());
					}
				} else if (problemNumber == 2) {
					LinkedList<Character> batch = new LinkedList<>();
					for (int i = 0; i < Integer.parseInt(tokens[1]); i++) {
						batch.addLast(blocks.get(
								Integer.parseInt(tokens[3])-1).pop()
						);
					}
					blocks.get(Integer.parseInt(tokens[5])-1)
							.addAll(0, batch);
				} else {
					throw new RuntimeException();
				}
			}
			return blocks.stream().map(l -> String.valueOf(l.get(0))).collect(Collectors.joining());
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
