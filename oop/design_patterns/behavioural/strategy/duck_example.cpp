
#include <string>
#include <iostream>

//
// About Quacking
//

class IQuackBehaviour {
public:
	IQuackBehaviour() = default;
	~IQuackBehaviour() = default;
	virtual void Quack() = 0;
};

class SimpleQuackBehaviour : public IQuackBehaviour {
public:
	SimpleQuackBehaviour() = default;
	~SimpleQuackBehaviour() = default;

	void Quack() override {
		std::cout << "Quack! Quack!\n";
	}
};

class TripleQuackBehaviour : public IQuackBehaviour {
public:
	TripleQuackBehaviour() = default;
    ~TripleQuackBehaviour() = default;

	void Quack() override {
		std::cout << "Quack! Quack! Quack!\n";
	}
};

class RubberQuackBehaviour : public IQuackBehaviour {
public:
	RubberQuackBehaviour() = default;
    ~RubberQuackBehaviour() = default;

	void Quack() override {
		std::cout << "Quuuuuuaaaack!\n";
	}
};

//
// About Flying
//

class IFlyBehaviour {
public:
	IFlyBehaviour() = default;
    ~IFlyBehaviour() = default;
	virtual void Fly() = 0;
};

class JetFlyingBehaviour : public IFlyBehaviour {
public:
	JetFlyingBehaviour() = default;
    ~JetFlyingBehaviour() = default;

	void Fly() override {
		std::cout << "Bzzzzzzzzz\n";
	}
};

class WingFlyingBehaviour : public IFlyBehaviour {
public:
	WingFlyingBehaviour() = default;
    ~WingFlyingBehaviour() = default;

	void Fly() override {
		std::cout << "Huf Huf\n";
	}
};

class DreamFlyingBehaviour : public IFlyBehaviour {
public:
	DreamFlyingBehaviour() = default;
    ~DreamFlyingBehaviour() = default;

	void Fly() override {
		std::cout << "Zzzhuf zzzhuf\n";
	}
};

//
// About Displaying
//

class IDisplayBehaviour {
public:
	IDisplayBehaviour() = default;
    ~IDisplayBehaviour() = default;
	virtual void Display() = 0;
};

class AsTextDisplayingBehaviour : public IDisplayBehaviour {
public:
	AsTextDisplayingBehaviour() = default;
    ~AsTextDisplayingBehaviour() = default;
	void Display() override {
		std::cout << "D-U-C-K\n";
	}
};

class AsGraphicsDisplayingBehaviour : public IDisplayBehaviour {
public:
	AsGraphicsDisplayingBehaviour() = default;
    ~AsGraphicsDisplayingBehaviour() = default;
	void Display() override {
		std::cout << "1011001\n";
	}
};


class Duck {
public:
	Duck(IQuackBehaviour &qb, IFlyBehaviour &fb, IDisplayBehaviour &db) :
		quacking(qb), flying(fb), displaying(db) {}

    void Quack()
	{
		this->quacking.Quack();
	}

	void Display()
	{
		this->displaying.Display();
		}

	void Fly() {
		this->flying.Fly();
	}

private:
	IQuackBehaviour &quacking;
	IFlyBehaviour &flying;
	IDisplayBehaviour &displaying;
};

int main(int argc, char *const argv[])
{
	AsGraphicsDisplayingBehaviour graphics_algorithm;
	JetFlyingBehaviour flying_algorithm;
	RubberQuackBehaviour quacking_algorithm;

	Duck ducky(quacking_algorithm, flying_algorithm, graphics_algorithm);
	ducky.Quack();
	ducky.Display();
	ducky.Fly();

	return 0;
}
