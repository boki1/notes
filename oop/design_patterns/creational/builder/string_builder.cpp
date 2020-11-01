#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>

namespace stringbuilder {

    class StringBuilder {
    public:
        StringBuilder() {
            this->str = new char[StringBuilder::INITIAL_SIZE];
            this->capacity = this->length = StringBuilder::INITIAL_SIZE - 1;
            this->str[StringBuilder::INITIAL_SIZE - 1] = 0;
            this->length = 0;
        }

        ~StringBuilder() {
            delete[] this->str;
        }

    public:
        ssize_t GetLength() const { return this->length; }

        void Append(const std::string &other) {
            if (this->length + other.size() > this->capacity) {
                char *p = this->str;
                ssize_t new_capacity = strlen(p) + strlen(other.c_str());
                new_capacity += (new_capacity / 2) + sizeof "";
                this->str = new char[new_capacity];
                this->capacity = new_capacity;
                strcpy(this->str, p);
                delete[] p;
            }

            strcat(this->str, other.c_str());
            this->length += other.length();
        }

        std::string AsString() {
            std::string result(this->str);
            return result;
        }


        friend std::ostream &operator<<(std::ostream &l, StringBuilder &s);

    private:
        static const ssize_t INITIAL_SIZE = 1 << 2;
        char *str;
        ssize_t length;
        ssize_t capacity;
    };

    std::ostream &operator<<(std::ostream &l, StringBuilder &s) {
        l << s.str << " (" << s.length << ")" << '\n';

        return l;
    }

}  // namespace stringbuilder

int main(int argc, char *const argv[]) {
    stringbuilder::StringBuilder s;
    std::string line;
    for (int _ = 0; _ < 5; _++) {
        std::cout << "Input something: ";
        std::cin >> line;
        s.Append(line);
    }

    std::string result = s.AsString();
    std::cout << result << '\n';

    return EXIT_SUCCESS;
}
