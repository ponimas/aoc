#include <fstream>
#include <iostream>

#include "boost/variant.hpp"
#include <fmt/core.h>
#include <fmt/ranges.h>

typedef boost::make_recursive_variant<
    int, std::vector<boost::recursive_variant_>>::type packet;

int main(int argc, char *argv[]) {
  if (argc < 2) {
    return 1;
  }

  std::ifstream file(argv[1]);

  for (std::string line; std::getline(file, line);) {
    if (line.empty())
      continue;

    packet pkt{};
    int pos = 1;
    packet* p = &pkt;
    packet* prev;
    std::cout << line << std::endl;
    while (pos < line.size()) {
      std::cout << pos << std::endl;
      if (line[pos] == '[') {
        packet sub{};
        prev = p;
        p = &sub;
        pos++;
      } else if (line[pos] == ']') {
        p = prev;
        pos++;
      } else {
        int nxt = line.find_first_not_of("0123456789", pos);
        std::cout << line.substr(pos, nxt - pos) << "|" << std::endl;
        pos = nxt + 1;
      }
    }
  }
}
