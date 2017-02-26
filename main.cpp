#include <iostream>
#include "BigIntegerLibrary.hh"
using namespace std;

int isFactorial(BigInteger n, BigInteger i = 1) {
	if (n == i) {
		return i;
	}
	else if (n % i == 0) {
		return isFactorial(n / i, i + 1);
	}
	else {
		return -1;
	}
}

int main() {
	cout << isFactorial(51090942171709440000);
	return 0;
}