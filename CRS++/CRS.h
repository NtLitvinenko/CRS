#include <iostream>
#include <vector>
#include <string>

using namespace std;

string print_rgb(int r, int g, int b, string text) {
    return "\033[38;2;" + to_string(r) + ";" + to_string(g) + ";" + to_string(b) + "m" + text + "\033[0m";
}

class Win {
private:
    int x;
    int y;
    string name;
    vector<vector<string>> pixels;
public:
    Win(int x, int y, string name) {
        this->x = x;
        this->y = y;
        this->name = name;
        this->pixels = vector<vector<string>>(y, vector<string>(x, "█"));
    }

    void edit_rgb(int x, int y, vector<int> rgb = {255, 255, 255}, string symbol = "█") {
        this->pixels[y][x] = print_rgb(rgb[0], rgb[1], rgb[2], symbol);
    }

    void print() {
        for (int i = 0; i < this->y; i++) {
            for (int j = 0; j < this->x; j++) {
                if (j != this->x - 1) {
                    cout << this->pixels[i][j];
                } else {
                    cout << this->pixels[i][j] << endl;
                }
            }
        }
    }
};