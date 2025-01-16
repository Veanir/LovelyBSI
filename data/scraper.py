import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig, CacheMode
from urllib.parse import urljoin

BASE_URL = "https://wazniak.mimuw.edu.pl"

# List of all pages to crawl (lectures and labs)
PAGES_TO_CRAWL = [
    # Lectures
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_1:Wprowadzenie_do_problematyki_bezpieczeństwa_systemów_komputerowych",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_2:Podstawowe_definicje_i_problemy",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_3:Ogólne_własności_bezpieczeństwa_informacji",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_4:Podstawowe_elementy_kryptografii",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_5:Wykorzystanie_kryptografii",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_6:",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_7:",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_8:",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_9:",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_10:",
    
    # Labs
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_1:Mechanizmy_lokalnej_kontroli_dostępu",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_2:Domeny_zaufania,_mechanizmy_kontroli_zdalnego_dostępu",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_3:Umacnianie_ochrony_systemu_opearacyjnego_serwerowych_środowisk_MS_Windows",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_4:Utwardzanie_ochrony_systemu_operacyjnego_serwerowych_środowisk_Linuksowych:_RSBAC",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_5:Modularne_systemy_uwierzytelniania_i_kontroli_dostępu_do_systemu_operacyjnego",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_6:Ograniczone_środowiska_wykonywania_aplikacji,_ograniczone_powłoki_systemu_operacyjnego_środowisk_serwerowych,_delegacja_uprawnień_administracyjnych",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_7:Systemy_kryptograficznej_ochrony_komunikacji_warstwy_aplikacyjnej",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_8:Zabezpieczanie_komunikacji_pocztowej,_integracja_mechanizmów_kryptograficznych_z_usługami_pocztowymi",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_9:Zabezpieczanie_serwerów_usług_aplikacyjnych_na_przykładzie_WWW_(uwięzienie_w_piaskownicy)",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_10:Konstrukcja_urzędów_certyfikacji_standardu_OpenSSL,_zarządzanie_certyfikatami",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_11:Tworzenie_sieci_VPN_w_środowisku_Linux_i_Windows",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_12:Systemy_programowych_zapór_sieciowych",
    "/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_laboratorium_13:Systemy_wykrywania_włamań_IDS_(snort)"
]

async def main():
    # Configure browser
    browser_config = BrowserConfig(headless=True)
    
    # Configure the crawler
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        word_count_threshold=1,  # Don't skip any content
        page_timeout=80000
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        all_content = []
        
        # Crawl each page
        for page in PAGES_TO_CRAWL:
            url = urljoin(BASE_URL, page)
            print(f"Crawling: {url}")
            try:
                result = await crawler.arun(url=url, config=crawler_config)
                if result.markdown:
                    # Extract title from the page path
                    title = page.split(":")[-1].replace("_", " ")
                    all_content.append(f"# {title}\n\n{str(result.markdown)}\n\n---\n\n")
            except Exception as e:
                print(f"Error crawling {url}: {str(e)}")
        
        # Save all content to a single markdown file
        with open("data/output.md", "w", encoding='utf-8') as f:
            f.write("\n".join(all_content))

if __name__ == "__main__":
    asyncio.run(main())