# Crear una función que calcule el descuento aplicado a un producto. Recibe
# dos parámetros (precio original y precio con descuento) y devuelve el
# porcentaje de descuento aplicado.

def calculate_discount (original_price, price_with_discount):
    #Function calculates the amount of discount
    #Takes the original price and the modified price
    #Returns the result of the calculation which is the amount of discount
    discount_calculation = original_price - price_with_discount
    return discount_calculation

original_price_txt = input("Ingrese el precio original")
original_price_float = int(original_price_txt)

price_with_discount_txt = input("Ingrese el precio con descuento aplicado")
price_with_discount_float = int(price_with_discount_txt)

print(f"El descuento corresponde a ${calculate_discount(original_price_float, price_with_discount_float)}")