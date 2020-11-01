#include <cstdlib>
#include <iostream>

namespace singleton {

class President {

public:
	static President *AcquirePresident() {
		if (!instance) {
			std::cout << "Creating new instance\n";
			instance = new President;
		} else {
			std::cout << "Instance already exists\n";
		}

		return instance;
	}

	bool New(std::string new_name, ssize_t new_age) {
		President *p = AcquirePresident();
		std::cout << "Changing instance\n";
		p->name = new_name;
		p->age = new_age;
		p->years_left = President::MANDATE_YEARS;
		return false;
	}

	void Display(std::ostream &l=std::cout) {
		l << *President::instance;
	}

	static const ssize_t MANDATE_YEARS = 6;

private:
	President() {
		this->name = "Default name";
		this->age = 13;
		this->years_left = MANDATE_YEARS;
	}

	friend std::ostream &operator<<(std::ostream &l, President &p);

private:
	// One way of initializing a static member is by making it 'inline'
	// inline static President *instance = 0;
	// But this is available from C++17
	static President *instance;

	std::string name;
	ssize_t age;
	ssize_t years_left;
};

// This is the classical way of initializing a private static member
// <member type><class>::<member> = <value>;
President *President::instance = 0;

std::ostream &operator<<(std::ostream &l, President &p) {
	l << p.name << " (" << p.age << " years old) with " << p.years_left << " years left in his/hers mandate\n";
	return l;
}

}

int main(int argc, char* const argv[]) {

	singleton::President *p = singleton::President::AcquirePresident();
	std::cout << *p << '\n';

	(void) p->New("Ivan", 42);
	std::cout << *p << '\n';

	(void) p->New("Goshka", 34);
	std::cout << *p << '\n';



    return EXIT_SUCCESS;
}
