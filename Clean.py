import pandas as pd


file_name = 'amazon.csv' 

try:
    print(f"Cargando {file_name}...")
    df = pd.read_csv(file_name)
    print("¡Archivo cargado correctamente!")
    

    print("Iniciando limpieza...")
    

    df['actual_price'] = df['actual_price'].astype(str)
    

    df['actual_price'] = df['actual_price'].str.replace('₹', '', regex=False)
    df['actual_price'] = df['actual_price'].str.replace('$', '', regex=False)
    df['actual_price'] = df['actual_price'].str.replace(',', '', regex=False)
    

    df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')
    

    print("-" * 30)
    print("Tipos de datos finales:")
    print(df['actual_price'].dtypes)
    print("\nPrimeros 5 precios limpios:")
    print(df[['actual_price']].head())
    
except FileNotFoundError:
    print(f"ERROR: No encuentro el archivo '{file_name}'.")
    print("Asegúrate de que el archivo CSV esté en la misma carpeta que este script.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")






if 'discounted_price' in df.columns:
    df['discounted_price'] = df['discounted_price'].astype(str)
    df['discounted_price'] = df['discounted_price'].str.replace('₹', '', regex=False)
    df['discounted_price'] = df['discounted_price'].str.replace('$', '', regex=False)
    df['discounted_price'] = df['discounted_price'].str.replace(',', '', regex=False)
    df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
    print("Columna 'discounted_price' limpia.")


if 'rating' in df.columns:
    df['rating'] = df['rating'].astype(str).str.replace('|', '', regex=False)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    print("Columna 'rating' limpia.")


if 'rating_count' in df.columns:
    df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '', regex=False)
    df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')
    print("Columna 'rating_count' limpia.")

output_file = 'amazon_cleaned.csv'
df.to_csv(output_file, index=False)

print("-" * 30)
print(f"Archivo guardado como: {output_file}")