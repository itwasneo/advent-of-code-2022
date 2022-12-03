use std::collections::HashSet;

use crate::day_1_1::read_lines;

#[allow(dead_code)]
fn day_3_1() -> u32 {
    let mut total_prios = 0;
    if let Ok(lines) = read_lines("../input/input_3_1.txt") {
        for line in lines {
            if let Ok(items) = line {
                let array_length = items.len() / 2;
                let first_group: HashSet<char> = items[..array_length].chars().collect();
                let second_group: HashSet<char> = items[array_length..].chars().collect();
                if let Some(common_item) = first_group.intersection(&second_group).next() {
                    total_prios += get_priority(*common_item);
                }
            }
        }
    }
    total_prios
}

#[allow(dead_code)]
fn get_priority(c: char) -> u32 {
    if c.is_ascii_lowercase() {
        return (c as u32) - 96;
    }
    (c as u32) - 38
}

#[cfg(test)]
mod tests {

    use super::day_3_1;

    #[test]
    fn day_3_1_test() {
        let result = day_3_1();
        println!("day_3_1_solution: {}", result);
    }
}
