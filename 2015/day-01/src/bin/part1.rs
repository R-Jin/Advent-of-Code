fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    return (input.matches('(').count() - input.matches(')').count()).to_string();
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn t1() {
        let result = part1("(())");
        assert_eq!(result, 0.to_string());
    }

    fn t2() {
        let result = part1("()()");
        assert_eq!(result, 0.to_string());
    }

    fn t3() {
        let result = part1("(((");
        assert_eq!(result, 3.to_string());
    }

    fn t4() {
        let result = part1("(())(()(()(");
        assert_eq!(result, 3.to_string());
    }

    fn t5() {
        let result: String = part1("))(((((");
        assert_eq!(result, 3.to_string());
    }

    fn t6() {
        let result: String = part1("())");
        assert_eq!(result, (-1).to_string());
    }

    fn t7() {
        let result: String = part1("))(");
        assert_eq!(result, (-1).to_string());
    }
    
    fn t8() {
        let result: String = part1(")))");
        assert_eq!(result, (-3).to_string());
    }

    fn t9() {
        let result: String = part1(")())())");
        assert_eq!(result, (-3).to_string());
    }

}