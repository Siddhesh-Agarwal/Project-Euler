#include <cstddef>
#include <iostream>
#define THRESHOLD 0.1

bool is_prime(int n) {
  if (n <= 1)
    return false;
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}

int main() {
  std::size_t value_on_diagonal = 1;
  std::size_t diagonal_count = 0;
  std::size_t prime_count = 0;
  std::size_t size_length = 1;
  while (true) {

    if (is_prime(value_on_diagonal)) {
      prime_count++;
    }
    if (diagonal_count % 4 == 0) {
      size_length += 2;
    }
    if (static_cast<double>(prime_count) / diagonal_count < THRESHOLD) {
      std::cout << size_length - 2 << std::endl;
      return 0;
    }
    value_on_diagonal += size_length - 1;
    diagonal_count++;
  }
  return 0;
}
