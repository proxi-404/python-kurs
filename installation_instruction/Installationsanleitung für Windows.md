Hier in diesem Dokument findet ihr die Links und Installationsanleitungen für die Programme und Python Packages, die wir im Kurs verwenden werden.

## Python 

1. Gehe auf https://www.python.org/downloads/ und klicke dort auf "Download Python 3.12.0" 
2. Führe die heruntergeladene Datei aus. 
3. Setze unten den Haken bei "Add python.exe to PATH"
![[PythonInstallation.png]]
5. Drücke dann "Install Now"
6. Wenn die Installation abgeschlossen ist drücke noch auf "Disable path length limit" und bestätige die Berechtigungsaufforderung mit Ja
## Visual Studio Code
werden wir als unsere IDE verwenden um Python Code zu schreiben und auszuführen.

1. Geh auf die Webseite https://code.visualstudio.com/ und lade dort die "Stable Build" Version für Windows herunter
2. Installiere die heruntergeladene Datei mit den vorgegebenen Einstellungen
3. Öffne Visual Studio Code
4. Gehe auf der linken Seite auf "Extensions"
![[VSCodeExtensions.png]]
6. Gebe dort in die Suchleiste "Jupyter" ein und wähle dann den Installationsbutton aus![[VSJupyterInstallation.png]]
7. Suche ebenfalls in der Suchleiste "Python" und installiere die Extension. ![[VSCodePython.png]]
## Package Installationen
Wichtig ist, dass dieser Schritt erst gemacht werden kann, wenn Python nach der obigen Anleitung installiert ist.

1.  Drücke die Tasten "Win + R"  
2. Gib dort "cmd" ein und drücke Enter
3. Gib in dem sich dort öffnenden  Fenster folgenden Befehl ein und drücke Enter: 
```
pip install numpy matplotlib tk scipy pandas notebook tabulate import-ipynb
```
dieser Befehl installiert alle nötigen Python Packages, die wir während des Kurses brauchen

## Ausführen des Testskriptes
Neben der Installationsanleitung habt ihr eine Datei "0_system_check.ipynb" bekommen. 
Diese könnt ihr unter Windows über den Explorer mit rechtsklick öffnen
![[ExplorerTestOpening.png]]
Oder ihr öffnet Visual Studio Code geht dort auf Datei -> Datei öffnen und wählt die Datei aus.
![[CodeTestOpening.png]]
Wenn die Datei geöffnet ist, dann könnt ihr den Test über zwei Felder ausführen. Der "run all" Button führt alle Zellen aus, der "execute cell" Button führt die einzelne Zelle aus.
![[Systemcheck.png]]
Wenn das ganze ausgeführt ist, sollte eure Ausgabe wie folgt aussehen:
![[SuccessfulTest.png]]
Wenn Ihr Probleme habt oder eure Ausgabe nicht so aussieht, meldet euch gerne bei uns! 
Wir helfen euch dann weiter!