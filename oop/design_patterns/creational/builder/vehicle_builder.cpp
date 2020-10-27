#include <iostream>
#include <string>

class Vehicle {

public:
	Vehicle() = default;
	~Vehicle() = default;

	void Display() {
		std::cout << "-------------" << '\n';
		std::cout << "Model: " << prod_year << '\n';
		std::cout << "Year: " << model << '\n';
		std::cout << "# of seats: " << num_of_seats << '\n';
		std::cout << "kind of seats: " << seat_type << '\n';
		std::cout << "-------------" << '\n';
	}

	void SetSeatInfo(unsigned num, std::string kind) {
		this->num_of_seats = num;
		this->seat_type = kind;
	}

	void SetDetails(std::string mod, unsigned year) {
		this->model = mod;
		this->prod_year = year;
	}

private:
	std::string model;
	unsigned num_of_seats;
	std::string seat_type;
	unsigned prod_year;
};

class IVehicleBuilder {

public:
	virtual void BuildPartSeats() = 0;
	virtual void BuildPartDetails() = 0;
	virtual Vehicle &GetResult() = 0;

};


class MotorcycleBuilder : public IVehicleBuilder {

public:

	void BuildPartSeats() override
	{
		this->result.SetSeatInfo(1, "Leather");
	}

	void BuildPartDetails() override
	{
		this->result.SetDetails("CycleMotors Inc.", 2042);
	}

	Vehicle &GetResult() override {
		return this->result;	
	}

private:
	Vehicle result;
};

class TruckBuilder : public IVehicleBuilder {

public:


	void BuildPartSeats() override
	{
		this->result.SetSeatInfo(3, "Fabric");
	}

	void BuildPartDetails() override
	{
		this->result.SetDetails("TruckyTrucks", 2043);
	}

	Vehicle &GetResult() override {
		return result;		
	}

private:
	Vehicle result;
};

class VehicleShop {

public:
	VehicleShop() = default;
	~VehicleShop() = default;

	void Construct(IVehicleBuilder &builder) const {
		builder.BuildPartSeats();
		builder.BuildPartDetails();
	}

};

int main(int argc, char *const argv[])
{
	VehicleShop director;
	
	MotorcycleBuilder bMotocycles;
	TruckBuilder bTrucks;

	director.Construct(bMotocycles);
	Vehicle motor = bMotocycles.GetResult();

	director.Construct(bTrucks);
	Vehicle truck = bTrucks.GetResult();

	motor.Display();
	truck.Display();

	return 0;
}
