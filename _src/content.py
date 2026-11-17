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
    {"slug": "schlosser", "title": "Schlosser (m/w/d)", "kind": "job", "area": "Werkstatt", "img": img("2022/08/Schlosserei.jpg")},
    {"slug": "ladearbeiter", "title": "Ladearbeiter (m/w/d)", "kind": "job", "area": "Logistik", "img": img("2022/08/image23.jpg")},
    {"slug": "maschinenbediener", "title": "Maschinenbediener (m/w/d)", "kind": "job", "area": "Produktion", "img": img("2022/08/image16.jpg")},
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
