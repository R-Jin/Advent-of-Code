fn main() {
    let input = include_str!("./input");
    let result = part1(input);
    dbg!(result);
}

fn part1(input: &str) {
    let engine_schematic: Vec<&str> = input.lines().collect();
}

#[cfg(test)]
mod tests {
    use super::*;

    fn t1() {
        // assert_eq!()
    }
}
// Sudo code
// matrix = input converted to list with all the lines of the input
// for line in matrix:
//     if is symbol: 
//         if found adjacent number:
//             parse number and add to total


// is symbol:

