#include <ctime>
#include <cstdlib>

#include <iostream>
#include <chrono>
#include <thread>


void show_date(void) {
    const auto now = std::chrono::system_clock::now();
    const std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    std::cout << "Current date: " << std::ctime(&now_time) << std::endl;
}

int main(void) {
    std::thread worker(show_date);
    worker.join();
    return EXIT_SUCCESS;
}
