import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_wikipedia_page(topic):
    url = f"https://fr.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Une erreur s'est produite lors de la requete : {response.status_code}, Verifiez bien que la page existe.")
        return None

def get_article_title(soup):
    return soup.find('h1').text

def get_article_summary(soup):
    content_div = soup.find('div', class_='mw-parser-output')
    
    if not content_div:
        return "Contenu introuvable."

    paragraphs = content_div.find_all('p', recursive=False) 

    for paragraph in paragraphs:

        if paragraph.text.strip() and not paragraph.find_parent('div', class_='hatnote'):

            text = paragraph.text.strip()
            if len(text) > 20:
                return text

    return "Aucun résumé disponible."

def get_headings(soup):
    headings =[heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://fr.wikipedia.org{href}")
    return list(set(links))[:5]

while True:
    topic = input("Entrez le sujet de votre recherche (ou appuyez sur 'q' pour quitter): ").strip()
    if topic.lower() == "q":
        break
    page_content = get_wikipedia_page(topic)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        realted_links = get_related_links(soup)

        print("\n--- Details de l'article ---")
        print(f"\nTitre : {title}")
        print(f"\nResume : \n{summary}")
        print("\n--- Contenu ---")
        for heading in headings[:5]:
            print(f"- {heading}")
        print("\n--- Liens ---")
        for link in realted_links:
            print(f"- {link}")

        p = input("Voulez vous enregistrer l'article dans un fichier ? (o/n) : ").strip().lower()
        if p == "o":
            with open(f"{title}.txt", "w", encoding="utf-8") as file:
                file.write(title + "\n\n" + summary + "\n\n" + "\n".join(headings[:5]) + "\n\n" + "\n".join(realted_links))
            print("L'article a bien ete enregistré.")
        if p == "n":
            pass
