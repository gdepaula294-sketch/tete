#2. Crie um programa que calcule a área de um retângulo (base × altura) e o perímetro (2 × (base + altura)).
B = float(input('Digite sua base: '))
A = float(input('Digite sua altura: '))
#Calculo de área 
area = B * A
#Calculo de prerímetro
perimetro = (2*(B + A))

print(f'Seu retangulo tem {area} de áreas \ne {perimetro} de perímetros.')