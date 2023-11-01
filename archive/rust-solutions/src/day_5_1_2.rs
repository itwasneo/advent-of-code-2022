use crate::day_3_2::get_reader;
use std::collections::VecDeque;
use std::io::BufRead;

#[allow(dead_code)]
fn day_5(_problem_number: u8) -> String {
    let mut blocks: [VecDeque<char>; 9] = Default::default();

    if let Ok(mut reader) = get_reader("../input/input_5_1.txt") {
        // Filling the blocks
        for _ in 0..8 {
            let mut token_number = 0;
            loop {
                let mut token_buff = Vec::<u8>::default();

                // Read until space
                reader.read_until(b' ', &mut token_buff).unwrap();

                // Remove the last char which is space
                let token = token_buff[..token_buff.len() - 1].to_vec();
                if token[1] != b'*' {
                    blocks[token_number].push_back(token[1] as char);
                }
                token_number += 1;

                // Treat last element differently, read until LF
                if token_number > 7 {
                    let mut last_token_buff = Vec::<u8>::default();
                    reader.read_until(10, &mut last_token_buff).unwrap();

                    // Remove last char
                    let last_token = last_token_buff[..last_token_buff.len() - 1].to_vec();
                    if last_token[1] != b'*' {
                        blocks[token_number].push_back(last_token[1] as char);
                    }
                    break;
                }
            }
        }
        // Reading redundant lines
        let mut tmp = String::default();
        reader.read_line(&mut tmp).unwrap();
        reader.read_line(&mut tmp).unwrap();

        println!("{:?}", blocks);
        loop {
            let mut buff = Vec::<u8>::default();

            // First token, 'move' word, if can't read the first word it means EOF
            reader.read_until(b' ', &mut buff).unwrap();
            if buff.len() == 0 {
                break;
            }
            // Second token, Number of crates to be moved
            buff.truncate(0);
            reader.read_until(b' ', &mut buff).unwrap();
            let n = buff[..buff.len() - 1].iter().next().unwrap() - 48;

            // Third token, 'from' word
            reader.read_until(b' ', &mut buff).unwrap();

            // Fourth token, first block
            buff.truncate(0);
            reader.read_until(b' ', &mut buff).unwrap();

            // Care subtracting 49 instead of 48 due to correct for blocks indices
            let from = (buff[..buff.len() - 1].iter().next().unwrap() - 49) as usize;

            // Fifth token, 'to' word
            reader.read_until(b' ', &mut buff).unwrap();

            // Sixth token, second block
            buff.truncate(0);
            reader.read_until(10, &mut buff).unwrap();
            // Care subtracting 49 instead of 48 due to correct for blocks indices
            let to = (buff[..buff.len() - 1].iter().next().unwrap() - 49) as usize;

            for _ in 0..n {
                let p = blocks[from].pop_front().unwrap();
                blocks[to].push_front(p);
            }
        }
        println!("{:?}", blocks);
    }
    return "69".to_owned();
}

#[cfg(test)]
mod tests {
    use super::day_5;

    #[test]
    fn day_5_1() {
        let result = day_5(1);
        println!("day_5_1_solution: {}", result);
        assert_eq!("69", result);
    }
}
