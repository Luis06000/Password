# Password Manager Matrix

Un gestionnaire de mots de passe élégant avec une interface inspirée de Matrix, permettant de générer des mots de passe sécurisés et de vérifier leur force.

## 🌟 Fonctionnalités

### Générateur de Mots de Passe
- Personnalisation de la longueur (4-50 caractères)
- Options de composition :
  - Lettres minuscules (a-z)
  - Lettres majuscules (A-Z)
  - Chiffres (0-9)
  - Caractères spéciaux (!@#$...)
- Copie en un clic
- Interface moderne avec effet glassmorphism

### Vérificateur de Force
- Analyse en temps réel
- Évaluation sur 5 niveaux :
  - Très faible
  - Faible
  - Moyen
  - Fort
  - Très fort
- Suggestions d'amélioration personnalisées
- Affichage visuel de la force

## 🎨 Design
- Animation Matrix en arrière-plan
- Interface en glassmorphism
- Thème vert Matrix
- Design responsive
- Navigation fluide sans rechargement

## 🛠️ Technologies Utilisées
- Python (Flask)
- HTML5
- CSS3
- JavaScript (Vanilla)
- Canvas pour l'animation Matrix

## 📦 Installation

1. Clonez le repository
```bash
git clone https://github.com/luis06000/Password.git
```

2. Installez les dépendances
```bash
pip install -r requirements.txt
```

3. Démarrez l'application
```bash
python app.py
```


4. Ouvrez votre navigateur à l'adresse `http://localhost:5000`

## 💻 Utilisation

### Générer un Mot de Passe
1. Sélectionnez la longueur souhaitée
2. Cochez les options désirées
3. Cliquez sur "Générer"
4. Utilisez le bouton "Copier" pour copier le mot de passe

### Vérifier un Mot de Passe
1. Entrez le mot de passe à vérifier
2. Cliquez sur "Vérifier"
3. Consultez l'évaluation et les suggestions

## 🔒 Critères de Sécurité

Le vérificateur évalue les critères suivants :
- Longueur minimale (8 caractères)
- Présence de majuscules
- Présence de minuscules
- Présence de chiffres
- Présence de caractères spéciaux

## 🌐 Compatibilité

- Chrome (recommandé)
- Firefox
- Safari
- Edge

Note : L'effet de glassmorphism peut varier selon les navigateurs.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## ✨ Auteur

@Luis06000
