use std::io::BufRead;

use crate::day_3_2::get_reader;

#[allow(dead_code)]
fn day_4_1() -> u32 {
    let mut result: u32 = 0;
    if let Ok(mut reader) = get_reader("../input/input_4_1.txt") {
        loop {
            let mut first_start = Vec::<u8>::new();
            let mut first_end = Vec::<u8>::new();
            let mut second_start = Vec::<u8>::new();
            let mut second_end = Vec::<u8>::new();

            // Reading the start of first group
            if let Ok(byte_count) = reader.read_until(b'-', &mut first_start) {
                if byte_count == 0 {
                    break;
                }
            }

            // Reading the end of first group
            if let Ok(byte_count) = reader.read_until(b',', &mut first_end) {
                if byte_count == 0 {
                    break;
                }
            }

            // Reading the start of second group
            if let Ok(byte_count) = reader.read_until(b'-', &mut second_start) {
                if byte_count == 0 {
                    break;
                }
            }

            // Reading the end of second group
            if let Ok(byte_count) = reader.read_until(10, &mut second_end) {
                if byte_count == 0 {
                    break;
                }
            }

            // Calculating the actual start and end indices of groups
            let f_s = first_start[..first_start.len() - 1]
                .into_iter()
                .map(|c| c - 48)
                .fold(0, |ans, i| ans * 10 + i);
            let f_e = first_end[..first_end.len() - 1]
                .into_iter()
                .map(|c| c - 48)
                .fold(0, |ans, i| ans * 10 + i);
            let s_s = second_start[..second_start.len() - 1]
                .into_iter()
                .map(|c| c - 48)
                .fold(0, |ans, i| ans * 10 + i);
            let s_e = second_end[..second_end.len() - 1]
                .into_iter()
                .map(|c| c - 48)
                .fold(0, |ans, i| ans * 10 + i);

            if f_s >= s_s && f_e <= s_e || s_s >= f_s && s_e <= f_e {
                result += 1;
            }
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::day_4_1;

    #[test]
    fn day_4_1_test() {
        let result = day_4_1();
        println!("day_4_1_solution: {}", result);
        assert_eq!(477, result);
    }
}
