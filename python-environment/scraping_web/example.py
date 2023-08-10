from selenium import webdriver

# URL de la página de búsqueda
url = "https://www.amazon.com/s/?keywords=laptop"

# Iniciar el navegador y abrir la página en el
driver = webdriver.Chrome()
driver.get(url)

# Encuentra todos los elementos de productos en la página
product_elements = driver.find_elements_by_css_selector('.s-result-item')

# Itera a través de los elementos y extrae la información
for product_element in product_elements:
    try:
        # Encuentra el elemento que contiene el nombre del producto
        name_element = product_element.find_element_by_css_selector('.a-size-medium')
        product_name = name_element.text
        
        # Encuentra el elemento que contiene el precio del producto
        price_element = product_element.find_element_by_css_selector('.a-offscreen')
        product_price = price_element.text
        
        # Imprime la información del producto
        print("Producto:", product_name)
        print("Precio:", product_price)
        print("-" * 30)
    except:
        # Si no se pueden encontrar los elementos, pasa al siguiente producto
        pass

# Cierra el navegador
driver.quit()