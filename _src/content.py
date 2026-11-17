"""Single source of content, taken from atterer.de and Stahlkatalog 2026."""

IMG = "https://www-static.atterer.de/wp-content/uploads/"


def img(path):
    return IMG + path


LOGO = img("2024/03/Logo_stahlcenter_transparent_2024.png")
TOPCOMPANY = img("2026/01/TopCompany2026_EMailSignatur_DE.png")
ISO_CERT = img("2026/01/Zertifikat-DIN-EN-ISO-gueltig-bis-11122026.jpg")
ISO_LOGO = img("2022/09/logo-iso-9001.png")

COMPANY = {
    "name": "Atterer Stahlcenter GmbH",
    "street": "Siemensring 34",
    "city": "87616 Marktoberdorf",
    "phone": "+49 8342 / 9641 – 600",
    "phone_href": "tel:+4983429641600",
    "fax": "+49 8342 / 18 13",
    "email": "info@atterer.de",
    "career_email": "karriere@atterer.com",
    "hours": "Mo – Fr, 07:30 – 17:00 Uhr",
    "maps": "https://www.google.com/maps/search/?api=1&query=Atterer+Stahlcenter+GmbH+Siemensring+34+Marktoberdorf",
    "maps_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d566272.3968141536!2d10.169667708615384!3d47.94999538543669!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x41086410137ed691%3A0xf21222a479112089!2sAtterer%20Stahlcenter%20GmbH!5e0!3m2!1sde!2sde!4v1711114035636!5m2!1sde!2sde",
    "oneclick": "https://ntgt.de/a/s.aspx?s=496314X108573551X33548",
    "bewerber_ds": "https://usercontent.one/wp/www.atterer.de/wp-content/uploads/2022/09/bewerber_info_ds.pdf?media=1689164935",
    "social": [
        ("Facebook", "https://www.facebook.com/atterer.stahlcenter"),
        ("Instagram", "https://www.instagram.com/atterer_stahlcenter/"),
        ("LinkedIn", "https://www.linkedin.com/company/atterer-stahlcenter-gmbh/"),
        ("XING", "https://www.xing.com/pages/attererstahlcentergmbh"),
    ],
}

INTRO = [
    "Die Atterer Stahlcenter GmbH ist der Marktführer im Allgäu unter den Betonstahlbiegereien. Mit mehr als 150 Mitarbeitern am Standort in Marktoberdorf beliefern wir seit über 100 Jahren Bauunternehmen im bayerischen Raum und im angrenzenden Österreich mit Betonstahl und Bauprodukten.",
    "Aufgrund unseres vielseitigen Produktportfolios und dem Ziel uns kontinuierlich zu verbessern, ist das Atterer Stahlcenter ein innovativer Dienstleister und verlässlicher Partner für Bauunternehmer aller Größen.",
    "Das Atterer Stahlcenter in Marktoberdorf ist ein stetig wachsendes Unternehmen, das mit seinen Partnerunternehmen der Atterer Gruppe in Deutschland und Vorarlberg kontinuierlich seine Marktführerschaft ausbaut.",
]

PRODUCTS_INTRO = [
    "Auf unserem großzügigen 30.000 m² großen Gelände erwartet Sie eine vielfältige Auswahl an hochwertigen Stahlprodukten und Dienstleistungen. Unsere 12.000 m² große Halle beherbergt das gesamte Sortiment an Formstählen sowie unsere leistungsstarke Betonstahlbiegerei.",
    "Darüber hinaus bieten wir ein umfassendes Standardsortiment für Bauunternehmer, Schlosser, Stahl- und Metallbauer. Mit unserem modernen Maschinenpark bearbeiten wir alle Produkte nach Ihren individuellen Bedürfnissen.",
]

# Numbers: site + "Atterer in Zahlen" (Stahlkatalog 2026)
NUMBERS = [
    ("1886", "", "gegründet in Marktoberdorf"),
    ("150", "+", "motivierte Mitarbeiter"),
    ("30.000", " m²", "Gelände, davon 12.000 m² Halle"),
    ("25", "", "eigene LKWs"),
    ("1.000", "+", "Bauprojekte pro Jahr"),
    ("500", "+", "zufriedene Kunden"),
]

VALUES = [
    ("Höchste Qualität & Zuverlässigkeit", "Seit 2014 nach DIN EN ISO 9001 zertifiziert, jedes Jahr erfolgreich re-zertifiziert."),
    ("Vorsprung durch Innovation", "Moderner Maschinenpark, BAMTEC® und geschweißte Bewehrungsmodule für schnellere Baustellen."),
    ("Faire Preise", "Schnell, preisgünstig, unkompliziert – vom Einzelauftrag bis zum Großprojekt."),
    ("Partnerschaft auf Augenhöhe", "Familiengeführt in der 4. Generation. „Was will mein Kunde?“ – seit 1886."),
]

PRODUCTS = [
    {"slug": "bewehrungsstahl", "title": "Bewehrungsstahl", "short": "Gewi-Stahl SAS 500 / 550 Bewehrungssystem", "img": img("2024/03/Bewehrungsstahl.jpg"), "hero": img("2024/12/Stahl-2banner.jpg")},
    {"slug": "geschweisste-bewehrungsmodule", "title": "Geschweißte Bewehrungsmodule", "short": "Zeit- und somit Kosteneinsparung auf Ihren Baustellen", "img": img("2024/03/Geschweisste-Bewehrungsmodulel.jpg"), "hero": img("2022/08/image17a.jpg")},
    {"slug": "bamtec", "title": "BAMTEC®", "short": "Das wirtschaftliche Verfahren zur Bewehrung von Decken, Bodenplatten und Wänden aus Stahlbeton.", "img": img("2024/03/BAMTEC.jpg"), "hero": img("2022/08/image21.jpg")},
    {"slug": "oenorm-stahl", "title": "ÖNORM-Stahl", "short": "ÖMAT-Schlaufenmatte, Bewehrungsstahl nach ÖNORM, Überdeckungsstöße mit Schlaufe", "img": img("2024/03/OeNORM.jpg"), "hero": img("2022/08/image18.jpg")},
    {"slug": "bohrpfahl-bewehrungskoerbe", "title": "Bohrpfahl-Bewehrungskörbe", "short": "Produziert in unserem Werk in Marktoberdorf", "img": img("2024/03/Bohrpfaehle.jpg"), "hero": img("2022/08/Bohrpfahl_2.jpg")},
    {"slug": "schweissarbeiten", "title": "Schweißarbeiten", "short": "Schweißarbeiten an Stützen, Trägern & Betonstahl", "img": img("2024/03/Schweissarbeiten.jpg"), "hero": img("2022/08/Schweissen.jpg")},
    {"slug": "schalungszubehoer", "title": "Schalungszubehör", "short": "Zubehör für Schalung und Bewehrung ab Lager", "img": img("2022/08/image23.jpg"), "hero": img("2022/08/image23.jpg")},
    {"slug": "formstahl", "title": "Formstahl", "short": "Das gesamte Sortiment an Formstählen, auf Wunsch angearbeitet", "img": img("2022/08/Schlosserei.jpg"), "hero": img("2022/08/Schlosserei.jpg")},
]

JOBS = [
    {"slug": "vertriebsinnendienst", "title": "Vertriebsinnendienst (m/w/d)", "kind": "job", "area": "Büro", "img": img("2024/10/Bauzeichner-job.jpg")},
    {"slug": "betonstahlbieger", "title": "Betonstahlbieger (m/w/d)", "kind": "job", "area": "Produktion", "img": img("2025/08/Betonstahlbiegerei_2.jpg")},
    {"slug": "bohrpfahl-schweisser", "title": "Bohrpfahl-Schweißer (m/w/d)", "kind": "job", "area": "Produktion", "img": img("2024/03/Atterer-Stahlcenter_31-07-2019-46.jpg")},
    {"slug": "schlosser", "title": "Schlosser (m/w/d)", "kind": "job", "area": "Werkstatt", "img": img("2025/08/Schlosser.jpg")},
    {"slug": "ladearbeiter", "title": "Ladearbeiter (m/w/d)", "kind": "job", "area": "Logistik", "img": "https://usercontent.one/wp/www.atterer.de/wp-content/uploads/2024/03/Atterer-Stahlcenter_31-07-2019-101.jpg"},
    {"slug": "maschinenbediener", "title": "Maschinenbediener (m/w/d)", "kind": "job", "area": "Produktion", "img": img("2024/03/image00036.jpg")},
    {"slug": "lkw-fahrer", "title": "LKW-Fahrer (m/w/d)", "kind": "job", "area": "Logistik", "img": img("2024/03/LKW_Atterer-Stahlcenter-GmbH.jpg")},
    {"slug": "ausbildung", "title": "Ausbildung", "kind": "ausbildung", "area": "Industriekaufleute, Groß- und Außenhandel", "img": img("2025/05/Azubis-2025.jpg")},
    {"slug": "initiativbewerbung", "title": "Initiativbewerbung", "kind": "initiativ", "area": "Keine passende Stelle dabei?", "img": img("2025/02/produktion.jpg")},
]

APPLY_STEPS = [
    ("One-Click-Bewerbung", "Einfach die ONE-CLICK-BEWERBUNG ohne Unterlagen ausfüllen – oder per E-Mail an karriere@atterer.com bewerben."),
    ("Wir melden uns", "Wir melden uns bei Dir und laden Dich gegebenenfalls zu einem Gespräch ein."),
    ("Probearbeit", "Du kannst Deine zukünftige Arbeit und unser Team unverbindlich im Rahmen einer Probearbeit kennenlernen."),
]

GALLERY = [img(p) for p in [
    "2022/08/Bohrpfahl_1.jpg", "2022/08/image16.jpg", "2022/08/image17a.jpg", "2022/08/Schlosserei.jpg",
    "2022/08/Schweissen.jpg", "2022/08/image21.jpg", "2025/02/produktion.jpg", "2022/08/image28.jpg",
    "2022/08/image19a.jpg", "2022/08/image18.jpg", "2022/08/Bohrpfahl_2.jpg", "2022/08/image23.jpg",
    "2022/08/image25.jpg", "2022/08/image24.jpg",
]]

BEWEHRUNG = {
    "lead": "SAS 500 / 550 Gewindestahl – Muffe und Stab in höchster Qualität aufeinander abgestimmt.",
    "features": [
        "Muffe und Stab in höchster Qualität aufeinander abgestimmt",
        "Endlos schraubbares, robustes und baustellengerechtes Grobgewinde",
        "Vollstoß (100 %) in einer Ebene zulässig",
        "Stahllängen werden individuell zugeschnitten und gebogen",
        "Sonderausführungen möglich, z. B. Verzinken von Stahl und Zubehör",
        "Zulassungen in diversen europäischen Ländern für Stabdurchmesser 12 mm bis 63 mm",
        "Zugelassen für außergewöhnliche Lastfälle",
        "Umwandlung aller Systeme in SAS 500 möglich",
        "Einfach und günstig",
    ],
    "vs": [
        "Unempfindliches Grobgewinde, das beschädigt oder verschmutzt werden kann",
        "Kürzen und Verlängern des Gewindestahls problemlos möglich",
        "Keine teuren Sondermuffen oder Adapter erforderlich (z. B. für gekröpfte Stützeneisen)",
        "Montage trotz Winkelabweichung bis zu 3,5° leicht durchführbar",
    ],
    "diameters": [12, 14, 16, 20, 25, 28, 32, 40, 50, 63],
    "images": [img("2024/03/Bewehrungsstahl.jpg"), img("2024/12/Stahl-2banner.jpg"), img("2025/08/Betonstahlbiegrei.jpg")],
}

QM_TEXT = "Seit 2014 sind wir zertifiziert im Qualitätsmanagement-System nach DIN EN ISO 9001, welches seither kontinuierlich gestärkt und verbessert wurde. Die jährliche Re-Zertifizierung wurde seitdem erfolgreich absolviert."

NAV = [
    {"label": "Firma", "href": "firma.html", "children": [
        ("Unsere Geschichte", "firma.html#geschichte"),
        ("Atterer hilft", "firma.html#hilft"),
        ("Qualitätsmanagement", "qualitaetsmanagement.html"),
    ]},
    {"label": "Produkte", "href": "produkte.html", "children": [(p["title"], p["slug"] + ".html") for p in PRODUCTS]},
    {"label": "Karriere", "href": "karriere.html", "children": [
        ("Offene Stellen", "karriere.html#stellen"),
        ("Ausbildung", "ausbildung.html"),
        ("Initiativbewerbung", "initiativbewerbung.html"),
    ]},
    {"label": "Downloads", "href": "downloads.html", "children": []},
    {"label": "Kontakt", "href": "kontakt.html", "children": []},
]

TIMELINE = [
    ("1886", "Gründung der „Eisenhandlung Atterer“", "Anton Atterer gründet mit seiner Frau Theresia die Eisenhandlung. 1887 folgt der erste Großauftrag: Petroleum für die Straßenlaternen der Gemeinde.", img("2024/03/Atterer_Stahlcenter_Post_Anton_1080x1080_03-300x300.jpg")),
    ("1920", "Matthias Atterer übernimmt", "Nach dem Krieg meistert Matthias mit seiner Frau und Tochter Theresia die schwierige und entbehrungsreiche Zeit.", img("2024/03/Atterer_Stahlcenter_Post_Matthias_1080x1080_03-300x300.jpg")),
    ("1949", "Der erste LKW", "Die Gemeinde erlebt den ersten Aufschwung, das Handwerk blüht auf und die Auftragsbücher sind gut gefüllt.", None),
    ("1954", "Hans Wachter übernimmt die Leitung", "Er hängt seinen Lehrerberuf an den Nagel. Gemeinsam erleben die Eheleute das Wirtschaftswunder und erweitern das Sortiment.", None),
    ("1985", "Halle für die Betonstahlbearbeitung", "Nach mehreren Erweiterungen des Stammhauses und dem 3.000 m² großen Lagerplatz (1971) entsteht die erste Halle für Betonstahl.", None),
    ("1986", "100 Jahre Atterer", "Im Jubiläumsjahr übernimmt Andreas Wachter die Geschicke der Firma.", img("2024/03/Atterer_Stahlcenter_Post_Andreas_1080x1080-300x300.jpg")),
    ("1994", "Das Atterer Stahlcenter entsteht", "Mit einer 3.600 m² großen Halle. 1996 folgt das Werkcenter mit 2.800 m² Verkaufs- und Lagerfläche.", None),
    ("2009", "Stahlcenter in heutiger Form", "27.000 m² Hallen- und Lagerfläche. Gründung des Mindener Stahlhandels für Bauunternehmen von Kassel bis Hamburg.", None),
    ("2013", "Eberswalder Stahlhandel", "Auf 10.000 m² entsteht ein hochmoderner Biegebetrieb. 2014 folgt die Zertifizierung nach ISO 9001.", None),
    ("2026", "140 Jahre Atterer", "Geleitet von Andreas Wachter, unterstützt von seiner Frau Petra und mehr als 150 Mitarbeitern. Gemeinsam gewachsen.", None),
]

UC = "https://usercontent.one/wp/www.atterer.de/wp-content/uploads/"
CATALOG_PDF = UC + "2026/06/Stahlkatalog_2026_3.pdf"

QM = {
    "lead": "Zertifizierung nach DIN EN ISO 9001",
    "text": [
        "Seit 2014 sind wir zertifiziert im Qualitätsmanagement-System nach DIN EN ISO 9001:2008, welches seither kontinuierlich gestärkt und verbessert wurde.",
        "Seitdem wurde die jährliche Re-Zertifizierung erfolgreich absolviert.",
        "Für uns ist die Zertifizierung ein wichtiger Baustein zur kontinuierlichen Verbesserung unserer Unternehmensprozesse und wir erhöhen damit auch die Zufriedenheit aller Partner und Mitarbeiter.",
    ],
    "hero": img("2024/03/Auftragserfassung.jpg"),
}

# Generic product pages (Bewehrungsstahl has its own template)
PRODUCT_PAGES = {
 "geschweisste-bewehrungsmodule": {
  "title": "Geschweißte Bewehrungsmodule", "sub": "Zeit- und Kosteneinsparung",
  "lead": "Einzelne Betonstabstahl-Bügel werden mit den Längseisen zu einem Korb verschweißt – gefertigt nach Ihren Vorgaben bzw. Bewehrungsplänen.",
  "hero": img("2024/03/Atterer-Stahlcenter_31-07-2019-59.jpg"),
  "specs": [("Bügel-Ø", "6 – 20 mm"), ("Korbquerschnitt", "bis ca. 200 × 200 cm"), ("Korblänge", "bis 12 m"), ("Bügelabstand", "frei wählbar")],
  "sections": [
   {"h": "Was sind Bewehrungsmodule?", "list": [
     "Einzelne Betonstabstahl-Bügel werden mit den Längseisen zu einem Korb verschweißt.",
     "Bügel mit Stahldurchmessern von 6 – 20 mm und jeder transportfähigen Größe bis zu ca. 200 x 200 cm können zu Körben verschweißt werden.",
     "Jeder beliebige Abstand zwischen den Bügeln ist möglich.",
     "Innerhalb eines Korbes können auch unterschiedliche Abstände zwischen den Bügeln dargestellt werden.",
     "Korblängen bis 12 m (abhängig vom Handling auf Ihrer Baustelle) in einem Stück sind möglich.",
     "Fertigung nach Ihren Vorgaben bzw. Bewehrungsplänen."]},
   {"h": "Einsatzgebiete", "tags": ["Sohlen-/Wandanschlüsse", "Fundament-/Sohlenanschlüsse", "Fundamente", "Eckverbindungen", "Fugenband- und Randeinfassungen", "Stützen (auch rund)", "Balken", "Ringbalken"]},
   {"h": "Vorteile gegenüber Mattenkörben", "list": [
     "Herstellung filigranerer Bewehrungsteile.",
     "Genauere Maße der durch Bügelautomaten gefertigten Bügel.",
     "Biegeformen, die mit Matten nicht mehr gefertigt werden können. Kein Verschnitt.",
     "Kein Zuschneiden auf die erforderliche Länge der Bewehrungsteile.",
     "Das Ausschneiden der Querstäbe entfällt, wenn 2 Körbe ineinander gesteckt werden sollen."]},
   {"h": "Vorteile gegenüber mit Hand geflochtenen Körben", "list": [
     "Genauer, da maschinell vorgefertigt.",
     "Deutlich höhere Eigenstabilität des fertigen Bewehrungskorbes (weniger Durchhängeeffekt).",
     "Schneller! Erhebliche Minderung der Flechtzeit auf Ihren Baustellen!",
     "Zeitreserven lassen sich schaffen, kürzere Bauzeiten, Vorhaltekosten der auf den Baustellen befindlichen Maschinen und Einrichtungen werden verringert."],
    "img": img("2022/09/elemente-035_red.jpg")},
   {"h": "Nutzen Sie die Vorteile unserer Bewehrungsmodule", "faq": [
     ("Wie?", "Sie geben uns die Position im Bewehrungsplan an oder benutzen unser Bestellformular."),
     ("Preise?", "Für die Betonstahl-Bügel den vereinbarten Preis für Betonstabstahl geschnitten / gebogen, zzgl. der Aufpreise gem. Preisliste „Bewehrungsmodule“, Ausgabe Januar 2015."),
     ("Lieferzeit?", "Kurzfristig nach Absprache.")],
    "pdfs": [("Bewehrungsmodule Produktionsliste", UC + "2022/09/2019-bewehrungsmodule-produktionsliste.pdf")]},
  ]},
 "bamtec": {
  "title": "BAMTEC®", "sub": "Rollbewehrung für Decken, Bodenplatten und Wände",
  "lead": "BAMTEC ist das wirtschaftliche Verfahren zur Bewehrung von Decken, Bodenplatten und Wänden aus Stahlbeton.",
  "hero": img("2024/03/BAMTEC_1200.jpg"),
  "specs": [("Verlegezeit", "80 – 90 % sparen"), ("Material", "bis 40 % sparen"), ("Fertigung", "computergesteuert"), ("Bauzeit", "verkürzt")],
  "sections": [
   {"h": "Welche Vorteile bietet BAMTEC?", "list": [
     "Sparen Sie 80 – 90 % der Verlegezeit",
     "Sparen Sie 40 % Material durch frei wählbare Stabdurchmesser, Stababstände und Stablängen",
     "Erhöhen Sie die Verlegequalität durch einfache Positionierung und exakte Stablängen",
     "Qualitätssicherung durch computergesteuerte und vollautomatische Fertigung",
     "Einfache Bewehrungspläne",
     "Ergonomische Arbeitsweise auf der Baustelle",
     "Verkürzung der Gesamtbauzeit",
     "CO₂-Einsparung durch Materialeffizienz"]},
   {"h": "Vom Plan zur verlegten Bewehrung", "gallery": [(img("2022/09/fertigungsplan.jpeg"), "Fertigungsplan"), (img("2022/09/verlegeplan_web.jpeg"), "Verlegeplan"), (img("2022/09/uebersichtsplan_web.jpeg"), "Übersichtsplan")]},
   {"h": "Welchen Service bietet Ihnen Atterer?", "p": ["BAMTEC spart Ihnen Zeit und Geld. In unserer Verlegeanleitung erklären wir Schritt für Schritt, wie BAMTEC verlegt wird."],
    "pdfs": [("BAMTEC Katalog", IMG + "2022/09/bamtec-prospekt-en-de_klein-.pdf"), ("Projekteröffnungsbogen BAMTEC", IMG + "2022/09/pebbamtec-2019.pdf"), ("BAMTEC Verlegeanleitung", IMG + "2022/09/2019-bamtec-verlegeanleitung.pdf"), ("BAMTEC Konstruktionshandbuch", UC + "2022/11/2022-08-29-Atterer-BAMTEC-Konstruktionshandbuch.pdf")]},
  ]},
 "oenorm-stahl": {
  "title": "ÖNORM-Stahl", "sub": "Bewehrung nach österreichischer Norm",
  "lead": "ÖMAT-Schlaufenmatte, Distanzstreifen, RIPA-Anschlusskörbe und Durchstanz-Bewehrungselemente nach ÖNORM – für Ihre Baustellen in Österreich.",
  "hero": img("2024/03/Atterer-Stahlcenter_31-07-2019-15.jpg"),
  "sections": [
   {"h": "ÖMAT-Schlaufenmatte", "p": [
     "Überdeckungsstöße in Mattenquerrichtung (mit Schlaufe) – patentgeschützt.",
     "Die Entscheidung, ob Verlegeart 1 oder 2 gewählt werden soll, hängt sowohl vom erforderlichen Stahlquerschnitt als auch von der wirtschaftlichen Mattenausteilung ab.",
     "Abweichend von den Abbildungen können die Schlaufen im Übergriffsbereich auch gleichsinnig angeordnet sein. An der Wirkungsweise der Stöße ändert sich dadurch nichts. Die Querbewehrung der Typenreihen CS und AS beträgt ca. 20 % der Längsbewehrung bei Verlegeart 2. Für die Überdeckungsstöße in Mattenlängsrichtung gelten die entsprechenden Normvorschriften."],
    "img": img("2022/09/OeNORM-1.jpeg")},
   {"h": "Distanzstreifen hqDS", "p": ["Hochqualitativer Abstandhalter zwischen den beiden Bewehrungslagen. Empfohlen wird ein Verlege-Achsabstand der Distanzstreifen hqDS von ca. 50 cm, das entspricht ca. einem Stück pro m² obere Bewehrung. Bei stärkerer oberer Bewehrung kann der Verlegeabstand vergrößert werden. Unterstellungslänge: 200 cm."]},
   {"h": "RIPA-Anschlusskorb", "p": ["Der RIPA®-Anschlusskorb macht Schluss mit dem mühsamen Aufstellen einzelner Bügel, mit dem langwierigen Fixieren an Längseisen, mit dem lästigen Umkippen fast fertiger Bügelkörbe. Er ermöglicht das Verlegen der Fundamentanschlusseisen mit wenigen Handgriffen. Mit den umgebogenen freien Enden bzw. dem angeschweißten Querdraht entspricht der Anschlusskorb den Sicherheitsvorschriften der Bauarbeiterschutzverordnung."],
    "img": img("2022/09/OeNORM-2.jpeg")},
   {"h": "Durchstanz-Bewehrungs-Element DE", "list": [
     "Schnell verlegte Lösung zur Schubabdeckung bei Platten.",
     "Durchstanzelemente DE werden in verschiedenen Höhen und Schenkellängen erzeugt und können generell als Durchstanzbewehrung in allen Stahlbetonflächentragwerken eingesetzt werden. Sie werden rotationssymmetrisch bzw. sternförmig angeordnet. Die Höhe ergibt sich aus der Plattendicke abzüglich der Betondeckungen und der Höhen der unteren und oberen Bewehrungslage. Sie eignen sich besonders als Durchstanzbewehrung im Stützenbereich punktförmig gestützter Platten (Flachdecken).",
     "Verlegung: Die Elemente werden zwischen den unteren und oberen Lagen der Biegebewehrung verlegt und dienen damit gleichzeitig als Abstandhalter. Im Allgemeinen werden acht Elemente mit einem Öffnungswinkel von je 22,5° rotationssymmetrisch im Stützenkopfbereich verlegt. Bei zweireihiger, fischgrätartiger Anordnung kann durch Ineinanderstecken eine Vergrößerung der Durchstanzbewehrung erzielt werden."],
    "pdfs": [("Registrierungsbescheinigung ÖNORM B 4707 (B 550)", IMG + "2026/08/260414-UeA-Zertifikat-Salzburg-bis-30042031.pdf")]},
  ]},
 "bohrpfahl-bewehrungskoerbe": {
  "title": "Bohrpfahl-Bewehrungskörbe", "sub": "Produktion in Marktoberdorf",
  "lead": "Gefertigt auf unseren beiden Korbschweißmaschinen – in B 500 S bzw. in österreichischer oder schweizer Stahlgüte und Zulassung.",
  "hero": img("2024/03/Atterer-Stahlcenter_31-07-2019-46.jpg"),
  "specs": [("Außendurchmesser", "180 – 1.300 mm"), ("Länge in einem Stück", "bis 22 m"), ("Transport", "bis 19,40 m"), ("Mit eigenem Kran-LKW", "bis 18,00 m")],
  "sections": [
   {"h": "Fertigung", "p": [
     "Auf unseren beiden Korbschweißmaschinen fertigen wir in einem Außendurchmesserbereich von 180 mm bis zu einer Größe von 1.300 mm und in Längen bis zu 22 m in einem Stück. Wir können Körbe bis zu einer Länge von 19,40 m mit unserem Fuhrpark transportieren und bis zu einer Länge von 18,00 m sogar mit unseren eigenen Kran-LKWs auf Ihre Baustelle liefern.",
     "Die Steifigkeit wird durch das händische Einschweißen von Aussteifungsringen erreicht. Gegen den Auftrieb bei verrohrten Pfählen wird ein Bodenblech an das Fußkreuz angeschweißt. Die Abstandshalter werden aus Betonstahl oder auf Wunsch auch aus Flachstahl hergestellt und fest bzw. federnd angeschweißt."],
    "img": img("2024/03/Bohrpfahl_800.jpg")},
   {"h": "SOB-Pfähle", "p": ["Bei SOB-Pfählen (Schnecken-Ortbetonverfahren) werden die Längseisen nach dem Schweißen angeknickt und mit Einzelringen fixiert. Rüttelklingen sind auf Wunsch ebenfalls möglich."], "img": img("2024/03/Bohrpfahl_2_800.jpg")},
   {"h": "Sonderausstattungen", "tags": ["Einbau von Wickelfalzrohren", "Einbau von Kunststoffrohren", "Einbau von Stahlrohren zur Druckprüfung", "Aufbau mit Gewi-Stahl zur bauseitigen Verlängerung", "Einschweißen von Stahlträgern"]},
   {"h": "Zertifiziert durch die SLV München", "p": ["Unsere Schweißarbeiten an Bohrpfahl-Bewehrungskörben sind zertifiziert."], "pdfs": [("Zertifikat EN 1090", IMG + "2022/09/atterer-zertifikat-en-1090.pdf")]},
  ]},
 "schweissarbeiten": {
  "title": "Schweißarbeiten", "sub": "an Stützen, Trägern & Betonstahl",
  "lead": "Ein Team ausgebildeter Schweiß-Fachkräfte nimmt sich Ihrer Aufträge an, stellt fristgerecht Ihre Teile her und liefert sie auf Wunsch direkt zum Einsatzort.",
  "hero": img("2024/03/Atterer-Stahlcenter_31-07-2019-110.jpg"),
  "specs": [("Kopfbolzen", "DIN ISO 14555"), ("Stahlbau", "DIN EN 1090 EXC 2"), ("Betonstahl", "DIN EN ISO 17660"), ("Güten", "S 235 / S 355")],
  "sections": [
   {"h": "Einbauplatten mit Kopfbolzen", "p": ["Wir schweißen Kopfbolzen auf alle Anschweißplatten, Träger u. starkwandige Rohre von 10 – 22 mm (13/16/19/22 mm) mit Zulassung und Zertifizierung nach DIN ISO 14555."], "imgs": [img("2024/05/Stahlkatalog-2022-20-3.jpg"), img("2024/05/stahlkatalog-bild-3.png")]},
   {"h": "Schweißarbeiten von Stützen und Trägern", "p": ["Wir schweißen Stahlstützen aus Stahlrohren und Stahlträgern mit Anschweiß-, Aussteifungs-, Kopf- und Fußplatten, Anschweißplatten, Konsolen etc. in Qualität S 235 und S 355 mit Zulassung und Zertifizierung nach DIN EN 1090 EXC 2."], "imgs": [img("2024/05/beton-bold-1.jpg"), img("2024/05/beton-bild-2.jpg")]},
   {"h": "Betonstahlschweißen", "p": ["Wir schweißen Betonstahl als Überlappstöße, in Form von Bewehrungskörben und an Stahlplatten mit Zulassung und Zertifizierung nach DIN EN ISO 17660."], "imgs": [img("2024/05/beton-5.jpg"), img("2024/05/beton-4.jpg")],
    "pdfs": [("Zertifikat EN 1090-2", UC + "2024/03/Zertifikat-EN-1090-gueltig-bis-11-2026.pdf"), ("Zertifikat DIN EN ISO 17660 (2026 – 2029)", IMG + "2026/06/Bescheinigung-DIN-EN-ISO-17660-Schw-BST-bis-19052029.pdf")]},
  ],
  "contact_email": "formstahl@atterer.com"},
 "schalungszubehoer": {
  "title": "Schalungszubehör", "sub": "Umfangreiches Lieferprogramm",
  "lead": "Vom Abstandhalter bis zum Fundamenterder: alles, was Sie neben Betonstahl auf der Baustelle brauchen.",
  "hero": img("2024/03/Schalungszubehoer.jpg"),
  "sections": [
   {"h": "Lieferprogramm", "tags": ["Schöck Einbauteile", "Durchstanzbewehrung", "Abstandshalter", "Rückbiegeanschlüsse", "Maueranschlussschienen", "Halfenprodukte", "Bindedrähte", "Grundmauerschutz", "Wanddurchführungen", "Blitzschutz / Fundamenterder", "Erdungsbänder / -draht & Zubehör"]},
  ]},
 "formstahl": {
  "title": "Formstahl", "sub": "Trägeranarbeitung leicht gemacht",
  "lead": "Der leistungsstarke Partner für alle, die Formstahl verarbeiten und Betonstahl verbauen: umfassendes Trägersortiment in unserer 12.000 m² großen Halle – auf Wunsch gesägt, gebohrt, gestrahlt, konserviert oder verzinkt.",
  "hero": img("2024/03/Atterer-Stahlcenter_31-07-2019-1.jpg"),
  "specs": [("Trägerprofile am Lager", "50+"), ("Bearbeitungslänge", "bis 18.000 mm"), ("Breite", "bis 1.000 mm"), ("Strahlen", "SA 2,5")],
  "sections": [
   {"h": "Trägeranarbeitung", "p": ["Wir können computergesteuert millimetergenau Träger auf Gehrungen schneiden und diese auch gleich bohren. In der Zeit, in der Sie sonst die Löcher anzeichnen, hat unsere moderne Kaltenbach-Säge-Bohranlage die Löcher bereits an der richtigen Stelle gebohrt. Das spart Ihnen Arbeit und erhöht Ihre Wettbewerbsfähigkeit erheblich."], "img": img("2024/05/Kaltenbach.jpg")},
   {"h": "Leistungen", "services": [
     ("Bohren", "Drei Bohrspindeln bearbeiten Stahlprofile und Bleche bis 1.000 mm Breite und 18.000 mm Länge in einem Durchlauf.", ["CNC-gesteuert, drei Bohrspindeln", "Bohrdurchmesser 10 bis 40 mm", "Länge 18.000 mm, Breite 1.000 mm"]),
     ("Sägen", "Träger bis 1.000 mm Breite und aus Längen bis zu 18.000 mm – 90° oder auf Gehrung, millimeter- und winkelgenau.", ["CNC-gesteuertes Sägezentrum", "Gehrungen einseitig bis 68°", "Breite ab 60 bis 1.000 mm"]),
     ("Strahlen", "Reinheitsgrad SA 2,5 gemäß DIN EN ISO 12944-4 für Träger, Rohre, Profile und Bleche.", ["Stahlkugel-Strahlen", "Breite 50 bis 1.500 mm", "Bleche ab 5 mm Stärke"]),
     ("Konservieren", "Primer in Schichtdicken von 15 – 40 µm nach DIN EN ISO 12944-5, rotbraun oder hellgrau.", ["Wasserlösliche Lacke", "Schichtdicke 15 bis 40 µm", "Breite 50 bis 1.500 mm"]),
     ("Verzinken", "Langlebige Konservierung von Profilen und Konstruktionen durch Feuerverzinkung.", ["Schichtdicke 45 bis 85 µm", "Länge bis 18.000 mm", "Breite 50 bis 1.500 mm"]),
     ("Pulverbeschichten", "Profile bis 5 Meter Länge in allen RAL-Farben. Fragen Sie uns hierzu an.", ["Alle RAL-Farben", "Bis 5 m Länge"])]},
   {"h": "Formstahl-Lagersortiment", "p": ["Wir führen mehr als 50 verschiedene Trägerprofile in verschiedenen Längen am Lager. Das bedeutet: Wir sind sofort lieferfähig! Sämtliche Profile sind auch in S355 lieferbar."],
    "table": [("UNP", "80 – 400 mm"), ("IPE", "80 – 400 mm"), ("HEM", "100 – 240 mm"), ("HEA", "100 – 340 mm"), ("HEB", "100 – 400 mm")]},
   {"h": "Stahlcenter-Sortiment", "table": [
     ("Profile", "Formstahl, Breitflanschträger, Stabstahl, Spezialprofile, Breitflach- und Bandstahl"),
     ("Rohre", "Gas-, Siede- und Konstruktionsrohre, Vierkant- und Rechteckrohre, MSH-Rohre, RP-Rohre, Stahlbauhohlprofile"),
     ("Verzinktes Material", "Form- und Stabstahl sowie Bleche"),
     ("Bleche", "Fein-, Grob- und Belagbleche, Wildmaßbleche"),
     ("Edelstahl", "Bleche, Stabstahl, Rohre"),
     ("Metallbau", "Gitterroste, Halfeneisen, Zäune, Wellengitter, Doppelstabmatten, Schrauben"),
     ("Kunststoffe", "Baukunststoffe für Überdachungen und Balkonplatten, Werzalit-Produkte, technische Kunststoffe"),
     ("Bewehrungsstahl", "Betonstahl, Baustahlmatten, Abstandshalter, Draht, Bauzubehör"),
     ("Dach- und Wandprofile", "Trapezbleche, Sinuswellen, PUR-Sandwichpaneele, Brandschutzelemente, Kassetten, Lichtplatten, maßgefertigte Kantteile, Flachbleche als Tafeln oder Coils")]},
   {"h": "Tourenplan", "p": ["Unser Fuhrpark besteht aus 7 Sattelzügen und 7 Pritschen-LKWs, davon 5 mit Ladekränen und Plane. Wir beliefern Sie zuverlässig innerhalb unserer Touren. Ab 5 t Liefermenge beliefern wir Sie auch separat nach Ihren Terminwünschen."],
    "tours": [
     ("Landsberg", "Unterthingau, Kaufbeuren, Bad Wörishofen, Mindelheim, Kirchheim, Schwabmünchen, Landsberg am Lech, Ammersee-West, Denklingen"),
     ("Oberland", "Pfronten, Füssen, Steingaden, Oberammergau, Garmisch, Murnau, Penzberg, Weilheim, Peißenberg, Peiting, Schongau"),
     ("Oberallgäu", "Kempten, Memmingen, Isny, Immenstadt, Sonthofen, Oberstdorf, Oy-Mittelberg"),
     ("Augsburg – Schwaben", "Königsbrunn, Friedberg, Augsburg, Altenmünster, Günzburg, Krumbach, Thannhausen"),
     ("München – West", "Wolfratshausen, Starnberger See, Ammersee Ost, Fürstenfeldbruck, München, Germering")]},
  ]},
}

STD_BENEFITS = ["Attraktive Entlohnung mit Leistungszulage", "Umfassende soziale & monetäre Benefits", "Werkwohnung bei Bedarf"]

JOB_PAGES = {
 "vertriebsinnendienst": {"title": "Technischer Vertriebsinnendienst – innovative Bewehrungslösungen (m/w/d)", "short": "Vertriebsinnendienst (m/w/d)", "type": "Vollzeit", "area": "Büro",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt eine(n) Mitarbeiter(in) für den technischen Vertriebsinnendienst für innovative Bewehrungslösungen.",
   "aufgaben": ["Technische und kaufmännische Betreuung von Kunden", "Unterstützung des Außendienstes bei Projekten und Ausschreibungen", "Erstellung und Bearbeitung von Angeboten, Kalkulationen und technischen Unterlagen für BAMTEC Rollbewehrung, ZENTOR Schraubanschlüsse und Schweißmodule", "Eigenständige Nachverfolgung von Angeboten & Projekten"],
   "profil": ["Du hast eine abgeschlossene technische oder kaufmännische Ausbildung im Baustoffhandel oder im Baugewerbe, bspw. als Maurer", "Du hast bestenfalls Berufserfahrung im Vertriebsinnendienst", "Du bist kommunikativ und hast Freude an Verhandlungen", "Du hast bestenfalls Vorkenntnisse im Bereich Stahl, Baustoffe und ähnlicher Produkte", "Du bist motiviert, gut strukturiert und zeigst Eigeninitiative"],
   "img": img("2024/10/Bauzeichner-job.jpg"), "img2": img("2024/03/BAMTEC.jpg")},
 "betonstahlbieger": {"title": "Betonstahlbieger (m/w/d)", "short": "Betonstahlbieger (m/w/d)", "type": "Vollzeit, 2-Schicht", "area": "Produktion",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt Mitarbeiter für unsere Betonstahlbiegerei.",
   "aufgaben": ["Bedienung von Betonstahl-Schneideanlagen", "Bedienung von Betonstahl-Biegemaschinen", "Bedienung von Betonstahl-Bügel-Biegeautomaten"],
   "bieten": STD_BENEFITS,
   "profil": ["Du hast bestenfalls Berufserfahrung als Maschinenbediener und/oder an Schlagscheren", "Du hast bestenfalls einen gültigen Kran- & Gabelstaplerschein", "Du bist motiviert und arbeitest eigenständig", "Schichtarbeit (2-Schicht) ist für Dich kein Problem"],
   "img": img("2025/08/Betonstahlbiegerei_2.jpg"), "img2": img("2025/08/Betonstahlbiegrei.jpg")},
 "bohrpfahl-schweisser": {"title": "Bohrpfahl-Schweißer (m/w/d)", "short": "Bohrpfahl-Schweißer (m/w/d)", "type": "Vollzeit", "area": "Produktion",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt einen Mitarbeiter für unsere Bohrpfahlfertigung.",
   "aufgaben": ["Bedienung eines Schweißroboters zur Herstellung von Bohrpfählen", "Herstellung von Zubehörteilen für Bohrpfähle mittels Biegemaschinen", "Schweißarbeiten an Bohrpfählen"],
   "bieten": STD_BENEFITS + ["Einen sicheren Job in modernem Arbeitsumfeld"],
   "profil": ["Du hast bestenfalls Berufserfahrung als Schweißer oder Maschinenbediener", "Du hast Erfahrung mit den gängigen Schweißverfahren und eine gültige Schweißzertifizierung", "Du bist motiviert, arbeitest gerne im Team, aber auch eigenständig"],
   "img": img("2024/03/Atterer-Stahlcenter_31-07-2019-46.jpg"), "img2": img("2024/03/Bohrpfahl_800.jpg")},
 "schlosser": {"title": "Schlosser (m/w/d)", "short": "Schlosser (m/w/d)", "type": "Vollzeit", "area": "Werkstatt",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt einen Mitarbeiter für unsere Schlosserei.",
   "aufgaben": ["Durchführung von Schweiß-, Bohr- und Schneidarbeiten nach technischen Zeichnungen", "Anfertigung und Montage von Metallkonstruktionen und Bauteilen"],
   "bieten": ["Attraktive & leistungsgerechte Entlohnung", "Umfassende soziale & monetäre Benefits", "Werkwohnung bei Bedarf"],
   "profil": ["Du hast bestenfalls eine abgeschlossene Berufsausbildung als Schlosser", "Du verfügst über Berufserfahrung als Schlosser", "Du hast Erfahrung mit den gängigen Schweißverfahren und eine gültige Schweißzertifizierung", "Du bist motiviert, arbeitest strukturiert und eigenständig"],
   "img": img("2025/08/Schlosser.jpg"), "img2": img("2025/08/Schweissarbeiten.jpg")},
 "ladearbeiter": {"title": "Ladearbeiter (m/w/d)", "short": "Ladearbeiter (m/w/d)", "type": "Vollzeit, 2–3-Schicht", "area": "Logistik",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt einen Mitarbeiter für unser Verladeteam.",
   "aufgaben": ["Be- & Entladen unserer LKWs mittels Brückenkränen und Gabelstaplern", "Erfassung verladener Bunde in unserem ERP-System mittels Scanner", "Zwischenlagerung von produziertem Material", "Kommissionierung & Verladung von Bauzubehör und Baustahlmatten"],
   "profil": ["Du arbeitest sorgfältig & genau", "Du hast EDV-Grundkenntnisse", "Du hast einen Kranführerschein oder bist bereit, diesen zu erwerben", "Du hast bestenfalls einen LKW-Führerschein CE", "Du bist bereit zur Schichtarbeit in einem 2–3-Schichtmodell (Auswahl möglich)"],
   "img": UC + "2024/03/Atterer-Stahlcenter_31-07-2019-101.jpg", "img2": img("2022/08/image23.jpg")},
 "maschinenbediener": {"title": "Maschinenbediener (m/w/d)", "short": "Maschinenbediener (m/w/d)", "type": "Vollzeit, Schicht", "area": "Produktion",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt einen Maschinenbediener für unsere Säge-, Bohr- & Beschichtungsanlage.",
   "aufgaben": ["Bedienung der Sägebohranlage", "Bedienung der Strahl- und Konservierungsanlage", "Bestückung und Entnahme von Trägern und Profilen aus Stapeljochen", "Transport von Trägern und Profilen mittels Kran- und Magnettraverse", "Lager- und Kommissionierarbeiten"],
   "profil": ["Du verfügst über eine Ausbildung in einem Metallberuf", "Du hast mehrjährige Erfahrung in der Bearbeitung von Metallen", "Du hast Erfahrung in der Bedienung von Maschinen", "Du bist bereit zur Schichtarbeit", "Du arbeitest sorgfältig und genau"],
   "img": img("2024/03/image00036.jpg"), "img2": img("2024/03/image00044.jpg")},
 "lkw-fahrer": {"title": "LKW-Fahrer (m/w/d)", "short": "LKW-Fahrer (m/w/d)", "type": "Vollzeit", "area": "Logistik", "badge": "Führerschein bezahlen wir!",
   "intro": "Wir suchen für unseren Standort in Marktoberdorf zum nächstmöglichen Zeitpunkt Verstärkung für unser Logistik-Team als LKW-Fahrer.",
   "aufgaben": ["Belieferung von Baustellen unserer Kunden mit Bewehrungsstahl, geschweißten Bewehrungskörben oder Bohrpfählen", "Auslieferung von Formstahl (Träger, Bleche, Stabstahl und Rohre) an die Betriebsstätten unserer Kunden"],
   "profil": ["Du hast einen Führerschein Klasse CE (alt Klasse II)", "Du hast Freude am Fahren", "Du verfügst über Berufserfahrung", "Du überzeugst mit einem hohen Maß an Sorgfalt und Verantwortungsbewusstsein", "Du hast bestenfalls einen Kranführerschein und/oder Staplerführerschein (Klasse L) oder bist bereit, diesen zu erwerben"],
   "img": img("2024/03/LKW_Atterer-Stahlcenter-GmbH.jpg"), "img2": img("2024/03/LKW_2_Atterer-Stahlcenter-GmbH.jpg")},
}

INITIATIV = {
 "text": [
  "Solltest Du unter unseren aktuellen Stellenangeboten keine passende Position gefunden haben, dann bewirb Dich einfach initiativ bei uns. Wir sind stets an engagierten und leistungsfähigen Mitarbeitenden interessiert.",
  "Bitte bewirb Dich online mit einer aussagekräftigen Bewerbung (Motivationsschreiben, Lebenslauf und Zeugnisse). Gerne prüfen wir Deine Unterlagen und teilen Dir zeitnah mit, ob wir Dir aktuell eine Möglichkeit anbieten können.",
  "Wir sichern Dir den vertraulichen Umgang mit Deinen persönlichen Daten zu. Diese werden nicht an Dritte weitergegeben und ausschließlich für den Bewerbungsvorgang genutzt."],
 "note": "Bitte gib Deinen Gehaltswunsch und frühesten Starttermin in Deiner Bewerbung an.",
 "img": img("2025/02/produktion.jpg"),
}

AUSBILDUNG = {
 "title": "Ausbildung 2027/28",
 "hero": UC + "2025/05/Atterer-Ausbildung-2025_2.jpg",
 "intro": ["Was kommt nach der Schule? Wo gibt’s hier bei uns im schönen Allgäu so richtig coole Ausbildungsstellen mit bester Perspektive auf eine Karriere im führenden Stahlhandel der Region?",
           "Raus aus der Schule, rein in die Ausbildung! Finde die für Dich passende Stelle und bewirb Dich gleich online ohne jegliche Dokumente. Wir kommen danach direkt auf Dich zu und gehen die nächsten Schritte gemeinsam."],
 "facts": [("Bewerben ab", "sofort"), ("Ausbildungsstart", "1. September 2027/28"), ("Dauer", "2,5 – 3 Jahre")],
 "magazin": UC + "2026/07/Ausbildung-WEB.pdf", "magazin_img": UC + "2026/07/Ausbildung-WEB.jpg",
 "story": {"name": "Theresia Friedl", "title": "Von der Ausbildung in die erweiterte Geschäftsleitung", "text": "Oft fällt einem genau eine Sache als junger Mensch besonders schwer: sich bei all den Optionen, die sich einem bieten, überhaupt zu entscheiden …", "img": UC + "2025/05/Theresia-Friedl.jpg"},
 "gf_img": UC + "2025/05/Atterer-Geschaeftsfuehrung.jpg",
 "gf_caption": "Andreas Wachter (Geschäftsführender Gesellschafter) und Florian Sailer (Geschäftsführer)",
 "gf_title": "Gemeinsam die Zukunft gestalten",
 "gf_text": [
  "Die Welt verändert sich in rasantem Tempo – ob geopolitisch, wirtschaftlich oder technologisch. Gerade in unsicheren Zeiten zeigt sich, wie wichtig ein stabiles Fundament ist. Für uns als Atterer Stahlcenter GmbH bedeutet das: regional verwurzelt, zukunftsorientiert und bereit, Verantwortung zu übernehmen – für unsere Kunden, unsere Region und ganz besonders für unsere Nachwuchstalente.",
  "Aktuell erleben wir in Deutschland eine Phase großer Investitionen in Infrastruktur und Industrie. Der Bedarf an verlässlichen Partnern im Stahlbereich ist so hoch wie selten zuvor. Das eröffnet uns nicht nur starke Wachstumschancen, sondern auch viele spannende Aufgaben – Aufgaben, die wir gemeinsam mit engagierten Auszubildenden gestalten wollen.",
  "Wer heute eine Ausbildung beginnt, hat die Zukunft auf seiner Seite. Wir glauben fest daran, dass man nicht in die Ferne schweifen muss, um Großes zu bewegen: Hier, in unserer Heimat, gibt es jede Menge Potenzial – und mit einem starken, familiengeführten Unternehmen im Rücken eröffnen sich Perspektiven, die weit über die Ausbildung hinausgehen.",
  "Wir freuen uns auf junge Menschen, die mit uns gestalten wollen – mit Neugier, Einsatzfreude und einem sicheren Gespür für Qualität. Herzlich willkommen!"],
 "berufe": [
  {"title": "Kaufmann/-frau im Groß- und Außenhandel", "slug": "ausbildung-kaufmann", "img": UC + "2025/05/Aussenhandelskauffrau_850.jpg", "text": "Jeder Auftrag ist wichtig. Und Du wickelst ihn ab. Du bist die Schnittstelle und Schaltzentrale im Büro: Du kümmerst Dich um unsere Kunden, kalkulierst, erstellst passende Angebote und wickelst Aufträge ab."},
  {"title": "Industriekaufmann/-frau", "slug": "ausbildung-industriekaufmann", "img": UC + "2025/05/Industriekaufmann_frau.jpg", "text": "Du lernst die Abläufe in unserem Stahlcenter kennen und entwickelst Dich zum Organisationstalent. Analysieren und dann optimieren sind Dein Metier!"},
  {"title": "Berufskraftfahrer (m/w/d)", "slug": None, "full": True, "img": UC + "2025/05/Berufskraftfahrer-Ausbildung.jpg", "text": "Du lernst innerhalb von 3 Jahren alles, um souverän und zuverlässig unsere blauen Atterer-LKW in Süddeutschland, der Schweiz und Österreich zu bewegen."},
  {"title": "Kfz-Mechatroniker/-in", "slug": None, "img": UC + "2025/05/LKW-Mechaniker.jpg", "text": "Wir haben richtig viele LKW und die brauchen Deine Fürsorge. Dabei lernst Du in einer nagelneuen Werkstatt alles, was technisch und mechanisch dafür nötig ist!"},
  {"title": "Fachinformatiker/-in", "slug": None, "img": UC + "2025/05/Ausbildung-Fachinformatiker_in_850.jpg", "text": "Neu seit 2025: Schwerpunkt Systemintegration oder Daten- & Prozessanalyse. Du administrierst unsere Systeme und bringst uns in Prozessen und Software weiter."},
 ],
 "hardfacts": [UC + "2025/05/Verguetung.jpg", UC + "2025/05/Arbeitszeit.jpg", UC + "2025/05/Urlaub.jpg"],
 "benefits_img": UC + "2025/05/Benefits.jpg",
}

AUSBILDUNG_PAGES = {
 "ausbildung-industriekaufmann": {"title": "Industriekaufmann/-frau (m/w/d)", "start": "Ausbildungsstart September 2026",
   "intro": "Du lernst die Abläufe und Tätigkeiten in unserem Stahlcenter kennen und entwickelst Dich zum Organisationstalent. Du verwaltest die Aufträge, kennst Dich im Warenwirtschaftssystem aus und behältst die Übersicht aller Produktionsprozesse. Analysieren und dann optimieren sind Dein Metier!",
   "ausbildung": ["Du lernst allgemeine Tätigkeiten in der Verwaltung kennen", "Du wirkst bei der Arbeitsvorbereitung mit", "Du erhältst umfassende Kenntnisse in unserem Warenwirtschaftssystem", "Du lernst alle Abläufe im Unternehmen von der Bestellung bis zur Lieferung auf die Baustelle kennen", "Du erstellst Auswertungen und Statistiken", "Du erhältst Einblicke in die Buchhaltung", "Du bist Bindeglied zwischen Büro und Produktion"],
   "du_intro": "Neben guten Noten (mittlere Reife oder (Fach-)Abitur), Leistungsbereitschaft und Freude an der Arbeit solltest Du:",
   "img": img("2024/07/Industriekaufmann_1200.jpg"), "img2": img("2025/05/Ausbildung-Industriekauffrau.jpg")},
 "ausbildung-kaufmann": {"title": "Kaufmann/-frau im Groß- und Außenhandel (m/w/d)", "start": "Ausbildungsstart September 2026",
   "intro": "Jeder Auftrag ist wichtig. Und Du wickelst ihn ab. Du bist die Schnittstelle und Schaltzentrale im Büro, denn Du kümmerst Dich um unsere Kunden, hörst genauestens zu, kalkulierst und erstellst optimal passende Angebote und kümmerst Dich auch um die Abwicklung der Aufträge.",
   "ausbildung": ["Du bekommst ein umfangreiches Fachwissen zu unseren Produkten", "Du lernst Verkaufsgespräche zu führen", "Du berätst unsere Kunden fachmännisch", "Du erstellst und kalkulierst Angebote", "Du wickelst Aufträge vom Angebot bis zur Rechnung ab", "Du übernimmst Aufgaben in der Arbeitsvorbereitung", "Du lernst allgemeine Verwaltungstätigkeiten kennen", "Du erhältst umfangreiche Kenntnisse in unserem Warenwirtschaftssystem", "Du wirkst bei der Beschaffung von Materialien mit"],
   "du_intro": "Neben guten Noten (mindestens mittlere Reife), Leistungsbereitschaft und Freude an der Arbeit solltest Du:",
   "img": img("2024/07/Aussenhandelskauffrau_1200.jpg"), "img2": img("2025/05/Ausbildung-Gross-und-Aussenhandelskaufmann.jpg")},
}
AUSBILDUNG_DU = ["Freude am Verkaufen und im Umgang mit Menschen haben", "Freude an Büro- und Verwaltungsarbeiten haben", "Kontaktfreudig sein", "Ein selbstbewusstes, sicheres und freundliches Auftreten haben", "Sorgfältig arbeiten", "Verlässlich, ehrlich, pünktlich und zuverlässig sein", "Interesse an betriebswirtschaftlichen Zusammenhängen mitbringen"]

DOWNLOADS = [
 ("Stahlkatalog", [("Stahlkatalog 2026", CATALOG_PDF, "PDF, 6 MB")]),
 ("Formulare", [
   ("Kontoeröffnungsantrag", UC + "2025/05/Kontoeroeffnungsantrag-2024.pdf", "PDF"),
   ("Projekteröffnungsbogen", UC + "2022/09/peb-062019.pdf", "PDF"),
   ("Projekteröffnungsbogen Baustoffhändler", UC + "2022/09/pebb-062019.pdf", "PDF"),
   ("Projekteröffnungsbogen BAMTEC", UC + "2022/09/pebbamtec-062019.pdf", "PDF"),
   ("Bestellblatt Stahlcenter", UC + "2022/09/04_2016_bestellblatt.pdf", "PDF"),
   ("Bestellformular Mattenliste", UC + "2022/09/2016_mattenliste.pdf", "PDF"),
   ("Bestellformular Bewehrungsstahl", UC + "2022/09/fax-nachricht-formular.pdf", "PDF")]),
 ("Zertifikate", [
   ("DIN EN ISO 9001 Zertifikat", UC + "2026/01/F49_490115226_web_v1_cd8aff9c-5f2b-4a08-8e62-9b0ce96f77b8_de.pdf", "PDF"),
   ("Zertifikat EN 1090-2", UC + "2024/03/Zertifikat-EN-1090-gueltig-bis-11-2026.pdf", "PDF"),
   ("Zertifikat DIN EN ISO 17660 (2026 – 2029)", IMG + "2026/06/Bescheinigung-DIN-EN-ISO-17660-Schw-BST-bis-19052029.pdf", "PDF"),
   ("Lenton Übereinstimmungszertifikat", IMG + "2026/06/EU-20240401-DD-DIBt-Z-1.5-200-LENTON-WW-EU-GE.pdf", "PDF")]),
 ("Dokumente", [
   ("Bewehrungsmodule Produktionsliste", UC + "2022/09/2019-bewehrungsmodule-produktionsliste.pdf", "PDF"),
   ("Ü-Kennzeichnung von Betonstahl und Lagermatten", UC + "2022/09/2014-ue-kennzeichen.pdf", "PDF"),
   ("Registrierungsbescheinigung ÖNORM B 4707 (B 550)", IMG + "2026/08/260414-UeA-Zertifikat-Salzburg-bis-30042031.pdf", "PDF"),
   ("Freistellungsbescheinigung § 48 b EStG", UC + "2024/06/Freistellungsbescheinigung-bis-11-1-2027-zum-Steuerabzug-bei-Bauleistungen-gem.-§-48-b-Abs.-1-EStG.pdf", "PDF"),
   ("Lenton Allg. bauaufsichtliche Zulassung", UC + "2022/09/lenton-zulassung-germany-dibt-z-1.5.200-dibt-edition-.pdf", "PDF"),
   ("Bewerberinfo", UC + "2022/09/bewerber_info_ds-1.pdf", "PDF"),
   ("BAMTEC Konstruktionshandbuch", UC + "2022/11/2022-08-29-Atterer-BAMTEC-Konstruktionshandbuch.pdf", "PDF")]),
]
CATALOG_IMG = UC + "2026/05/Stahlkatalog_2026-1.jpg"

IMPRESSUM = [
 ("Angaben gemäß § 5 TMG", ["Atterer Stahlcenter GmbH<br>Siemensring 34<br>87616 Marktoberdorf", "Handelsregister: HRB 8204<br>Registergericht: Kempten", "Vertreten durch die Geschäftsführer:<br>Dipl.-Betriebswirt (FH) Andreas Wachter<br>M.Sc. (TU) Florian Sailer"]),
 ("Kontakt", ["Telefon: 08342 / 9641-0<br>Telefax: 08342 / 1813<br>E-Mail: info@atterer.com"]),
 ("Weitere Postadresse", ["Atterer Kochen & Schenken<br>Eberle-Kögl-Str. 20<br>87616 Marktoberdorf"]),
 ("Quellenangaben für die verwendeten Bilder und Grafiken", ["Fotolia, eigene Bilder und Bilder von Lieferanten und Partnerunternehmen"]),
 ("Umsatzsteuer-ID", ["Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz: DE 813 730 517"]),
 ("Angaben zur Berufshaftpflichtversicherung", ["Name und Sitz des Versicherers: Gothaer Allgemeine Versicherungs AG, 50598 Köln", "Geltungsraum der Versicherung: Deutschland"]),
 ("EU-Streitschlichtung", ["Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: https://ec.europa.eu/consumers/odr/. Unsere E-Mail-Adresse finden Sie oben im Impressum."]),
 ("Verbraucherstreitbeilegung / Universalschlichtungsstelle", ["Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen."]),
]
