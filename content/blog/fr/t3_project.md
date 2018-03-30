title: Le projet T3+
icon: icon-link
summary: 
slug: t3+-project
date: 2018-03-30
modified: 2018-03-30
lang: fr

Le projet **T3+** s'inscrit dant le cadre notre mission de suivi statistique de la pêcherie thonière à la senne tropicale française et à la canne dans les océans Atlantique et Indien. Ce suivi se décompose d’une part en une collecte de données sur le terrain en continu, et d’autre part en une séries de traitements statistiques appliqués à ces données afin de les rendre exploitables à de questions d’expertise (p. ex. évaluation de stock) et de recherche plus académiques en lien avec les thèmes de recherche de l’IRD (p. ex. conservation de la biodiversité) . Une fois validées, ces données constituent les statistiques officielles de la France et sont communiquées chaque année aux commissions thonières internationales en charge de la gestion des stocks de thons tropicaux : la Commission Internationale pour la Conservation des Thonidés de l’Atlantique (CICTA) et la Commission des Thons de l’Océan Indien (CTOI).

Pour cela plusieurs types d’informations sont collectés :

- Journaux de bord (ou logbooks) : Ils donnent des informations sur les poids totaux pêchés, par catégories commerciales (espèce et classe de taille). Les informations offrent une couverture presque exhaustive mais approximative, surtout concernant la composition spécifique.
- Plans de cuve (ou chargement) : Documents permettant de faire la correspondance entre cuves et coups de pêche géolocalisés. Ils permettent d’établir le plan d’échantillonnage des cuves en sélectionnant des échantillons provenant d’une même strate (au sens de Pallarés & Hallier 1997),
- Enquêtes au débarquement (ou échantillons) : Menées aux  principaux ports de débarquements (Abidjan, Dakar, Victoria et Antsiranana), elles couvrent l'ensemble des débarquements et consistent en des échantillonnages de taille et de composition spécifique réalisés sur certaines cuves des thoniers au cours du débarquement. Elles fournissent des informations fiables mais sur une fraction seulement des débarquements.

On croise ensuite ces données pour en déduire :

- Une couverture exhaustive à l’échelle de l’année et de la flotte nationale, géolocalisée et « redressée » en tonnage (c-à-d. ajustée aux poids des débarquements) et en composition spécifique (c-à-d. corrigée en appliquant la composition spécifique dérivée des enquêtes aux ports),
- L’effort, exprimé comme le temps de recherche, ceci faisant appel à des relations entre la durée de la calée et le poids pêché qui sont dérivées de données collectées en mer par les observateurs embarqués,
- Des structures de taille à l’échelle des captures totales, ceci faisant appel à des relations morphométriques qui sont dérivées d’échantillonnages biologiques réalisés essentiellement aux conserveries d’Abidjan et Victoria.

Ces traitements sont initialement réalisés par le jeu de programmes T3 (Traitement des Thons Tropicaux), dont T3+ présenté ici est le successeur.
T3+ est un système d’information intégré dans le sens où il assure à la fois le traitement et la gestion des données. Dans ce but il intègre une base de données (sous PostgreSQL) apte à consolider conjointement les données source et les données traitées, ainsi que l’ensemble des résultats des différentes étapes de traitement intermédiaires.

## Liens

1. La forge du projet: [https://gitlab.com/ultreiaio/ird-t3/](https://gitlab.com/ultreiaio/ird-t3/])
2. La documentation du projet: [https://t3.ultreia.io/](https://t3.ultreia.io/)
