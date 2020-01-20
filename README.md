# Pet Project for Advanced Software Engineering WS 2018/19
This Pet project was inspired by a tic tac toe game from this particular website <https://inventwithpython.com/chapter10.html>. It is based on a simple model and the evaluation of human kind  playing this game over the time. Thus the turn of computer follows this findings. In this documentation I will show UML diagrams and some metrics for the code, as well as some clean code concepts.

# UML Diagrams

# Metrics
[![Quality Gate Status](http://localhost:9000/api/project_badges/measure?project=pet_project&metric=alert_status)](http://localhost:9000/dashboard?id=pet_project)

# Clean Code

# Dsl

# Functional Programing 


# PET_Project_19

### Clean Code 

##Don´t Repeat Yourself (DRY)
Warum?
Jede Doppelung von Code oder auch nur Handgriffen leistet Inkonsistenzen und Fehlern Vorschub.
Evolvierbarkeit	  
Korrektheit	  
Produktionseffizienz	  
Kontinuierliche Verbesserung	  
Single Developer
Das DRY-Prinzip lautet: Don’t Repeat Yourself – Wiederhole dich nicht. Es gilt seit den Anfängen der Softwareentwicklung – sonst gäbe es keine Unterprogramme und keine Datennormalisierung. Dennoch ist es wahrscheinlich das am meisten missachtete Prinzip. Denn nichts ist einfacher, als Code durch Copy&Paste zu wiederholen. Gerade dann, wenn es mal schnell gehen soll, passiert das allzuoft.

Clean Code Developer üben sich im roten Grad daher darin, dieses Prinzip stets zu beachten. Sie sind sich bewusst, wann sie Code oder andere Artefakte wiederholen. Sie erkennen solche Wiederholungen, die sie selbst oder andere erzeugt haben. Sie bereinigen Wiederholungen durch Refaktorisierungen – wenn keine anderen Prinzipien oder Beschränkungen dagegen sprechen.

##Keep it simple, stupid (KISS)
Warum?
Wer mehr tut als das Einfachste, lässt den Kunden warten und macht die Lösung unnötig kompliziert.
Evolvierbarkeit	  
Korrektheit	  
Produktionseffizienz	  
Kontinuierliche Verbesserung	  
Single Developer
Oder um es mit Albert Einsteins Worten zu sagen: “Alles sollte so einfach wie möglich gemacht werden, aber nicht einfacher.”. Für die Evolvierbarkeit des Codes ist zwingende Voraussetzung, dass der Code verständlich ist. Eine einfache, klare und leicht verständliche Lösung sollte daher immer bevorzugt werden. Wenn man seinen eigenen Code nach kurzer Zeit schon nicht mehr versteht, sollten die Alarmglocken klingen. Noch wichtiger aber ist, dass auch andere Entwickler den Code schnell verstehen können. Dabei helfen regelmäßige Reviews und Pair Programming. Sie dienen der Kontrolle, ob tatsächlich die einfachste Lösung verwendet wurde.

Gerade in technischen Details steckt die Versuchung, eine komplizierte Lösung anzustreben. Das Bekannte, naheliegende ist manchmal zu “langweilig” – und schon hat sich eine komplizierte Lösung eingeschlichen. Wenn die einfache Lösung auch funktioniert, sollte ihr Vorrang gewährt werden. Das gleiche gilt für Datenstrukturen. Wenn ein IEnumerable reicht, sollte keine ICollection oder sogar IList verwendet werden.

##Ein Versionskontrollsystem einsetzen
Warum?
Angst vor Beschädigung eines “running system” lähmt die Softwareentwicklung. Mit einer Versionsverwaltung ist solche Angst unbegründet. Die Entwicklung kann schnell und mutig voranschreiten.
Evolvierbarkeit	  
Korrektheit	  
Produktionseffizienz	  
Kontinuierliche Verbesserung	  
Team
Unabdingbare Voraussetzung für jeden Clean Code Developer ist es, seinen Code unter den Schutz eines Versionskontrollsystems zu stellen. Ob das Mercurial, Git, Subversion, VSS, TFS oder Vault ist, spielt dabei keine Rolle. Wir meinen nur, dass heute keine Arbeit an Code mehr durchgeführt werden sollte, ohne ihn in einem Versionskontrollsystem zu pflegen. Der Grund dafür ist ganz simpel: Ein Versionskontrollsystem befreit von Angst. Und Angstfreiheit ist nötig, um mutig die Prinzipien und Praktiken des CCD-Wertesystems umzusetzen.

Ein Versionskontrollsystem nimmt die Angst, etwas falsch und damit kaputt zu machen. Wenn Code in ihm gehalten wird, kann jeder CCD den Code nach Belieben verändern, ohne befürchten zu müssen, einen erreichten Stand zu zerstören. Nichts geht verloren. Das Versionskontrollsystem ist wie eine Zeitmaschine für Code.

Damit ist ein Versionskontrollsystem die allerbeste Grundlage für alles Lernen. Denn Lernen bedeutet Fehler machen. Mit einem Versionskontrollsystem als Sicherheitsnetz können wir uns alle Fehler erlauben. Deshalb: Erste Voraussetzung für den Einstieg ins Clean Code Development ist der ständige Gebrauch eines Versionskontrollsystems.

Wo das im Projekt nicht möglich ist, sehen wir das Fundament für Clean Code Development abwesend. Wir würden auch nicht verstehen, warum der Einsatz eines Versionskontrollwerkzeuges nicht möglich sein sollte. Kosten müssen dafür nicht anfallen und der Einarbeitungsaufwand in die einfachsten Funktionen ist minimal. CCD schreibt ja keine bestimmte Nutzung eines Versionskontrollsystems vor, sondern nur, dass eines benutzt werden muss.

Siehe auch unter Tools.


##Einfache Refaktorisierungsmuster anwenden
Warum?
Code verbessern ist leichter, wenn man typische Verbesserungshandgriffe kennt. Ihre Anwendungsszenarien machen sensibel für Schwachpunkte im eigenen Code. Als anerkannte Muster stärken sie den Mut, sie anzuwenden.
Evolvierbarkeit	  
Korrektheit	  
Produktionseffizienz	  
Kontinuierliche Verbesserung	  
Single Developer
Um Code immer ein wenig besser zu hinterlassen, als man ihn vorgefunden hat, sind mehr oder weniger große Eingriffe nötig. Die kann ein Clean Code Developer dank des Versionskontrollsystems angstfrei vornehmen. Doch wie macht er sich die Arbeit möglichst einfach?

Das Schlüsselwort lautet “Refaktorisierung”. Martin Fowler hat das Refaktorisieren/Refactoring in seinem gleichnamigen Buch als grundlegende Technik zur Erhöhung der Codequalität beschrieben. Er definiert darin eine Anzahl von Codeveränderungsmustern, um “code smells”, d.h. suboptimale Strukturen oder allgemeiner Missachtungen von Prinzipien, zu bereinigen.

Für den roten Grad ist darin vor allem die Refaktorisierung Methode extrahieren relevant, um dem DRY-Prinzip zu genügen. Die wenden Clean Code Developer an, um mehrfach vorkommenden Code in eine Methode zu extrahieren, die statt seiner an den Wiederholungsorten aufgerufen wird.

Als zweite Refaktorisierung sollte bei der Arbeit am roten Grad das Umbenennen wo nötig eingesetzt werden. Sie passt zur Pfadfinderregel, denn eine oft anzutreffende “Unsauberkeit” im Quellcode sind kryptische Namen.

Refaktorisierungen können von Hand angewandt werden, doch es gibt auch Werkzeugunterstützung. Moderne IDEs wie Visual Studio bieten einige Refactoringmuster, weitere Tools listet unsere Werkzeugliste.

“Refactoring” wie “Clean Code” gehören zur Pflichtlektüre jedes Clean Code Developers ab dem roten Grad.

Für weitere Informationen siehe auch unter refactoring-legacy-code.net.

##Source Code Konventionen
Warum?
Code wird häufiger gelesen als geschrieben. Daher sind Konventionen wichtig, die ein schnelles Lesen und Erfassen des Codes unterstützen.
Evolvierbarkeit	  
Korrektheit	  
Produktionseffizienz	  
Kontinuierliche Verbesserung	  
Team
Wir betrachten die folgenden Aspekte als wichtig:

Namensregeln
Richtig Kommentieren
Damit wollen wir nicht zum Ausdruck bringen, dass andere Konventionen unwichtig sind, wir wollen nur mit diesen beiden beginnen, weil sie uns elementar erscheinen. Bei allen Code Konventionen ist uns nämlich eines ganz wichtig: es geht weniger um die konkrete Ausgestaltung, sondern um konsequentes Einhalten der Konvention. Und es geht um das Bewusstsein, dass Konventionen notwendig sind.

Namensregeln
Warum?
Ohne Namensregeln muss man sich wieder und wieder auf den Stil einzelner Entwickler einstimmen.
Namensregeln sollen den Leser des Codes dabei unterstützen den Code zu verstehen. Da es z.B. hilfreich ist, Felder von lokalen Variablen zu unterscheiden, könnte dies durch eine Namensregel unterstützt werden. Wie eine solche Konvention im Einzelfall aussieht ist Geschmacksache. Manche bevorzugen “this.xyz” andere “_xyz”. Welche Variante man wählt ist uns nicht wichtig. Uns kommt es darauf an, dass die Konvention konsequent eingehalten wird. Die Notwendigkeit einer Namensregel für z.B. Felder hängt ferner vom Kontext ab. In einer Klasse mit 400 Zeilen wäre uns eine Namensregel, die Felder gegenüber Variablen hervorhebt, sehr wichtig, in überschaubaren Klassen tritt sie dagegen eher in den Hintergrund. Mit Hilfe der Root Cause Analysis geht der Clean Code Developer der eigentlichen Ursache für die Notwendigkeit einer Namensregel auf den Grund.
Richtig kommentieren
Warum?
Unnötige oder gar falsche Kommentare halten beim Lesen auf. Der Code sollte so klar und deutlich sein, dass er möglichst ohne Kommentare auskommt.
Salopp gesagt ist ein Kommentar im Code ein Hinweis darauf, dass der Code noch verbessert werden kann. Typisch für solche Fälle sind 3 Zeilen Code, die mit einem Kommentar überschrieben sind. An der Stelle hilft es wahrscheinlich, die drei Zeilen als Methode zu extrahieren (Refactoring: Extract Method) und den Kommentar als Name der Methode zu verwenden. Ganz allgemein kann der Bedarf an Kommentaren reduziert werden, in dem man gute Namen verwendet für Variablen, Methoden, Klassen, etc.
Statt
    int laenge; // in mm
besser
    int laengeInMM; 
Statt
    public double Preis() {
        // Berechnet den Bruttopreis ...
    }
besser
    public Money BruttoPreis() {
        ...
    } 
Kommentiert werden sollte nicht was man tut, sondern, wenn überhaupt, wieso man etwas tut.




