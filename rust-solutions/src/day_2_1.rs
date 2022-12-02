use crate::day_1_1::read_lines;
use std::collections::HashMap;

// A -----> ROCK
// B -----> PAPER
// C -----> SCISSORS

// X -----> ROCK
// Y -----> PAPER
// Z -----> SCISSORS

// AX ----> 3 + 1 = 4
// AY ----> 6 + 2 = 8
// AZ ----> 0 + 3 = 3

// BX ----> 0 + 1 = 1
// BY ----> 3 + 2 = 5
// BZ ----> 6 + 3 = 9

// CX ----> 6 + 1 = 7
// CY ----> 0 + 2 = 2
// CZ ----> 3 + 3 = 6

#[allow(dead_code)]
fn day_2_1() -> u16 {
    let mut scores = HashMap::<String, u16>::new();
    scores.insert("A X".to_owned(), 4);
    scores.insert("A Y".to_owned(), 8);
    scores.insert("A Z".to_owned(), 3);
    scores.insert("B X".to_owned(), 1);
    scores.insert("B Y".to_owned(), 5);
    scores.insert("B Z".to_owned(), 9);
    scores.insert("C X".to_owned(), 7);
    scores.insert("C Y".to_owned(), 2);
    scores.insert("C Z".to_owned(), 6);

    let mut total_score: u16 = 0;
    if let Ok(lines) = read_lines("../input/input_2_1.txt") {
        for line in lines {
            if let Ok(match_state) = line {
                if let Some(score) = scores.get(&match_state) {
                    total_score += score;
                }
            }
        }
    }

    total_score
}

#[cfg(test)]
mod tests {
    use super::day_2_1;

    #[test]
    fn day_2_1_test() {
        let result = day_2_1();
        println!("day_2_1_solution: {:?}", result);
        assert_eq!(result, 12156);
    }
}
