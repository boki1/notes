## OOP Glossary

**abstract class**
	- primary purpose to define an interface
	- cannot be instantiated

**abstract coupling**
	- given a class A that maintains a reference to an abstract class B, A is said to be abstractly coupled to B
	- A refers to a _type_ of object and not a concrete object

**abstract operation**
	- an operation which declares a signature without providing an implementation

**acquaintance relationship**
	- a class which refers to another class

**aggregate object**
	- object composed of subobjects or _parts_

**aggregation relationship**
	- the relationship between an aggregate object and its parts

**black-box reuse**
	- based on object _composition_
	- objects do not reveal _any internal details_

**class**
	- defines an interface and implementation
	- behaviour and attributes

**class diagram**
	- depicts class' structure, operations and the relationship between other classes and it

**class operation**
	- _static member function_
	- targeted to a class, not to an individual object

**concrete class**
	- no abstract operations
	- can be instantiated

**constructor**
	- operation which initializes new instances 

**coupling**
	- components' dependency on each other

**delegation**
	- _run-time inheritance_
	- targets the instances rather then the type
	- Example with the _delegation link_ being the instance of `A`: 
	```c++
	class A {

	public:
		A() {}
		void bar() { std::cout << "Bar from A" << '\n'; }
	};

	class B {
	public:
		B(A a_inst) { this.a = a_inst; }
		void foo() { std::cout << "Foo from B" << '\n'; }
		void bar() { this.a.foo(); }
	private:
		A a;

	};
	```

**design pattern**
	- explains a general recurring design problem in OO system
	- provides an applicable solution

**destructor**
	- invoked to finalize an object

**dynamic binding/dispatch**
	- also knows as: run-time/late binding 
	- run-time association of a request to an object and one of its operations
	- Example:

	```c++
	struct Function {
		virtual ~Function() {}
		virtual int doit(int, int) const = 0;
	};
	struct Add: Function {
		virtual int doit(int a, int b) const override { return a + b; } 
	};
	struct Substract: Function {
		virtual int doit(int a, int b) const override { return a - b; } 
	};

	int main() {
		char op = 0;
		std::cin >> op;

		std::unique_ptr<Function> func =
			op == '+' ? std::unique_ptr<Function>{new Add{}}
					  : std::unique_ptr<Function>{new Substract{}};

		std::cout << func->doit(4, 5) << "\n";
	}
	```


**encapsulation**
	- the process of hiding the representation and the implementation in an object
	- operations are the only way to change the representation

**framework**
	- a set of cooperating classes which make up a reusable design for a specific OO system

**friend class**
	- a class which has the same access rights to the operations and data of a class as that class itself

**inheritance**
	- _class_ inheritance defines a new class in terms of one or more parent classes
	- the new class is called subclass (or a derived class)
	- combines _interface_ inheritance and _implementation_ inheritance

**instance variable**
	- data which defines part of object representation
	- also known as data member

**interaction diagram**
	- shows the flow of requests between objects

**interface**
	- the set of all signatures defined by an object's operations

**metaclass**
	- the class of a class object
	- only for languages where classes are class objects(Smalltalk, Python, etc.)

**object**
	- run-time entity which packages both representation and operations

**composition**
	- assembling objects to get more complex behaviour

**object diagram**
	- depicts a particular object structure at run-time

**object reference**
	- value identifying another object

**operation**
	- member function or method

**overriding**
	- redefining an operation in a subclass

**parameterized type**
	- also known as templates
	- leaves some constituent types unspecified until the point of use

**parent class**
	- superclass; base class or ancestor class

**polymorhism**
	- substitute object of matching interface for one another at run-time
	
**private inheritance**
	- inherited solely for its implementation

**protocol**
	- extends the concept of `interface`
	- a sequence of operations

**receiver**
	- the target of a specific request

**request**
	- also known as `message`
	- object performs an operation after receiving a message from another object

**signature**
	- method prototype
	- name, parameters and return value

**subclass**
	- also known as derived class

**subsystem**
	- independent set of classes which collaborate to fulfill a set of responsibilities

**subtype**
	- a type is a subtype of another if its interface contains the interface of the other type

**supertype**
	- the parent type from which a type inherits

**toolkit**
	- independent set of classes which collaborate to fulfill a set of responsibilities without defining the design of an application

**type**
	- the name of an interface

**white-box reuse**
	- based on class inheritance
