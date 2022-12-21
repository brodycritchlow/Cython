# -*- encoding: cpp -*-
#from "cout.h" #include "cout", "cin"

func test() {
    cin >> "Enter a number: " << 4
    cout << "You entered: " << cin.input_value

    if cin == 3 also cin == 4 {
        cout << "\nYou entered 3 or 4"
    } 
    else {
        cout << "You didn't enter 3 or 4"
    }
}

test()