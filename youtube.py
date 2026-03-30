import sys

def go_to_dinorank(browser):
    # Abrir nueva pestaña y entrar a DinoRank
    email = "seo@agenciadigitalamd.com"
    password = "SEOMnbvcxz1"

    try:
        dinorank_page = browser.new_page()
        dinorank_page.goto("https://dinorank.com/login/")
        dinorank_page.wait_for_load_state("networkidle")
        dinorank_page.wait_for_timeout(3000)
        dinorank_page.fill("//input[@id='usuario']", email)
        dinorank_page.fill("//input[@id='password']", password)
        dinorank_page.click("//button[@id='botonLogin']")
        dinorank_page.wait_for_load_state("networkidle")
        dinorank_page.wait_for_timeout(3000)
        title = dinorank_page.title()
        print(title.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))
    except Exception as e:
        print(f"Error al iniciar sesión en DinoRank: {e}")
        browser.close()
    # Ir a TF*IDF y prominencia
    dinorank_page.goto("https://dinorank.com/densidad-prominencia/")
    dinorank_page.wait_for_load_state("networkidle")
    dinorank_page.wait_for_timeout(3000)

    # Seleccionar el proyecto amerikancash.com
    dinorank_page.wait_for_selector("//div[@class='dropdown-icon']")
    dinorank_page.click("//div[@class='dropdown-icon']")
    dinorank_page.wait_for_timeout(1500)
    dinorank_page.fill("input#inputSelectorProyecto", "amerikancash")
    dinorank_page.wait_for_timeout(1500)
    dinorank_page.click("li:has-text('amerikancash.com')")
    dinorank_page.wait_for_timeout(2000)
    print("Proyecto amerikancash.com seleccionado.")

    # Ingresar keyword y URL
    keyword = "compra y venta de dolares"
    url_analizar = "https://amerikancash.com/compra-y-venta-de-dolares/"
    dinorank_page.fill("input#keyword", keyword)
    dinorank_page.fill("input#url", url_analizar)
    print("Keyword y URL ingresados.")

    # Click en Analizar y confirmar modal
    dinorank_page.click("button#buscaKresearch")
    dinorank_page.wait_for_timeout(2000)
    dinorank_page.click("button.confirm")
    print("Analisis iniciado...")

    # Esperar a que carguen las graficas
    dinorank_page.wait_for_selector("[class*='grafica'], [class*='chart'], canvas, [id*='grafica']", timeout=60000)
    dinorank_page.wait_for_timeout(3000)
    print("Graficas de prominencia cargadas.")
