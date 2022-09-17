def massa(imc):
    if imc < 18.5:
        resul = "Muito baixo do peso"
    elif 18.5 <= imc < 25:
        resul = "Peso Normal"
    elif 25 <= imc < 30:
        resul = "Pré-Obesidade"
    elif 30 <= imc < 34:
        resul = "Obesidade Grau I"
    elif 35 <= imc < 40:
        resul = "Obesidade Grau I"
    elif imc >= 40:
        resul = "Obesidade Grau III"
    return resul

r = massa(24)
print(r)