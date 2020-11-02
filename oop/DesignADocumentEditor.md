# Chapter 2: Design a Document Editor

In order to have a single interface for all types of *stuff* represented on the screen, we introduce the `Glyph` abstract class.

- `Glyph` - **The base class**
	- Its derived have the following responsibilities:
		- *To know how to draw itself*
		- *To know how to detect collision*
		- *To know its structure*
	- The method protoypes look similarly to this:
		- About *Drawing*
		```c++
		void Draw(Window *);
		void Bounds(Rectangle *);
		```
		-About *Collision*
		```c++
		bool Intersects(Point &);
		 ```
		- About *Strcuture*
		```c++
		bool Insert(Glyph &, Position);
		Glyph &Insert(Position);
		 ```

Let's take a look at the subclasses which implement `Glyph`.

- `Character` - this is how we add **text** functionalities to our document editor.
- `Row` - this is a bigger unit of text
- `Rectangle` - about shapes
- `Polygon` - etc.

*What are the differences between their implementation?*
- `Row`
	- This is the different one
	- Here we have `children`.
	
	- The methods:
		- 

We add a subclass `MonoGlyph` to provide a simple way of implementing  `Border` and `Scroller`.

All types of *stuff* derives from it e.g. `Character`, `Rectangle`, `Row`, etc. Let's take a look at each one seperately.





