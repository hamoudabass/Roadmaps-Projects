# Unit Converter
A Web page to convert between different units of measurement part of the [Roadmap.sh](https://roadmap.sh) frontend project challenges.

## 📁 Project Structure

```
unit-converter/
├── index.html
├── pages/
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
└── assets/
    ├── css/
    │   └── styles.css
    └── js/
        └── script.js
```

--

## ✨ Features


- 📏 **Length Conversion** — meters, millimeters, centimeters, kilometers, inches, feet, yards, miles
- ⚖️ **Weight Conversion** — milligrams, grams, kilograms, ounces, pounds
- 🌡️ **Temperature Conversion** — Celsius, Fahrenheit, Kelvin-
---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/hamoudabass/Roadmaps-Projects.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Roadmaps-Projects/unitconverter
   ```

3. Open `index.html` in your browser or use **Live Server** in VS Code.

---

## 🧮 Conversion Logic

### Length
All values are converted through **meters** as the base unit.

### Weight
All values are converted through **grams** as the base unit.

### Temperature
Temperature uses direct formulas since multiplication alone isn't sufficient:

| From → To | Formula |
|---|---|
| Celsius → Fahrenheit | `(C × 9/5) + 32` |
| Celsius → Kelvin | `C + 273.15` |
| Fahrenheit → Celsius | `(F - 32) × 5/9` |
| Kelvin → Celsius | `K - 273.15` |

## 🛠️ Built With

- HTML5
- CSS3 (View Transitions API)
- Vanilla JavaScript (No frameworks)

---

## 📌 Roadmap.sh Challenge

This project is part of the [Roadmap.sh Frontend Projects](https://roadmap.sh/projects/unit-converter).

---

## 👤 Author

**hamoudabass** — [GitHub](https://github.com/hamoudabass)