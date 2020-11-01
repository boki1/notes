#include <algorithm>
#include <iostream>

//////
// Widgets and Labels
//
class Label {
public:
    Label() : contents("Label") {}

    void Display() { std::cout << contents << std::endl; }

    void Set(std::string label_contents) { contents = label_contents; }
    const std::string& Get() const { return contents; }

protected:
    std::string contents;
};

class Widget {
public:
	Widget() = default;
	Widget(Label *l) : label(l) {}
    virtual void Display() = 0;
    void SetLabel(std::string label_contents) { label->Set(label_contents); }

protected:
    Label* label;
};

class DoubleLineWidget : public Widget {
public:
	DoubleLineWidget(Label *l) { this->label = l; }

    void Display() {
	std::string l = label->Get();
	std::string horizontal_border(l.size() + 4, '=');
	std::string padding(l.size() / 2, ' ');
	std::cout << "+  " << horizontal_border << "  +" << '\n';
	std::cout << "+  " << padding << l << padding << "  +" << '\n';
	std::cout << "+  " << horizontal_border << "  +" << '\n';
    }
};

class SingleLineWidget : public Widget {
public:
	SingleLineWidget(Label *l) { this->label = l; }

    void Display() {
	std::string l = label->Get();
	std::string horizontal_border(l.size() + 4, '-');
	std::string padding(l.size() / 2, ' ');
	std::cout << "+  " << horizontal_border << "  +" << '\n';
	std::cout << "+  " << padding << l << padding << "  +" << '\n';
	std::cout << "+  " << horizontal_border << "  +" << '\n';
    }
};

class LowerCaseLabel : public Label {
public:
    LowerCaseLabel(std::string label_contents) {
	contents = label_contents;
	std::transform(contents.begin(), contents.end(), contents.begin(),
		       ::tolower);
    }
};

class UpperCaseLabel : public Label {
public:
    UpperCaseLabel(std::string label_contents) {
	contents = label_contents;
	std::transform(contents.begin(), contents.end(), contents.begin(),
		       ::toupper);
    }
};

//////
// Widget Factories

class WidgetFactory {
public:
    virtual Widget *CreateWidget() = 0;
    virtual Label *CreateLabel() = 0;
};

class DoubleLineWidgetFactory : public WidgetFactory {
    Widget *CreateWidget() override {
		Label *l = this->CreateLabel();
		DoubleLineWidget *dlw = new DoubleLineWidget(l);
		return dlw;
	}

    Label *CreateLabel() override {
		return new UpperCaseLabel("aSdF");
	}
};

class SingleLineWidgetFactory : public WidgetFactory {
	Widget *CreateWidget() override {
		Label *l = this->CreateLabel();
		SingleLineWidget *slw = new SingleLineWidget(l);
		return slw;
	}

	Label *CreateLabel() override {
		return new LowerCaseLabel("aSdF");
	}
};

int main(int argc, char* const argv[]) {
	WidgetFactory *factoryA = new DoubleLineWidgetFactory();
	WidgetFactory *factoryB = new SingleLineWidgetFactory();

	Widget *fromA = factoryA->CreateWidget();
	Widget *fromB = factoryB->CreateWidget();

	fromA->Display();
	std::string separator(16, '~');
	std::cout << '\n' << separator << "\n\n";
	fromB->Display();

    return 0;
}

