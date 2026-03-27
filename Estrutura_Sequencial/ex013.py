gb = float(input("Digite o valor em GB: ").replace(',', '.'))

mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB equivalem a:")
print(f"- {mb:.2f} Megabytes (MB)")
print(f"- {kb:.2f} Kilobytes (KB)")
