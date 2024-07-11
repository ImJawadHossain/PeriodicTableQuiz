import random
import time

# Dictionary of elements with atomic numbers and masses
elements = {
    1: {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "atomic_mass": 1},
    2: {"name": "Helium", "symbol": "He", "atomic_number": 2, "atomic_mass": 4},
    3: {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "atomic_mass": 7},
    4: {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "atomic_mass": 9},
    5: {"name": "Boron", "symbol": "B", "atomic_number": 5, "atomic_mass": 11},
    6: {"name": "Carbon", "symbol": "C", "atomic_number": 6, "atomic_mass": 12},
    7: {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "atomic_mass": 14},
    8: {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "atomic_mass": 16},
    9: {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "atomic_mass": 19},
    10: {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "atomic_mass": 20},
    11: {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "atomic_mass": 23},
    12: {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "atomic_mass": 24},
    13: {"name": "Aluminium", "symbol": "Al", "atomic_number": 13, "atomic_mass": 27},
    14: {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "atomic_mass": 28},
    15: {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "atomic_mass": 31},
    16: {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "atomic_mass": 32},
    17: {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "atomic_mass": 35.5},
    18: {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "atomic_mass": 40},
    19: {"name": "Potassium", "symbol": "K", "atomic_number": 19, "atomic_mass": 39},
    20: {"name": "Calcium", "symbol": "Ca", "atomic_number": 20, "atomic_mass": 40},
    21: {"name": "Scandium", "symbol": "Sc", "atomic_number": 21, "atomic_mass": 45},
    22: {"name": "Titanium", "symbol": "Ti", "atomic_number": 22, "atomic_mass": 48},
    23: {"name": "Vanadium", "symbol": "V", "atomic_number": 23, "atomic_mass": 51},
    24: {"name": "Chromium", "symbol": "Cr", "atomic_number": 24, "atomic_mass": 52},
    25: {"name": "Manganese", "symbol": "Mn", "atomic_number": 25, "atomic_mass": 55},
    26: {"name": "Iron", "symbol": "Fe", "atomic_number": 26, "atomic_mass": 56},
    27: {"name": "Cobalt", "symbol": "Co", "atomic_number": 27, "atomic_mass": 59},
    28: {"name": "Nickel", "symbol": "Ni", "atomic_number": 28, "atomic_mass": 59},
    29: {"name": "Copper", "symbol": "Cu", "atomic_number": 29, "atomic_mass": 63.5},
    30: {"name": "Zinc", "symbol": "Zn", "atomic_number": 30, "atomic_mass": 65},
    31: {"name": "Gallium", "symbol": "Ga", "atomic_number": 31, "atomic_mass": 70},
    32: {"name": "Germanium", "symbol": "Ge", "atomic_number": 32, "atomic_mass": 73},
    33: {"name": "Arsenic", "symbol": "As", "atomic_number": 33, "atomic_mass": 75},
    34: {"name": "Selenium", "symbol": "Se", "atomic_number": 34, "atomic_mass": 79},
    35: {"name": "Bromine", "symbol": "Br", "atomic_number": 35, "atomic_mass": 80},
    36: {"name": "Krypton", "symbol": "Kr", "atomic_number": 36, "atomic_mass": 84},
    37: {"name": "Rubidium", "symbol": "Rb", "atomic_number": 37, "atomic_mass": 85},
    38: {"name": "Strontium", "symbol": "Sr", "atomic_number": 38, "atomic_mass": 88},
    39: {"name": "Yttrium", "symbol": "Y", "atomic_number": 39, "atomic_mass": 89},
    40: {"name": "Zirconium", "symbol": "Zr", "atomic_number": 40, "atomic_mass": 91},
    41: {"name": "Niobium", "symbol": "Nb", "atomic_number": 41, "atomic_mass": 93},
    42: {"name": "Molybdenum", "symbol": "Mo", "atomic_number": 42, "atomic_mass": 96},
    43: {"name": "Technetium", "symbol": "Tc", "atomic_number": 43, "atomic_mass": 98},
    44: {"name": "Ruthenium", "symbol": "Ru", "atomic_number": 44, "atomic_mass": 101},
    45: {"name": "Rhodium", "symbol": "Rh", "atomic_number": 45, "atomic_mass": 103},
    46: {"name": "Palladium", "symbol": "Pd", "atomic_number": 46, "atomic_mass": 106},
    47: {"name": "Silver", "symbol": "Ag", "atomic_number": 47, "atomic_mass": 108},
    48: {"name": "Cadmium", "symbol": "Cd", "atomic_number": 48, "atomic_mass": 112},
    49: {"name": "Indium", "symbol": "In", "atomic_number": 49, "atomic_mass": 115},
    50: {"name": "Tin", "symbol": "Sn", "atomic_number": 50, "atomic_mass": 119},
    51: {"name": "Antimony", "symbol": "Sb", "atomic_number": 51, "atomic_mass": 122},
    52: {"name": "Tellurium", "symbol": "Te", "atomic_number": 52, "atomic_mass": 128},
    53: {"name": "Iodine", "symbol": "I", "atomic_number": 53, "atomic_mass": 127},
    54: {"name": "Xenon", "symbol": "Xe", "atomic_number": 54, "atomic_mass": 131},
    55: {"name": "Caesium", "symbol": "Cs", "atomic_number": 55, "atomic_mass": 133},
    56: {"name": "Barium", "symbol": "Ba", "atomic_number": 56, "atomic_mass": 137},
    57: {"name": "Lanthanum", "symbol": "La", "atomic_number": 57, "atomic_mass": 139},
    58: {"name": "Cerium", "symbol": "Ce", "atomic_number": 58, "atomic_mass": 140},
    59: {"name": "Praseodymium", "symbol": "Pr", "atomic_number": 59, "atomic_mass": 141},
    60: {"name": "Neodymium", "symbol": "Nd", "atomic_number": 60, "atomic_mass": 144},
    61: {"name": "Promethium", "symbol": "Pm", "atomic_number": 61, "atomic_mass": 145},
    62: {"name": "Samarium", "symbol": "Sm", "atomic_number": 62, "atomic_mass": 150},
    63: {"name": "Europium", "symbol": "Eu", "atomic_number": 63, "atomic_mass": 152},
    64: {"name": "Gadolinium", "symbol": "Gd", "atomic_number": 64, "atomic_mass": 157},
    65: {"name": "Terbium", "symbol": "Tb", "atomic_number": 65, "atomic_mass": 159},
    66: {"name": "Dysprosium", "symbol": "Dy", "atomic_number": 66, "atomic_mass": 163},
    67: {"name": "Holmium", "symbol": "Ho", "atomic_number": 67, "atomic_mass": 165},
    68: {"name": "Erbium", "symbol": "Er", "atomic_number": 68, "atomic_mass": 167},
    69: {"name": "Thulium", "symbol": "Tm", "atomic_number": 69, "atomic_mass": 169},
    70: {"name": "Ytterbium", "symbol": "Yb", "atomic_number": 70, "atomic_mass": 173},
    71: {"name": "Lutetium", "symbol": "Lu", "atomic_number": 71, "atomic_mass": 175},
    72: {"name": "Hafnium", "symbol": "Hf", "atomic_number": 72, "atomic_mass": 178},
    73: {"name": "Tantalum", "symbol": "Ta", "atomic_number": 73, "atomic_mass": 181},
    74: {"name": "Tungsten", "symbol": "W", "atomic_number": 74, "atomic_mass": 184},
    75: {"name": "Rhenium", "symbol": "Re", "atomic_number": 75, "atomic_mass": 186},
    76: {"name": "Osmium", "symbol": "Os", "atomic_number": 76, "atomic_mass": 190},
    77: {"name": "Iridium", "symbol": "Ir", "atomic_number": 77, "atomic_mass": 192},
    78: {"name": "Platinum", "symbol": "Pt", "atomic_number": 78, "atomic_mass": 195},
    79: {"name": "Gold", "symbol": "Au", "atomic_number": 79, "atomic_mass": 197},
    80: {"name": "Mercury", "symbol": "Hg", "atomic_number": 80, "atomic_mass": 200.6},
    81: {"name": "Thallium", "symbol": "Tl", "atomic_number": 81, "atomic_mass": 204},
    82: {"name": "Lead", "symbol": "Pb", "atomic_number": 82, "atomic_mass": 207},
    83: {"name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "atomic_mass": 209},
    84: {"name": "Polonium", "symbol": "Po", "atomic_number": 84, "atomic_mass": 209},
    85: {"name": "Astatine", "symbol": "At", "atomic_number": 85, "atomic_mass": 210},
    86: {"name": "Radon", "symbol": "Rn", "atomic_number": 86, "atomic_mass": 222},
    87: {"name": "Francium", "symbol": "Fr", "atomic_number": 87, "atomic_mass": 223},
    88: {"name": "Radium", "symbol": "Ra", "atomic_number": 88, "atomic_mass": 226},
    89: {"name": "Actinium", "symbol": "Ac", "atomic_number": 89, "atomic_mass": 227},
    90: {"name": "Thorium", "symbol": "Th", "atomic_number": 90, "atomic_mass": 232},
    91: {"name": "Protactinium", "symbol": "Pa", "atomic_number": 91, "atomic_mass": 231},
    92: {"name": "Uranium", "symbol": "U", "atomic_number": 92, "atomic_mass": 238},
    93: {"name": "Neptunium", "symbol": "Np", "atomic_number": 93, "atomic_mass": 237},
    94: {"name": "Plutonium", "symbol": "Pu", "atomic_number": 94, "atomic_mass": 244},
    95: {"name": "Americium", "symbol": "Am", "atomic_number": 95, "atomic_mass": 243},
    96: {"name": "Curium", "symbol": "Cm", "atomic_number": 96, "atomic_mass": 247},
    97: {"name": "Berkelium", "symbol": "Bk", "atomic_number": 97, "atomic_mass": 247},
    98: {"name": "Californium", "symbol": "Cf", "atomic_number": 98, "atomic_mass": 251},
    99: {"name": "Einsteinium", "symbol": "Es", "atomic_number": 99, "atomic_mass": 252},
    100: {"name": "Fermium", "symbol": "Fm", "atomic_number": 100, "atomic_mass": 257},
    101: {"name": "Mendelevium", "symbol": "Md", "atomic_number": 101, "atomic_mass": 258},
    102: {"name": "Nobelium", "symbol": "No", "atomic_number": 102, "atomic_mass": 259},
    103: {"name": "Lawrencium", "symbol": "Lr", "atomic_number": 103, "atomic_mass": 266},
    104: {"name": "Rutherfordium", "symbol": "Rf", "atomic_number": 104, "atomic_mass": 267},
    105: {"name": "Dubnium", "symbol": "Db", "atomic_number": 105, "atomic_mass": 268},
    106: {"name": "Seaborgium", "symbol": "Sg", "atomic_number": 106, "atomic_mass": 269},
    107: {"name": "Bohrium", "symbol": "Bh", "atomic_number": 107, "atomic_mass": 270},
    108: {"name": "Hassium", "symbol": "Hs", "atomic_number": 108, "atomic_mass": 269},
    109: {"name": "Meitnerium", "symbol": "Mt", "atomic_number": 109, "atomic_mass": 278},
    110: {"name": "Darmstadtium", "symbol": "Ds", "atomic_number": 110, "atomic_mass": 281},
    111: {"name": "Roentgenium", "symbol": "Rg", "atomic_number": 111, "atomic_mass": 282},
    112: {"name": "Copernicium", "symbol": "Cn", "atomic_number": 112, "atomic_mass": 285},
    113: {"name": "Nihonium", "symbol": "Nh", "atomic_number": 113, "atomic_mass": 286},
    114: {"name": "Flerovium", "symbol": "Fl", "atomic_number": 114, "atomic_mass": 289},
    115: {"name": "Moscovium", "symbol": "Mc", "atomic_number": 115, "atomic_mass": 290},
    116: {"name": "Livermorium", "symbol": "Lv", "atomic_number": 116, "atomic_mass": 293},
    117: {"name": "Tennessine", "symbol": "Ts", "atomic_number": 117, "atomic_mass": 294},
    118: {"name": "Oganesson", "symbol": "Og", "atomic_number": 118, "atomic_mass": 294},
}


def quiz(elements, max_atomic_number, min_atomic_number, quiz_format):
    # Filter elements based on atomic number <= max_atomic_number
    filtered_elements = [element for element in elements.values() if element['atomic_number'] <= max_atomic_number and element['atomic_number'] >= min_atomic_number] 
    # Shuffle the filtered elements and select them
    selected_elements = random.sample(filtered_elements, len(filtered_elements))
    start_time = time.time()

    score = 0
    for element in selected_elements:
        print()
        print(f"   👉Element :  {element['name']} ({element['symbol']})")
        try:
            user_input = float(input("   Enter the Number: "))
            if user_input == element[quiz_format]:
                print("   Correct!✅")
                score += 1
            else:
                print(f"   Wrong!❌ Correct answer: {element[quiz_format]}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nQuiz completed in {time_taken:.2f} seconds. OR {time_taken/60:.2f} minutes")
    print(f"Your score is: {score}/{len(filtered_elements)}")

if __name__ == "__main__":
    quiz_format = int(input("Atomic Number (1)  | Atomic Mass(2): "))
    
    min_atomic_number = int(input("Min atomic number: "))
    max_atomic_number = int(input("Max atomic number: "))
    if quiz_format == 1:
        while True:
            quiz(elements, max_atomic_number, min_atomic_number, "atomic_number")
            input("Press 1 for practice Again:  ")
        
    else:
         while True:
             quiz(elements,max_atomic_number,min_atomic_number, "atomic_mass")
             input("Press 1 for practice Again:  ")
         
         
         
    
