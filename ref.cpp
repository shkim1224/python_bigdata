#include <iostream>

int main() {
    int originalVariable = 10;
    int &referenceVariable = originalVariable;

    std::cout << "Original variable: " << &originalVariable << std::endl;
    std::cout << "Reference variable: " << &referenceVariable << std::endl;

    // Modifying the value through the reference variable
    referenceVariable = 20;

    std::cout << "Modified original variable: " << originalVariable << std::endl;
    std::cout << "Modified reference variable: " << referenceVariable << std::endl;

    return 0;
}
