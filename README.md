# Projet Team PFE  

Ce guide d'utilisation explique comment cloner le projet, configurer l'authentification avec un token GitHub et collaborer efficacement en utilisant Git.  

---  

## 1. Cloner le dépôt Git  

1. Ouvrez un terminal.  
2. Clonez le projet avec la commande suivante :  
   ```bash
   git clone https://github.com/ImenMabroukIMSR/projet-team-pfe.git
   ```
3. Accédez au dossier du projet :  
   ```bash
   cd projet-team-pfe
   ```
4. Créez une nouvelle branche pour chaque candidat :  
   ```bash
   git checkout -b feature-<nom_du_candidat>
   ```

---  

## 2. Enregistrer son Token GitHub pour les Pushs  

### Génération du Token d'authentification  

1. Allez sur GitHub → **Developer Settings** → **Personal Access Tokens**.  
2. Cliquez sur **Generate new token (classic)**.  
3. Donnez un nom au token et définissez **No Expiration** (ou une durée spécifique si nécessaire).  
4. Cochez la permission **repo**.  
5. Cliquez sur **Generate token**.  
6. **Copiez et enregistrez ce Token** en lieu sûr.  

### Configuration du Token dans Git  

1. Enregistrez le token pour ne pas avoir à le saisir à chaque push :  
   ```bash
   git config --global credential.helper store
   ```
2. Poussez votre première modification avec le token :  
   ```bash
   git push https://<Username>:<TON_TOKEN>@github.com/ImenMabroukIMSR/projet-team-pfe.git
   ```

---  

## 3. Ajouter et Pousser ses Modifications  

1. Ajoutez les fichiers modifiés :  
   ```bash
   git add .
   ```
2. Effectuez un commit avec un message explicatif :  
   ```bash
   git commit -m "Premier commit"
   ```
3. Poussez votre branche sur le dépôt distant :  
   ```bash
   git push origin feature-<nom_du_candidat>
   ```

---  

## 4. Après chaque modification  

1. Vérifiez votre branche actuelle :  
   ```bash
   git branch
   ```  
   - Si vous n'êtes pas sur votre branche, basculez dessus :  
     ```bash
     git checkout feature-<nom_du_candidat>
     ```
2. Vérifiez les fichiers modifiés :  
   ```bash
   git status
   ```
3. Ajoutez les fichiers modifiés :  
   ```bash
   git add .
   ```  
   - Ou ajoutez un fichier spécifique :  
     ```bash
     git add path/to/file.py
     ```
4. Effectuez un commit avec un message clair :  
   ```bash
   git commit -m "Description des modifications"
   ```
5. Poussez les modifications sur GitHub :  
   ```bash
   git push origin feature-<nom_du_candidat>
   ```

---  

Ce guide permet à chaque stagiaire de comprendre les étapes essentielles pour collaborer efficacement sur le projet en respectant les bonnes pratiques Git. 🚀

