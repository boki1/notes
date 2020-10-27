#Builder


#### Intent

Separates the construction of a complex object from its representation so that the same construction could be used for multiple and different instances.

#### When to use?

The construction algorithm needs to be flexible in order to provide a way for instantiating different kinds of objects based on their independent parts and assembly. If that is the case, then `Builder` is an applicable pattern.

#### Components

These are the participating classes, in order to provide a useful implementation for the current pattern: `Builder`, `ConcreteBuilder`, `Director`, `Product`. 

`Builder` is an interface used to declare the signature for generating parts of `Product`. 

`ConcreteBuilder` is responsible for providing a specific implementation for the construction and assembly of `Product`. As the name suggests, it implements `Builder` and keeps track of the representations created.

`Director` constructs an object using the interface declared in`Builder`.

`Product` is the complex object which is under construction. `ConcreteBuilder` builds the product's internal members and defines the process by which they are assembled into complex objects' representation.

#### Example

Let's say there is the interface `IVehicleBuilder` and it is implemented by the subclasses `MotorcycleBuilder`  and `TruckBuilder`. In this case, the role of `Director` would be fulfilled by a `Shop` class which has the responsibility to use the behaviour defined in the concrete-builders in order to produce an assembled complex object. Last, but not least, is the `Vehicle` class which is the actual product resulted from the director's management in bringing the parts together.

#### Diagram

![Diagram for the `Builder` pattern.](https://www.dofactory.com/img/diagrams/net/builder.gif)
