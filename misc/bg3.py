languages = [
    ('ar', 'العربيّة', 'أضف الى سلة التسوق'),
    ('ca', 'català', 'Afegeix a la cistella'),
    ("cs", 'česky', 'Vložit do košíku'),
    ("da", 'dansk', 'Læg i kurv'),
    ('de', 'Deutsch', 'In Warenkorb legen'),
    ("en-gb", 'English', 'Add to basket'),
    ("el", 'Ελληνικά', 'Προσθήκη στο καλάθι'),
    ("es", 'español', 'Añadir al carrito'),
    ("fi", 'suomi', 'Lisää koriin'),
    ("fr", 'français', 'Ajouter au panier'),
    ("it", 'italiano', 'Aggiungi al carrello'),
    ("ko", '한국어', '장바구니 담기'),
    ("nl", 'Nederlands', 'Voeg aan winkelmand toe'),
    ("pl", 'polski', 'Dodaj do koszyka'),
    ("pt", 'Português', 'Adicionar ao carrinho'),
    ("pt-br", 'Português Brasileiro', 'Adicionar à cesta'),
    ("ro", 'Română', 'Adauga in cos'),
    ("ru", 'Русский', 'Добавить в корзину'),
    ("sk", 'Slovensky', 'Pridať do košíka'),
    ("uk", 'Українська', 'Додати в кошик'),
    ("zh-hans", '简体中文', 'Add to basket'),
]
x = []
for row in languages:
    x.append(row[0])
print(x)
y = [row[0] for row in languages]
print(y)