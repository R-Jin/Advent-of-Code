fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> String {
    let mut count = 0;
    for (i, c) in input.chars().enumerate() {
        if c == '(' {
            count += 1;
        } else if c == ')' {
            count -= 1;
        }
        if count < 0 {
            return (i + 1).to_string();
        }
    }
    return (-1).to_string();
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]

    fn t1() {
        let result = part2(")");
        assert_eq!(result, 1.to_string());
    }

    fn t2() {
        let result = part2("()())");
        assert_eq!(result, 5.to_string());
    }
}