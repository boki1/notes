pub trait Delimiter {
    fn next_occurance(&self, s: &str) -> Option<(usize, usize)>;
}

pub struct StrSplit<'haystack, D> {
    remainder: Option<&'haystack str>,
    delimeter: D,
}

impl<'haystack, D> StrSplit<'haystack, D> {
    pub fn new(haystack: &'haystack str, delimeter: D) -> Self {
        Self {
            remainder: Some(haystack),
            delimeter,
        }
    }
}

impl<'haystack, D> Iterator for StrSplit<'haystack, D>
where
    D: Delimiter,
{
    type Item = &'haystack str;

    fn next(&mut self) -> Option<Self::Item> {
        // Acquire a mutable reference to the remainder
        // After that unpack
        let remainder = self.remainder.as_mut()?;
        if let Some((begin, end)) = self.delimeter.next_occurance(remainder) {
            let until_delimiter = &remainder[..begin];
            *remainder = &remainder[end..];
            Some(until_delimiter)
        } else {
            // Takes (consumes) the object in Option
            self.remainder.take()
        }
    }
}

impl Delimiter for &str {
    fn next_occurance(&self, s: &str) -> Option<(usize, usize)> {
        s.find(self).map(|begin| (begin, begin + self.len()))
    }
}

impl Delimiter for char {
    fn next_occurance(&self, s: &str) -> Option<(usize, usize)> {
        s.char_indices()
            .find(|(_, c)| c == self)
            .map(|(start, _)| (start, start + 1))
    }
}

pub fn until_delim(s: &str, c: char) -> &str {
    StrSplit::new(s, c)
        .next()
        .expect("strsplit always returns one result from iteration")
}

#[test]
fn tail() {
    let haystack = "a b c ";
    let letters: Vec<_> = StrSplit::new(haystack, " ").collect();

    assert_eq!(letters, vec!["a", "b", "c", ""]);
}

#[test]
fn basic() {
    let haystack = "a b c d e";
    let letters: Vec<_> = StrSplit::new(haystack, " ").collect();

    assert_eq!(letters, vec!["a", "b", "c", "d", "e"]);
}

#[test]
fn find_char() {
    let haystack = "hello world";
    let until = until_delim(haystack, 'l');

    assert_eq!(until, "he");
}

#[test]
fn empty_delim() {
    // let _haystack = "asdf";
    // let _delim = "";

    // let letters = StrSplit::new(haystack, delim).collect();
    // assert_eq!(letters, vec!["a", "b", "c", "d"]);

    // ----------------------------
    // No support for this case
    // Test fails always
    assert_eq!(1, 0);
}
