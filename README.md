Importieren des git:

git clone https://github.com/TjorbenTH/Modellierung.git
cd python-projekt


👥 4. Zusammenarbeit – typische Git-Befehle
Änderungen vornehmen und hochladen

#Code ändern oder neue Datei erstellen
git status  # zeigt neue/änderte Dateien
git add datei.py
git commit -m "Neue Funktion hinzugefügt"
git push

Änderungen von anderen holen
git pull

Konflikte vermeiden: Best Practices
Vor dem Bearbeiten: git pull
Nach dem Bearbeiten: git add ., git commit, git push
Keine .pyc-Dateien, virtuelle Umgebungen oder große Daten im Repo speichern
.gitignore nutzen (z. B. für venv/, __pycache__/)


🔄 5. Optional: Branches verwenden
Für größere Änderungen empfiehlt es sich, Branches zu nutzen:
git checkout -b feature/neue-funktion

# Änderungen machen
git add .
git commit -m "Neue Funktion"
git push origin feature/neue-funktion
Dann einen Pull Request auf GitHub erstellen.

✅ Beispiel .gitignore für Python
__pycache__/
*.py[cod]
*.egg-info/
.env
venv/
