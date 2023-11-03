pub fn solve() {
    let content = read_input();

    // let mut max = 0;
    // let mut current = 0;
    // for l in content.lines() {
    //     if l.is_empty() {
    //         if current > max {
    //             max = current;
    //         }
    //         current = 0;
    //     } else {
    //         current += l.parse::<u32>().expect("Parsing error");
    //     }
    // }
    println!("Part 1: {}", "<RESULT>");

    part_2(content);
}

fn part_2(_input: String) {
    println!("Part 2: {}", "<RESULT>");
}

fn read_input() -> String {
    let current_dir = std::env::current_dir().expect("Failed to get current_dir");
    let file_path = current_dir.join("input/input_1.txt");

    let content = std::fs::read_to_string(file_path).expect("Failed read the content of the file");
    content.trim().to_owned()
}
