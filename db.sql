CREATE TABLE IF NOT EXISTS user (
    id_user INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role_user ENUM('admin', 'commercial') NOT NULL DEFAULT 'commercial',
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS client (
    id_client INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    company_name VARCHAR(150) NOT NULL,
    contact_name VARCHAR(150),
    email VARCHAR(150) NOT NULL,
    phone VARCHAR(30),
    address TEXT,
    statut ENUM('actif', 'inactif', 'prospect') DEFAULT 'prospect',
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contact (
    id_contact INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    type_contact ENUM('appel', 'email', 'rendez-vous') NOT NULL,
    date_contact DATETIME DEFAULT CURRENT_TIMESTAMP,
    comments TEXT,

    id_client INT NOT NULL,
    id_user INT NOT NULL,

    FOREIGN KEY (id_client)
        REFERENCES client(id_client)
        ON DELETE CASCADE,

    FOREIGN KEY (id_user)
        REFERENCES user(id_user)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS project (
    id_project INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    project_name VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    statut ENUM('en cours', 'terminé', 'annulé') DEFAULT 'en cours',

    id_client INT NOT NULL,

    FOREIGN KEY (id_client)
        REFERENCES client(id_client)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS invoice (
    id_invoice INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    invoice_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10,2) NOT NULL,
    statut ENUM('brouillon', 'envoyé', 'accepté', 'refusé') DEFAULT 'en attente',

    id_client INT NOT NULL,
    id_project INT UNIQUE,

    FOREIGN KEY (id_client)
        REFERENCES client(id_client)
        ON DELETE CASCADE,

    FOREIGN KEY (id_project)
        REFERENCES project(id_project)
        ON DELETE CASCADE
);

CREATE INDEX idx_client_statut ON client(statut);
CREATE INDEX idx_contact_date ON contact(date_contact);
CREATE INDEX idx_project_statut ON project(statut);
