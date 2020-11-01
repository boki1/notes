class Employee {

public:
	Employee() = default;
	Employee(const Employee &other) : state(other.GetState()) {}

	virtual Employee *Clone() const = 0;

	int GetState() const {
		return this->state;
	}

protected:
	int state;
};

class Developer: public Employee
{
	Developer() = default;
	Developer(const Developer &other) : state(other.GetState()) {}

	Employee *Clone() const override
	{
		return new Developer(*this);
	}
private:
	int state;
};

class QualityAssurance: public Employee
{
	QualityAssurance() = default;
	QualityAssurance(const QualityAssurance &other) : state(other.GetState()) {}

	Employee *Clone() const override
	{
		return new QualityAssurance(*this);
	}
private:
	int state;
};

int main(int argc, char *const argv[]) {
	Employee *dev, *qa;

	return 0;
}
