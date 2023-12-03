use std::collections::HashMap;

fn main() {
    let input = include_str!("./input");
    let result = part1(input);
    dbg!(result);
}

fn part1(input: &str) -> i32 {
    let mut game_id_sum = 0;

    let lines = input.lines();

    let mut possible_game;
    for line in lines {
        possible_game = true;
        let mut split_line = line.split(": ");
        let game_id = parse_game_id(split_line.next().unwrap());
        for cube in parse_cube_set(split_line.next().unwrap()) {
            if !cube_is_possible(cube) {
                possible_game = false;
                break;
            }
        }
        if possible_game {
            game_id_sum += game_id;
        }
    }
    game_id_sum
}


fn cube_is_possible(input: &str) -> bool {
    let possible_bag = HashMap::from([
        ("red", 12),
        ("green", 13),
        ("blue", 14),
    ]);

    let mut split_input = input.split(" ");
    let size: i32 = split_input.next().unwrap().parse().unwrap();
    let color = split_input.next().unwrap();

    return possible_bag.get(color).unwrap() >= &size
}

fn parse_cube_set(input: &str) -> Vec<&str> {
    input.split(&[',', ';'][..]).map(|str| str.trim()).collect()
}

fn parse_game_id(input: &str) -> i32 {
    input.split(' ').skip(1).next().unwrap().parse().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn game_id_test() {
        assert_eq!(parse_game_id("Game 1"), 1);
        assert_eq!(parse_game_id("Game 10"), 10);
        assert_eq!(parse_game_id("Game 100"), 100);
    }

    #[test]
    fn cube_set_test() {
        assert_eq!(parse_cube_set("3 blue, 4 red; 1 red"), vec!["3 blue", "4 red", "1 red"]);
    }

    #[test]
    fn possible_cube_test() {
        assert_eq!(cube_is_possible("3 blue"), true);
        assert_eq!(cube_is_possible("12 red"), true);
        assert_eq!(cube_is_possible("15 blue"), false);
    }

    #[test]
    fn t1() {
        let test_input = include_str!("./test_input");
        assert_eq!(part1(test_input), 8);
    }
}