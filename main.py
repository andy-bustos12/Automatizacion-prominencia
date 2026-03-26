from playwright.sync_api import sync_playwright
from youtube import go_to_youtube

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://amerikancash.com/compra-y-venta-de-dolares/")
        page.wait_for_selector("(//a[@class='elementor-item'][normalize-space()='Precios'])[1]")
        page.wait_for_timeout(5000)
        page.click("(//a[@class='elementor-item'][normalize-space()='Precios'])[1]")
        page.wait_for_timeout(4000)
        print("Redirigiendo a youtube..")  # Espera 2 segundos para que la página cargue completamente
        go_to_youtube(page, browser)
        import sys
        title = page.title()
        print(title.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))
        browser.close()

if __name__ == "__main__":
    main()