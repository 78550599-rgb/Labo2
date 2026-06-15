# main.py

print("=== Depurar RPG Live Games ===")

nombre = input("Ingresa tu nombre: ")
print("\nhttps://github.com/78550599-rgb/Labo2.git")
print(f"Bienvenido, {nombre}.")

nivel = 1
experiencia = 0

print("\nEstado inicial:")
print(f"Nivel: {nivel}")
print(f"Experiencia: {experiencia}")

experiencia += 50

if experiencia >= 50:
    nivel += 1
    print("\n¡Has subido de nivel!")

print("\nEstado actual:")
print(f"Nivel: {nivel}")
print(f"Experiencia: {experiencia}")