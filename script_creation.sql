CREATE TABLE categorie(
	id_categorie int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_categorie varchar(30),
    description_categorie varchar(255),
    lien_page_categorie varchar(255)
);
CREATE TABLE recette(
	id_recette int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    titre_recette varchar(120),
    lien_image varchar(255),
    description varchar(255),
    temp_prepa int,
    temp_repo int,
    temp_cuis int,
    new tinyint(1),
    lien_video varchar(255),
    valide tinyint(1)
);
CREATE TABLE element_diaporama(
	id_element int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    lien_image varchar(255),
    lien_description varchar(255)
);
CREATE TABLE fetes(
	id_fete int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_fete varchar(30),
    description_fete varchar(255)
);
CREATE TABLE recette_fetes(
	id_fete int NOT NULL,
    id_recette int NOT NULL,
    PRIMARY KEY(id_fete,id_recette),
    FOREIGN KEY(id_fete) REFERENCES fetes(id_fete),
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette)
);
CREATE TABLE saison(
	id_saison int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_saison varchar(20)
);

CREATE TABLE utilisateur(
	id_user int not null PRIMARY KEY AUTO_INCREMENT,
    nom_user varchar(30),
    prenom_user varchar(30),
    email_user varchar(30) UNIQUE,
    age_user int ,
    date_de_naissance date,
    sexe char,
    password varchar(120),
    valide tinyint(1),
    token varchar(255)
);

CREATE TABLE noter(
	id_recette int NOT null,
    id_user int not null,
    date date not null,
    note int 
);

CREATE TABLE admin(
	id_admin int not null PRIMARY KEY AUTO_INCREMENT,
    nom_admin varchar(30),
    prenom_admin varchar(30),
    email_admin varchar(30) UNIQUE,
    age_admin int ,
    date_de_naissance date,
    sexe char,
    password varchar(120),
    token varchar(255)
);

CREATE TABLE etape(
	id_recette int not null,
    ordre int not null,
    description varchar(255),
    dure time,
    PRIMARY KEY(id_recette,ordre),
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette)
);

CREATE TABLE element_site(
	id_element varchar(30) PRIMARY KEY not null,
    couleur varchar(20)
);

CREATE TABLE parametre_site(
	id_parametre varchar(30) PRIMARY KEY not null,
    valeur varchar(20)
);

CREATE TABLE ingredient(
	id_ingr int PRIMARY KEY not null AUTO_INCREMENT,
    nom_ingr varchar(40) UNIQUE,
    healthy tinyint(1),
    calories int,
    type varchar(20)
);

CREATE TABLE recette_ingredient(
	id_recette int not null,
    id_ingr int not null,
    PRIMARY KEY(id_recette,id_ingr),
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette),
    FOREIGN KEY(id_ingr) REFERENCES ingredient(id_ingr)
);

CREATE TABLE info_nutr(
	id_info int not null PRIMARY KEY AUTO_INCREMENT,
    glucide int,
    lipide int,
    minéraux int,
    vitaminA int,
    vitaminB int,
    vitaminC int,
    vitaminD int,
    vitaminE int
);


CREATE TABLE ingr_info_nutr(
	id_info int not null,
    id_ingr int not null,
    PRIMARY KEY(id_info,id_ingr),
    FOREIGN KEY(id_ingr) REFERENCES ingredient(id_ingr),
    FOREIGN KEY(id_info) REFERENCES info_nutr(id_info)
);

CREATE TABLE news(
	id_news int not null PRIMARY key AUTO_INCREMENT,
    description varchar(255),
    liens_image varchar(120),
    lien_video varchar(120),
    id_recette int,
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette)
);

CREATE TABLE prefere(
	id_recette int not null,
    id_user int not null,
    PRIMARY KEY(id_recette,id_user),
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette),
    FOREIGN KEY(id_user) REFERENCES utilisateur(id_user)
);

CREATE TABLE recette_saison(
	id_recette int not null,
    id_saison int not null,
    PRIMARY KEY(id_recette,id_saison),
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette),
    FOREIGN KEY(id_saison) REFERENCES saison(id_saison)
);

CREATE TABLE ingredient_saison(
	id_ingr int not null,
    id_saison int not null,
    PRIMARY KEY(id_ingr,id_saison),
    FOREIGN KEY(id_ingr) REFERENCES ingredient(id_ingr),
    FOREIGN KEY(id_saison) REFERENCES saison(id_saison)
);






