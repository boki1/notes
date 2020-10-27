## Lifetimes
## Main resouce: (Jon Gjengset - Lifetimes Annotations)[https://www.youtube.com/watch?v=rAl-9HwD858&t=1409s]
### Rustlang 1.8(?)


**What are lifetimes?**

Lifetimes are Rust-specific mechanism providing way for SE to write safer code.

**When to use them?**

Imagine the following code structure.
We are implementating a `struct` providing a result from `split()` call on a string e.g. `StrSplit`. 

This structure holds the string we want to split on - `full`, and the string we want to split by - `delim`.

So the structure of out string-split will look like that:

```rust

struct StrSplit {
	full: &str,
	delim: &str
}

```

Let's see how are we going to use this.

```rust 
fn foo() {
	string: &str = "This is an example string";
	for part in StrSplit::new(&string, " ") {
		// do something with `part`
	}
}
```

One thing to note here is that in order to make this example to compile and work successfully, we need to implement the `Iterator` trait for are `struct StrSplit`. 
(This code is not going to be included here in order to simplify the explanation.)

_So, where is the problem? How are lifetimes related to this?_

Well, suppose we pass a `str` reference to `StrSplit::new()` which gets deallocated immediately after the `StrSplit::new()` call.
Then, out `StrSplit` instance gets invalid, because its fields reference deallocated memory. In order to fix this issue, `lifetime` are introduced.

**How do we use them?**

For our example we have 3 references. We need to tell the Rust compiler how long are these references going to be valid.

Suppose we read a line from a file. And, for some reason, we need to look at each word separately. For this we may use our `StrSplit` structure. What parameters are we going to pass? Well, let's say we loop through each line of file one at a time, let's call this variable `line`. And in order to iterate over `line`'s words we need to split it by `" "` - let's call our delimiter `space`.

How long are these variables going to contain valid data? Well, `line` is going to change on every file read, so it's lifetime is going to be for a single iteration - let's call this lifetime `a`. On the other hand, `space` is a constant for the whole file operation, so it has a different lifetime. Let's call it `b`.

After we know all this, let's figure out _what lifetime will `StrSplit` have_.

Let's check again what is the result we are trying to achieve.

```rust 
fn foo() {
	[...]
	for line in OpenFile::some_read_function(&file) {
		string: &str = "This is an example string";
		for part in StrSplit::new(&string, " ") {
			// do something with `part`
		}
	}
	[...]
}
```

Now it is pretty obvious, isn't it?
The `StrSplit` instance will live for one file read only. Or i.e for as much as `line` lives, or - `a` again.

**How do we implement this?**


