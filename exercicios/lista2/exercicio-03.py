xgreen = float(input('Digite o valor da banda espectral da faixa do verde (Xgreen) = '))
xred = float(input('Digite o valor da banda espectral da faixa do vermelho (Xred) = '))
xnir = float(input('Digite o valor da banda espectral da faixa do Infravermelho próximo (Xnir) = '))

ndwi = (xgreen - xnir) / (xgreen + xnir)
ndvi = (xnir - xred) / (xnir + xred)

print("\n--------Resultado--------")
print(f"NDWI = {ndwi}")
print(f"NDVI = {ndvi}")
