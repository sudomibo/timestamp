#include <cstdio>
#include <chrono>

static long int get_current_timestamp() {
	const auto now = std::chrono::system_clock::now();
	return std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count();
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char** argv) {
	printf("%ld\n", get_current_timestamp());
	return 0;
}

