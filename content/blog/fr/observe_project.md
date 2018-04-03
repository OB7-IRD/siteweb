title: Le projet ObServe
icon: icon-link
summary: 
slug: observe-project
date: 2018-04-03
modified: 2018-04-03
lang: fr

## Contexte
Le projet **ObServe** s'inscrit  dans notre mission de suivi scientifique et statistique de la pêcherie thonière à la senne tropicale française et à la canne dans les océans Atlantique et Indien. Nous conservons des séries historiques disponibles depuis les années 50 pour l'océan Atlantique et le début des années 80 pour l'Indien. Les principaux objectifs de l’observatoire sont :

- Caractériser la dynamique et l'impact de la pêcherie sur les espèces capturées au travers du suivi des journaux de pêches, d’échantillonnages lors des débarquements et d'observateurs embarqués.
- Étudier la biodiversité des écosystèmes pélagiques et analyser l’impact des pêches thonières sur les autres espèces : requins, tortues, mammifères marins et oiseaux.
- Étudier le fonctionnement et l’exploitation des écosystèmes pélagiques.
- Fournir les données annuelles de référence aux tutelles décisionnaires (Direction des Pêches Maritimes et de l’Aquaculture (DPMA) et Union Européenne (UE).

L’Ob7 a mis en œuvre un système d’information pour répondre à cette mission ainsi que des collaborations scientifiques pour le partage des méthodes de suivi et d'outils d’analyse des données avec d’autres institutions de recherche sur les pêches thonières, en particulier avec nos partenaires du Sud.

Concernant la pêche à la senne le système d’information comprend :

- La collecte des données règlementaires issues des livres de bord
- La réalisation d’échantillonnages de tailles sur les débarquements au port
- La collecte des bons de débarquements établis par les conserveries
- Le suivi de la filière du marché local
- La collecte de données d’observation à bord par des observateurs scientifiques
- La récupération des données VMS auprès de l’institution de référence (SNSP)

Concernant la pêche à la palangre réunionnaise le système comprend :

- La collecte de données d’observation à bord par des observateurs scientifiques
- La collecte de données d’auto échantillonnage à bord par les équipages

## Le système intégré ObServe
ObServe est le système informatique pour le moment dédié à la gestion des données d’observation des pêcheries à la senne et à la palangre. Il prend en charge leur saisie (à bord ou à terre, en ligne ou hors ligne), leur consolidation dans un dépôt central, et leur diffusion par requêtes ou interfaçage avec d’autres systèmes. Plusieurs instances du système, de plusieurs organismes par exemple, peuvent par ailleurs communiquer pour synchroniser leurs données de référence et échanger leurs données métier.

Le système se compose d’une base de données sur serveur PostgreSQL, d’un serveur de service web, et d’une application d’édition et d’administration à installer sur les postes des utilisateurs. Ce document se concentre sur la description du modèle de données sous-jacent, implanté à la fois sur le dépôt central sous SGBDR PostgreSQL, et dans les logiciels eux-mêmes sous SGBDR H2 Database (pour leur fonctionnement hors ligne).

Le système est actuellement utilisé par les organismes suivants : l’IRD, les TAAF, le CAP RUN, le Parc Marin de Mayotte, Oceanic Développement (France), l’AZTI, l’IEO (Espagne), BigEye (Côte d’Ivoire) et la SFA (Seychelles).

## Liens

1. La forge du projet: [https://gitlab.com/ultreiaio/ird-observe](https://gitlab.com/ultreiaio/ird-observe])
2. La documentation du projet: [https://ultreiaio.gitlab.io/ird-observe/](https://ultreiaio.gitlab.io/ird-observe/)
