def massa(imc):
    if imc < 18.50:
        resul = "Muito baixo do peso"
    elif 18.5 <= imc < 25.0:
        resul = "Peso Normal"
    elif 25.0 <= imc < 29.99:
        resul = "Pré-Obesidade"
    elif 30.0 <= imc < 34.99:
        resul = "Obesidade Grau I"
    elif 35.00 <= imc < 39.99:
        resul = "Obesidade Grau I"
    elif imc >= 40:
        resul = "Obesidade Grau III"
    return resul

