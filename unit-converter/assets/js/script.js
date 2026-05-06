const result = document.getElementById("conversion-result");

function conversionLength(){
    
    const length = Number(document.getElementById("length").value);
    const convertFrom = document.getElementById("convertFrom").value;
    const convertTo = document.getElementById("convertTo").value;


    lengthConversion = {
        m : 1,
        mm : 1000,
        cm : 100,
        km : 0.001,
        in : 39.37,
        ft : 3.281,
        yd : 1.094,
        mi : 0.001609,
    };

    let toMeter = length / lengthConversion[convertFrom];
    let toUnitWanted = toMeter * lengthConversion[convertTo];

    result.textContent = `${length} ${convertFrom} = ${toUnitWanted} ${convertTo}`;
    
}

function conversionWeigth() {
    const weight = Number(document.getElementById("weigth").value);
    const convertFrom = document.getElementById("convertFrom").value;
    const convertTo = document.getElementById("convertTo").value;

    const weightConversion = {
        mg: 1000,   // 1g = 1000mg
        g:  1,      // base unit
        kg: 0.001,  // 1g = 0.001kg
        oz: 0.03527, // 1g = 0.03527oz
        lb: 0.00220, // 1g = 0.00220lb
    };

    let toGram = weight / weightConversion[convertFrom];
    let toUnitWanted = toGram * weightConversion[convertTo];

    result.textContent = `${weight} ${convertFrom} = ${toUnitWanted.toFixed(2)} ${convertTo}`;
} 

function conversionTemperature() {
    const temperature = Number(document.getElementById("temperature").value);
    const convertFrom = document.getElementById("convertFrom").value;
    const convertTo = document.getElementById("convertTo").value;
   

    // Étape 1 — Convertir en Celsius (base)
    let toCelsius;

    if (convertFrom === "c") {
        toCelsius = temperature;
    } else if (convertFrom === "f") {
        toCelsius = (temperature - 32) * (5 / 9);
    } else if (convertFrom === "k") {
        toCelsius = temperature - 273.15;
    }

    // Étape 2 — Convertir Celsius vers l'unité voulue
    let toUnitWanted;

    if (convertTo === "c") {
        toUnitWanted = toCelsius;
    } else if (convertTo === "f") {
        toUnitWanted = (toCelsius * 9 / 5) + 32;
    } else if (convertTo === "k") {
        toUnitWanted = toCelsius + 273.15;
    }

    result.textContent = `${temperature} °${convertFrom.toUpperCase()} = ${toUnitWanted.toFixed(2)} °${convertTo.toUpperCase()}`;
}
    