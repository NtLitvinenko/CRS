#include <iostream>
#include "CRS.h"
#include <thread>
#include <chrono>
using namespace std;

int main(){
    system("chcp 65001 > nul");
    Win *pixs = new Win(120, 30, "Bussy");
    using namespace std::this_thread; // sleep_for, sleep_until
    using namespace std::chrono; // nanoseconds, system_clock, seconds

    while (true){
        sleep_for(milliseconds(50));
        pixs->edit_rgb(4, 4, {255, 0, 0});
        pixs->print();
        sleep_for(milliseconds(50));
        pixs->edit_rgb(4, 4, {0, 255, 0});
        pixs->print();
        sleep_for(milliseconds(50));
        pixs->edit_rgb(4, 4, {0, 0, 255});
        pixs->print();
    }
}