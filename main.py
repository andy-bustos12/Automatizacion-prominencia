from playwright.sync_api import sync_playwright
from youtube import go_to_dinorank

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
      # Espera 2 segundos para que la página cargue completamente
        go_to_dinorank(browser)
        browser.close()

if __name__ == "__main__":
    main()