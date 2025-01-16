# Wprowadzenie do problematyki bezpieczeństwa systemów komputerowych

# Bezpieczeństwo systemów komputerowych - wykład 1:Wprowadzenie do problematyki bezpieczeństwa systemów komputerowych
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie do problematyki bezpieczeństwa systemów komputerowych](https://wazniak.mimuw.edu.pl/<#Wprowadzenie_do_problematyki_bezpieczeństwa_systemów_komputerowych>)
    * [1.1 Co to jest bezpieczeństwo?](https://wazniak.mimuw.edu.pl/<#Co_to_jest_bezpieczeństwo?>)
    * [1.2 Czynniki decydujące o znaczeniu bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Czynniki_decydujące_o_znaczeniu_bezpieczeństwa>)
    * [1.3 Zagrożenia bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Zagrożenia_bezpieczeństwa>)
    * [1.4 Komponenty systemu informatycznego w kontekście bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Komponenty_systemu_informatycznego_w_kontekście_bezpieczeństwa>)
    * [1.5 Ogólne problemy konstrukcji zabezpieczeń](https://wazniak.mimuw.edu.pl/<#Ogólne_problemy_konstrukcji_zabezpieczeń>)
    * [1.6 Strategia bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Strategia_bezpieczeństwa>)
      * [1.6.1 Określenie zasobów = „Co chronić?”](https://wazniak.mimuw.edu.pl/<#Określenie_zasobów_=_„Co_chronić?”>)
      * [1.6.2 Identyfikacja zagrożeń = „Przed czym chronić?”](https://wazniak.mimuw.edu.pl/<#Identyfikacja_zagrożeń_=_„Przed_czym_chronić?”>)
    * [1.7 Polityka bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Polityka_bezpieczeństwa>)
      * [1.7.1 Zakres](https://wazniak.mimuw.edu.pl/<#Zakres>)
      * [1.7.2 Specyfikacja środków](https://wazniak.mimuw.edu.pl/<#Specyfikacja_środków>)
      * [1.7.3 Normy i zalecenia zarządzania bezpieczeństwem](https://wazniak.mimuw.edu.pl/<#Normy_i_zalecenia_zarządzania_bezpieczeństwem>)


## Wprowadzenie do problematyki bezpieczeństwa systemów komputerowych
### Co to jest bezpieczeństwo?
Przedstawienie problematyki bezpieczeństwa systemów komputerowych systemów komputerowych należy rozpocząć od zdefiniowania pojęcia bezpieczeństwa. Niestety trudno skonstruować uniwersalną i jednoznaczną definicję tego pojęcia, która pokryłaby wszystkie oczekiwania stawiane w tej dziedzinie systemom komputerowym. Literatura przedmiotu podaje bardzo dużo, często znacznie odbiegających od siebie definicji. Przykład ciekawej definicji można znaleźć w [1]: 
Def.
    **System komputerowy** jest **bezpieczny** , jeśli jego użytkownik może na nim polegać, a zainstalowane oprogramowanie działa zgodnie ze swoją specyfikacją. W myśl tej definicji, możemy system uznać za bezpieczny, jeśli np. można od niego oczekiwać, że wprowadzone na stałe dane nie zostaną utracone, nie ulegną zniekształceniu i nie zostaną pozyskane przez nikogo nieuprawnionego - ufamy, że system będzie przechowywał i chronił dane.
Bezpieczeństwo jest elementem szerszego kontekstu, nazywanego wiarygodnością systemu komputerowego. W kontekście tym wyróżnia się w sumie cztery atrybuty wiarygodności: 
**System wiarygodny =**
    - dyspozycyjny (_available_) = dostępny na bieżąco
    - niezawodny (_reliable_) = odporny na awarie
    - bezpieczny (_secure_) = zapewniający ochronę danych
    - bezpieczny (_safe_) = bezpieczny dla otoczenia, przyjazny dla środowiska
### Czynniki decydujące o znaczeniu bezpieczeństwa
O doniosłości problematyki bezpieczeństwa dla współczesnej cywilizacji decyduje przede wszystkim wszechobecność technik komputerowych. W szczególności rozważyć należy następujące zagadnienia: 
  * rola systemów informatycznych (szczególnie sieci) dla funkcjonowania współczesnej cywilizacji jest nie do przecenienia; nie ma już praktycznie obszaru działalności człowieka, w którym żadne elementy techniki komputerowej (bądź szerzej mikroprocesorowej) nie byłyby obecne. Jako drobny przykład niech posłuży telefonia komórkowa, towarzysząca dziś człowiekowi niemal ciągle i wszędzie;
  * trudności związane ze skonstruowaniem i eksploatacją systemu spełniającego wysokie wymagania w zakresie bezpieczeństwa (niedoskonałości technologii, konfiguracji i polityki bezpieczeństwa) stwarzają niebezpieczeństwo niedopracowanego pod względem bezpieczeństwa i niezawodności produktu informatycznego lub nieodpowiedniego pod owym względem wykorzystania tego produktu;
  * elementarny konflikt interesów występujący pomiędzy użytecznością systemu a ryzykiem związanym z jego wykorzystaniem rodzi szereg pragmatycznych problemów (często całkowicie pozatechnicznych) związanych z oczywistymi utrudnieniami we wdrożeniu i użytkowaniu systemów o podwyższonym bezpieczeństwie.


### Zagrożenia bezpieczeństwa
Zagrożenia bezpieczeństwa mają różną naturę. Mogą być najzupełniej przypadkowe lub powstać w efekcie celowego działania. Mogą wynikać z nieświadomości lub naiwności użytkownika, bądź też mogą być motywowane chęcią zysku, poklasku lub odwetu. Mogą pochodzić z zewnątrz systemu lub od jego środka. 
Większość działań skierowanych w efekcie przeciwko bezpieczeństwu komputerowemu jest w świetle aktualnego prawa traktowana jako przestępstwa. Możemy tu wyróżnić w szczególności: 
  * włamanie do systemu komputerowego
  * nieuprawnione pozyskanie informacji
  * destrukcja danych i programów
  * sabotaż (sparaliżowanie pracy) systemu
  * piractwo komputerowe, kradzież oprogramowania
  * oszustwo komputerowe i fałszerstwo komputerowe
  * szpiegostwo komputerowe


Istotne jest, iż w przypadku jurysdykcji większości krajów europejskich, praktycznie wszystkie przypadki naruszające bezpieczeństwo wyczerpują znamiona przestępstw określonych w obowiązującym prawie. 
W Polsce w szczególności mają tu zastosowanie: 
  * artykuły 267-269 Kodeksu Karnego
  * artykuł 287 Kodeksu Karnego


(<http://www.gazeta-it.pl/prawo/przestepstwa_komputerowe.html>) 
Zazwyczaj przestępstwa te nie są ścigane z oskarżenia publicznego, lecz na wniosek pokrzywdzonego. 
W kontekście bezpieczeństwa komputerowego powszechnie spotyka użycie popularnego terminu hacker na określenie osoby podejmującej atak. Termin ten oryginalnie nie posiadał wydźwięku pejoratywnego. Wg „The Hacker's Dictionnary" (Guy L. Steele et al.) hacker jest to (1) osoba, której sprawia przyjemność poznawanie szczegółowej wiedzy na temat systemów komputerowych i rozszerzanie tej umiejętności, w przeciwieństwie do większości użytkowników, którzy wolą uczyć się niezbędnego minimum; (2) osoba, która entuzjastycznie zajmuje się programowaniem i nie lubi teorii dotyczącej tej dziedziny. W związku z tym w niniejszych materiałach stosować będziemy bardziej odpowiednie terminy (zależnie od typu rozważanego ataku), takie jak: cracker, intruz, włamywacz, napastnik, wandal czy po prostu - przestępca. 
Przykłady ataków na systemy informatyczne znaleźć można w wielu dziedzinach życia osobistego, gospodarki, przemysłu czy funkcjonowania organów państwowych. Przykładowo w 1997 r. CIWARS (Centre for Infrastructural Warfare Studies) odnotował 2 incydenty (w Brazylii i w Australii) zaciekłej konkurencji gospodarczej, w których zaatakowały się wzajemnie (omawianymi później atakami SYN flood) konkurujące ze sobą firmy ISP (operatorzy dostępu do Internetu). Jako działania anarchistyczne można sklasyfikować przykładowo incydent z 1997 r., w którym grupa Damage Inc. zastąpiła witrynę Urzędu Rady Ministrów stroną proklamującą utworzenie Hackrepubliki Polskiej i Centrum Dezinformacyjnego Rządu z odsyłaczami do playboy.com. Być może jako terroryzm natomiast - incydent z 1998 r., gdy w akcie protestu przeciwko próbom nuklearnym grupa Milw0rm zaatakowała systemy indyjskiego BARC (Bhabba Atomic Research Center). 
### Komponenty systemu informatycznego w kontekście bezpieczeństwa
Elementarne składniki systemu informatycznego jakie należy wyróżnić przy omawianiu problematyki bezpieczeństwa to: 
  * stanowisko komputerowe i infrastruktura sieciowa
  * system operacyjny i usługi narzędziowe
  * aplikacje użytkowe


### Ogólne problemy konstrukcji zabezpieczeń
Problematyka bezpieczeństwa, jak każda dziedzina, podlega pewnym ogólnym prawom, niektórym sformalizowanym, innym - nieformalnym. Można wyróżnić pewne truizmy obowiązujące podczas projektowania i realizowania zabezpieczeń. Niektóre z nich to: 
  * Nie istnieje absolutne bezpieczeństwo. Wiąże się to z wieloma przyczynami. Jedną z nich jest fakt, iż nigdy nie jesteśmy w stanie przewidzieć z góry wszystkich możliwych zagrożeń, tym bardziej że często należy opracowywać zabezpieczenia z odpowiednim wyprzedzeniem. Szybki rozwój technologii informatycznych implikuje powstawanie coraz to nowych zagrożeń. Czas reakcji na nie nigdy nie jest zerowy i w związku z tym nawet dla najlepiej opracowanego systemu zabezpieczeń istnieje ryzyko powstania okresu dezaktualizacji zastosowanych mechanizmów bezpieczeństwa. Ewolucja zagrożeń pociąga za sobą wyścig atakujących i broniących („policjantów i złodziei"). Innym istotnym powodem niemożliwości osiągnięcia 100% bezpieczeństwa jest ludzka słabość, w szczególności omylność projektantów, programistów, użytkowników systemów informatycznych, skutkująca błędami w oprogramowaniu systemowym i aplikacyjnym oraz niewłaściwym lub niefrasobliwym jego wykorzystaniu. 


Skoro zatem nie mamy 100% bezpieczeństwa, jaki jego poziom można uznać za zadowalający? Otóż wydaje się, że najwłaściwszą odpowiedzią na to pytanie jest - taki, który okaże się dla atakującego na tyle trudny do sforsowania, wymagając operacji żmudnych lub czasochłonnych, iż uczyni to atak nieatrakcyjnym lub nieekonomicznym (lub oczywiście nieopłacalnym wg innego kryterium obranego przez atakującego). Zatem należy na tyle utrudnić włamywaczowi atak, aby z niego zrezygnował widząc marne, choć nadal niezerowe, szanse powodzenia. 
  * Napastnik na ogół nie pokonuje zabezpieczeń, tylko je obchodzi. Przeprowadzenie skutecznego ataku na jakikolwiek aktywny mechanizm zabezpieczeń jest raczej czasochłonne i stosowane tylko w ostateczności. Zwykle mniej kosztowne i szybsze jest znalezienie luki w środowisku systemu informatycznego, zabezpieczanego owym mechanizmem niż łamanie jego samego, która to luka pozwoli skutecznie wtargnąć do systemu nie jako „z boku" zabezpieczeń. Przy tej okazji warto wspomnieć, że okazuje się niezmiennie od wielu lat, iż większość ataków przeprowadzanych na systemy informatyczne realizowana jest „od środka", czyli przez zaufanych, poniekąd, użytkowników systemu, którzy znając system jakim się posługują niewątpliwie łatwiej mogą znaleźć i wykorzystać luki bezpieczeństwa.
  * Nie należy pokładać zaufania w jednej linii obrony. Z poprzedniej obserwacji wynika, że obejście aktywnego mechanizmu zabezpieczeń często bywa możliwe i może istotnie narażać bezpieczeństwo całego systemu. W związku z tym, naturalną konsekwencją tego jest konstruowanie wielopoziomowych zabezpieczeń poprzez budowanie kolejnych swoistych „linii obrony", z których każda po przejściu poprzedniej stanowić będzie, przynajmniej potencjalnie, kolejną zaporę dla atakującego.
  * Złożoność jest najgorszym wrogiem bezpieczeństwa. Skomplikowane systemy są trudne do opanowania, również pod względem bezpieczeństwa. Istotnym usprawnieniem zarządzania systemem jest jego modularna konstrukcja, dająca szansę na zwiększenie kontroli nad konfiguracją i funkcjonowaniem systemu. Dotyczy to również wielopoziomowych zabezpieczeń.
  * System dopóty nie jest bezpieczny, dopóki nie ma pewności że jest. Bardzo łatwo popełnić błąd zakładając zupełnie inaczej - dopóki brakuje odnotowanych symptomów, iż bezpieczeństwo systemu zostało naruszone, możemy spać spokojnie. Zaobserwowanie ataku nie jest trywialne nawet w systemie poprawnie monitorowanym. Ponadto symptomy ataku zwykle występują dopiero po jego zakończeniu, kiedy to może być zbyt późno by przeprowadzać akcję ratunkową, kiedy ucierpiały już newralgiczne składniki systemu, poufne dane lub reputacja firmy.


Wzrost poziomu bezpieczeństwa odbywa się kosztem wygody. Użytkownicy systemu pragną przede wszystkim efektywności i wygody swojej pracy. 
### Strategia bezpieczeństwa
Opracowanie skutecznych zabezpieczeń jest problemem bardzo złożonym. Wymaga uwagi i systematyczności na każdym etapie. Niewątpliwie decydujące znaczenia ma etap projektowy, na którym popełnione błędy mogą być nienaprawialne w kolejnych etapach. Etap projektowy powinien rozpocząć się od wypracowania strategii firmy dotyczącej bezpieczeństwa (i to nie wyłącznie systemu informatycznego). Polega to w ogólnym schemacie na odpowiedzi na następujące pytania: 
  1. „Co chronić?” (określenie zasobów)
  2. „Przed czym chronić?” (identyfikacja zagrożeń)
  3. „Ile czasu, wysiłku i pieniędzy można poświęcić na należną ochronę” (oszacowanie ryzyka, analiza kosztów i zysku)


#### Określenie zasobów = „Co chronić?”
Zasoby jakie mogą podlegać ochronie obejmują m.in. (w zależności od typu instytucji, dziedziny działalności itp.): 
  * sprzęt komputerowy
  * infrastruktura sieciowa
  * wydruki
  * strategiczne dane
  * kopie zapasowe
  * wersje instalacyjne oprogramowania
  * dane osobowe
  * dane audytu
  * zdrowie pracowników
  * prywatność pracowników
  * zdolności produkcyjne
  * wizerunek publiczny i reputacja


#### Identyfikacja zagrożeń = „Przed czym chronić?”
Zagrożenia jakie należy rozważyć stanowią m.in.: 
  * włamywacze komputerowi
  * infekcje wirusami
  * destruktywność pracowników / personelu zewnętrznego
  * błędy w programach
  * kradzież dysków / laptopów (również w podróży służbowej)
  * utrata możliwości korzystania z łączy telekomunikacyjnych
  * bankructwo firmy serwisowej / producenta sprzętu
  * choroba administratora / kierownika (jednoczesna choroba wielu osób)
  * powódź


### Polityka bezpieczeństwa
Polityka bezpieczeństwa stanowi element polityki biznesowej firmy. Jest to formalny dokument opisujący strategię bezpieczeństwa. Jej realizacja podlega oczywistym etapom: 
  1. zaprojektowanie
  2. zaimplementowanie
  3. zarządzanie (w tym monitorowanie i okresowe audyty bezpieczeństwa)


Szczególnie godnym podkreślenia jest etap 3. odzwierciedlający ciągłą ewolucję jaką przechodzą działalność firmy, środowisko rynkowe jej funkcjonowania, zagrożenia i technologie obrony. Wymaga to ciągłego "trzymania ręki na pulsie". 
#### Zakres
Zakres tematyczny jaki powinna obejmować polityka bezpieczeństwa to: 
  * definicja celu i misji polityki bezpieczeństwa
  * standardy i wytyczne których przestrzegania wymagamy
  * kluczowe zadania do wykonania
  * zakresy odpowiedzialności


#### Specyfikacja środków
Polityka bezpieczeństwa winna definiować środki jej realizacji obejmujące takie elementy jak: 
  * ochrona fizyczna
  * polityka proceduralno-kadrowa (odpowiedzialność personalna)
  * mechanizmy techniczne


#### Normy i zalecenia zarządzania bezpieczeństwem
Istnieje wiele dokumentacji poświęconej realizacji polityki bezpieczeństwa, w tym również norm i standardów międzynarodowych, którymi należy posiłkować się przy opracowywaniu własnej polityki bezpieczeństwa. Pod tym względem kanonem jest norma ISO/IEC Technical Report 13335 (ratyfikowana w naszym kraju jako PN-I-13335). Norma ta jest dokumentem wieloczęściowym obejmującym następujące zagadnienia: 
TR 13335-1 terminologia i modele
TR 13335-2 metodyka planowania i prowadzenia analizy ryzyka, specyfikacja wymagań stanowisk pracy związanych z bezpieczeństwem systemów informatycznych
TR 13335-3 techniki zarządzania bezpieczeństwem
    - zarządzanie ochroną informacji
    - zarządzanie konfiguracją systemów IT
    - zarządzanie zmianami
TR 13335-4 metodyka doboru zabezpieczeń
WD 13335-5 zabezpieczanie połączeń z sieciami zewnętrznymi
Jednakże norm ISO dotyczących bezpieczeństwa jest wiele. Można tu wymienić chociażby bogaty podzbiór (wycinek listy do roku 1995): 
```
ISO 2382-8:1986 Information processing systems - Vocabulary - Part 08: Control, integrity and security
ISO 6551:1982 Petroleum liquids and gases - Fidelity and security of dynamic measurement - Cabled transmission of electric and/or electronic pulsed data
ISO 7498-2:1989 Information processing systems - Open Systems Interconnection - Basic Reference Model - Part 2: Security Architecture
ISO/IEC 7816-4:1995 Information technology - Identification cards - Integrated circuit(s) cards with contacts - Part 4: Interindustry commands for interchange
ISO/IEC 9796:1991 Information technology - Security techniques - Digital signature scheme giving message recovery
ISO/IEC 9797:1994 Information technology - Security techniques - Data integrity mechanism using a cryptographic check function employing a block cipher algorithm
ISO/IEC 9798-1:1991 Information technology - Security techniques - Entity authentication mechanisms - Part 1: General model
ISO/IEC 9798-2:1994 Information technology - Security techniques - Entity authentication - Part 2: Mechanisms using symmetric encipherment algorithms
ISO/IEC 9798-3:1993 Information technology - Security techniques - Entity authentication mechanisms - Part 3: Entity authentication using a public key algorithm
ISO/IEC 9798-4:1995 Information technology - Security techniques - Entity authentication - Part 4: Mechanisms using a cryptographic check function
ISO/IEC 10118-1:1994 Information technology - Security techniques - Hash-functions - Part 1: General
ISO/IEC 10118-2:1994 Information technology - Security techniques - Hash-functions - Part 2: Hash-functions using an n-bit block cipher algorithm
ISO/IEC 10164-7:1992 Information technology - Open Systems Interconnection - Systems Management: Security alarm reporting function
ISO/IEC 10164-8:1993 Information technology - Open Systems Interconnection - Systems Management: Security audit trail function
ISO/IEC DIS 10181-1 Information technology - Open Systems Interconnection - Security Frameworks for Open Systems: Overview
ISO/IEC DIS 10181-2 Information technology - Open Systems Interconnection - Security frameworks for open systems: Authentication framework
ISO/IEC DIS 10181-3 Information technology - Open Systems Interconnection - Security frameworks in open systems - Part 3: Access control
ISO/IEC DIS 10181-4 Information technology - Open Systems Interconnection - Security frameworks in Open Systems - Part 4: Non-repudiation
ISO/IEC DIS 10181-5 Information technology - Security frameworks in open systems - Part 5: Confidentiality
ISO/IEC DIS 10181-6 Information technology - Security frameworks in open systems - Part 6: Integrity
ISO/IEC DIS 10181-7 Information technology - Open Systems Interconnection - Security Frameworks for Open Systems: Security Audit Framework
ISO/IEC 10736:1995 Information technology - Telecommunications and information exchange between systems - Transport layer security protocol
ISO/IEC 10745:1995 Information technology - Open Systems Interconnection - Upper layers security model
ISO 11166-1:1994 Banking - Key management by means of asymmetric algorithms - Part 1: Principles, procedures and formats
ISO 11166-2:1994 Banking - Key management by means of asymmetric algorithms - Part 2: Approved algorithms using the RSA cryptosystem
ISO 11442-1:1993 Technical product documentation - Handling of computer-based technical information - Part 1: Security requirements
ISO/IEC 11577:1995 Information technology - Open Systems Interconnection - Network layer security protocol
ISO/IEC DIS 11586-1 Information technology - Open Systems Interconnection - Generic upper layers security: Overview, models and notation
ISO/IEC DIS 11586-2 Information technology - Open Systems Interconnection - Generic upper layers security: Security Exchange Service Element (SESE) service specification
ISO/IEC DIS 11586-3 Information technology - Open Systems Interconnection - Generic upper layers security: Security Exchange Service Element (SESE) protocol specification
ISO/IEC DIS 11586-4 Information technology - Open Systems Interconnection - Generic upper layers security: Protecting transfer syntax specification
ISO/IEC DIS 11586-5 Information technology - Open Systems Interconnection - Generic Upper Layers Security: Security Exchange Service Element Protocol Implementation Conformance Statement (PICS) 
ISO/IEC DIS 11586-6 Information technology - Open Systems Interconnection - Generic Upper Layers Security: Protecting Transfer Syntax Implementation Conformance Statement (PICS) 
ISO/IEC DIS 11770-1 Information technology - Security techniques - Key management - Part 1: Framework
ISO/IEC DIS 11770-2 Information technology - Security techniques - Key management - Part 2: Mechanisms using symmetric techniques
ISO/IEC DISP 12059-7 Information technology - International Standardized Profiles - OSI Management - Common information for management functions - Part 7: Security alarm reporting
ISO/IEC DISP 12059-8 Information technology - International Standardized Profiles - OSI Management - Common information for management functions - Part 8: Security audit trail
ISO/IEC DISP 12060-6 Information technology - International Standardized Profiles - OSI Management - Management functions - Part 6: Security management capabilities 
ISO/IEC DTR 13335-1 Information technology - Guidelines for the management of IT security - Part 1: Concepts and models for IT security
ISO/IEC DTR 13335-2 Information technology - Guidelines for the management of IT security - Part 2: Planning and managing IT security (Future Technical Report)
ISO/IEC DTR 13335-3 Information technology - Guidelines for the management of IT security - Part 3: Techniques for the management of IT security
ISO/IEC TR 13594:1995 Information technology - Lower layers security
ISO/IEC DIS 14980 Information technology - Code of practice for information security management

```

[1] Simson Garfinkel, "Practical Unix and Internet Security", II ed., O'Reilly, 2003 

---


# Podstawowe definicje i problemy

# Bezpieczeństwo systemów komputerowych - wykład 2:Podstawowe definicje i problemy
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Podstawowe definicje i problemy](https://wazniak.mimuw.edu.pl/<#Podstawowe_definicje_i_problemy>)
    * [1.1 Klasy ataków](https://wazniak.mimuw.edu.pl/<#Klasy_ataków>)
      * [1.1.1 pasywne / aktywne](https://wazniak.mimuw.edu.pl/<#pasywne_/_aktywne>)
      * [1.1.2 lokalne / zdalne](https://wazniak.mimuw.edu.pl/<#lokalne_/_zdalne>)
    * [1.2 Ogólne formy ataku elektronicznego](https://wazniak.mimuw.edu.pl/<#Ogólne_formy_ataku_elektronicznego>)
    * [1.3 Podstawowe fazy ataku](https://wazniak.mimuw.edu.pl/<#Podstawowe_fazy_ataku>)
    * [1.4 Podstawowe środki ostrożności](https://wazniak.mimuw.edu.pl/<#Podstawowe_środki_ostrożności>)
      * [1.4.1 Elementarna ochrona stacji roboczej](https://wazniak.mimuw.edu.pl/<#Elementarna_ochrona_stacji_roboczej>)
      * [1.4.2 Elementarna ochrona sieci lokalnej](https://wazniak.mimuw.edu.pl/<#Elementarna_ochrona_sieci_lokalnej>)
      * [1.4.3 Elementarna ochrona usług sieciowych](https://wazniak.mimuw.edu.pl/<#Elementarna_ochrona_usług_sieciowych>)
    * [1.5 Złożoność problemu stosowania zabezpieczeń](https://wazniak.mimuw.edu.pl/<#Złożoność_problemu_stosowania_zabezpieczeń>)
    * [1.6 Stosowanie mechanizmów bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Stosowanie_mechanizmów_bezpieczeństwa>)
      * [1.6.1 Zasada naturalnego styku z użytkownikiem](https://wazniak.mimuw.edu.pl/<#Zasada_naturalnego_styku_z_użytkownikiem>)
      * [1.6.2 Zasada spójności poziomej i pionowej](https://wazniak.mimuw.edu.pl/<#Zasada_spójności_poziomej_i_pionowej>)
      * [1.6.3 Zasada minimalnego przywileju](https://wazniak.mimuw.edu.pl/<#Zasada_minimalnego_przywileju>)
      * [1.6.4 Zasada domyślnej odmowy dostępu](https://wazniak.mimuw.edu.pl/<#Zasada_domyślnej_odmowy_dostępu>)
    * [1.7 Elementarne pojęcia](https://wazniak.mimuw.edu.pl/<#Elementarne_pojęcia>)
      * [1.7.1 1.Identyfikacja (ang. identification)](https://wazniak.mimuw.edu.pl/<#1.Identyfikacja_\(ang._identification\)>)
      * [1.7.2 2.Uwierzytelnianie (ang. authentication)](https://wazniak.mimuw.edu.pl/<#2.Uwierzytelnianie_\(ang._authentication\)>)
      * [1.7.3 3.Autoryzacja (ang. authorization)](https://wazniak.mimuw.edu.pl/<#3.Autoryzacja_\(ang._authorization\)>)
      * [1.7.4 4.Kontrola dostępu (ang. access control)](https://wazniak.mimuw.edu.pl/<#4.Kontrola_dostępu_\(ang._access_control\)>)
      * [1.7.5 5.Poufność (ang. confidentiality)](https://wazniak.mimuw.edu.pl/<#5.Poufność_\(ang._confidentiality\)>)
      * [1.7.6 6.Nienaruszalność (integralność; ang. data integrity)](https://wazniak.mimuw.edu.pl/<#6.Nienaruszalność_\(integralność;_ang._data_integrity\)>)
      * [1.7.7 7.Autentyczność (ang. authenticity)](https://wazniak.mimuw.edu.pl/<#7.Autentyczność_\(ang._authenticity\)>)
      * [1.7.8 8.Niezaprzeczalność (ang. nonrepudiation)](https://wazniak.mimuw.edu.pl/<#8.Niezaprzeczalność_\(ang._nonrepudiation\)>)
    * [1.8 Autoryzacja](https://wazniak.mimuw.edu.pl/<#Autoryzacja>)
      * [1.8.1 Zasób (obiekt)](https://wazniak.mimuw.edu.pl/<#Zasób_\(obiekt\)>)
      * [1.8.2 Podmiot](https://wazniak.mimuw.edu.pl/<#Podmiot>)
      * [1.8.3 Prawa dostępu](https://wazniak.mimuw.edu.pl/<#Prawa_dostępu>)
      * [1.8.4 Filozofie przydziału uprawnień](https://wazniak.mimuw.edu.pl/<#Filozofie_przydziału_uprawnień>)
    * [1.9 Kontrola dostępu do danych](https://wazniak.mimuw.edu.pl/<#Kontrola_dostępu_do_danych>)
      * [1.9.1 Uznaniowa kontrola dostępu (Discretionary Access Control)](https://wazniak.mimuw.edu.pl/<#Uznaniowa_kontrola_dostępu_\(Discretionary_Access_Control\)>)
      * [1.9.2 Ścisła kontrola dostępu (Mandatory Access Control)](https://wazniak.mimuw.edu.pl/<#Ścisła_kontrola_dostępu_\(Mandatory_Access_Control\)>)
    * [1.10 Klasy bezpieczeństwa systemów komputerowych](https://wazniak.mimuw.edu.pl/<#Klasy_bezpieczeństwa_systemów_komputerowych>)


## Podstawowe definicje i problemy
### Klasy ataków
#### pasywne / aktywne
Pod względem interakcji atakującego z atakowanym systemem wyróżniamy ataki: 
  * pasywne - atakujący ma dostęp do danych (komunikacji) w systemie, mogąc je odczytać, lecz ich nie modyfikuje - przykład: podsłuch komunikacji pomiędzy legalnymi użytkownikami systemu.


[![Bsi-w-02-01.png](https://wazniak.mimuw.edu.pl/images/thumb/0/08/Bsi-w-02-01.png/700px-Bsi-w-02-01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-01.png>)
  * aktywne - atakujący pośredniczy w przetwarzaniu danych (komunikacji) w systemie, mogąc je nie tylko odczytać, lecz również sfałszować czy spreparować z premedytacją, tak by uzyskać zamierzony cel ataku - taki atak nazywa się popularnie „człowiek w środku" (ang. „ _man in the middle_ ").


[![Bsi-w-02-02.png](https://wazniak.mimuw.edu.pl/images/thumb/4/47/Bsi-w-02-02.png/700px-Bsi-w-02-02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-02.png>)
#### lokalne / zdalne
Pod względem źródła rozpoczęcia ataku wyróżniamy ataki: 
  * lokalny - atakujący już ma dostęp do systemu (konto) i próbuje zwiększyć swe uprawnienia
  * zdalny - atakujący nie posiada jeszcze żadnych uprawnień w systemie atakowanym


### Ogólne formy ataku elektronicznego
Najczęściej spotykanymi formami ataku są: 
  * podszywanie (ang. _masquerading_) - atakujący (osoba, program) udaje inny podmiot, w domyśle zaufany systemowi atakowanemu, np. fałszywy serwer www podszywa się pod znaną witrynę internetową
  * podsłuch (ang. _eavesdropping_) - pozyskanie danych składowanych, przetwarzanych lub transmitowanych w systemie - typowy przykład: przechwycenie niezabezpieczonego hasła klienta przesyłanego do serwera
  * odtwarzanie (ang. _replaying_) - użycie ponowne przechwyconych wcześniej danych, np. hasła
  * manipulacja (ang. _tampering_) - modyfikacja danych w celu zrekonfigurowania systemu lub wprowadzenia go do stanu, z którego atakujący może osiągnąć bezpośrednio lub pośrednio korzyść (np. zastosować skuteczny atak gotowym narzędziem)
  * wykorzystanie luk w systemie (ang. _exploiting_) - posłużenie się wiedzą o znanej luce, błędzie w systemie lub gotowym narzędziem do wyeksploatowania takiej luki - bardzo częste w przypadku ataków zdalnych


Konkretne przypadki ataków ewoluują wraz z rynkiem informatycznym. Można np. przedstawić rys historyczny prawdopodobnie najbardziej typowych ataków przeprowadzanych w Internecie na przestrzeni ostatnich lat: 
[![Bsi-w-02-03a.png](https://wazniak.mimuw.edu.pl/images/thumb/f/f4/Bsi-w-02-03a.png/700px-Bsi-w-02-03a.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-03a.png>)
### Podstawowe fazy ataku
W czasie przeprowadzania ataku pojawiają się zwykle mniej lub bardziej jawnie następujące ogólne fazy: 
  1. skanowanie (wyszukanie słabości, np. sondowanie usług)
  2. wyznaczenie celu (np. niezabezpieczona usługa, znany exploit)
  3. atak na system
  4. modyfikacje systemu umożliwiające późniejszy powrót
  5. usuwanie śladów
  6. propagacja ataku


### Podstawowe środki ostrożności
W celu zminimalizowania podatności na typowe ataki należy stosować elementarne zasady „higieny osobistej". Dotyczą one wszystkich komponentów systemu informatycznego, stanowisk komputerowych, infrastruktury sieciowej , usług aplikacyjnych. 
#### Elementarna ochrona stacji roboczej
Do podstawowych środków ochrony stanowisk komputerowych można zaliczyć przykładowo: 
  * uniemożliwienie startowania systemu z nośników wymiennych
  * ograniczenie wykorzystania przestrzeni lokalnych dysków twardych
  * ograniczenie stosowania nośników wymiennych (stacji dyskietek, nagrywarek)
  * rejestracja prób dostępu do systemu i ich limitowanie (kontrola, kto i kiedy korzystał z systemu)
  * bezpieczne kasowanie poufnych danych
  * uniemożliwienie usunięcia / wyłączenia zabezpieczeń, np. antywirusowych
  * konsekwentna polityka haseł użytkowników


#### Elementarna ochrona sieci lokalnej
Do podstawowych środków ochrony infrastruktury sieciowej można zaliczyć przykładowo: 
  * dobór medium i topologii gwiazdy (okablowanie strukturalne)
  * fizyczna ochrona pomieszczeń z węzłami sieci i serwerami
  * zdefiniowanie listy stanowisk, z których dany użytkownik może uzyskać dostęp do systemu (adresy MAC lub IP)
  * usuwanie nieużywanych kont użytkowników


#### Elementarna ochrona usług sieciowych
Procedura ochrony dostępu do usług sieciowych polega w ogólności na skrupulatnym przeprowadzeniu następującej sekwencji operacji: 
  1. usunięcie z systemu wszystkich usług zbędnych, najlepiej poprzez całkowite odinstalowanie, a co najmniej - dezaktywację
  2. zastąpienie usług niezbędnych odpowiednikami o podwyższonym bezpieczeństwie (jeśli to możliwe i takie odpowiedniki są dostępne)
  3. kontrola dostępu do pozostałych usług (np. poprzez zapory sieciowe _firewall_)


### Złożoność problemu stosowania zabezpieczeń
Z realizacją zabezpieczeń związany jest szereg problemów, stawiających broniących od razu na pozycji gorszej niż atakującego. Dotyczą one m.in. asymetrii obrony i ataku, konieczności uwzględniania kontekstu całego otoczenia celu zabezpieczeń oraz trudności utrzymania poprawności zabezpieczeń (zarządzania i pielęgnacji). 
  * **asymetria**


_Aby skutecznie zabezpieczyć system należy usunąć ''_**wszystkie''**_słabości, aby skutecznie zaatakować - wystarczy znaleźć ''_**jedną''**_._
  * **kontekst otoczenia systemu**


_Bezpieczeństwo powinno być rozważane w kontekście nie pojedynczego systemu informatycznego, ale całego otoczenia, w którym on się znajduje._
  * **zarządzanie i pielęgnacja**


_Zabezpieczenie systemu nie jest pojedynczą operacją, ale ciągłym procesem._
### Stosowanie mechanizmów bezpieczeństwa
W związku z w/w trudnościami realizacji zabezpieczeń istotne jest stosowanie kilku podstawowych reguł, w szczególności są to: 
  * zasada naturalnego styku z użytkownikiem
  * zasada spójności poziomej i pionowej
  * zasada minimalnego przywileju
  * zasada domyślnej odmowy dostępu


#### Zasada naturalnego styku z użytkownikiem
Zabezpieczenie nie możne być postrzegane przez użytkowników jako nienaturalny element systemu, stanowiący utrudnienie w ich pracy. Jeśli wprowadzony zostanie nawet najbardziej wyrafinowany mechanizm bezpieczeństwa, którego jednak stosowanie będzie wymagało od użytkowników dodatkowo zbyt obciążających ich (czasochłonnych) operacji, to wkrótce wypracują oni sposób jego permanentnego obejścia i - w efekcie stanie się ów mechanizm bezużyteczny. 
#### Zasada spójności poziomej i pionowej
Stosowanie zabezpieczeń w systemie musi zapewniać podstawowy warunek kompletności: spójność poziomą i pionową. Są one odpowiednikiem reguły „trwałości łańcucha", która mówi, iż cały łańcuch jest tak trwały, jak jego najsłabsze ogniwo. Spójność pozioma wymaga aby wszystkie, spośród potencjalnie wielu komponentów w danej warstwie systemu (jako dobry przykład modelu warstwowego można tu obrać model OSI obowiązujący w sieciach komputerowych), zostały zabezpieczone na jednakowym poziomie. W życiu codziennym spotykamy przykłady tej reguły - gdy zabezpieczamy okna pomieszczenia kratami, to wszystkie, a nie co drugie, gdy budujemy ogrodzenie, to do wysokości identycznie trudniej do sforsowania na całej jego długości. Gdy zabezpieczamy protokoły komunikacyjne danej warstwy modelu OSI, którymi posługuje się nasz system, to wszystkie niezbędne, a nie tylko jeden wybrany, choćby był on popularniejszy i częściej wykorzystywany od pozostałych. 
Spójność pionowa mówi o konieczności zastosowania kompletnych zabezpieczeń „w pionie" - jak kraty w oknach na pierwszym piętrze, to i na parterze czy innej „dostępnej" z zewnątrz kondygnacji, analogicznie - jak jedna warstwa przez którą istnieje dostęp do systemu, to każda inna, w której niezależnie taki dostęp też jest możliwy. 
#### Zasada minimalnego przywileju
Użytkownikom należy udzielać uprawnień w sposób zgodny z polityką bezpieczeństwa - tylko i wyłącznie takich, które są niezbędne do zrealizowania ich pracy. Zmianie zakresu obowiązków użytkownika powinna towarzyszyć zmiana zakresu uprawnień. 
#### Zasada domyślnej odmowy dostępu
Jeśli na podstawie zdefiniowanych reguł postępowania mechanizmy obrony nie potrafią jawnie rozstrzygnąć, jaką decyzję podjąć wobec analizowanych operacji (np. nadchodzącego pakietu protokołu komunikacyjnego), to decyzją ostateczną powinna być odmowa dostępu (odrzucenie pakietu). Wiele urządzeń i protokołów jest jednak domyślnie konfigurowanych inaczej, czy to w celu wygody użytkownika, czy z założenia wynikającego z ich funkcji (por. routing). 
### Elementarne pojęcia
W celu przedstawienia problematyki ataku i obrony należy wprowadzić definicje niezbędnych pojęć. Dotyczyć one będą w szczególności użytkowników, ale także i innych komponentów systemu. 
##### 1.Identyfikacja (ang. identification)
  * możliwość rozróżnienia użytkowników, np. użytkownicy są identyfikowani w systemie operacyjnym za pomocą UID (_user identifier_)


##### 2.Uwierzytelnianie (ang. authentication)
  * proces weryfikacji tożsamości użytkownika; najczęściej opiera się na tym: 
    * co użytkownik wie (_proof by knowledge_), np. zna hasło
    * co użytkownik ma (_proof by possession_), np. elektroniczną kartę identyfikacyjną


##### 3.Autoryzacja (ang. authorization)
  * proces przydzielania praw (dostępu do zasobów) użytkownikowi


##### 4.Kontrola dostępu (ang. access control)
  * procedura nadzorowania przestrzegania praw (dostępu do zasobów)


##### 5.Poufność (ang. confidentiality)
  * ochrona informacji przed nieautoryzowanym jej ujawnieniem


##### 6.Nienaruszalność (integralność; ang. data integrity)
  * ochrona informacji przed nieautoryzowanym jej zmodyfikowaniem (ew. detekcja takiej modyfikacji)


##### 7.Autentyczność (ang. authenticity)
  * pewność co do pochodzenia (autorstwa i treści) danych


##### 8.Niezaprzeczalność (ang. nonrepudiation)
  * ochrona przed fałszywym zaprzeczeniem 
    * przez nadawcę - faktu wysłania danych
    * przez odbiorcę - faktu otrzymania danych


### Autoryzacja
Z procesem autoryzacji związane są kolejne pojęcia: 
##### Zasób (obiekt)
  * jest jednostką, do której dostęp podlega kontroli
  * przykłady: programy, pliki, relacje bazy danych, czy całe bazy danych
  * obiekty o wysokiej granulacji: poszczególne krotki bazy danych


##### Podmiot
  * ma dostęp do zasobu
  * przykłady: użytkownik, grupa użytkowników, terminal, komputer, aplikacja, proces


##### Prawa dostępu
  * określają dopuszczalne sposoby wykorzystania zasobu przez podmiot


#### Filozofie przydziału uprawnień
W dowolnym modelu autoryzacji można stosować jedną z poniższych czterech możliwych filozofii: 
  1. Wszystko jest dozwolone.
  2. Wszystko, co nie jest (jawnie) zabronione, jest dozwolone.
  3. Wszystko, co nie jest (jawnie) dozwolone, jest zabronione.
  4. Wszystko jest zabronione.


Z praktycznego punktu widzenia w grę wchodzić mogą środkowe dwie. Jak można zaobserwować, tylko trzecia jest zgodna z zasadą minimalnego przywileju i domyślnej odmowy dostępu. 
### Kontrola dostępu do danych
Wyróżnia się dwie ogólne metody kontroli dostępu do danych: uznaniową (DAC) i ścisłą. (MAC) Istnieją też ich różne warianty - jak np. kontrola oparta o role (RBAC) powszechnie spotykana np. systemach baz danych. 
#### Uznaniowa kontrola dostępu (Discretionary Access Control)
Podstawowe własności tego podejścia są następujące: 
  * właściciel zasobu może decydować o jego atrybutach i uprawnieniach innych użytkowników systemu względem tego zasobu
  * DAC oferuje użytkownikom dużą elastyczność i swobodę współdzielenia zasobów
  * powszechnym zagrożeniem jest niefrasobliwość przydziału uprawnień (np. wynikająca z nieświadomości lub zaniedbań) i niewystarczająca ochrona zasobów
  * najczęściej uprawnienia obejmują operacje odczytu i zapisu danych oraz uruchomienia programu


#### Ścisła kontrola dostępu (Mandatory Access Control)
Podstawowe własności tego podejścia są następujące: 
  * precyzyjne reguły dostępu automatycznie wymuszają uprawnienia
  * nawet właściciel zasobu nie może dysponować prawami dostępu
  * MAC pozwala łatwiej zrealizować (narzucić) silną politykę bezpieczeństwa i konsekwentnie stosować ją do całości zasobów


Ścisła kontrola dostępu operuje na tzw. poziomach zaufania wprowadzając **etykiety poziomu zaufania**(_sensitivity labels_) przydzielane w zależności np. od stopnia poufności. Mogą one być następjące: 
```
 ogólnie dostępne < do użytku wewn. < tylko dyrekcja < tylko zarząd

```

czy w innego typu instytucji: 
```
 jawne < poufne < tajne < ściśle tajne

```

Oprócz poziomu zaufania, każdy zasób posiada kategorię przynależności danych. Kategorie te nie są hierarchiczne i reprezentują jedynie rodzaj wykorzystania danych, np.: 
```
 FINANSOWE, OSOBOWE, KRYPTO, MILITARNE

```

W celu określenia uprawnień w systemach MAC są konstruowane **etykiety ochrony danych**. Składają się one z 2 parametrów: poziomu zaufania i kategorii informacji, np. 
```
 (tajne, {KRYPTO})
 (ściśle tajne, {KRYPTO,MILITARNE})

```

Na zbiorze etykiet ochrony danych określona jest relacja wrażliwości: 
```
 (ściśle tajne, {KRYPTO,MILITARNE}) -> (tajne, {KRYPTO})

```

Jest to relacja częściowego porządku, nie wszystkie etykiety do niej należą. Przykładowo może nie być określona relacja pomiędzy etykietą: 
```
 (ściśle tajne, {KRYPTO,MILITARNE})

```

a etykietą: 
```
 (tajne, {FINANSOWE,KRYPTO})

```

Wobec podmiotów i zasobów w systemie MAC narzucone są niezmienne reguły, które wymusza system. Podmiot nie może mianowicie czytać danych o wyższej etykiecie (_read-up_) niż swoja aktualna. Podmiot nie może również zapisywać danych o niższej etykiecie (_write-down_) niż swoja aktualna. Zbiór reguł przedstawia rysunek: 
```
 MAC 1:Użytkownik może uruchomić tylko taki proces, który posiada etykietę nie wyższą od aktualnej etykiety użytkownika.
 MAC 2:Proces może czytać dane o etykiecie nie wyższej niż aktualna etykieta procesu.
 MAC 3:Proces może zapisać dane o etykiecie nie niższej niż aktualna etykieta procesu.

```

**Reguły MAC**
### Klasy bezpieczeństwa systemów komputerowych
W historii dziedziny bezpieczeństwa systemów komputerowych od początku starano się stworzyć reguły klasyfikacji systemów. Opracowano standardy certyfikacji: 
  * Trusted Computer System Evaluation Criteria (TCSEC "Orange Book") - USA <http://www.radium.ncsc.mil/tpep/library/rainbow/5200.28-STD.html> ; jest to standard opracowany w USA, ale stał się pierwszym powszechnym takim standardem w skali światowej. Owiązujący w latach 1983-2000 stał się podstawą opracowywania podobnych norm w Europie i na świecie. Bardzo często nawet współcześnie znajduje się odwołania do certyfikatów tego standardu.
  * Information Technology Security Evaluation Criteria (ITSEC) - EU <http://www.cesg.gov.uk> ; obowiązywał w 1991-1997. Powstał głównie z angielskiego CESG2/DTIEC, francuskiego SCSSI i niemieckiego ZSIEC.
  * Common Criteria Assurance Levels (EAL) - aktualnie obowiązujący standard będący w istocie złączeniem ITSEC, TCSEC oraz CTCPEC (Kanada). Od 1996 powszechnie znany jako Common Criteria for Information Technology Security Evaluation (CC; <http://www.commoncriteria.org>). Od 1999 roku zaakceptowany jako międzynarodowa norma ISO15408 ( EAL v.2).


Poniżej zostaną przedstawione wymagania klas bezpieczeństwa systemów komputerowych wg oryginalnej propozycji TCSEC "Orange Book". Schematyczne porównanie klas różnych standardów można znaleźć w tablece 1. 
KLASA WŁASNOŚCI 
D
    - minimalna ochrona (właściwie jej brak)
C1
    - identyfikacja i uwierzytelnianie użytkowników,
    - hasła chronione
    - luźna kontrola dostępu na poziomie właściciela / grupy / pozostałych użytkowników
    - ochrona obszarów systemowych pamięci
C2
    - kontrola dostępu na poziomie poszczególnych użytkowników
    - automatyczne czyszczenie przydzielanych obszarów pamięci
    - wymagana możliwość rejestracji dostępu do zasobów
B1
    - etykietowane poziomy ochrony danych
B2
    - ochrona strukturalna - jądro ochrony
    - weryfikacja autentyczności danych i procesów
    - informowanie użytkownika o dokonywanej przez jego proces zmianie poziomu bezpieczeństwa
    - wykrywanie zamaskowanych kanałów komunikacyjnych
    - ścisła rejestracja operacji
B3
    - domeny ochronne
    - aktywna kontrola pracy systemu (security triggers)
    - bezpieczne przeładowanie systemu
A1
    - formalne procedury analizy i weryfikacji projektu i implementacji systemu
**Tabelka 1. Porównanie klas bezpieczeństwa systemów komputerowych**
[![Bsi-w-02-04.png](https://wazniak.mimuw.edu.pl/images/thumb/a/a0/Bsi-w-02-04.png/100px-Bsi-w-02-04.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-04.png>)
[![Bsi-w-02-05.png](https://wazniak.mimuw.edu.pl/images/thumb/f/f1/Bsi-w-02-05.png/100px-Bsi-w-02-05.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-05.png>)
**TCSEC** | **ITCES** | **CC / EAL**  
---|---|---  
D  | E0  | EAL1   
C1  | E1, F-C1  | EAL2   
C2  | E2, F-C2  | EAL3   
B1  | E3, F-B1  | EAL4   
B2  | E4, F-B2  | EAL5   
B3  | E5, F-B3  | EAL6   
A1  | E6, F-B3  | EAL7   
Popularne systemy operacyjne plasują się na różnych poziomach klas bezpieczeństwa. Trzeba zaznaczyć, iż uzyskanie certyfikatu danej klasy jest operacją formalną i odpłatną. 
[![Bsi-w-02-06.png](https://wazniak.mimuw.edu.pl/images/thumb/f/fe/Bsi-w-02-06.png/700px-Bsi-w-02-06.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-02-06.png>)
Źródło: „[https://wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_2:Podstawowe_definicje_i_problemy&oldid=9502](https://wazniak.mimuw.edu.pl/<https:/wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_2:Podstawowe_definicje_i_problemy&oldid=9502>)”
---


# Ogólne własności bezpieczeństwa informacji

# Bezpieczeństwo systemów komputerowych - wykład 3:Ogólne własności bezpieczeństwa informacji
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Ogólne własności bezpieczeństwa informacji](https://wazniak.mimuw.edu.pl/<#Ogólne_własności_bezpieczeństwa_informacji>)
    * [1.1 Podstawowe własności bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Podstawowe_własności_bezpieczeństwa>)
    * [1.2 Poufność informacji](https://wazniak.mimuw.edu.pl/<#Poufność_informacji>)
      * [1.2.1 Zagrożenia](https://wazniak.mimuw.edu.pl/<#Zagrożenia>)
      * [1.2.2 Mechanizmy obrony](https://wazniak.mimuw.edu.pl/<#Mechanizmy_obrony>)
    * [1.3 Uwierzytelnianie](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie>)
    * [1.4 Mechanizmy uwierzytelniania użytkowników](https://wazniak.mimuw.edu.pl/<#Mechanizmy_uwierzytelniania_użytkowników>)
      * [1.4.1 Klasyczne uwierzytelnianie użytkownika](https://wazniak.mimuw.edu.pl/<#Klasyczne_uwierzytelnianie_użytkownika>)
      * [1.4.2 Zdalne potwierdzanie tożsamości użytkownika](https://wazniak.mimuw.edu.pl/<#Zdalne_potwierdzanie_tożsamości_użytkownika>)
      * [1.4.3 Uwierzytelnianie jednokrotne (SSO – single sign-on)](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_jednokrotne_\(SSO_–_single_sign-on\)>)
      * [1.4.4 Hasła jednorazowe (OTP – one-time passwords)](https://wazniak.mimuw.edu.pl/<#Hasła_jednorazowe_\(OTP_–_one-time_passwords\)>)
      * [1.4.5 Inne mechanizmy uwierzytelniania](https://wazniak.mimuw.edu.pl/<#Inne_mechanizmy_uwierzytelniania>)
    * [1.5 Autoryzacja i kontrola dostępu do zasobów](https://wazniak.mimuw.edu.pl/<#Autoryzacja_i_kontrola_dostępu_do_zasobów>)
      * [1.5.1 Mechanizmy ochrony dostępu do danych](https://wazniak.mimuw.edu.pl/<#Mechanizmy_ochrony_dostępu_do_danych>)
    * [1.6 Utrudnianie podsłuchu](https://wazniak.mimuw.edu.pl/<#Utrudnianie_podsłuchu>)
    * [1.7 Nienaruszalność informacji (integralność)](https://wazniak.mimuw.edu.pl/<#Nienaruszalność_informacji_\(integralność\)>)
      * [1.7.1 Zagrożenia](https://wazniak.mimuw.edu.pl/<#Zagrożenia_2>)
      * [1.7.2 Mechanizmy obrony](https://wazniak.mimuw.edu.pl/<#Mechanizmy_obrony_2>)
    * [1.8 Dostępność informacji](https://wazniak.mimuw.edu.pl/<#Dostępność_informacji>)
      * [1.8.1 Zagrożenia](https://wazniak.mimuw.edu.pl/<#Zagrożenia_3>)


## Ogólne własności bezpieczeństwa informacji
### Podstawowe własności bezpieczeństwa
Często wyróżnia się 3 podstawowe własności bezpieczeństwa informacji, których zachowanie jest konieczne w większości zastosowań systemów informatycznych. Są to poufność, nienaruszalność i dostępność informacji (rysunek 1). 
[![Bsi-w-03-01.png](https://wazniak.mimuw.edu.pl/images/thumb/6/66/Bsi-w-03-01.png/700px-Bsi-w-03-01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-01.png>)
**Rysunek '**_1'_**. Trzy podstawowe własności bezpieczeństwa informacji**
Zajmiemy się teraz omówieniem wybranych zagrożeń związanych z tymi trzema własnościami oraz krótkim przedstawieniem mechanizmów stosowanych w celu osiągnięcia tych własności. 
### Poufność informacji
#### Zagrożenia
Poufność, rozumiana - jak wiemy - jako ochrona przed nieautoryzowanym ujawnieniem (odczytem) informacji, narażona jest na ataki poprzez: 
  * nieuprawniony dostęp do danych w miejscu składowania w systemie, np. w bazie danych
  * nieuprawniony dostęp do danych w miejscu przetwarzania, np. w aplikacji końcowej użytkownika
  * podsłuchanie danych przesyłanych w sieci


Szczególny nacisk można położyć na szeroko rozumiany podsłuch, który dotyczy nie tylko oczywistego przypadku transmisji danych. Należy podkreślić techniczną możliwość podsłuchu zdalnego większości urządzeń infrastruktury systemu komputerowego, poprzez tzw. receptory Van Ecka. Dotyczy to urządzeń emitujących promieniowanie elektromagnetyczne (jak np. monitory ekranowe, szczególnie starszego typu - CRT). Zatem ten rodzaj podsłuchu stanowi teoretyczne zagrożenie również dla danych składowanych oraz przetwarzanych na stanowiskach komputerowych, niezależnie od komunikacji sieciowej. 
#### Mechanizmy obrony
W celu ochrony informacji przed jej nieautoryzowanym odczytem należy przede wszystkim umieć określić czy zamierzony odczyt jest autoryzowany oraz zminimalizować prawdopodobieństwo „wycieku" danych poza mechanizmem kontroli dostępu (w transmisji). Zatem mechanizmy obrony stosowane do zapewnienia poufności realizować będą następujące zadania: 
  * uwierzytelnianie
  * autoryzację i kontrolę dostępu do zasobów
  * utrudnianie podsłuchu


Omówimy kolejno problematykę wymienionych zadań i pokażemy przykłady mechanizmów, które je realizują. 
### Uwierzytelnianie
W systemach informatycznych stosuje się następujące rodzaje uwierzytelniania: 
  1. uwierzytelnianie jednokierunkowe – polega na uwierzytelnieniu jednego podmiotu (uwierzytelnianego), np. klienta aplikacji, wobec drugiego (uwierzytelniającego) – serwera. Obrazuje to rysunek 2. Uwierzytelnienie następuje poprzez zweryfikowanie danych uwierzytelniających przekazanych przez podmiot uwierzytelniany. Typowymi danymi uwierzytelniającymi są np. identyfikator użytkownika i jego hasło dostępu.
[![Bsi-w-03-02.png](https://wazniak.mimuw.edu.pl/images/thumb/8/82/Bsi-w-03-02.png/700px-Bsi-w-03-02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-02.png>)
**Rysunek '**_2'_**. Uwierzytelnianie jednokierunkowe**
  2. uwierzytelnianie dwukierunkowe – polega na kolejnym lub jednoczesnym uwierzytelnieniu obu podmiotów (które są wzajemnie i naprzemiennie uwierzytelnianym oraz uwierzytelniającym). Obrazuje to rysunek 3. Jeżeli wzajemne uwierzytelnianie następuje sekwencyjnie (np. najpierw klient wobec serwera, a później serwer wobec klienta), mówimy o uwierzytelnianiu dwuetapowym, natomiast jednoczesne uwierzytelnienie obu stron nazywamy jednoetapowym.
[![Bsi-w-03-03.png](https://wazniak.mimuw.edu.pl/images/thumb/f/f2/Bsi-w-03-03.png/700px-Bsi-w-03-03.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-03.png>)
**Rysunek '**_3'_**. Uwierzytelnianie dwukierunkowe**
  3. uwierzytelnianie z udziałem zaufanej trzeciej strony – włącza w proces uwierzytelniania trzecią zaufaną stronę, która bierze na siebie ciężar weryfikacji danych uwierzytelniających podmiotu uwierzytelnianego. Po pomyślnej weryfikacji podmiot uwierzytelniany otrzymuje poświadczenie, które następnie przedstawia zarządcy zasobu, do którego dostępu żąda (serwerowi). Schemat ten pokazuje rysunek 4. Podstawową zaletą tego podejścia jest przesunięcie newralgicznej operacji uwierzytelniania do wyróżnionego stanowiska, które można poddać szczególnie podwyższonemu zabezpieczeniu. Należy też podkreślić potencjalną możliwość wielokrotnego wykorzystania wydanego poświadczenia (przy dostępie klienta do wielu zasobów, serwerów). Zaufana trzecia strona może być lokalna dla danej sieci komputerowej (korporacyjnej) lub zewnętrzna (wykorzystująca infrastrukturę uwierzytelniania dostępną w sieci rozległej np. publiczne urzędy certyfikujące).
[![Bsi-w-03-04.png](https://wazniak.mimuw.edu.pl/images/thumb/d/dd/Bsi-w-03-04.png/700px-Bsi-w-03-04.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-04.png>)
**Rysunek '**_4'_**. Uwierzytelnianie z udziałem zaufanej trzeciej strony**


### Mechanizmy uwierzytelniania użytkowników
#### Klasyczne uwierzytelnianie użytkownika
W przypadku wielu współczesnych środowisk informatycznych, systemów operacyjnych lub systemów zarządzania bazami danych, funkcjonuje klasyczny mechanizm uwierzytelniania poprzez hasło. Proces uwierzytelniania rozpoczyna klient żądając zarejestrowania w systemie (_login_). Serwer pyta o identyfikator (nazwę) użytkownika, a następnie o hasło i decyduje o dopuszczeniu do sieci. W większości przypadków nazwa użytkownika i hasło są przesyłane tekstem jawnym, co stanowić może kolejny problem zapewnienia poufności, jaką właśnie mamy osiągnąć stosując opisywany mechanizm. Stąd też takie klasyczne podejście nadaje się do wykorzystania jedynie w ograniczonej liczbie przypadków, kiedy np. mamy uzasadnioną skądinąd pewność wykluczenia możliwości podsłuchu danych uwierzytelniających. 
[![Bsi-w-03-05.png](https://wazniak.mimuw.edu.pl/images/thumb/8/83/Bsi-w-03-05.png/700px-Bsi-w-03-05.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-05.png>)
**Rysunek '**_5'_**. Klasyczne uwierzytelnianie użytkownika**
Hasła nie są najefektywniejszą, ani najbezpieczniejszą formą weryfikacji tożsamości użytkownika, z następujących powodów 
  * hasło można złamać:
  * odgadnąć, np. metodą przeszukiwania wyczerpującego (_brute-force attack_) lub słownikową (_dictionary attack_) - często hasła są wystarczająco nieskomplikowane by ułatwiło to odgadnięcie ich przez atakującego
  * podsłuchać w trakcie niezabezpieczonej transmisji
  * wykraść z systemowej bazy haseł użytkowników - zwykle hasła nie są przechowywane w systemie w postaci jawnej, często są zakodowane funkcją jednokierunkową lub zaszyfrowane, jednak niekiedy można stosunkowo łatwo jest pobrać i następnie starać się odzyskać ich oryginalną postać
  * pozyskać inną metodą (np. kupić)
  * hasła się starzeją - czas przez który możemy z dużą pewnością polegać na tajności naszego hasła skraca się nieustannie, przez co hasła wymagają systematycznych zmian na nowe
  * w niektórych środowiskach aplikacyjnych stosuje się predefiniowane konta użytkowników (również o charakterze administracyjnym) i przypisuje się im dość powszechnie znane hasła domyślne - usuwanie lub dezaktywowanie takich kont czy zmiany haseł wymagają dużej staranności


Hasła są przedmiotem ataków - słownikowego i metodą przeszukiwania wyczerpującego. Słownikowy atak polega na podejmowaniu kolejnych prób zweryfikowania czy hasło wybierane ze zbioru popularnie stosowanych haseł (tzw. słownika) odpowiada hasłu aktualnie ustawionemu dla konta będącego celem ataku. Wariantem tego ataku jest wykradzenie nawet zakodowanych danych uwierzytelniających z systemu, aby po weryfikować czy kolejne hasła ze słownika dają po odpowiednim zakodowaniu którąś z postaci przechowywanych w systemie. 
Przykładem analizy podatności haseł na atak słownikowy jest kilkukrotnie wykonane badanie, znane powszechnie jako raport Kleina. Operacje wykonywane w tym badaniu doskonale odzwierciedlają metodologię tworzenia słownika i mogą być doskonałą ilustracją zagrożeń wynikających z wyboru słabych haseł. W skrócie opisując Klein wykonał następujące operacje służące do uzyskania słownika haseł: 
  * wejściową postać słownika utworzyły nazwy użytkowników w systemie, ich inicjały oraz inne dostępne informacje (np. daty urodzin)
  * następnie dodane zostały imiona i ich permutacje, nazwy miejsc, nazwiska sławnych ludzi, tytuły filmów i książek S-F oraz nazwiska postaci, dziedziny sportu i terminy sportowe
  * wejściowy rozmiar słownika objął w efekcie ok. 1 500 haseł
  * na tej zawartości słownika wykonane zostały przekształcenia powszechnie stosowane przez użytkowników: np. zmiana pierwszej litery na wielką, zastąpienie pierwszej litery znakiem sterującym, zamianę litery _o_ na 0 czy _l_ na 1, utworzenie liczby mnogiej, dodanie przed- i przyrostków
  * dalej dołączone zostały kombinacje małych i wielkich liter haseł
  * co dało łącznie ok. 1 000 000 słów


Z tak przygotowanym słownikiem zrealizowano atak na hasła użytkowników w rzeczywistym systemie. Efekty przedstawia poniższa lista trafień haseł (fragment) ze słownika wg poszczególnych kategorii (bez uwzględniania wśród nich przekształceń i kombinacji): 
  * nazwa użytkownika: ponad 10%
  * nazwy pospolite: ponad 16%
  * imiona żeńskie: 4,8%
  * imiona męskie: 4%
  * mity i legendy: 2%
  * sport: 0,8%
  * słownik środowiska korekty językowej dostępny w systemie operacyjnym (/usr/dict/words): blisko 30%


Wszystkie wymienione kategorie (nie jest to lista kompletna) należy uznać, jak widać, za słabe hasła i wystrzegać się ich przy wyborze własnego. 
Przeszukiwanie wyczerpujące („atak brutalny") polega kolejnym weryfikowaniu całej przestrzeni haseł, czyli wybieraniu wszystkich możliwych permutacji znaków z alfabetu wykorzystywanego przy ustawianiu hasła użytkownika. Taki atak jest oczywiście kosztowny czasowo - wymaga prób dopasowania każdej permutacji do odgadywanego hasła, co zależy od wielkości alfabetu i długości hasła (rozmiaru przestrzeni haseł). 
Prawdopodobieństwo odgadnięcia hasła wyraża wzór (1): 
P = L ⋅ R S {\displaystyle P={\frac {L\cdot R}{S}}} ![{\\displaystyle P={\\frac {L\\cdot R}{S}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/f6732ea27c9e5bdcbb6f27b2821d1a4d4b9fc8c3) (**0**) 
gdzie
    _L_ = czas obowiązywania hasła
    _R_ = współczynnik szybkości (ilość prób na jednostkę czasu)
    _S_ = przestrzeń haseł - dla haseł o długości _k_ z alfabetu _N_ znaków: _S = N_ _k_
Uwzględniając zagrożenia wynikające z przedstawionych ataków na hasła, można zaproponować następujące „żelazne reguły" higieny haseł: 
czego nie wolno
  * wybierać hasła o długości krótszej niż 6 znaków
  * wybierać jako hasło znanego słowa, imienia, nazwiska, daty urodzenia, numeru telefonu, numeru rejestracyjnego
  * zmieniać hasła tak, by nowe było zależne od starego (np. z 012345 na 123456)
  * zapisywać hasła w widocznych lub łatwo dostępnych miejscach (jak np. fragment biurka zakryty klawiaturą, wnętrze szuflady czy płyta z danymi)
  * informować nikogo o swoim haśle


co należy
  * wybierać długie i mało znane słowo lub frazę (kombinacja różnych znaków)
  * wybrać hasło w sposób na tyle losowy na ile tylko możliwe
  * zmieniać hasło możliwie często, lecz w nieprzewidywalny sposób
  * zmienić hasło natychmiast, jak tylko rodzi się podejrzenie, że ktoś mógł je poznać


co warto
  * opracować własny algorytm generowania haseł - wybór pierwszych liter słów ulubionej fraszki, ostatnich znaków z wersów wiersza lub wybranej strony książki itp.
  * zlecić systemowi wygenerowanie trudnego hasła


#### Zdalne potwierdzanie tożsamości użytkownika
W środowisku sieci TCP/IP wypracowano mechanizm prostego potwierdzania tożsamości użytkownika, który żąda zdalnego uwierzytelniania. W tym celu powstał standard RFC 1413 opisujący usługę o nazwie ident. Niezależnie od jej aktualnej przydatności i powszechności warto zdawać sobie sprawę z istoty jej działania, którą łatwo opisać w następujący sposób: 
  * użytkownik uruchamia klienta usługi i nawiązuje połączenie z serwerem
  * serwer kontaktuje się z wydzielonym serwerem - identd, pracującym na stacji klienta (113/tcp) w celu poświadczenia nazwy (lub identyfikatora) użytkownika wykorzystującego usługę


[![Bsi-w-03-07.png](https://wazniak.mimuw.edu.pl/images/thumb/2/27/Bsi-w-03-07.png/700px-Bsi-w-03-07.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-07.png>)
**Rysunek '**_6'_**. Klasyczne uwierzytelnianie użytkownika**
Należy też zdawać sobie sprawę z potencjalnych zagrożeń jakie niesie udostępnianie przez usługę ident informacji o przynależności procesów dokonujących komunikacji sieciowej (nie tylko klientów). W standardzie RFC 1413 oraz w praktycznych implementacjach nie realizuje się bowiem uwierzytelniania podmiotu żądającego informacji z tej usługi, może ona być zatem również nadużyta przez potencjalnego włamywacza. 
#### Uwierzytelnianie jednokrotne (SSO – single sign-on)
Procedury uwierzytelniania jednokrotnego są częściowym rozwiązaniem problemu ochrony danych uwierzytelniających przed złamaniem w systemie wielozasobowym, np. sieci komputerowej z wieloma serwerami. 
Ideą procedury uwierzytelniania jednokrotnego jest minimalizacja ilości wystąpień danych uwierzytelniających w systemie - hasło powinno być podawana jak najrzadziej. Zgodnie z tą zasadą, jeśli jeden z komponentów systemu (np. system operacyjny) dokonał pomyślnie uwierzytelniania użytkownika, pozostałe komponenty (np. inne systemy lub zarządcy zasobów) ufać będą tej operacji i nie będą samodzielnie wymagać podawania ponownie danych uwierzytelniających. Przy tym jest możliwe teoretycznie, że wszystkie komponenty samodzielnie korzystają z odmiennych mechanizmów uwierzytelniana. Wówczas, dodatkowo po pierwszorazowym uwierzytelnieniu użytkownika, system może oddelegować specjalny moduł do przechowywania odrębnych danych uwierzytelniających użytkownika i poświadczania w przyszłości jego tożsamości wobec innych komponentów systemu. 
Schemat SSO przedstawia rysunek 7. W przedstawionej na rysunku sytuacji tylko jeden serwer dokonuje uwierzytelniania klienta, reszta ufa uwierzytelnianiu dokonanemu przez ten serwer. 
[![Bsi-w-03-08.png](https://wazniak.mimuw.edu.pl/images/thumb/c/cc/Bsi-w-03-08.png/700px-Bsi-w-03-08.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-08.png>)
**Rysunek '**_7'_**. Uwierzytelnianie jednokrotne (SSO)**
#### Hasła jednorazowe (OTP – one-time passwords)
Istota wykorzystania haseł jednorazowych wynika zamiaru ochrony ich przed przechwyceniem i nieautoryzowanym wykorzystanie, w przyszłości. Jednak nie polega na zapewnieniu ich poufności w transmisji lecz na uczynieniu ich _de facto_ bezwartościowymi po przechwyceniu. Opiera się na, jak sama nazwa wskazuje, tylko użyciu danej postaci hasła tylko raz. Hasła jednorazowe mają przy każdym kolejnym uwierzytelnieniu inną postać. Raz przechwycone hasło jednorazowe nie jest przydatne, bowiem przy kolejnym uwierzytelnieniu będzie obowiązywać już inne. Komunikacja między podmiotami procesu uwierzytelniania może być zatem jawna. Stosujące takie hasła procedury uwierzytelniania muszą jedynie oferować brak możliwości odgadnięcia na podstawie jednego z haseł, hasła następnego. 
Hasła jednorazowe generowane są przy pomocy listy haseł, synchronizacji czasu lub metody zawołanie-odzew. Dostępne są najczęściej w następujących postaciach: listy papierowe, listy-zdrapki, tokeny programowe i tokeny sprzętowe. 
Listy haseł to najprostsza i najtańsza metoda identyfikacji metodą haseł jednorazowych. Użytkownik otrzymuje listę zawierająca ponumerowane hasła. Ta sama lista zostaje zapisana w bazie systemu identyfikującego. W trakcie logowania użytkownik podaje swój identyfikator, a system prosi o podanie hasła z odpowiednim numerem. Klient za każdym razem posługuje się kolejnym niewykorzystanym hasłem z listy. 
[![Bsi-w-03-09.png](https://wazniak.mimuw.edu.pl/images/thumb/f/f9/Bsi-w-03-09.png/700px-Bsi-w-03-09.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-09.png>)
**Rysunek '**_8'_**. Uwierzytelnianie metodą listy haseł jednorazowych**
W metodzie z synchronizacją czasu (_time synchronization_) klient generuje **unikalny kod** w funkcji pewnego parametru **X** użytkownika (identyfikatora, kodu pin, hasła, numeru seryjnego karty identyfikacyjnej) oraz bieżącego **czasu**. Serwer następnie weryfikuje otrzymany od klienta kod korzystając z identycznej funkcji (z odpowiednią tolerancją czasu). 
[![Bsi-w-03-10.png](https://wazniak.mimuw.edu.pl/images/thumb/4/49/Bsi-w-03-10.png/700px-Bsi-w-03-10.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-10.png>)
**Rysunek '**_9'_**. Uwierzytelnianie metodą z synchronizacją czasu**
Natomiast w metodzie zawołanie-odzew (_challenge-response_) serwer pyta o nazwę użytkownika, a następnie przesyła unikalny ciąg („zawołanie"). Klient koduje otrzymany ciąg (np. swoim hasłem lub innym tajnym parametrem pełniącym rolę klucza) i odsyła jako „odzew". Serwer posługując się identycznym kluczem weryfikuje poprawność odzewu. 
[![Bsi-w-03-11.png](https://wazniak.mimuw.edu.pl/images/thumb/8/81/Bsi-w-03-11.png/700px-Bsi-w-03-11.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-11.png>)
**Rysunek '**_10'_**. Uwierzytelnianie metodą listy haseł jednorazowych**
Tokeny programowe to specjalne programy generujące hasła. W zależności od implementacji program na podstawie kwantu czasu lub zawołania serwera generuje hasło jednorazowe, które weryfikuje serwer. 
Token sprzętowy jest małym przenośnym urządzeniem spełniającym wszystkie funkcje tokenu programowego. 
Pewną ciekawostką zyskującą na popularności jest wykorzystanie telefonu komórkowego w uwierzytelnianiu za pomocą haseł jednorazowych. Cały proces polega przesłaniu hasła jednorazowego z serwera na telefon w postaci wiadomości SMS. W tym przypadku rola telefonu jako swoistego tokena sprowadza się tylko do medium odbierającego i wyświetlającego dane. 
#### Inne mechanizmy uwierzytelniania
Do uwierzytelniania użytkowników można wykorzystać również przedmioty, których posiadaniem musi się wykazać uwierzytelniany. Mogą to być np. karty magnetyczne, karty elektroniczne czy tokeny USB. Ponadto, w przypadku ludzi, można posłużyć się również cechami osobowymi wynikającymi z odmienności parametrów niektórych naturalnych składników organizmu (uwierzytelnianie biometryczne), takich jak m.in.: 
  * klucz DNA
  * małżowina uszna
  * geometria twarzy
  * termogram twarzy
  * termogram dłoni
  * obraz żył krwionośnych na zaciśniętej pięści
  * odcisk palca (dermatoglify)
  * chód
  * geometria dłoni
  * tęczówka oka
  * odcisk dłoni
  * obraz siatkówki
  * podpis odręczny
  * głos


### Autoryzacja i kontrola dostępu do zasobów
#### Mechanizmy ochrony dostępu do danych
Zadania autoryzacji i kontroli dostępu legalnych użytkowników należą do podstawowych funkcji systemów operacyjnych czy systemów zarządzania bazą danych oraz środowisk przetwarzania rozproszonego. W większości przypadków te funkcje są realizowane podobnie. 
Aktualnie jednym z najczęściej stosowanych mechanizmów weryfikacji praw dostępu jest lista kontroli dostępu, której implementacje, w zależności od konkretnego systemu, noszą nazwy ACL (Access Control List), ARL (Access Rights List) lub Trustees. Ogólna koncepcja działania mechanizmu listy kontroli polega na wyspecyfikowaniu dla każdego udostępnianego zasobu listy indywidualnych użytkowników lub ich grup bądź kategorii oraz przydzieleniu im podzbiorów uprawnień wybranych ze zbioru wszystkich uprawnień dostępnych dla danego zasobu (rysunek 11). 
[![Bsi-w-03-12.png](https://wazniak.mimuw.edu.pl/images/thumb/9/9f/Bsi-w-03-12.png/700px-Bsi-w-03-12.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-03-12.png>)
**Rysunek '**_11'_**. Lista kontroli dostępu do pliku**
W kolejnych modułach (<A HREF="bsk-m6.doc">moduł 6</A> i (<A HREF="bsk-m11.doc">moduł 11</A>) omówione zostaną przykłady realizacji autoryzacji i kontroli dostępu użytkowników wybranych systemów operacyjnych oraz systemów zarządzania bazą danych. 
### Utrudnianie podsłuchu
Atak poprzez podsłuch jest zwykle skierowany przeciwko określonym zasobom i ma konkretny cel (np. przechwycenie hasła, lub zawartości konkretnych plików). Atak taki w istocie polega na wykonaniu operacji umożliwiających dostęp do kanału transmisyjnego (wpięcie się do medium transmisyjnego, podłączenie do stacji bazowej sieci bezprzewodowej itp.) a następnie wyłuskaniu z całego ruchu odbywającego się w tym kanale informacji poszukiwanych. 
Ogólna koncepcja utrudniania podsłuchu polega zatem na uczynieniu możliwie jak najbardziej kłopotliwym obu kroków ataku - wpięcia się do kanału komunikacyjnego i wyłuskania użytecznych danych. Operacje utrudniania podsłuchu obejmują: 
  * stosowanie topologii sieciowej utrudniającej ewentualny posłuch lub ułatwiającej jego wykrycie, np. topologii gwiazdy (okablowanie strukturalne)
  * stosowanie medium mniej podatnego na podsłuch; przykładowo popularne przewodowe media transmisyjne można uszeregować wg łatwości i skuteczności ich ewentualnego podsłuchu: UTP -> FTP -> STP -> SSTP -> FO
  * utrudnianie wyłuskania użytecznych danych poprzez sztuczne generowanie ruchu (_traffic padding_) - wypełnianie wolnego pasma przenoszenia sieci danymi bezużytecznymi, co czyni trudniejszym, przynajmniej potencjalnie, rozróżnienie danych użytecznych od reszty (w wyniku zwiększenia proporcji danych bezużytecznych w całym ruchu)
  * tworzenie zamkniętych grup użytkowników, poprzez separację ruchu sieciowego kierowanego z i do odrębnych grup użytkowników systemu (wspierają to już dojrzałe technologie VLAN ACL, Wire-rate ACL i in.)
  * kontrola dostępu do zasobów infrastruktury sieciowej, poprzez dopuszczanie do udziału w ruchu sieciowym tylko uwierzytelnionych stacji sieciowych (co realizuje np. protokół IEEE 802.1x)
  * szyfrowanie danych - stanowiące niewątpliwie najbardziej uniwersalny mechanizm ochrony poufności danych (czy ja zobaczymy wkrótce - szerzej rozumianej ochrony danych)
  * ograniczanie emisji elektromagnetycznej - atak przez przechwycenie promieniowania van Ecka jest nadal tańszy od innego typu ataków na poufność danych (np. ataku kryptoanalitycznego), mimo że wymaga bardzo specjalistycznego sprzętu. Skutecznie można utrudnić ten atak poprzez wykorzystanie materiałów pochłaniających istotnie dużą część promieniowania elektromagnetycznego. Mamy do dyspozycji ekranujące materiały konstrukcyjne (obudowy komputerów i urządzeń peryferyjnych) oraz ekranujące materiały elastyczne do przygotowania pomieszczeń (tapety, wykładziny podłogowe i sufitowe). W niektórych zastosowaniach, jak np. przetwarzanie danych niejawnych, obowiązuje standard TEMPEST (_Transient Electromagnetic Pulse Emanation Standard_), który definiuje wymagania stanowiska komputerowego o ograniczonej emisji elektromagnetycznej. Stanowiska komputerowe zgodne z TEMPEST to wydatek rzędu kilkunastu, kilkudziesięciu tysięcy złotych.


### Nienaruszalność informacji (integralność)
Kolejnym po poufności aspektem bezpieczeństwa omawianym w tym module jest nienaruszalność informacji, rozumiana jako ochrona danych przed ich nieautoryzowanym zmodyfikowaniem (dostępem do zapisu, w odróżnieniu od poufności, która oznacza ochronę przed nieautoryzowanym dostępem do odczytu). 
#### Zagrożenia
Zagrożeniem nienaruszalności informacji jest zatem celowa lub przypadkowa modyfikacja danych przez nieuprawnionych użytkowników bądź oprogramowanie (np. wirusowe). 
#### Mechanizmy obrony
Mechanizmy obrony stosowane do zapewnienia nienaruszalności informacji obejmują w szczególności: 
  * kontrolę dostępu do danych - wymienione wcześniej mechanizmy list kontroli dostępu
  * sumy kontrolne zbiorów danych (np. plików dyskowych)
  * kryptograficzne sumy kontrolne i podpis elektroniczny
  * rejestrację operacji na danych (_auditing_) - niezbędną dla formalnego wykrycia naruszeń integralności; zwykle spotyka się podział danych audytu co najmniej na rejestr zdarzeń systemowych oraz rejestr zdarzeń aplikacji.
  * kontrolę antywirusową


### Dostępność informacji
#### Zagrożenia
Wśród zagrożeń nienaruszalności informacji należy wymienić przede wszystkim: 
Źródło: „[https://wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_3:Ogólne_własności_bezpieczeństwa_informacji&oldid=9499](https://wazniak.mimuw.edu.pl/<https:/wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_3:Ogólne_własności_bezpieczeństwa_informacji&oldid=9499>)”





---


# Podstawowe elementy kryptografii

# Bezpieczeństwo systemów komputerowych - wykład 4:Podstawowe elementy kryptografii
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Podstawowe elementy kryptografii](https://wazniak.mimuw.edu.pl/<#Podstawowe_elementy_kryptografii>)
    * [1.1 Podstawowe pojęcia](https://wazniak.mimuw.edu.pl/<#Podstawowe_pojęcia>)
    * [1.2 Proste szyfry](https://wazniak.mimuw.edu.pl/<#Proste_szyfry>)
      * [1.2.1 Szyfrowanie metodą podstawiania](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_metodą_podstawiania>)
      * [1.2.2 Szyfrowanie metodą przestawiania](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_metodą_przestawiania>)
    * [1.3 Zasada Kerckhoffsa](https://wazniak.mimuw.edu.pl/<#Zasada_Kerckhoffsa>)
    * [1.4 Szyfrowanie z kluczem](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_z_kluczem>)
    * [1.5 Szyfrowanie symetryczne](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_symetryczne>)
      * [1.5.1 tożsamość problemu poufności wiadomości z problemem tajności klucza](https://wazniak.mimuw.edu.pl/<#tożsamość_problemu_poufności_wiadomości_z_problemem_tajności_klucza>)
      * [1.5.2 problem dystrybucji klucza](https://wazniak.mimuw.edu.pl/<#problem_dystrybucji_klucza>)
      * [1.5.3 problem skalowalności](https://wazniak.mimuw.edu.pl/<#problem_skalowalności>)
      * [1.5.4 autentyczność](https://wazniak.mimuw.edu.pl/<#autentyczność>)
    * [1.6 Przykłady algorytmów symetrycznych](https://wazniak.mimuw.edu.pl/<#Przykłady_algorytmów_symetrycznych>)
      * [1.6.1 Algorytm DES (Data Encryption Standard)](https://wazniak.mimuw.edu.pl/<#Algorytm_DES_\(Data_Encryption_Standard\)>)
      * [1.6.2 Deszyfrowanie w algorytmie DES](https://wazniak.mimuw.edu.pl/<#Deszyfrowanie_w_algorytmie_DES>)
      * [1.6.3 Kryptoanaliza algorytmu DES](https://wazniak.mimuw.edu.pl/<#Kryptoanaliza_algorytmu_DES>)
      * [1.6.4 Tryby pracy algorytmu DES](https://wazniak.mimuw.edu.pl/<#Tryby_pracy_algorytmu_DES>)
      * [1.6.5 Algorytm CDMF (Commercial Data Masking Facility)](https://wazniak.mimuw.edu.pl/<#Algorytm_CDMF_\(Commercial_Data_Masking_Facility\)>)
      * [1.6.6 Odporność algorytmu DES](https://wazniak.mimuw.edu.pl/<#Odporność_algorytmu_DES>)
      * [1.6.7 Algorytm 3DES (Triple DES)](https://wazniak.mimuw.edu.pl/<#Algorytm_3DES_\(Triple_DES\)>)
      * [1.6.8 Algorytm IDEA (International Data Encryption Algorithm)](https://wazniak.mimuw.edu.pl/<#Algorytm_IDEA_\(International_Data_Encryption_Algorithm\)>)
      * [1.6.9 Algorytm Rijndeal](https://wazniak.mimuw.edu.pl/<#Algorytm_Rijndeal>)
      * [1.6.10 Standard AES (Advanced Encryption Standard)](https://wazniak.mimuw.edu.pl/<#Standard_AES_\(Advanced_Encryption_Standard\)>)
    * [1.7 Inne algorytmy symetryczne](https://wazniak.mimuw.edu.pl/<#Inne_algorytmy_symetryczne>)
      * [1.7.1 Algorytmy RC2 / RC4 / RC5 / RC6](https://wazniak.mimuw.edu.pl/<#Algorytmy_RC2_/_RC4_/_RC5_/_RC6>)
      * [1.7.2 Algorytmy z rodziny CAST](https://wazniak.mimuw.edu.pl/<#Algorytmy_z_rodziny_CAST>)
      * [1.7.3 Algorytm SAFER](https://wazniak.mimuw.edu.pl/<#Algorytm_SAFER>)
      * [1.7.4 Algorytm Blowfish](https://wazniak.mimuw.edu.pl/<#Algorytm_Blowfish>)
  * [2 Szyfrowanie asymetryczne](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_asymetryczne>)
    * [2.1 Przykłady algorytmów asymetrycznych](https://wazniak.mimuw.edu.pl/<#Przykłady_algorytmów_asymetrycznych>)
      * [2.1.1 Algorytm RSA (Rivest–Shamir–Adleman)](https://wazniak.mimuw.edu.pl/<#Algorytm_RSA_\(Rivest–Shamir–Adleman\)>)
      * [2.1.2 Algorytm ElGamala (ELG)](https://wazniak.mimuw.edu.pl/<#Algorytm_ElGamala_\(ELG\)>)
    * [2.2 Literatura](https://wazniak.mimuw.edu.pl/<#Literatura>)
    * [2.3 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)


## Podstawowe elementy kryptografii
Mechanizmy kryptografii są powszechnie wykorzystywane w dziedzinie bezpieczeństwa systemów komputerowych. Stanowią bardzo uniwersalne narzędzie osiągania poufności, integralności czy autentyczności, są stosowane w procedurach uwierzytelniania, do ochrony danych składowanych i komunikacji sieciowej. Należą niewątpliwie do najważniejszych mechanizmów bezpieczeństwa. 
Bieżący moduł przedstawia elementarne pojęcia dziedziny kryptografii i prezentuje podstawowe koncepcje algorytmów szyfracji. Celem dydaktycznym modułu jest wyrobienie intuicji działania popularnych technik kryptograficznych i ich własności. Kolejny moduł przedstawi podstawowe zastosowania mechanizmów kryptograficznych w informatyce. 
### Podstawowe pojęcia
Kryptografia jest dziedziną kryptologii - nauki operującej bardzo formalnym i relatywnie skomplikowanym aparatem matematycznym. Nie jest celem tego modułu przedstawienie tego aparatu, lecz jedynie przybliżenie istoty operacji szyfrowania i deszyfrowania. Wymaga to jednak minimalnej ilości jasno definiowanych terminów. Niniejszy rozdział przedstawia podstawowe pojęcia, które wykorzystywane będą w dalszej części modułu. 
**Kryptologia** jest to wiedza naukowa obejmująca kryptografię i kryptoanalizę. 
**Kryptografia** jest dziedziną obejmująca zagadnienia związane z _utajnieniem_ danych (w kontekście przesyłania wiadomości i zabezpieczenia dostępu do informacji) przed niepożądanym dostępem. Przez utajnienie należy tu rozumieć taką operację, która powoduje że wiadomość jest trudna do odczytania (rozszyfrowania) przez podmiot nie znający tzw. _klucza rozszyfrowującego_ - dla takiego podmiotu wiadomość będzie wyłącznie niezrozumiałym ciągiem wartości (znaków). 
**Kryptoanaliza** natomiast to dziedzina kryptologii zajmująca się _łamaniem_ szyfrów, czyli odczytywaniem zaszyfrowanych danych bez posiadania kluczy rozszyfrowujących. 
Dane, które poddawane będą operacjom ochrony kryptograficznej nazywać tu będziemy po prostu **tekstem jawnym** lub **wiadomością czytelną**. 
**Kryptogramem** (**szyfrogramem**) będziemy nazywali zaszyfrowaną postać wiadomości czytelnej. 
**Klucz szyfrowania** to ciąg danych służących do szyfrowania wiadomości czytelnej w kryptogram za pomocą _algorytmu szyfrowania_. Klucz ten jest odpowiednio ustalany (uzgadniany) przez nadawcę w fazie szyfrowania. 
**Klucz rozszyfrowujący** jest z kolei ciągiem danych służących do rozszyfrowania kryptogramu do postaci wiadomości czytelnej za pomocą algorytmu deszyfrowania. Naturalnie, klucz ten odpowiada w pewien sposób kluczowi szyfrowania wykorzystanemu w fazie szyfrowania. 
W niektórych przypadkach będziemy mieli do czynienia z ciekawą własnością przemienności kluczy. **Przemienność kluczy** oznacza, że role dwóch kluczy z pary mogą ulec przestawieniu. Mianowicie informację zaszyfrowaną jednym kluczem można rozszyfrować tylko przy pomocy odpowiadającego mu drugiego klucza z pary, i odwrotnie, informację zaszyfrowaną drugim kluczem można rozszyfrować wyłącznie przy pomocy klucza pierwszego. 
### Proste szyfry
Teraz przejdziemy do zademonstrowania prostych operacji kryptograficznych, które wykorzystywane są również w bardzo skomplikowanych procesach szyfrowania i deszyfrowania. Świadomość ich funkcjonowania jest niezbędna dla zrozumienia istoty aktualnie wykorzystywanych algorytmów szyfrowania. 
#### Szyfrowanie metodą podstawiania
Szyfrowanie metodą podstawiania jest prawdopodobnie najprostszą koncepcją utajniania informacji. Było już stosowane w czasach antycznych. Przykładem a przykład może u posłużyć szyfr wykorzystywany przez Juliusza Cezara do utajniania korespondencji wojskowej, nazywany na jego cześć szyfrem Cezara (notabene jest to jedno z pierwszych nazwisk związanych z kryptografią). 
Działanie tej metody szyfrowania polega na wykonaniu na każdym znaku wiadomości czytelnej przekształcenia szyfrującego polegającego na zastąpieniu tego znaku innym o pozycji w alfabecie przesuniętej o zadaną ilość znaków względem znaku szyfrowanego. Przy czym pozostajemy wyłącznie w dziedzinie alfabetu wejściowego (przesunięcie pozycji jest w istocie rotacją - „zapętla się" po osiągnięciu końcowego znaku alfabetu na jego początek). Operację taką nazywa się z tego powodu monogramem. 
Operację szyfrującą na znaku _x_ możemy zatem zapisać formalnie jako  f ( x ) = x + Δ {\displaystyle f(x)=x+\Delta } ![{\\displaystyle f\(x\)=x+\\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/c906a61e5a305bda6812ad36f785be613df45804), gdzie dodawanie oznacza zmianę (rotację!) pozycji znaku w alfabecie, a symbol  Δ {\displaystyle \Delta } ![{\\displaystyle \\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/32769037c408874e1890f77554c65f39c523ebe2) oznacza wartość przesunięcia przy podstawianiu. Należy zaobserwować, iż w istocie zatem wartość  Δ {\displaystyle \Delta } ![{\\displaystyle \\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/32769037c408874e1890f77554c65f39c523ebe2) jest kluczem szyfrowania. Jest to również klucz deszyfrowania, gdzie deszyfrowanie polega na „odejmowaniu" pozycji znaku o wartość  Δ {\displaystyle \Delta } ![{\\displaystyle \\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/32769037c408874e1890f77554c65f39c523ebe2). Dla szyfru Cezara wartość  Δ {\displaystyle \Delta } ![{\\displaystyle \\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/32769037c408874e1890f77554c65f39c523ebe2) jest stała i wynosi 3. Natomiast dla kodu nazywanego Captain Midnight  Δ {\displaystyle \Delta } ![{\\displaystyle \\Delta }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/32769037c408874e1890f77554c65f39c523ebe2) jest kluczem zmiennym. 
```
 szyfr Cezara:	**Parser nie mógł rozpoznać (błąd składni): {\displaystyle "A" \Rightarrow ( "A" + 3 ) = "D"}**
 kod Captain Midnight:	**Parser nie mógł rozpoznać (błąd składni): {\displaystyle "A" \Rightarrow ( "A" + \Delta); 	\Delta = 1,\ldots,26}**

```

**Rysunek '**_1'_**. Przykłady monogramów**
Szyfry monoalfabetyczne mogą być konstruowane i opisywane różnymi wzorami matematycznymi. W powyższym przykładzie funkcję podstawienie zapisywaliśmy  f ( x ) {\displaystyle f(x)} ![{\\displaystyle f\(x\)}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/202945cce41ecebb6f643f31d119c514bec7a074). W kryptologii częściej stosuje się zapis  E [ x | k ] {\displaystyle E[x|k]} ![{\\displaystyle E\[x|k\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/5210e590024b563b7a0d9d481e67691faa1f5c94), gdzie  E [ ] {\displaystyle E[]} ![{\\displaystyle E\[\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/c8a9d82c5433051fda256f05b0af0b22398f706c) jest operacją szyfrowania (ang. _encryption_), a _k_ oznacza użyty klucz. W niniejszym module będziemy stosowali najczęściej uproszczony zapis postaci  E k [ x ] {\displaystyle E_{k}[x]} ![{\\displaystyle E_{k}\[x\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/321faf16d35642ec110f2cedae8a5b526bfbe22a)
Oto przykłady formalnych definicji przekształceń monoalfabetycznych: 
  * f ( x ) = x + k {\displaystyle f(x)=x+k} ![{\\displaystyle f\(x\)=x+k}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/38cee8659d1d5c45dd0c4002a936ef7f7f3643d7) E [ x | k ] = x + k {\displaystyle E[x|k]=x+k} ![{\\displaystyle E\[x|k\]=x+k}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/0b2f6851ea90b5b44424c057ca673f7fb92515e3) E k [ x ] = x + k {\displaystyle E_{k}[x]=x+k} ![{\\displaystyle E_{k}\[x\]=x+k}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/711a32f69180f6f805fb3b4da7a3185658964104)
  * f ( x ) = x ⋅ k mod n {\displaystyle f(x)=x\cdot k{\bmod {n}}} ![{\\displaystyle f\(x\)=x\\cdot k{\\bmod {n}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/d63385fab8c275172b16b63058b5755d461acad5) E [ x | k ] = x ⋅ k mod n {\displaystyle E[x|k]=x\cdot k{\bmod {n}}} ![{\\displaystyle E\[x|k\]=x\\cdot k{\\bmod {n}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e9b9733f5b08b4a56c36ac257980b843e0b8973a)
  * f ( x ) = ( x ⋅ a + b ) mod n {\displaystyle f(x)=(x\cdot a+b){\bmod {n}}} ![{\\displaystyle f\(x\)=\(x\\cdot a+b\){\\bmod {n}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bb337f25e82803dd0f56286f5dd0be6254fc87f1) E [ x | a , b ] = ( x ⋅ a + b ) mod n {\displaystyle E[x|a,b]=(x\cdot a+b){\bmod {n}}} ![{\\displaystyle E\[x|a,b\]=\(x\\cdot a+b\){\\bmod {n}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/ff2c5e62277b037de6d83649f8aea95ec3114f39)


#### Szyfrowanie metodą przestawiania
Inną podstawową operacją kryptograficzną jest przestawianie treści wiadomości czytelnej. Polega ono na przestawieniu kolejności wystąpienia znaków („wymieszaniu") testu jawnego. Kryptogram rozszyfrowujemy wykonując odwrotne przestawianie. 
Najprostszym przypadkiem szyfrowania metodą przestawiania jest przestawienie losowe. W jego przypadku kolejne znaki wiadomości czytelnej przyjmują przypadkowe pozycje w kryptogramie. Takie szyfrowanie ma sens dla relatywnie niedużych wiadomości (rysunek 2). 
[![Bsi-w-04-01.png](https://wazniak.mimuw.edu.pl/images/thumb/9/99/Bsi-w-04-01.png/200px-Bsi-w-04-01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-01.png>)
**Rysunek '**_2'_**. Przykład szyfrowania metodą przestawiania losowego**
W rzeczywistych przypadkach, przestawienie nie jest losowe, lecz wynika z określonego wzoru zadanego np. figurą geometryczną. Najprostszą przydatną figurą transpozycji jest prostokąt. Dokładniej mamy do czynienia z macierzą prostokątną, w której pozycje wpisujemy wiadomość czytelną (lub też kolejne bloki całej wiadomości, których długości odpowiadają ilości elementów macierzy - czyli inaczej - jej rozmiarowi). Wiadomość wpisywana jest do macierzy, przyjmijmy, wierszami. Kryptogram tworzy się spisując zawartość tak wypełnionej macierzy, ale kolumnami (rysunek 3). 
Rolę klucza szyfrowania pełnią wymiary figury transpozycji. W przykładzie z rysunku byłby to rozmiar macierzy: _k_ = (5,4). 
W celu utrudnienia złamania szyfru, operację transpozycji można powiązać w permutacją kolejności kolumn, przed spisaniem zawartości macierzy do krytpogramu. Innymi słowy, można przykładowo spisywać najpierw zawartość kolumny 2-giej, potem 5-tej, później 3-ciej, dopiero dalej 1-szej i na końcu 4-tej. Klucz szyfrowania przyjmuje tu postać: _k_ = (5,4;2-5-3-1-4). 
Dalsze wzmocnienie jakości szyfrowania można osiągnąć poprzez dodatkowe skomplikowanie operacji szyfrowania. Można stosować macierze o wierszach zmiennej długości bądź przestawienie przekątnokolumnowe, albo też szyfry siatkowe czy zastosować całkiem inną figurę transpozycji. 
[![Bsi-w-04-02.png](https://wazniak.mimuw.edu.pl/images/thumb/7/7f/Bsi-w-04-02.png/200px-Bsi-w-04-02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-02.png>)
**Rysunek '**_3'_**. Przykład szyfrowania metodą przestawiania losowego**
### Zasada Kerckhoffsa
Najprostsze z przedstawionych metod szyfrowania opierają swoją siłę na tajności procedury szyfrowania. Każdy, kto pozna tę procedurę, bez większego trudu i w relatywnie krótkim czasie jest w stanie odtworzyć wiadomość czytelną z dowolnego kryptogramu. 
Szyfry najczęściej spotykane współcześnie w systemach informatycznych opierają swą siłę nie na tajności samego algorytmu lecz jedynie na tajności zmiennego parametru tego algorytmu, jakim jest klucz. Jest to zgodne z powszechnie uznaną regułą, nazywaną zasadą Kerckhoffsa: 
```
 **Algorytm szyfrowania i deszyfrowania jest jawny**

```

**Rysunek '**_4'_**. Zasada Kerckhoffsa**
Zgodnie z tą zasadą, algorytm może być, a nawet z wielu względów powinien być publicznie znany. Przemawia za tym ułatwienie publicznej oceny i dyskusji jakości, jakie potencjalnie oferuje powszechna dostępność każdego nowo-opracowanego algorytmu dla światowej rzeszy kryptoanalityków. Dzięki temu, łatwiej i wcześniej można wykryć ewentualne luki w koncepcji algorytmu bądź w samej jego konstrukcji. 
### Szyfrowanie z kluczem
Rysunek 5 przedstawia ogólny schemat szyfrowania z użyciem klucza, jaki stosować będziemy w niniejszym module. Użytkownicy uczestniczący w komunikacji, na tym schemacie - Alicja i Bolek, posługują się swoimi kluczami, odpowiednio - KA oraz KB, aby przesłać zaszyfrowaną wiadomość od Alicji do Bolka. Alicja poddaje szyfrowaniu wiadomość czytelną M z użyciem klucza szyfrowania KA operacją **Parser nie mógł rozpoznać (Błąd konwersji. Serwer („https://wazniak.mimuw.edu.pl/api/rest_”) zgłosił: „Cannot get mml. TeX parse error: Double subscripts: use braces to clarify”): {\displaystyle E_{K}_{A}[M]}** uzyskując szyfrogram **S**
Następnie szyfrogram **S** jest przesyłany do Bolka, który poddaje go operacji **Parser nie mógł rozpoznać (Błąd konwersji. Serwer („https://wazniak.mimuw.edu.pl/api/rest_”) zgłosił: „Cannot get mml. TeX parse error: Double subscripts: use braces to clarify”): {\displaystyle D_{K}_{B}[S]}** rozszyfrowania z kluczem KB. 
[![Bsi-w-04-03.png](https://wazniak.mimuw.edu.pl/images/thumb/9/97/Bsi-w-04-03.png/600px-Bsi-w-04-03.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-03.png>)
**Rysunek '**_5'_**. Schemat ogólny szyfrowania z kluczem**
Formalny zapis tych operacji przedstawia rysunek 6. Wynika z niego własność szyfrowania z kluczem: **Parser nie mógł rozpoznać (Błąd konwersji. Serwer („https://wazniak.mimuw.edu.pl/api/rest_”) zgłosił: „Cannot get mml. TeX parse error: Double subscripts: use braces to clarify”): {\displaystyle D_{K}_{B}[E_{K}_{A}[M]]=M}** . 
[![Bsi-w-04-04.png](https://wazniak.mimuw.edu.pl/images/thumb/d/d3/Bsi-w-04-04.png/600px-Bsi-w-04-04.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-04.png>)
**Rysunek '**_6'_**. Formalny zapis operacji szyfrowania z kluczem**
W przypadku szyfrowania z kluczem spotykane są dwa schematy: szyfrowanie symetryczne i asymetryczne. 
### Szyfrowanie symetryczne
Szyfrowanie symetryczne jest schematem, który posiada następujące cechy 
  * występuje wspólny dla obu uczestników komunikacji tajny klucz KA-B (dalej oznaczany po prostu K)
  * stąd zapis formalny operacji szyfrowania symetrycznego ma postać:  E K [ M ] = S → S → D K [ S ] = M {\displaystyle E_{K}[M]=S\rightarrow S\rightarrow D_{K}[S]=M} ![{\\displaystyle E_{K}\[M\]=S\\rightarrow S\\rightarrow D_{K}\[S\]=M}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/ba4301cc55f06d2622a7c6a380834c0279efbce3)


[![Bsi-w-04-05.png](https://wazniak.mimuw.edu.pl/images/thumb/c/ce/Bsi-w-04-05.png/600px-Bsi-w-04-05.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-05.png>)
**Rysunek '**_7'_**. Ogólny schemat szyfrowania symetrycznego**
Własność szyfrowania symetrycznego ma zatem postać:  D K [ E K [ M ] ] = M {\displaystyle D_{K}[E_{K}[M]]=M} ![{\\displaystyle D_{K}\[E_{K}\[M\]\]=M}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/4b0a7b02aad3ca2c84aba69c0865aba803d18713). 
Szyfrowanie symetryczne jest o tyle ciekawe, że wymaga posłużenia się tylko jednym kluczem, dla obu uczestników komunikacji i w obu jej kierunkach (choć można wyobrazić sobie wariant tego schematu z oddzielnym kluczem na każdy kierunek). Uczestników takiej komunikacji może oczywiście być więcej niż dwoje i wówczas cała grupa może posługiwać się wspólnym kluczem. Jednak my będziemy tu zakładali zachowanie poufności komunikacji w pojedynczym kanale komunikacyjnym łączącym tylko dwoje uczestników. W związku z tym, pojedynczy klucz przypisany jest wyłącznie do jednej pary użytkowników i musi on być utajniony wobec innych osób. 
Konieczność utrzymania tajności klucza w obrębie jednej pary użytkowników rodzi szereg praktycznych problemów: 
##### tożsamość problemu poufności wiadomości z problemem tajności klucza
  * wiadomość jest bezpieczna dopóki osoba trzecia nie pozna tajnego klucza **K**


##### problem dystrybucji klucza
  * jak uzgodnić wspólny klucz bez osób trzecich, będąc oddalonym o setki, a nawet tysiące kilometrów?


##### problem skalowalności
  * dla 2 komunikujących się w systemie osób wymagane jest przechowywanie przez każdą z nich 1 klucza; dla 3 osób - 3 kluczy (przez każdą osobę); 4 os. = 6 kluczy; 10 os. = 45 kluczy; 100 os. = 4950 kluczy; ...


##### autentyczność
  * tajność klucza nie zapewnia autentyczności - nie można wykazać formalnie która z dwóch stron jest rzeczywistym nadawcą wiadomości, skoro obie posługują się tym samym kluczem.


### Przykłady algorytmów symetrycznych
#### Algorytm DES (Data Encryption Standard)
Algorytm DES (_Data Encryption Standard_) został opracowany w latach '70. przez firmę IBM na zamówienie NSA (_National Security Agency_) - rządowej agencji USA, będącej odpowiednikiem Agencji Bezpieczeństwa Wewnętrznego. Zespołem odpowiedzialnym za opracowanie DES w IBM kierował Horst Feistel. Zmodyfikowany przez NSA, algorytm DES został przyjęty jako standard krajowy w 1976 przez NBS (_National Bureau of Standards_ , obecnie NIST = _National Institute of Standards and Technology_) i objęty ochroną patentową oraz ograniczeniami ekportowymi. Należy od razu podkreślić, iż ochrona patentowa tego algorytmu już wygasła. W 1977 DES został opublikowany przez nieporozumienie między NSA a NBS (NSA spodziewało się, że standardem stanie się sam układ sprzętowy, lecz NBS opublikowało na tyle dużo szczegółów, iż możliwe stały się implementacje programowe tego algorytmu). 
Algorytm DES pracuje na 64-bitowych blokach tekstu jawnego, co odpowiada 8 znakom 8-bitowego kodu ASCII. Klucz składa się z 64 bitów, przy czym 8 z nich jest bitami parzystości. Zatem w istocie, w trakcie wyboru klucza można określić jedynie 56 bitów. 
Aktualnie standard DES nie jest już uważany za dostatecznie silny mechanizm kryptograficzny dla większości zastosowań, jednak wciąż jest bardzo często demonstrowany jako bardzo reprezentatywny przykład algorytmu symetrycznego szyfrowania. Dalej przedstawiony zostanie uproszczony szkic działania algorytmu DES, którego celem jest umożliwienie nabrania pewnej intuicji co do sposobu konstrukcji i pracy współczesnych algorytmów kryptograficznych. 
Algorytm działa w kilku wyraźnie zaznaczających się etapach nazywanych tu fazami. Fazy działania, znane dość powszechnie jako sieć Feistela, są następujące 
  * wstępna permutacja wejściowego bloku danych (na podstawie tabeli transpozycji)
  * podział bloku na lewą i prawą połowę o długości 32 bitów każda
  * 16 jednakowych rund - cykli operacji podstawiania i przestawiania wykorzystujących pewną funkcję _f_ , w czasie których dane zostają połączone z kluczem
  * połączenie lewej i prawej połowy bloku
  * permutacja końcowa (odwrotność permutacji wstępnej)


Schematycznie sieć Feistela przedstawia rysunek 8. 
[![Bsi-w-04-07.png](https://wazniak.mimuw.edu.pl/images/thumb/9/94/Bsi-w-04-07.png/600px-Bsi-w-04-07.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-07.png>)
'_Rysunek '_**8'**_. Sieć '_**Feistela**
Najbardziej skomplikowaną fazą jest każdy z 16 rund wykorzystujących funkcję _f_. Rundy te są w istocie iteracjami tych samych operacji. Każda kolejna runda, dokonuje tych samych obliczeń, ale na wynikach obliczeń z poprzedniej rundy i specjalnym podkluczu _K_ _i_ generowanym z 56b klucza _K_ 0 (64-bitowego klucza powstałego po usunięciu 8 bitów parzystości z wejściowego klucza szyfrowania). 
Początek każdej iteracji składa się z następujących kroków: 
  * 56 bitów klucza dzielone jest na dwie połowy po 28 bitów
  * w każdej iteracji bity obu połówek są cyklicznie przesuwane w lewo o jeden lub dwa bity, w zależności od numeru iteracji
  * ostatecznie wykonywana jest permutacja kompresująca, dzięki której z 56b klucza, otrzymujemy 48b podklucz _K_ _i_ używany w funkcji _f_(_L_ _i_ , _K_ _i_)
  * a połówki klucza podawane jest do następnej iteracji _i+_ 1


Kulminacyjnym etapem wykonania kolejnej rundy jest funkcja _f_. Jej działanie jest następujące: 
  * prawa połowa _R_ _i-_ 1 rozszerzana jest z 32 bitów do 48 bitów za pomocą permutacji rozszerzonej (e-blok) i sumowana mod 2 z 48 bitami podklucza _K_ _i_ danego cyklu
  * otrzymany wynik poddawany jest operacji podstawienia poprzez wykorzystanie bloków podstawień (S-bloki): 
    * ciąg 48 bitów dzielony jest na 8 bloków po 6 bitów
    * każdy ciąg 6 bitów jest redukowany do 4 bitów funkcją podstawienia
    * z 48 bitów otrzymujemy 32b ciąg, który poddawany jest permutacji zwykłej
    * następnie sumowany mod 2 z lewą połową _L_ _i-1_ bloku wejściowego


No koniec iteracji następuje zamiana lewej i prawej połowy bloku miejscami. 
Bloki podstawień (S-bloki; z ang. _Substitution blocks_) są zdefiniowane w standardzie DES i można je znaleźć w literaturze przedmiotowej. Każdy z 8 S-bloków jest inny, jednak w ogólności S-blok należy postrzegać jako tabelę 4 wiersze na 16 kolumn. Element tabeli jest 4b liczbą (podstawiana wartość). Wybór wiersza i kolumny za pomocą 6b wejścia wygląda następująco: 
  * pierwszy i ostatni bit 6b ciągu tworzy 2b liczbę
  * liczba ta wybiera wiersz
  * pozostałe środkowe 4 bity wybierają kolumnę


Wskazany element tabeli (4 bity) jest podawany na wyjście jako wynik podstawienia. 
#### Deszyfrowanie w algorytmie DES
Operacje deszyfrowania kryptogramu uzyskanego algorytmem DES są realizowane za pomocą tej samej sieci co operacje szyfrowania bloku tekstu jawnego. Różnica polega jedynie na tym, iż klucze stosowane są w kolejności odwrotnej od _K_ 16 do _K_ 1. 
#### Kryptoanaliza algorytmu DES
Istotą trudności kryptoanalizy algorytmu DES metodą przeszukiwania wyczerpującego jest złożoność obliczeniowa procesu dopasowania kolejnych możliwych wartości klucza. W latach 80-tych ubiegłego wieku wymagała ona czasu liczonego w setki/tysiące lat. W efekcie uczyniła ten standard odpornym na atak metodą przeszukiwania wyczerpującego. 
#### Tryby pracy algorytmu DES
Standard przewiduje wykorzystanie algorytmu DES w różnych trybach pracy nazywanych ECB, CBC, CFB i OFB. Dwa pierwsze to tryby blokowe, w których algorytm DES jest wykonywany wprost dokładnie tak jak na przedstawionym wcześniej szkicu, operując na kolejnych 8-znakowych blokach szyfrowanej wiadomości czytelnej. 
Tryb ECB (_Electronic CodeBook_)jest to podstawowy tryb szyfrowania blokowego. Jego własności można przedstawić następująco: 
  * cały tekst jawny jest dzielony na bloki 64b (ostatni blok, jeśli nie jest 8 znakowy, zostaje uzupełniony do 8 znaków nieistotnym wypełnieniem - ang. _padding_)
  * każdy 64b blok jest szyfrowany niezależnie
  * dla danego bloku i danego klucza wynik szyfrowania będzie zawsze ten sam
  * jeśli blok wystąpi w wiadomości częściej niż raz - za każdym razem otrzyma taki sam blok szyfrogramu ECB
  * przy pewnym standardowym formacie wiadomości (np. rozpoczynających się od tych samych stałych pól) stanowi ten tryb istotne ułatwienie dla kryptoanalityka.


Tryb CBC (_Cipher Block Chaining_) jest wolny od tej ostatniej wady. Umożliwia on uzależnienie postaci bloku kryptogramu nie tylko od treści szyfrowanego bloku wiadomości jawnej, lecz również od pewnego dodatkowego parametru - wektora inicjującego. Jego własności można przedstawić następująco: 
  * na pierwszym 64b bloku jest wykonywana operacja XOR z pewnym wektorem początkowym (IV = _Initialization Vector_) znanym nadawcy i odbiorcy  S 1 = E K [ M 1 ⊕ I V ] {\displaystyle S_{1}=E_{K}[M_{1}\oplus \;IV]} ![{\\displaystyle S_{1}=E_{K}\[M_{1}\\oplus \\;IV\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/b566e97eaa53bd99ac51d75525ea661b4dbfb24b)
  * wynikowy ciąg jest podawany na wejście algorytmu DES
  * na każdym kolejnym 64b bloku jest wykonywany XOR z zaszyfrowanym poprzednim blokiem przed podaniem na wejście algorytmu DES  S i = E K [ M i ⊕ S i − 1 ] {\displaystyle S_{i}=E_{K}[M_{i}\oplus S_{i-1}]} ![{\\displaystyle S_{i}=E_{K}\[M_{i}\\oplus S_{i-1}\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/ea4908f5a6c2f7d677d6b904ad81402668d8b1c3)
  * powtórzone takie same bloki 64b dadzą bloki zaszyfrowane różnej postaci
  * deszyfrowanie:  M i = D K [ S i ] ⊕ S i − 1 {\displaystyle M_{i}=D_{K}[S_{i}]\oplus S_{i-1}} ![{\\displaystyle M_{i}=D_{K}\[S_{i}\]\\oplus S_{i-1}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/f2b6222cb3e50c625dc617a097236cc342e21874)


Tryby blokowe nadają się doskonale do szyfrowania gotowych wiadomości, jednak nie są odpowiednia dla szyfrowania strumienia danych asynchronicznych, np. wprowadzanych z klawiatury lub pojawiających się w protokołach komunikacyjnych, w których nie można z góry określić tempa pojawiania się danych do przesłania (i zaszyfrowania) oraz ich ilości, w efekcie dających teksty zmiennej długości. W tym celu wprowadzono tryby szyfrowania strumieniowego szyfrujące każdorazowo po jednym znaku 8-bitowym: CFB (_Cipher FeedBack_) oraz OFB (_Output FeedBack_) - tzw. tryby sprzężenia zwrotnego. Opisują je następujące własności: 
  * w **CFB** na wejście funkcji szyfrującej podawana jest zawartość 64b rejestru przesuwnego - początkowo zawiera on IV, który jest szyfrowany:  R 1 = E K [ I V ] {\displaystyle R_{1}=E_{K}[IV]} ![{\\displaystyle R_{1}=E_{K}\[IV\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e12ac910be3c54d9ccfbb9e3138b8fbb606fa546)
  * na ośmiu najstarszych bitach rejestru jest wykonywany XOR ze znakiem szyfrowanym  M i : S i = R i ⊕ M i {\displaystyle M_{i}:S_{i}=R_{i}\oplus M_{i}} ![{\\displaystyle M_{i}:S_{i}=R_{i}\\oplus M_{i}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/628ed4fa501bee3fbd37785d25825fc5095c5bd8)
  * zawartość rejestru jest przesuwana w lewo 8b, a jako 8 najmłodszych jest wpisywany szyfrogram  S i {\displaystyle S_{i}} ![{\\displaystyle S_{i}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/de6e810a93f67802ecb603ee0e3324005c6e583e) wprowadzonego znaku ( R i + 1 {\displaystyle R_{i+1}} ![{\\displaystyle R_{i+1}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/fa91c65a2c9bf6bb806fa0c9f7dd2548a1301846))
  * wadą tego podejścia jest fakt iż uszkodzenie 1 bitu (np. w transmisji) propaguje się na 9 kolejnych znaków szyfrogramu
  * w **OFB** w miejsce 8 najmłodszych bitów wpisywany jest tylko szyfrogram 8 najstarszych (bez XOR z porcją tekstu szyfrowanego)
  * w trybie OFB błędy się nie propagują - uszkodzenie 1 bitu wpłynie tylko na rozszyfrowanie 1 znaku (zawierającego ten bit) - kryptoanalityk kontrolujący szyfrowany strumień może kontrolować zmiany w tekście jawnym


Powyższa dyskusja oraz znajomość praktycznych implementacji standardu DES skłania do następujących wniosków: 
  * ECB jest trywialny - nie powinien być stosowany do szyfrowania sesji danych; może być wykorzystany do przesłania kluczy oraz IV
  * w trybie CBC mogą z kolei występować problemy implementacyjne związane z IV 
    * celem IV jest upodobnienie bloków szyfrogramu do postaci losowych danych
    * typowe IV wartości nijak nie przypominają losowych (często zawierają powtarzające się najstarsze bity lub mają inną łatwą do przewidzenia strukturę)
    * nawet jeśli IV byłby prawdziwie losowy, to trzeba go przekazać odbiorcy (skoro jest losowy)
    * np. wysyłając w pierwszym bloku szyfrogramu (wydłuża to szyfrogram stanowiąc problem z małymi porcjami szyfrowanych danych)


#### Algorytm CDMF (Commercial Data Masking Facility)
Stany Zjednoczone, ojczyzna standardu DES, jak zresztą również inne kraje, traktują technologie kryptograficzne na równi z militarnymi i stosują ograniczenia w ich wykorzystaniu. Jednym z nich jest embargo eksportowe na wszelkie algorytmy i systemy kryptograficzne opracowane w USA. Również standard DES był objęty tymi ograniczeniami, a dokładniej jego ustandaryzowana postać posługująca się kluczem 56-bitowym. Natomiast algorytm CDMF, opracowany również przez IBM, został przygotowany specjalnie z myślą o wykorzystaniu również poza Stanami Zjednoczonymi i jest wolny od ograniczeń eksportowych. W istocie jest to wersja uproszczona DES operująca kluczem 40b, a dokładniej jest to algorytm DES uzupełniony o wstępną metodę skracania klucza 56b do 40b. 
#### Odporność algorytmu DES
Algorytm DES był przez wiele lat bezpieczny. Ze względu na złożoność obliczeniową kryptoanalizy, przy dostępnej mocy obliczeniowej, proces odnajdywania klucza metodą przeszukiwania wyczerpującego był wystarczająco nieefektywny, by uczynić ataki nieopłacalnymi. Jednak w 1998 r. algorytm DES z kluczem 56b został złamany w 56 godzin kryptoanalizy metodą przeszukiwania wyczerpującego. Koszt sprzętu (EFF DES Cracker) wówczas szacowano na 250 tys. USD. Rok później zajęło to już 22 godziny. Dziś to kwestia minut. 
#### Algorytm 3DES (Triple DES)
Istnieją jednak propozycje wzmocnienia siły algorytmu DES, np. poprzez praktyczne zwiększanie długości klucza. I tak algorytm 3DES stosuje jednocześnie trzy kolejne iteracje szyfrowania i deszyfrowania tekstu jawnego oryginalnym algorytmem DES. Każda iteracja może używać innego klucza 56b, co w efekcie daje klucz 168b. W praktyce najczęściej spotykany jest tryb DES-EDE (_encrypt-decrypt-encrypt_) z dwoma kluczami (razem 112b), wg rysunku 9: 
[![Bsi-w-04-08.png](https://wazniak.mimuw.edu.pl/images/thumb/9/93/Bsi-w-04-08.png/600px-Bsi-w-04-08.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-08.png>)
**Rysunek '**_9'_**. Schemat działania algorytmu 3DES**
#### Algorytm IDEA (International Data Encryption Algorithm)
Algorytm IDEA został opracowany w 1991r. przez Swiss Federal Institute of Technology (w zespole, którym kierowali James L. Massey i Xuejia Lai). W ogólnej koncepcji jest dość podobny do algorytmu DES, występują jedynie różnice w szczegółach. Przykładowo algorytm IDEA charakteryzują: 
  * 64b bloki danych (jak DES)
  * klucz 128b
  * 64b blok dzielony na 16b podbloki
  * a 128b klucz na 16b podklucze
  * 8 iteracji (w DES jest 16, ale w IDEA 1 iteracja odpowiada 2 w DES)


Fazy działania algorytmu IDEA przedstawiają się następująco: 
  * w każdym kroku cztery 16b podbloki danych poddawane są operacji dodawania modulo 2, dodawania modulo 216 i mnożenia modulo 216 z innymi blokami i z sześcioma 16b podkluczami.
  * pomiędzy każdym krokiem następuje zamiana drugiego i trzeciego podbloku.


Algorytm IDEA stosuje podklucze o następującej charakterystyce: 
  * 128-bitowy klucz jest dzielony na osiem 16-bitowych podkluczy
  * pierwszych 6 podkluczy jest używanych w pierwszej iteracji, 2 pozostałe podklucze - w kolejnej
  * następnie cały 128b klucz rotuje o 25 pozycji w lewo
  * tak otrzymany klucz jest ponownie dzielony na osiem 16b podkluczy, z których pierwsze 4 uzupełniają podklucze w drugiej iteracji, a kolejne 4 są przydzielane do trzeciej iteracji
  * w kluczu jest powtarzana rotacja o 25 pozycji w lewo - klucz jest ponownie dzielony na 8 podkluczy używanych w kolejnych krokach.


Opisane wyżej czynności powtarzane są do momentu przydzielenia kluczy do wszystkich kroków, przy czym w fazie zakończenia zamiast sześciu podkluczy, stosuje się tylko cztery podklucze. Łącznie w algorytmie wykorzystuje się 52 podklucze, które generowane są z wejściowego klucza szyfrującego. 
[![Bsi-w-04-09.png](https://wazniak.mimuw.edu.pl/images/thumb/7/77/Bsi-w-04-09.png/600px-Bsi-w-04-09.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-09.png>)
**Rysunek '**_10'_**. Siatka operacji w pojedynczej iteracji algorytmu IDEA**
Deszyfracja przebiega następująco: 
  * podklucze używane do deszyfrowania odpowiadają podkluczom szyfrowania podanym w odwrotnej kolejności,
  * operacje arytmetyczne przy użyciu czterech podkluczy są wykonywane nie na początku, ale na końcu deszyfrowania.


#### Algorytm Rijndeal
Algorytm Rijndeal został opracowany w 1999 przez Belgów: Joana Daemena i Vincenta Rijmena. Bloki wejściowe mają po 128, 196 lub 256 bitów. Klucze również mają długość 128b, 196b lub 256b. W zależności od wielkości bloku stosowana jest różna liczba iteracji: 10 (128b), 12 (196b) lub 14 (256b). Każda iteracja to następująca sekwencja wykonywana na poszczególnych bajtach danych i klucza: 
  1. podstawienie (S-bloki)
  2. przesuwanie (rzędów i kolumn bloku-macierzy)
  3. XOR.


[![Bsi-w-04-10.png](https://wazniak.mimuw.edu.pl/images/thumb/4/40/Bsi-w-04-10.png/600px-Bsi-w-04-10.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-10.png>)
'_Rysunek '_**11'**_. Uproszczony schemat pojedynczej iteracji algorytmu '_**Rijndeal**
#### Standard AES (Advanced Encryption Standard)
Standard AES jest następcą standardu DES obowiązującym w USA od 2001 r. Wykorzystuje algorytm Rijndeal. Algorytm ten wygrał oficjalną rywalizację z innymi zgłoszonymi do konkursu algorytmami, m.in. Serpent, Twofish, RC6, MARS. Stosuje tryb blokowy (blok 128b) i strumieniowy, klucze 128b, 192b, 256b (choć teoretycznie dopuszczalne również inne kombinacje). W standardzie wprowadzono też ciekawy nowy strumieniowy tryb licznikowy (CTR - _Counter Mode_), w którym dedykowany rejestr jest inkrementowany wraz z kolejnymi operacjami szyfrowania porcji danych. Tryb ten oferuje możliwość zrównoleglenia operacji na różnych porcjach danych. 
### Inne algorytmy symetryczne
#### Algorytmy RC2 / RC4 / RC5 / RC6
RC2, RC4, RC5 i RC6 to prawnie zastrzeżone algorytmy opracowane przez Ronalda Rivesta (pracownika MIT i jednocześnie założyciela firmy RSA Data Security), chociaż od 1994 kod źródłowy niektórych z nich jest szeroko dostępny w Internecie. Są to bardzo wydajne algorytmy symetryczne (ok. 10 razy szybsze od DES) o zmiennej długości klucza (do 2048b). RC2, RC5, RC6 to szyfry blokowe, natomiast RC4 jest szyfrem strumieniowym. Co ciekawe, niemal od samego początku swego istnienia posiadały specjalny status eksportowy USA dla kluczy 40b lub 56b (dla instytucji powiązanych z interesami USA). Dziś są powszechnie wykorzystywane w Lotus Notes, Apple OCE (_Open Collaboration Enviromnent_), Oracle, protokołach SSL i S-HTTP, sieciach bezprzewodowych i komórkowych. 
#### Algorytmy z rodziny CAST
Określenie CAST opisuje schemat zastosowany w rodzinie zbliżonych do DES algorytmów kryptograficznych o zmiennej długości kluczy i bloków. Najpowszechniej znany reprezentant to szyfr CAST-128 opublikowany w 1997 [RFC 2144]. 
#### Algorytm SAFER
To algorytm blokowy opracowany przez kolejną ważną postać kryptografii komputerowej - Jamesa L. Masseya. Popularne są: wersja z kluczem 64b (SAFER-K64) obejmująca 6 rund oraz wersja z kluczem 128b (SAFER-K128) - do 12 rund (rekomendowane 10). 
#### Algorytm Blowfish
Algorytm Blowfish, bardzo popularny zwłaszcza w produktach _open source_ , został opracowany w 1994 r. przez Bruce'a Schneiera. Blok danych ma 64 bity, a klucz podstawowy długość do 448b. W algorytmie występuje 16 iteracji wykorzystujących 18 kluczy pomocniczych (wyznaczanych każdorazowo przed szyfrowaniem i deszyfrowaniem) i 4 S-bloki 256-elementowe o wartościach zależnych od: klucza podstawowego, danych oraz liczby  π {\displaystyle \pi } ![{\\displaystyle \\pi }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/9be4ba0bb8df3af72e90a0535fabcc17431e540a). Deszyfrowanie jest operacją identyczną z szyfrowaniem - jedynie odwrotna zostaje kolejność kluczy pomocniczych. 
[![Bsi-w-04-11.png](https://wazniak.mimuw.edu.pl/images/f/f5/Bsi-w-04-11.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-11.png>)
## Szyfrowanie asymetryczne
Istotą szyfrowania asymetrycznego jest wyodrębnienie dwóch kluczy o odmiennych rolach: klucz prywatny i klucz publiczny. I tak przyjmiemy dalej iż odbiorca Bolek posiada parę kluczy: prywatny klucz kb oraz publiczny klucz KB. Z założenia klucz prywatny jest tajny znany wyłącznie właścicielowi. Publiczny klucz, natomiast, może być powszechnie znany. Aby przekazać zaszyfrowaną postać wiadomości do tego odbiorcy należy zaszyfrować wiadomość czytelną jego kluczem publicznym. Odszyfrowanie jest możliwe tylko przy użyciu klucza prywatnego, odpowiadającego użytemu uprzednio kluczowi publicznemu. 
Operacje szyfrowania opisuje zatem ogólny wzór: 
**Parser nie mógł rozpoznać (Błąd konwersji. Serwer („https://wazniak.mimuw.edu.pl/api/rest_”) zgłosił: „Cannot get mml. TeX parse error: Double subscripts: use braces to clarify”): {\displaystyle E_{K}_{B}[M]=S}**
a deszyfrację: 
**Parser nie mógł rozpoznać (Błąd konwersji. Serwer („https://wazniak.mimuw.edu.pl/api/rest_”) zgłosił: „Cannot get mml. TeX parse error: Double subscripts: use braces to clarify”): {\displaystyle D_{k}_{b}[S]=M}**
[![Bsi-w-04-12.png](https://wazniak.mimuw.edu.pl/images/thumb/a/a0/Bsi-w-04-12.png/600px-Bsi-w-04-12.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-12.png>)
**Rysunek '**_12'_**. Ogólny schemat szyfrowania asymetrycznego**
Istotne jest iż znajomość klucza publicznego KB nie wystarcza do naruszenia poufności szyfrogramu uzyskanego przy zastosowaniu tego klucza. 
Szyfrowanie asymetryczne idealnie nadaje się do zastosowania w następujących celach: 
  * zapewnienie poufności (rys. 13)


[![Bsi-w-04-13.png](https://wazniak.mimuw.edu.pl/images/thumb/8/8a/Bsi-w-04-13.png/600px-Bsi-w-04-13.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-13.png>)
**Rysunek '**_13'_**. Ogólny schemat zapewnienia poufności w szyfrowaniu asymetrycznym**
  * zapewnienie autentyczności (rys. 14)


[![Bsi-w-04-14.png](https://wazniak.mimuw.edu.pl/images/thumb/b/ba/Bsi-w-04-14.png/600px-Bsi-w-04-14.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-14.png>)
**Rysunek '**_14'_**. Ogólny schemat zapewnienia autentyczności w szyfrowaniu asymetrycznym**
### Przykłady algorytmów asymetrycznych
#### Algorytm RSA (Rivest–Shamir–Adleman)
Algorytm RSA został opublikowany w 1978 roku przez Ronalda Rivesta, Adi Shamira i Leonarda Adlemana. Niedawno wygasła jego ochrona patentowa. Algorytm ten pozwala w zasadzie dowolnie ustalić długość klucza. Wymaga użycia 2 dużych liczbpierwszych (przez duże rozumiemy tu liczby co najmniej stucyfrowe w systemie dziesiętnym). Do szyfrowania i deszyfrowania wykorzystuje operacje potęgowania dyskretnego. W efekcie wymaga dużej liczby działań arytmetycznych (jest zdecydowanie wolniejszy od DES - nawet do 1000 razy). 
Dobór kluczy jest najbardziej istotnym elementem pracy algorytmu. Schematycznie przedstawia ją rysunek 15. 
[![Bsi-w-04-15.png](https://wazniak.mimuw.edu.pl/images/thumb/a/a3/Bsi-w-04-15.png/600px-Bsi-w-04-15.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-04-15.png>)
**Rysunek '**_15'_**. Ogólny schemat pracy algorytmu RSA**
Schemat ten wymaga następujących wyjaśnień: 
  * liczba względnie pierwsza z (p-1) i (q-1) to inaczej Wykładnik Uniwersalny: dzieli się tylko przez 1, siebie oraz (p-1) i (q-1), czyli Najmniejsza Wspólna Wielokrotność, albo inaczej: Największy Wspólny Dzielnik (e, (p-1)(q-1)) = 1
  * odwrotność e można łatwo wyznaczyć rozszerzonym algorytmem Euklidesa.


Złamanie tak ustalonego klucza wymagałoby znalezienia efektywnej metody faktoryzacji dużych liczb - póki co takowa nie istnieje. 
#### Algorytm ElGamala (ELG)
Algorytm ten został opublikowany w 1985 roku, ale nie jest chroniony patentem. Brak również w jego przypadku ograniczeń eksportowych USA - wykorzystuje koncepcję (i patent) Diffiego-Helmana lecz ów patent wygasł w 1997 r. Szyfrowanie wymaga każdorazowo losowo wybranej wartość _k_ , dlatego też ten sam tekst jawny każdorazowo daje inny szyfrogram. Niestety wadą tego algorytmu jest fakt, iż szyfrogram jest dwukrotnie dłuższy od tekstu jawnego. 
Generowanie kluczy przebiega następująco: 
  * wybieramy losowo liczbę pierwszą _p_
  * wykorzystujemy multiplikatywną grupę modulo _p_ -  Z p ∗ {\displaystyle \mathbb {Z} _{p}^{*}} ![{\\displaystyle \\mathbb {Z} _{p}^{*}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bd11eda4e342a4a898bcaedf142264a67a722046)
  * gdzie _p_ jest liczbą pierwszą, a  Z p {\displaystyle \mathbb {Z} _{p}} ![{\\displaystyle \\mathbb {Z} _{p}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/dbc1df7227ef11fe88dccd2dae3adc7bbdeae5f4) jego ciałem skończonym ( G F ( p ) l u b Z / p Z {\displaystyle GF(p)lub\mathbb {Z} /p\mathbb {Z} } ![{\\displaystyle GF\(p\)lub\\mathbb {Z} /p\\mathbb {Z} }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/c4c614b6d59b2fb270d01276423695bc7dd67ff1))
  * wybieramy liczbę _g_ , która jest elementem pierwotnym (generatorem) grupy  Z p ∗ {\displaystyle \mathbb {Z} _{p}^{*}} ![{\\displaystyle \\mathbb {Z} _{p}^{*}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bd11eda4e342a4a898bcaedf142264a67a722046)
  * generator - generuje ciąg  1 , g , g 2 , g 3 , . . {\displaystyle 1,g,g^{2},g^{3},..} ![{\\displaystyle 1,g,g^{2},g^{3},..}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/814350800d5589b1227672883b531b0a492ab09d).
  * z którego tylko skończenie wiele należy do  Z p ∗ {\displaystyle \mathbb {Z} _{p}^{*}} ![{\\displaystyle \\mathbb {Z} _{p}^{*}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bd11eda4e342a4a898bcaedf142264a67a722046) (potem zaczną się powtarzać modulo _p_)
  * w ogólności mamy _q_ elementów:  1 , g , g 2 , . . . , g q − 1 ( g q mod p = 1 ) {\displaystyle 1,g,g^{2},...,g^{q-1}(g^{q}{\bmod {p}}=1)} ![{\\displaystyle 1,g,g^{2},...,g^{q-1}\(g^{q}{\\bmod {p}}=1\)}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/405d25816bbb66fd298b9483bb8882ff8c85d44a)
  * istnieje przynajmniej jedno _g_ generujące całą grupę! (tzn.  q = p − 1 {\displaystyle q=p-1} ![{\\displaystyle q=p-1}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/72f3e459926ed4bce21bba512ab06d73df86c5e1))
  * czyli zamiast 1, ..., _p_ -1 możemy grupę traktować jako  1 , g , g 2 , . . . , g p − 2 {\displaystyle 1,g,g^{2},...,g^{p-2}} ![{\\displaystyle 1,g,g^{2},...,g^{p-2}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/0bd1c4a7d27f21851bc65c576ef53bf0a53cb497)


W dalszej kolejności: 
  * wybieramy losowo liczbę  x < p {\displaystyle x<p} ![{\\displaystyle x<p}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/aa1bd94804b46ebc27c1bf2470175ea5d431098f)
  * obliczamy  y = q x mod p {\displaystyle y=q^{x}{\bmod {p}}} ![{\\displaystyle y=q^{x}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/80bbeb6fe2ffc59559d3cc997018f7cb926c8974)
  * klucz publiczny stanowią _y_ , _g_ i _p_ - zarówno _g_ , jak i _p_ mogą być wspólnie wykorzystywane przez grupę użytkowników (_mod_ _p_)
  * kluczem prywatnym jest _x_


Szyfrowanie przebiega następująco: 
  * wybieramy losowo liczbę _k_ względnie pierwszą z _p_
  * obliczamy  a = g k mod p {\displaystyle a=g^{k}{\bmod {p}}} ![{\\displaystyle a=g^{k}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e32d926c673ce653fe4c535adf240c8b90322529)
  * obliczamy  b = y k ⋅ M mod p {\displaystyle b=y^{k}\cdot M{\bmod {p}}} ![{\\displaystyle b=y^{k}\\cdot M{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bb7a4dc2139adb1d118e0663661b57ee45148871)
  * szyfrogram to para (_a,b_)


Deszyfrowanie przebiega następująco: 
  * M = b / a x mod p {\displaystyle M=b/a^{x}{\bmod {p}}} ![{\\displaystyle M=b/a^{x}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/82cf2ffc5e8313dc2403f4a62210f9b9a3b414fa)
  * ponieważ  a x ≡ g k x mod p {\displaystyle a^{x}\equiv g^{kx}{\bmod {p}}} ![{\\displaystyle a^{x}\\equiv g^{kx}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/7e843d79e9e54e9b73f7b985a21da3dabe546260)
  * b / a x ≡ y k ⋅ M / a x ≡ g x k ⋅ M / g k x ≡ M mod p {\displaystyle b/a^{x}\equiv y^{k}\cdot M/a^{x}\equiv g^{xk}\cdot M/g^{kx}\equiv M{\bmod {p}}} ![{\\displaystyle b/a^{x}\\equiv y^{k}\\cdot M/a^{x}\\equiv g^{xk}\\cdot M/g^{kx}\\equiv M{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/d5cc3e2a47bcb94d7a1d29e5125c4ff45ab2fb62)


### Literatura
```
[1] Janusz Stokłosa, Tomasz Bilski, Tadeusz Pankowski, "Bezpieczeństwo danych w systemach informatycznych", PWN, 2001

```

### Zadania
  1. Na czym polega kodowanie ROT-13 powszechnie wykorzystywane w Internecie?
  2. Na czym polega i do czego służy kodowanie MIME?
  3. Jaki będzie szyfrogram dla przykładu z rysunku 3, w przypadku użycia klucza _k_ = (5,4;2-5-3-1-4)?
  4. Wektor inicjujący IV powinien być każdorazowo unikalny, ale nie musi być tajny. Dlaczego?
  5. Dlaczego wersja 40b algorytmu DES była od początku wolna od ograniczeń eksportowych?


Źródło: „[https://wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_4:Podstawowe_elementy_kryptografii&oldid=82778](https://wazniak.mimuw.edu.pl/<https:/wazniak.mimuw.edu.pl/index.php?title=Bezpieczeństwo_systemów_komputerowych_-_wykład_4:Podstawowe_elementy_kryptografii&oldid=82778>)”
[Kategorie](https://wazniak.mimuw.edu.pl/</index.php?title=Specjalna:Kategorie> "Specjalna:Kategorie"): 
  * [Strony z błędami rozszerzenia math](https://wazniak.mimuw.edu.pl/</index.php?title=Kategoria:Strony_z_b%C5%82%C4%99dami_rozszerzenia_math&action=edit&redlink=1> "Kategoria:Strony z błędami rozszerzenia math \(strona nie istnieje\)")
  * [Strony z błędami renderowania wyrażeń matematycznych](https://wazniak.mimuw.edu.pl/</index.php?title=Kategoria:Strony_z_b%C5%82%C4%99dami_renderowania_wyra%C5%BCe%C5%84_matematycznych&action=edit&redlink=1> "Kategoria:Strony z błędami renderowania wyrażeń matematycznych \(strona nie istnieje\)")


---


# Wykorzystanie kryptografii

# Bezpieczeństwo systemów komputerowych - wykład 5:Wykorzystanie kryptografii
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wykorzystanie kryptografii](https://wazniak.mimuw.edu.pl/<#Wykorzystanie_kryptografii>)
    * [1.1 Potwierdzanie autentyczności danych](https://wazniak.mimuw.edu.pl/<#Potwierdzanie_autentyczności_danych>)
      * [1.1.1 Metoda 1:](https://wazniak.mimuw.edu.pl/<#Metoda_1:>)
      * [1.1.2 Metoda 2:](https://wazniak.mimuw.edu.pl/<#Metoda_2:>)
    * [1.2 Podpis cyfrowy](https://wazniak.mimuw.edu.pl/<#Podpis_cyfrowy>)
    * [1.3 Osiąganie poufności, autentyczności i nienaruszalności danych](https://wazniak.mimuw.edu.pl/<#Osiąganie_poufności,_autentyczności_i_nienaruszalności_danych>)
    * [1.4 Algorytmy skrótu](https://wazniak.mimuw.edu.pl/<#Algorytmy_skrótu>)
      * [1.4.1 Algorytm MD5](https://wazniak.mimuw.edu.pl/<#Algorytm_MD5>)
      * [1.4.2 Algorytm SHA (Secure Hash Algorithm)](https://wazniak.mimuw.edu.pl/<#Algorytm_SHA_\(Secure_Hash_Algorithm\)>)
      * [1.4.3 Algorytmy SHA-256 / SHA-384 / SHA-512](https://wazniak.mimuw.edu.pl/<#Algorytmy_SHA-256_/_SHA-384_/_SHA-512>)
      * [1.4.4 Algorytm RIPE-MD](https://wazniak.mimuw.edu.pl/<#Algorytm_RIPE-MD>)
      * [1.4.5 Algorytm HAVAL](https://wazniak.mimuw.edu.pl/<#Algorytm_HAVAL>)
      * [1.4.6 Algorytm ElGamal](https://wazniak.mimuw.edu.pl/<#Algorytm_ElGamal>)
    * [1.5 Standardy podpisu cyfrowego](https://wazniak.mimuw.edu.pl/<#Standardy_podpisu_cyfrowego>)
      * [1.5.1 Standard DSS (Digital Signature Standard)](https://wazniak.mimuw.edu.pl/<#Standard_DSS_\(Digital_Signature_Standard\)>)
      * [1.5.2 Standard SHS (Secure Hash Standard)](https://wazniak.mimuw.edu.pl/<#Standard_SHS_\(Secure_Hash_Standard\)>)
    * [1.6 Ataki na funkcje skrótu](https://wazniak.mimuw.edu.pl/<#Ataki_na_funkcje_skrótu>)
      * [1.6.1 Atak urodzinowy](https://wazniak.mimuw.edu.pl/<#Atak_urodzinowy>)
        * [1.6.1.1 Obserwacja 1:](https://wazniak.mimuw.edu.pl/<#Obserwacja_1:>)
        * [1.6.1.2 Obserwacja 2:](https://wazniak.mimuw.edu.pl/<#Obserwacja_2:>)
    * [1.7 Zarządzanie kluczami](https://wazniak.mimuw.edu.pl/<#Zarządzanie_kluczami>)
      * [1.7.1 problem przekazania klucza](https://wazniak.mimuw.edu.pl/<#problem_przekazania_klucza>)
      * [1.7.2 problem zmiany klucza](https://wazniak.mimuw.edu.pl/<#problem_zmiany_klucza>)
      * [1.7.3 problem doboru systemu szyfrowania](https://wazniak.mimuw.edu.pl/<#problem_doboru_systemu_szyfrowania>)
      * [1.7.4 Metoda Diffiego-Hellmana (DH)](https://wazniak.mimuw.edu.pl/<#Metoda_Diffiego-Hellmana_\(DH\)>)
    * [1.8 Dystrybucja kluczy publicznych](https://wazniak.mimuw.edu.pl/<#Dystrybucja_kluczy_publicznych>)
      * [1.8.1 Certyfikacja](https://wazniak.mimuw.edu.pl/<#Certyfikacja>)
        * [1.8.1.1 Certyfikaty zwykłe (tzw. powszechne)](https://wazniak.mimuw.edu.pl/<#Certyfikaty_zwykłe_\(tzw._powszechne\)>)
        * [1.8.1.2 Certyfikaty kwalifikowane:](https://wazniak.mimuw.edu.pl/<#Certyfikaty_kwalifikowane:>)
    * [1.9 Kryptograficzne zabezpieczenie danych](https://wazniak.mimuw.edu.pl/<#Kryptograficzne_zabezpieczenie_danych>)
    * [1.10 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)


## Wykorzystanie kryptografii
Bieżący moduł przedstawia koncepcje związane z wykorzystaniem mechanizmów kryptograficznych w systemach informatycznych. 
### Potwierdzanie autentyczności danych
Szyfrowanie asymetryczne, jak już wiemy z poprzedniego modułu, można wykorzystać do osiągnięcia własności autentyczności danych. Zastosować można potencjalnie 2 metody przedstawione poniżej. 
#### Metoda 1:
  * szyfrujemy całą wiadomość kluczem prywatnym nadawcy
  * kosztowne obliczeniowo - koszt rośnie z wielkością wiadomości


#### Metoda 2:
  * tworzymy skrót wiadomości o ustalonym z góry rozmiarze _n_
  * szyfrujemy kluczem prywatnym nadawcy tylko skrót
  * koszt mały - _n_ małe
  * koszt stały - nie rośnie z wielkością wiadomości i zależy tylko od _n_


Druga metoda wykorzystuje pojęcie skrótu, który jest wynikiem zastosowania pewnej funkcji matematycznej na treści wiadomości. Funkcja skrótu to jednokierunkowa funkcja  h [ M ] {\displaystyle h[M]} ![{\\displaystyle h\[M\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/8c29025aab86cbaf2afa676bf5ca45b3fbeb8622), a więc taka, która daje jednoznaczny wynik  d = h [ M ] {\displaystyle d=h[M]} ![{\\displaystyle d=h\[M\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/1832886ff7426af18cbaefd79fe2faca26bd24d2) (skrót, ang._message digest, fingerprint_) o stałym rozmiarze, przy wieloznacznym argumencie (M). Jej zadaniem w naszym przypadku jest dostarczyć odbiorcy narzędzia do zweryfikowania czy treść wiadomości nie została zmodyfikowana, przez osoby niepowołane. 
W istocie, w dziedzinie transmisji danych skróty wiadomości, lub ich odpowiedniki, powszechnie wykorzystywane są w celu potwierdzania integralności wiadomości od lat 70-tych ubiegłego wieku, choć zwykle ukrywają się pod różnymi nazwami: 
  * suma kontrolna (_checksum_) - negatywne potwierdzenia, retransmisje
  * funkcja kontrolna (_data integrity check_)
  * funkcja kontrolna wiadomości (_message integrity check_)
  * funkcja ściągająca (_contraction function_)
  * kod uwierzytelniający informacji (_data authentication code_)


Własności jakie musi posiadać odpowiednia dla nas funkcja skrótu to: 
  * kompresja: oznaczająca, że rozmiar skrótu musi być mniejszy od rozmiaru samej wiadomości  | d | < | M | {\displaystyle |d|<|M|} ![{\\displaystyle |d|<|M|}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/27ae0f39db6883491d86b6409d54692134a0e5a3)
  * łatwość obliczeń: czas wielomianowy wyznaczenia  h [ M ] {\displaystyle h[M]} ![{\\displaystyle h\[M\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/8c29025aab86cbaf2afa676bf5ca45b3fbeb8622) dla dowolnego  M {\displaystyle M} ![{\\displaystyle M}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/f82cade9898ced02fdd08712e5f0c0151758a0dd)
  * odporność na **podmianę** argumentu: dla danego  h [ M ] {\displaystyle h[M]} ![{\\displaystyle h\[M\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/8c29025aab86cbaf2afa676bf5ca45b3fbeb8622) obliczeniowo trudne znalezienie  M ′ {\displaystyle M^{\prime }} ![{\\displaystyle M^{\\prime }}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/fafb6c3d2d5712548534471d74417250c376ee5f) takiego, że  h [ M ] = h [ M ′ ] {\displaystyle h[M]=h[M^{\prime }]} ![{\\displaystyle h\[M\]=h\[M^{\\prime }\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/1f1c42e49137f7770c4c341e80da4ac5f5074e7d)
  * odporności na **kolizje** : obliczeniowo trudne znalezienie dwóch dowolnych argumentów  M ≠ M ′ {\displaystyle M\neq M^{\prime }} ![{\\displaystyle M\\neq M^{\\prime }}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/8c45f7a130ce5430c1ae82652b303ada73873d37) takiego, że  h [ M ] = h [ M ′ ] {\displaystyle h[M]=h[M^{\prime }]} ![{\\displaystyle h\[M\]=h\[M^{\\prime }\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/1f1c42e49137f7770c4c341e80da4ac5f5074e7d)


Zastosowania funkcji skrótu mogą obejmować: 
  * zapewnienie integralności wiadomości bez klucza kryptograficznego
  * zapewnienie integralności oraz autentyczności wiadomości: **MAC** - _message authentication code_(z kluczem kryptograficznym)


[![Bsi-w-05-01.png](https://wazniak.mimuw.edu.pl/images/thumb/e/ef/Bsi-w-05-01.png/600px-Bsi-w-05-01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-01.png>)
**Rysunek '**_1'_**. Zastosowanie funkcji skrótu**
### Podpis cyfrowy
Funkcje skrótu można wykorzystać do zrealizowania ciekawego i niezwykle ważnego narzędzia, jakim jest podpis cyfrowy. Najczęściej wykorzystywana jest w tym celu jest funkcja mieszająca HMACz kluczem _k_ asymetrycznym (_keying hash function_) -  h k [ M ] {\displaystyle h_{k}[M]} ![{\\displaystyle h_{k}\[M\]}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e3d3b7530d14a6a5a1b7dbeaf8bfd3c141775026). Wartość skrótu HMAC jest zaszyfrowana kluczem prywatnym nadawcy, być może dodatkowo z wykorzystaniem ziarna (_salt_) lub zawołania (_challenge_). 
Proces generowania i weryfikowania podpisu HMAC z kluczem przedstawia rysunek 2. Nadawca (Alicja) po przygotowaniu wiadomości M przygotowuje jej skrót H, który poddaje szyfrowaniu swoim kluczem prywatnym, który z założenia zna i posiada tylko nadawca. Po połączeniu M z zaszyfrowanym skrótem H' całość przekazuje do odbiorcy dowolnym kanałem komunikacyjnym. Tan następuje deszyfracja H' (przy użyciu otwarcie dostępnego klucza publicznego nadawcy) oraz niezależne wyliczenie skrótu H dla otrzymanego M. Porównanie H wyliczonego z odszyfrowanym wskazuje na autentyczność i nienaruszalność wiadomości M lub jej brak. Gdyby M została zmodyfikowana w trakcie transmisji do odbiorcy, wyliczony skrót nie pasowałby do odszyfrowanego z H'. Natomiast, gdyby nadawcą nie była Alicja, posłużenie się jej kluczem publicznym przy odszyfrowaniu H' nie dałoby skrótu identycznego z wyliczony przez odbiorcę H. 
[![Bsi-w-05-02.png](https://wazniak.mimuw.edu.pl/images/thumb/3/38/Bsi-w-05-02.png/600px-Bsi-w-05-02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-02.png>)
**Rysunek '**_2'_**. Zastosowanie funkcji skrótu**
### Osiąganie poufności, autentyczności i nienaruszalności danych
Możliwe jest jednoczesne osiągnięcie własności poufności, autentyczności i nienaruszalności wiadomości. Uzyskuje się to poprzez znane już szyfrowanie (np. asymetryczne) pary M + H' z poprzedniego przykładu, przed przesłaniem do odbiorcy. Przy tym szyfrowaniu musi oczywiście być wykorzystany odpowiedni klucz publiczny odbiorcy. Schemat ten przedstawia rysunek 3. 
[![Bsi-w-05-03.png](https://wazniak.mimuw.edu.pl/images/thumb/8/80/Bsi-w-05-03.png/600px-Bsi-w-05-03.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-03.png>)
**Rysunek '**_3'_**. Osiąganie poufności, autentyczności i nienaruszalności**
### Algorytmy skrótu
Pierwsze z powszechnie stosowanych algorytmów generowania skrótu na potrzeby ochrony autentyczności i nienaruszalności informacji - MD i MD2 (autorstwa Rona Rivesta) powstały w latach '80. Algorytm MD nie został nigdy oficjalnie opublikowany. Był wykorzystywany jako autorskie rozwiązanie w systemie pocztowym RSADSI. Natomiast MD2 został ustandaryzowany w dokumencie RFC 1319. W 1990 Ralph Merkle (Xerox) zaproponował algorytm HMAC o nazwie SNEFRU - kilkukrotnie szybszy od MD2. Na to Rivest odpowiedział algorytmem MD4 (RFC 1320). WWwww W roku 1992 złamano SNEFRU i wykryto pewną słabość MD4 w wersji 2-rund i wkrótce Rivest wzmocnił algorytm otrzymując trochę wolniejszy MD5 (RFC1321). 
#### Algorytm MD5
Algorytm MD5 posiada następujące cechy charakterystyczne: 
  * wykorzystuje 128b wektor IV
  * wykonuje 64 iteracje (4 rundy po 16 kroków)
  * daje skrót 128b
  * teoretyczna odporność na kolizje 264 jest współcześnie uznawana za zbyt słabą


#### Algorytm SHA (Secure Hash Algorithm)
Algorytm SHA został opracowany przez NSA (_National Security Agency_) i przyjęty przez NIST jako standard federalny w 1993r. Wersja oryginalna SHA (SHA-0) jest zbliżona do MD4. Algorytm ten posiada następujące cechy charakterystyczne: 
  * przekształca wiadomość o długości do 264b w skrót 160b
  * wykorzystuje 160b wektor IV
  * wykonuje 80 iteracji (4 rundy po 20 kroków)


Stosunkowo szybko wykryto słabości SHA-0 (choć ich natury nigdy nie opublikowano) i opracowano SHA-1 (ratyfikowany przez NIST), który jest często spotykany do dziś. Wykazuje odporność na kolizje 160b skrótu - 280 , która jest współcześnie uznawana również za zbyt słabą. 
#### Algorytmy SHA-256 / SHA-384 / SHA-512
Niedawno zaproponowano zupełnie nowe funkcje skrótu: SHA-256, SHA-384 oraz SHA-512, przystosowane do współpracy z kluczami AES (odpowiednio 128b, 192b i 256b). Dają skróty odpowiednio 256b, 384b i 512b. Nie doczekały się jeszcze szerszej analizy jednak dość powszechnie uznawane są za bezpieczne. Mają większą złożoność obliczeniową od poprzedników wymienionych wyżej. W praktyce okazuje się, iż algorytm SHA-384 ma identyczny koszt obliczeniowy co SHA-512, co czyni SHA-384 w praktyce bezużytecznym. Powszechnie spotykane są zatem jedynie SHA-256 oraz SHA-512. 
#### Algorytm RIPE-MD
Algorytm ten powstał w ramach europejskiego (EU) projektu RACE Integrity Primitives Evaluation - Message Digest. W uproszczeniu mówiąc jest to ulepszony wariant MD4 (zmodyfikowane rotacje i kolejność słów wiadomości) Oferuje skrót 128b. Wykorzystuje rejestr strumieniowy. Podczas generowania skrótu wykonuje równoległe 2 przebiegi (za każdym razem z innym zadanym parametrem) w każdej iteracji. Po każdej iteracji oba wyniki łączone z rejestrem strumieniowym. Prawdopodobnie posiada dużą odporność na ataki. 
#### Algorytm HAVAL
Algorytm HAVAL generuje skrót o zmiennej długości: 128b, 160b, 192b, 224b lub 256b. Można i jego uznać za wariant MD4, względem oryginału zmodyfikowano operacje rotacji. Stosuje wyrafinowane funkcje nieliniowe (o własności lawinowości), w każdej iteracji wykonuje inne permutacje. I posiada prawdopodobnie duża odporność na ataki. 
#### Algorytm ElGamal
Ostatnim z wymienionych algorytmów jest ElGamal. Algorytm ten początkowo opracowano właśnie dla realizacji podpisu cyfrowego HMAC. Podpisem wiadomości M jest para (_a_ , _b_), taka że: 
a = g k mod p {\displaystyle a=g^{k}{\bmod {p}}} ![{\\displaystyle a=g^{k}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e32d926c673ce653fe4c535adf240c8b90322529) b :: M = ( x a + k b ) mod p − 1 {\displaystyle b::M=(xa+kb){\bmod {p}}-1} ![{\\displaystyle b::M=\(xa+kb\){\\bmod {p}}-1}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/fae67e1798fb4e35b0a5fa8e5223249a4e6a2de7)
Weryfikacja podpisu cyfrowego następuje pomyślnie jeśli  ( y a a b ) mod p == g M mod p {\displaystyle (y^{a}a^{b}){\bmod {p}}==g^{M}{\bmod {p}}} ![{\\displaystyle \(y^{a}a^{b}\){\\bmod {p}}==g^{M}{\\bmod {p}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/988e1390744d78809334036f7999ce6a5082377b). 
### Standardy podpisu cyfrowego
W systemach informatycznych powszechnie spotykane są standardy podpisu cyfrowego opracowane w USA. Należą do nich starszy DSS i nowszy SHS 
#### Standard DSS (Digital Signature Standard)
DSS jest to standard NIST z kategorii FIST (_Federal Information processing STandard_) w wersjach z 1991 i 1993 roku. Obejmuje użycie skrótu SHA-1 oraz algorytmu DSA (_Digital Signature Algorithm_). 
#### Standard SHS (Secure Hash Standard)
Standard SHS to nowszy projekt NIST z 2001. Obejmuje użycie rodziny SHA-256 / SHA-384 / SHA-512. 
### Ataki na funkcje skrótu
Najpowszechniej znanym atakiem na funkcje skrótu jest atak urodzinowy. Poniżej przedstawiona zostanie koncepcja tego ataku. 
#### Atak urodzinowy
Paradoks dnia urodzin po lega na dokonaniu następujących obserwacji: 
##### Obserwacja 1:
  * pytanie: ile osób potrzeba na tej sali, aby z prawdopodobieństwem 50% znalazła się wśród nich taka, która obchodzi urodziny tego samego dnia co autor tych slajdów? (funkcja mieszająca odwzorowuje zbiór ludzi na 365 lub 366 dni roku)
  * odpowiedź: oczywiście 183.


##### Obserwacja 2:
  * pytanie: a ile potrzeba osób, aby wśród nich znalazły się 2 obchodzące urodziny tego samego dnia?
  * odpowiedź: tylko 23.


Uogólnienie tego paradoksu przebiega następująco. Mamy dany rozmiar _n_ danych wejściowych (ludzi - w przykładzie urodzin) oraz rozmiar _k_ zbioru wynikowego (daty urodzin). Dla _n_ mamy możliwych _n_(_n-_ 1)/2 par danych wejściowych i dla każdej pary oba elementy dadzą ten sam wynik z prawdopodobieństwem 1/_k_. Zatem, potrzeba _k_ /2 par aby z prawdopodobieństwem 50% wśród nich była taka jak szukamy - gdzie oba elementy mają tę samą wartość wyniku (datę urodzin). W efekcie jeśli  n > k {\displaystyle n>{\sqrt {k}}} ![{\\displaystyle n>{\\sqrt {k}}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/59bb5f9220f2634a13da0b01cc09971b45e46729) to szanse powodzenia są duże. Dla skrótu 128b potrzeba 2128 wiadomości aby znaleźć tę, która dała określony skrót, ale wystarczy 264 wiadomości aby znaleźć 2 o identycznym skrócie (znaleźć tzw. kolizję). 
Jako komentarz można podać, iż w połowie 2004 r. zespół kryptoanalityków pod kierunkiem Xuejia Lai wykazał zaskakujące kolizje w MD5 podając 2 ciągi po 128 B różniące się zaledwie 6-cioma bajtami. Natomiast na początku 2005 r. zespół kierowany przez Xiaoyuna Wanga wykazał w rodzinie SHA kolizje łatwiejsze niż należy oczekiwać z teoretycznej odporności. Mianowicie w przypadku SHA-1: kolizje dla 269 operacji (przy teoretycznej 280), dla SHA-1 w uproszczonej wersji (58-rund): kolizje dla 233 operacji i dla SHA-0: kolizje dla 239 operacji. 
### Zarządzanie kluczami
W procesie pozyskiwania i wykorzystania kluczy kryptograficznych występują pewne istotne problemy. Należą do nich poniższe: 
##### problem przekazania klucza
  * jak partnerowi komunikacji przekazać w sposób bezpieczny klucz niezbędny do szyfrowania / deszyfrowania?


##### problem zmiany klucza
  * jak go regularnie zmieniać?


##### problem doboru systemu szyfrowania
  * czy wybrać tajny klucz symetryczny? - występuje w tym przypadku, jak pamiętamy, problem skalowalności: 10 osób = 45 kluczy, 100 osób = 4950 kluczy
  * czy raczej wybrać publiczny klucz asymetryczny? - tu występuje problem autentyczności skąd pewność jego prawdziwości


Nie istnieje uniwersalne rozwiązanie wszystkich wymienionych problemów, jednak poniżej przedstawiona metoda zaproponowana przez Whitfielda Diffiego i Martina Hellmana jest częściowym rozwiązaniem problemu przekazania klucza. Jest to metoda ciekawa i powszechnie spotykana, dlatego warta bliższego poznania. 
#### Metoda Diffiego-Hellmana (DH)
Metoda Diffiego-Hellmana pozwala partnerom uzgodnić tajny klucz bez ryzyka ujawnienia go podsłuchującym. Początkowo ustalamy wspólny jednorazowy symetryczny**klucz sesji** (dla każdej sesji inny). Na potrzeby ustalenia klucza sesji wykorzystamy model asymetryczny. 
DH wykorzystuje multiplikatywną grupę modulo _p_ - oznaczaną  Z p ∗ {\displaystyle \mathbb {Z} _{p}^{*}} ![{\\displaystyle \\mathbb {Z} _{p}^{*}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bd11eda4e342a4a898bcaedf142264a67a722046). 
Przez  α {\displaystyle \alpha \ } ![{\\displaystyle \\alpha \\ }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/2e744c9d831e4b3c66ca542ff74bcda7e6caa3c7) oznaczmy element pierwotny grupy  Z p ∗ {\displaystyle \mathbb {Z} _{p}^{*}} ![{\\displaystyle \\mathbb {Z} _{p}^{*}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/bd11eda4e342a4a898bcaedf142264a67a722046). Zatem  α {\displaystyle \alpha \ } ![{\\displaystyle \\alpha \\ }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/2e744c9d831e4b3c66ca542ff74bcda7e6caa3c7) generujące całą grupę. 
Czyli zamiast 1, ..., _p_ -1 możemy grupę traktować jako 1,  α α 2 , . . . , α p − 2 {\displaystyle \alpha \,\alpha ^{2},...,\alpha ^{p-2}} ![{\\displaystyle \\alpha \\,\\alpha ^{2},...,\\alpha ^{p-2}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/698b4957de51f96396e6fb48d58bb7602bd598f3). 
Schemat postępowania w metodzie DH przedstawia rysunek 4. 
Każdy z użytkowników wybiera sobie w nieistotny sposób wartość klucza prywatnego k. Natomiast klucz publiczny K dobiera jako  α k {\displaystyle \alpha ^{k}} ![{\\displaystyle \\alpha ^{k}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/cbe2221400f734971e3aa0cd94f6703241e9fee1). Klucz ten jest swobodnie i otwarcie przykazywany drugiej stronie komunikacji. 
Klucz sesji dobierany jest przez każdą ze stron w taki sposób, że obie uzyskują identyczną wartość  Φ {\displaystyle \Phi \ } ![{\\displaystyle \\Phi \\ }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/a925b493413fdf9a3b499ada79ec3edadd236186), przy czym przechwycenie obu transmitowanych kluczy publicznych nie wystarcza do jego uzyskania. 
[![Bsi-w-05-04.png](https://wazniak.mimuw.edu.pl/images/thumb/c/c4/Bsi-w-05-04.png/600px-Bsi-w-05-04.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-04.png>)
**Rysunek '**_4'_**. Schemat postępowania w metodzie DH**
Metoda D-H nie jest, jak już zaznaczono, idealnym rozwiązaniem. Jest m.in. podatna n atak _man-in-the-middle_. Przyjmijmy, iż Edziu, znając  α {\displaystyle \alpha \ } ![{\\displaystyle \\alpha \\ }](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/2e744c9d831e4b3c66ca542ff74bcda7e6caa3c7), może skutecznie wkroczyć na etapie negocjacji klucza. Alicja i Bolek będą porozumiewać się poprzez Edzia za pomocą kluczy, które - jak im się będzie wydawać - wymienili ze sobą. 
### Dystrybucja kluczy publicznych
Rozważmy możliwe sposoby pozyskiwania kluczy publicznych szyfrowania asymetrycznego. Istnieją następujące warianty: 
  1. pobranie klucza bezpośrednio od właściciela
  2. pobranie klucza z centralnej bazy danych
  3. pobranie z własnej prywatnej bazy danych zapamiętanego wcześniej klucza pozyskanego sposobem 1 lub 2


Należy zwrócić uwagę, iż w ogólności istnieje ryzyko podstawienia przez nieuczciwą osobę (atakującego) własnego klucza pod klucz domniemanego użytkownika. 
Rozwiązaniem tego problemu, które zyskało dotychczas największą akceptację jest certyfikacja kluczy publicznych. 
#### Certyfikacja
Certyfikację stosuje się w celu uniknięcia podstawienia fałszywego klucza publicznego. Certyfikat jest poświadczeniem autentyczności podpisanym przez osobę (instytucję) godną zaufania, nazywaną urzędem poświadczającym CA(_Certification Authority_). certyfikat ma najczęściej formę dokumentu elektronicznego. Certyfikat zawiera podstawowe dane identyfikujące właściciela. W ogólnym przypadku, urząd poświadczający CA potwierdza, iż informacja opisująca właściciela klucza jest prawdziwa, a klucz publiczny faktycznie do niego należy. Certyfikat posiada też okres ważności wyznaczający czas przez który certyfikowane dane można uważać za poprawne. Niezależnie od okresu ważności certyfikowane klucze mogą zostać uznane za niepoprawne, np. gdy zaistnieje podejrzenie, iż ktoś nieuprawniony wszedł w posiadanie tajnego klucza prywatnego, odpowiadającego certyfikowanemu kluczowi publicznemu. Urząd poświadczający CA musi przechowywać listę niepoprawnych i nieaktualnych certyfikatów. Oczywiście, unieważnienie klucza jest także rodzajem certyfikatu. 
Struktura podstawowa typowego certyfikatu jest przedstawiona na rysunku 5. Oprócz wymienionych tam pól poszczególne certyfikaty mogą zawierać dodatkowe, specyficzne dla konkretnego urzędu CA lub zastosowań, do których certyfikaty są przeznaczone. Przykłady rzeczywistych certyfikatów możemy znaleźć w każdej przeglądarce internetowej. 
Jednym z najpopularniejszych współcześnie rodzajów certyfikatów są te zgodne ze standardem ITU-T X.509. Budowa certyfikatu X.509 v.3 obejmuje szereg elementów. Należą do nich: 
  * struktura podstawowa uzupełniona o zestaw danych identyfikacyjnych podmiotu certyfikatu
  * sposób wykorzystania klucza (przeznaczenie, np. do szyfrowania danych, do szyfrowania kluczy, do uzgadniania kluczy, do podpisywania danych, do osiągnięcia niezaprzeczalności)
  * informacje o polityce certyfikacji wydawcy certyfikatu (np. ograniczenia długości ścieżki certyfikacji, punkty dystrybucji list certyfikatów unieważnionych).


Ponadto istnieje opcjonalna możliwość tworzenia dodatkowych pól / parametrów identyfikacyjnych, wg potrzeb komunikujących się podmiotów. 
[![Bsi-w-05-06.png](https://wazniak.mimuw.edu.pl/images/thumb/0/03/Bsi-w-05-06.png/600px-Bsi-w-05-06.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-06.png>)
**Rysunek '**_5'_**. Schematyczna struktura typowego certyfikatu**
Dystrybucja kluczy przy wykorzystaniu certyfikatów przebiega następująco: 
  * w celu uzyskania certyfikatu użytkownik zwraca się do urzędu certyfikującego CA dostarczając mu swój klucz publiczny
  * do zweryfikowania certyfikatu niezbędny jest tylko i wyłącznie klucz publiczny urzędu certyfikującego
  * alternatywnie użytkownik może przesłać swój certyfikat do innych użytkowników z prośbą o poświadczenie jego autentyczności.


W tym ostatnim przypadku mówimy o systemie wzajemnej certyfikacji (sieci wzajemnego zaufania, ang. _web of trust_). Certyfikat użytkownika, dajmy na to - Alicji, poświadcza (podpisuje) z reguły kilko (kilkunastu) użytkowników. Jeśli po pobraniu przez Bolka, stwierdza on, że wśród podpisów znajdują się jakieś należące do zaufanych mu osób, uznaje on certyfikat za poświadczony. 
Zarówno rozwiązania instytucjonalne z urzędami certyfikującymi, jaki i system wzajemnego zaufania mają swoich zwolenników. 
W każdym przypadku istnieje dylemat, komu na tyle zaufać, aby mógł być on w pełni wiarygodny i poświadczać (wydawać) certyfikaty? Problem ten dotyczy przede wszystkim pierwszego kontaktu, zwłaszcza w relatywnie anonimowej sieci globalnej Internet, gdzie wzajemne kontakty, „w cztery oczy", nie są raczej najbardziej typowym sposobem komunikacji. Skąd zatem pewność, że certyfikat został pobrany z właściwego urzędu, czy że podpisy poświadczające jego autentyczność rzeczywiście są godne zaufania. ile może istnieć instytucji cieszących takim zaufaniem, iż certyfikaty przez nie podpisane możemy śmiało uznawać za rzetelnie zweryfikowane i autentyczne. 
Rozwiązaniem tego problemu jest system, w którym certyfikat musi przebyć pewną kilkuetapową procedurę uwierzytelniającą, a urzędy CA mogą tworzyć wielopoziomową hierarchię. Urzędy danego poziomu hierarchii wystawiają certyfikaty kluczy publicznych urzędom lub użytkownikom znajdującym się na niższym poziomie. Na szczycie znajduje jeden z nielicznych urzędów centralnych, który swym powszechnie uznanym autorytetem ostatecznie poświadcza poprawność całej procedury uwierzytelniającej certyfikat. 
[![Bsi-w-05-07.png](https://wazniak.mimuw.edu.pl/images/f/f4/Bsi-w-05-07.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-07.png>)
**Rysunek '**_6'_**. Hierarchia urzędów poświadczających**
Taka hierarchia urzędów poświadczających jest podstawą funkcjonowania niezwykle ważnego współcześnie mechanizmu informatycznego - **infrastruktury kluczy publicznych** - PKI (_Public Key Infrastructure_). Infrastruktura kluczy publicznych obejmuje sprzęt, oprogramowanie, ludzi, polityki bezpieczeństwa i procedury konieczne do utworzenia, zarządzania, przechowywania, dystrybucji i unieważniania certyfikatów kluczy publicznych w skali najczęściej ogólnonarodowej lub światowej. PKI oferuje często dodatkowe certyfikaty, np. Certyfikaty Znacznika Czasu (dla wiarygodnego potwierdzania czasu). W sieci Internet, PKI wykorzystuje specyfikację X.509 (PKIX, RFC 2459). 
PKI jest hierarchicznym systemem urzędów certyfikujących oferujących publicznie swoje usługi. Do usług tych należy między innymi: 
  * weryfikacja tożsamości użytkowników ubiegających się o certyfikaty
  * zarządzanie kluczami kryptograficznymi 
    * generowanie par kluczy dla użytkowników
    * bezpieczne przechowywanie kluczy
  * zarządzanie certyfikatami 
    * wystawienie certyfikatów kluczy publicznych
    * generowanie list certyfikatów unieważnionych CRL (_Certificate Revocation List_)


Komponenty systemu PKI to: 
  * urzędy CA
  * punkty rejestrujące, poręczające zgodność kluczy z identyfikatorami (lub innymi atrybutami) posiadaczy certyfikatów
  * użytkownicy certyfikatów podpisujący cyfrowo dokumenty
  * klienci weryfikujący podpisy cyfrowe i ścieżki certyfikacji do zaufanego CA
  * repozytoria przechowujące i udostępniające certyfikaty i listy unieważnień.


Repozytoriami certyfikatów i list unieważnień mogą być np.: 
  * serwery LDAP
  * respondery OCSP
  * serwery WWW
  * serwery FTP
  * serwery DNS (DNSsec)
  * agenci systemu katalogowego X.500 (DSA - _Directory System Agents_)
  * korporacyjne bazy danych


Mimo wysokiej przydatności systemów PKI, nie wszystkie problemy związane z certyfikacją zostały w pełni rozwiązane. Pozostaje przykładowo problem jednoznacznej identyfikacji podmiotu - jaki jest adekwatny kompromis pomiędzy pełnymi danymi identyfikującymi a prywatnością podmiotu? Rozwiązanie tego problemu na ogół przybliża się wprowadzając różne klasy certyfikacji o różnym poziomie zaufania. 
Inny problem to problem pierwszego certyfikatu - jak bezpiecznie certyfikować CA? Możliwym rozwiązaniem jest wzajemna certyfikacja różnych urzędów z PKI. Wielość hierarchicznych ośrodków certyfikacji umożliwia współpracę pomiędzy niezależnymi strukturami, również w zakresie wzajemnej certyfikacji. Innym powszechnie spotykanym rozwiązaniem są certyfikaty wybranych urzędów najwyższego poziomu hierarchii wbudowane na stałe w aplikacje (przeglądarki WWW, np. Netscape Navigator ma ponad 30 predefiniowanych certyfikatów urzędów CA). Wówczas, zakładając, iż integralność wersji binarnej aplikacji dystrybuowanej przez producenta nie została naruszona (co, notabene, można weryfikować również technikami kryptograficznymi), można przyjąć autentyczność kluczy publicznych zawartych w tych wbudowanych certyfikatach i bezpiecznie się nimi posługiwać do potwierdzania autentyczności urzędów niższego szczebla hierarchii. 
Mechanizmem pobierania certyfikatów CA powszechnie uznanym za standardowy jest przekazywanie ich jako typ MIME application/x-x509-ca-cert. Z kolei do popularnych protokołów wymiany informacji niezbędnych do właściwego zarządzania infrastrukturą kluczy publicznych zaliczyć można CMP (_Certificate Management Protocol_) oraz SCVP (_Simple Certificate Validation Protocol_). 
W myśl polskiego ustawodawstwa wyróżnia się dwa rodzaje certyfikatów: 
##### Certyfikaty zwykłe (tzw. powszechne)
  * obejmują takie zastosowania jak szyfrowanie danych, poczta, www, urządzenia sieciowe, oprogramowanie


##### Certyfikaty kwalifikowane:
  * wywołują skutki prawne równoważne podpisowi własnoręcznemu (Ustawa z dn. 18.09.2001 o podpisie elektronicznym)
  * przeznaczone dla osób fizycznych, wydawane na podstawie umowy i po (osobistej) weryfikacji tożsamości w Punkcie Rejestracji CA
  * znajdują zastosowanie w każdym przypadku składania oświadczenia woli (również e‑faktury)
  * nie służą do szyfrowania dokumentów


W naszym kraju istnieje wiele urzędów certyfikacji. Jedne z najstarszych to np.: 
  * Unizeto Certum www.certum.pl
  * Signet www.signet.pl
  * Sigillum www.sigillum.pl


### Kryptograficzne zabezpieczenie danych
Współcześnie dostępna jest ogromna ilość aplikacji szyfrowania plików i całych katalogów (fragmentów systemu plików). Można tu wymienić np. moduł jądra Linux _loop-AES_ (od wersji 2.4 jądra nosi nazwę _cryptoloop_). Oferuje on szyfrowanie całego systemu plików na poziomie jądra za pomocą urządzenia blokowego /dev/loop[1-8]. Przykładowe polecenie montowania zaszyfrowanego systemu plików pokazuje poniższa komenda powłoki systemu operacyjnego: 
```
 mount -t ext3 crypto.raw /mnt/crypto -oencryption=aes-256

```

Innym przykładem środowiska szyfrowania plików jest EncFS. Tworzy ono z wybranego katalogu wirtualny system plików w przestrzeni użytkownika, korzystając ze standardowego modułu jądra FUSE (_Filesystem in USErspace_). Przykładowe wywołanie operacji tego środowiska jest przedstawione poniżej: 
```
 encfs ~/.crypto.vfs ~/tajne_dane 

```

Wykonanie tego polecenia za pierwszym razem powoduje utworzenie pliku .crypto.vfs z zaszyfrowanym systemem plików, na podstawie zawartości katalogu tajne_dane. Przy kolejnych wywołaniach następuje podmontowanie .crypto.vfs z do katalogu tajne_dane. Odmontowanie niepotrzebnego już katalogu tajne_dane przebiega standardowo: 
```
 fusermount -u ~/tajne_dane

```

W systemie MS Windows z kolei zawarty jest moduł EFS (_Encrypted File System_), działający na partycjach NTFS od wersji Windows 2000. EFS działa jako usługa systemowa - przeźroczyście dla aplikacji użytkownika. Usługa ta wykorzystuje algorytm DESX, będący autorską odmianą 3DES firmy Microsoft. Przykład uaktywnienia funkcji szyfrowania pliku poprzez graficzny interfejs użytkownika pokazuje rysunek 7. 
Występują dwa rodzaje kluczy EFS tworzonych automatycznie przy pierwszym uaktywnieniu usługi (rysunek 8): 
  * klucz właściciela pliku przechowywany w certyfikacie użytkownika (na rysunku należy do użytkownika Administrator)
  * klucz uniwersalny usługi systemowej odtwarzania danych z kopii zapasowych - Data Recovery Agent (na rysunku również wystawiony przez i dla użytkownika Administrator, lecz nie jest dostępny ani dla niego, ani dla żadnego innego konta poza usługą Data Recovery Agent).


[![Bsi-w-05-08.png](https://wazniak.mimuw.edu.pl/images/thumb/c/ca/Bsi-w-05-08.png/600px-Bsi-w-05-08.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-08.png>)
**Rysunek '**_7'_**. Uaktywnienie funkcji szyfrowania pliku w MS Windows**
[![Bsi-w-05-09.png](https://wazniak.mimuw.edu.pl/images/thumb/0/02/Bsi-w-05-09.png/600px-Bsi-w-05-09.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi-w-05-09.png>)
**Rysunek '**_8'_**. Uaktywnienie funkcji szyfrowania pliku w MS Windows**
Ponadto istnieje wiele narzędzi kryptograficznego zabezpieczania komunikacji. Do najpopularniejszych rozwiązań należą protokoły komunikacyjne: 
  * SSH (_Secure Shell_)
  * SSL (_Secure Sockets Layer_) i TLS (_Transport Layer Security_)
  * PCT (_Private Communication Technology_)


oraz komponenty aplikacji użytkowych, takie jak: 
  * dla poczty elektronicznej: PGP, PEM, S/MIME, MIME/PGP, MSP
  * dla usługi www: S-HTTP
  * dla systemów e-commerce: SET (_Secure Electronic Transactions_).


Rozwiązania te i ich implementacje będą szerzej przedstawione w następnych modułach. 
### Zadania
  1. Dlaczego nadal wykorzystywane są oba systemy kryptograficzne: symetryczny i asymetryczne? Inaczej mówiąc: dlaczego szyfrowanie asymetryczne, oferujące więcej własności bezpieczeństwa, nie wyparło całkowicie szyfrowania symetrycznego?
  2. Rozważmy przypadek szczególny ataku _man-in-the-middle_ na realizację metody D-H: co się stanie jeśli Edziu przechwytując komunikację pomiędzy Alicją i Bolkiem zastąpi  K A = α k a {\displaystyle K_{A}=\alpha ^{ka}} ![{\\displaystyle K_{A}=\\alpha ^{ka}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/7d60eef856a389118e41a1f51f30ccfe77abc4b9) oraz  K B = α k b {\displaystyle K_{B}=\alpha ^{kb}} ![{\\displaystyle K_{B}=\\alpha ^{kb}}](https://wazniak.mimuw.edu.pl/api/rest_v1/media/math/render/svg/e1bcad9b9da11435a2746a029fc8f407b37b2956) przez wartość 1?


---


# 

# Bezpieczeństwo systemów komputerowych - wykład 6:
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Podstawowe problemy bezpieczeństwa sieci komputerowych](https://wazniak.mimuw.edu.pl/<#Podstawowe_problemy_bezpieczeństwa_sieci_komputerowych>)
    * [1.1 Warstwa sieciowa](https://wazniak.mimuw.edu.pl/<#Warstwa_sieciowa>)
      * [1.1.1 Adresacja](https://wazniak.mimuw.edu.pl/<#Adresacja>)
      * [1.1.2 Trasowanie](https://wazniak.mimuw.edu.pl/<#Trasowanie>)
      * [1.1.3 Fragmentacja pakietów](https://wazniak.mimuw.edu.pl/<#Fragmentacja_pakietów>)
      * [1.1.4 Pakiety rozgłoszeniowe](https://wazniak.mimuw.edu.pl/<#Pakiety_rozgłoszeniowe>)
      * [1.1.5 Odwzorowanie adresów](https://wazniak.mimuw.edu.pl/<#Odwzorowanie_adresów>)
    * [1.2 Warstwa transportowa](https://wazniak.mimuw.edu.pl/<#Warstwa_transportowa>)
    * [1.3 Warstwa aplikacyjna](https://wazniak.mimuw.edu.pl/<#Warstwa_aplikacyjna>)
      * [1.3.1 Identyfikacja usług](https://wazniak.mimuw.edu.pl/<#Identyfikacja_usług>)
    * [1.4 Usługi narzędziowe infrastruktury sieciowej](https://wazniak.mimuw.edu.pl/<#Usługi_narzędziowe_infrastruktury_sieciowej>)
    * [1.5 Typowe ataki na infrastrukturę sieciową](https://wazniak.mimuw.edu.pl/<#Typowe_ataki_na_infrastrukturę_sieciową>)
      * [1.5.1 Atak session hijacking](https://wazniak.mimuw.edu.pl/<#Atak_session_hijacking>)
      * [1.5.2 Atak TCP spoofing](https://wazniak.mimuw.edu.pl/<#Atak_TCP_spoofing>)
      * [1.5.3 Atak Denial of Service (DoS)](https://wazniak.mimuw.edu.pl/<#Atak_Denial_of_Service_\(DoS\)>)
        * [1.5.3.1 Atak SYN flood](https://wazniak.mimuw.edu.pl/<#Atak_SYN_flood>)
        * [1.5.3.2 Ping of Death](https://wazniak.mimuw.edu.pl/<#Ping_of_Death>)
        * [1.5.3.3 Smurf attack](https://wazniak.mimuw.edu.pl/<#Smurf_attack>)
        * [1.5.3.4 Fraglle attack](https://wazniak.mimuw.edu.pl/<#Fraglle_attack>)
        * [1.5.3.5 Land attack](https://wazniak.mimuw.edu.pl/<#Land_attack>)
      * [1.5.4 Metody obrony przed atakami DoS/DDoS](https://wazniak.mimuw.edu.pl/<#Metody_obrony_przed_atakami_DoS/DDoS>)
    * [1.6 Mechanizmy bezpieczeństwa zdalnego dostępu](https://wazniak.mimuw.edu.pl/<#Mechanizmy_bezpieczeństwa_zdalnego_dostępu>)
      * [1.6.1 PAP (_PPP Authentication Protocol_) RFC1334](https://wazniak.mimuw.edu.pl/<#PAP_\(PPP_Authentication_Protocol\)_RFC1334>)
      * [1.6.2 CHAP (_Challenge Handshake Authentication Protocol_) RFC1994](https://wazniak.mimuw.edu.pl/<#CHAP_\(Challenge_Handshake_Authentication_Protocol\)_RFC1994>)
      * [1.6.3 EAP (_PPP Extensible Authentication Protocol_) RFC2284](https://wazniak.mimuw.edu.pl/<#EAP_\(PPP_Extensible_Authentication_Protocol\)_RFC2284>)
      * [1.6.4 Protokół RADIUS (_Remote Access Dial-In User Service_) – RFC2138](https://wazniak.mimuw.edu.pl/<#Protokół_RADIUS_\(Remote_Access_Dial-In_User_Service\)_–_RFC2138>)
    * [1.7 Uwierzytelnianie stanowisk infrastruktury sieciowej](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_stanowisk_infrastruktury_sieciowej>)
    * [1.8 Bezpieczny system nazw](https://wazniak.mimuw.edu.pl/<#Bezpieczny_system_nazw>)
    * [1.9 Narzędzia bezpieczeństwa](https://wazniak.mimuw.edu.pl/<#Narzędzia_bezpieczeństwa>)
      * [1.9.1 DoS guard](https://wazniak.mimuw.edu.pl/<#DoS_guard>)
      * [1.9.2 Kryptograficzne zabezpieczenie komunikacji](https://wazniak.mimuw.edu.pl/<#Kryptograficzne_zabezpieczenie_komunikacji>)
    * [1.10 Pytania problemowe](https://wazniak.mimuw.edu.pl/<#Pytania_problemowe>)


## Podstawowe problemy bezpieczeństwa sieci komputerowych
Bieżący moduł przedstawia wybrane zagadnienia bezpieczeństwa związane bezpośrednio z niedoskonałościami współczesnych technologii sieci komputerowych. Omówione zostaną problemy bezpieczeństwa podstawowych protokołów sieciowych, klasyfikacja i przykłady ataków na środowiska sieciowe, podstawowe metody obrony oraz przykłady narzędzi podnoszących poziom bezpieczeństwa sieci 
Rysunek 1 przedstawia schemat prostej sieci komputerowej analizowany w dalszej części modułu jako przykładowy scenariusz ataków na środowisko sieciowe i obrony przed tymi atakami. Rozważać będziemy sieć lokalną hipotetycznego przedsiębiorstwa lub instytucji, obejmującą serwer aplikacyjny, np. z systemem bazy danych zawierającej dane przetwarzane w firmie, zbiór stacji roboczych, na których działają klienckie aplikacje użytkowników wykorzystujące informacje z bazy danych. Oprócz infrastruktury sieci lokalnej wyróżnimy jeszcze łącze do sieci rozległej. Przyjmijmy dla uatrakcyjnienia rozważań, iż jest to sieć publiczna, np. Internet. Utrzymywanie łącza do sieci rozległej może być wymagane chociażby z tego powodu, że pewne ograniczone informacje z bazy danych firma chce publicznie udostępniać swoim klientom poprzez usługę WWW. Oczywiście możliwych jest kilka punktów dostępowych do sieci rozległej, mogą to być np. łącza modemowe, analogowe lub cyfrowe typu xDSL, lub sieci bezprzewodowe z dostępem do Internetu. 
[![Bsk-m6-01-1.png](https://wazniak.mimuw.edu.pl/images/7/73/Bsk-m6-01-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-1.png>)
**Rysunek 1. Schemat sieci komputerowej analizowany jako scenariusz zagrożeń**
Rozważany scenariusz zagrożeń bezpieczeństwa obejmuje następujące przypadki: 
  1. Uzyskanie dostępu do konta w systemie / bazie danych, z czym wiąże się możliwość: 
    1. naruszenia własności poufności / integralności / dostępności przechowywanych w systemie danych
    2. rekonfiguracji systemu (co w istocie jest też naruszeniem własności integralności)
  2. Pozyskanie / modyfikacja transmitowanych danych 
    1. naruszenia własności poufności / integralności / dostępności danych transmitowanych między serwerem a stacjami roboczymi
  3. Rekonfiguracja sieci (urządzeń sieciowych, protokołów) – naruszenie integralności
  4. Zablokowanie funkcjonowania stacji / urządzeń sieciowych i w efekcie naruszenie własności dostępności informacji


Przyczyn tych zagrożeń należy przede wszystkim szukać w niedoskonałościach technologii sieciowych wykorzystywanych aktualnie. Należy od razu zaznaczyć, niejako tytułem usprawiedliwienia, iż większość tych technologii zostało zaprojektowanych wiele lat temu (pierwotne wersje niektórych rozważanych standardów datują się na wczesne lata 70-te ubiegłego wieku) i do dziś były zaledwie modernizowane na ogół w celu usprawnienia działania, dostosowania do nowych wymagań, a raczej rzadko dla nieznacznego podniesienia bezpieczeństwa. 
Obserwując właściwości technologii należących do kolejnych warstw modelu referencyjnego OSI, interesujących odkryć możemy dokonać już w warstwie pierwszej – fizycznej. Poniżej przypomniane zostaną, raczej jedynie hasłowo, tytułem zaakcentowania, najistotniejsze z tych właściwości. 
Elementami specyfikacji funkcjonalnej tej warstwy są topologie fizyczne i media komunikacyjne. 
Ze względu na własności zarówno poufności, integralności jak i dostępności możemy łatwo uszeregować typowe topologie sieciowe o najmniej do najbardziej bezpiecznej (zastanów się jak wygląda to uszeregowanie). Szczęśliwie najkorzystniej wypada tu najpowszechniej dziś spotykana topologia gwiazdy (przypomnij sobie jej własności). 
[![Bsk-m6-01-2.png](https://wazniak.mimuw.edu.pl/images/d/d3/Bsk-m6-01-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-2.png>)
**Rysunek 2. Modele typowych topologii sieciowych**
Również typowo dziś spotykane media można podobnie uszeregować, od najmniej bezpiecznych z natury – mediów bezprzewodowych, poprzez różne technologie skrętki komputerowej, niechaj wymienić tu: UTP, FTP, STP czy SSTP, aż po światłowód. 
W warstwie łącza danych pojawiają się już elementy inteligencji sieciowej – protokoły komunikacyjne. Najistotniejszym współcześnie jest niewątpliwie protokół Ethernet w różnych stosowanych standardach. 
Z punktu widzenia bezpieczeństwa architekturę sieci Ethernet wyróżniają następujące cechy: 
  * ruch niejawnie rozgłoszeniowy, współdzielenie medium (topologia logiczna)
  * komunikacja jawnie rozgłoszeniowa (adresy rozgłoszeniowe i grupowe)
  * możliwość pracy sterownika sieciowego w trybie diagnostycznym (_ang. promiscuous_)
  * stosowane proste liniowe sumy kontrolne (CRC) dla kontroli integralności transmitowanych ramek


Funkcjonujące w tej warstwie urządzenia sieciowe (mosty i przełączniki) charakteryzują następujące cechy: 
  * mostowanie transparentne (TB) i źródłowe (SR) i związana z tymi funkcjami selektywna propagacja danych (prosta lecz podatna na nadużycia odmiana filtracji)
  * automatyka obsługi dowolnych stacji i współpracy z innymi urządzeniami (np. protokół drzewa rozpinającego STP)


Z racji szczególnej roli wszechobecnej dziś rodziny protokołów TCP/IP, spośród kolejnych warstw modelu OSI najistotniejsze są te, które odwzorowują się najdokładniej na model internetowy. Dotyczy to warstwy sieciowej, transportowej oraz aplikacyjnej. 
W warstwie sieciowej szczególną uwagę należy zwrócić na problematykę: 
  * bezpołączeniowa semantyki i zawodnej transmisji pakietów (datagramów) IP
  * mechanizmów zautomatyzowanego wsparcia dla adresacji: ARP, RARP
  * funkcjonalności routingu dynamicznego
  * kapsułkowania (kopertowania) pakietów.


Zagadnienia dotyczące warstwy sieciowej są na tyle ważne, iż wymienione wyżej problemy zostaną omówione szerzeń w dalszej części bieżącego modułu. Wcześniej jednak podkreślone zostaną istotne cechy pozostałych ważnych warstw. 
Warstwa transportowa cechuje się funkcjonalnością której najistotniejsze elementy określa się mianem sterowania przepływem. 
Natomiast w warstwie aplikacyjnej pojawiają się problemy związane z niedoskonałościami popularnych protokołów (telnet, ftp, SMTP, POP, IMAP) na ogół nie dysponujących mechanizmami ochrony poufności oraz integralności i stosującymi mało wiarygodne mechanizmy uwierzytelniania. 
### Warstwa sieciowa
Protokół IP, jest najpowszechniej spotykanym protokołem sieciowym i analizę problemów bezpieczeństwa ograniczamy wyłącznie do aspektów dotyczących tego protokołu. 
[![Bsk-m6-01-3.png](https://wazniak.mimuw.edu.pl/images/9/91/Bsk-m6-01-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-3.png>)
**Rysunek 3. Format datagramu IP**
#### Adresacja
Adresacja jest jednym z zadań podstawowych protokołów warstwy sieciowej. Pola adresowe ustawiane są w nagłówku datagramu IP przez stację nadawczą (źródło, _ang. source_). Z zawartością pól adresowych wiążą się następujące problemy: 
  * nie ma gwarancji, że pakiet został wysłany z adresu wpisanego w polu _Source Address_
  * wiele systemów kontroluje to pole w momencie wysyłania datagramu
  * niektórzy operatorzy dostępu do Internetu stosują filtry blokujące pakiety z nieprawidłowym adresem źródłowym
  * mimo tego nie można polegać na poprawności adresu źródłowego odebranego pakietu.


Problemy te dyskwalifikują uwierzytelnianie poprzez wartość pola adresu źródłowego. Niestety wiele protokołów aplikacyjnych posiada wbudowane takie mechanizmy. Ewentualny atak na system może zatem polegać sfałszowaniu adresu źródłowego (IP spoofing). Kompromituje to procedury uwierzytelniania ofiary. 
#### Trasowanie
Trasowanie (routing) polegające na wyznaczaniu drogi do adresata. W przypadku protokołu IP trasowanie jest wykonywane pojedynczymi etapami. Zadanie to wykonuje router. Trasowanie jest niezwykle istotnym elementem działania warstwy sieciowej i związanych z nim jest kilka problemów: 
  * przeciążony router może odrzucać nadchodzące pakiety
  * za retransmisję odpowiadać muszą protokoły warstw wyższych
  * jeśli router zostanie „zalany” bardzo dużą masą pakietów (nieistotne czy prawidłowych), to ewentualne przeciążenie doprowadzi do zablokowania komunikacji (pakietów należących do aktywnych sesji – asocjacji IP)


Przeciążenie routera implikuje zagrożenia dostępności danych transmitowanych w pakietach kierowanych do niego. Co więcej, potencjalny atak zdalny skierowany przeciwko innym stacjom sieciowym może wykorzystywać chwilową niedostępność pakietów z oryginalnego źródła celem podszycia się pod źródłowy komputer. 
#### Fragmentacja pakietów
Fragmentacja datagramów IP jest często realizowaną funkcją, pierwotnie zamierzoną jako mechanizm optymalizacji kosztu przetwarzania pakietów. O wielkości fragmentów decyduje wartość MTU (_Maximum Transfer Unit_) związana z wielkością pola danych ramek warstwy drugiej OSI. Do fragmentacji dochodzić może na dowolnym etapie drogi między nadawcą a odbiorcą. Oryginalny datagram otrzymuje unikalny (w przybliżeniu) identyfikator, którym opatrywane są kolejne fragmenty. Kolejność fragmentów determinuje względny numer pierwszego bajtu przekazywanego w polu danych fragmentu liczony od początkowego bajtu oryginalnego datagramu (_Fragment Offset_). Scalanie fragmentów odbywa się na węźle odbiorcy. 
Fragmentacja może stanowić potencjalne źródło zagrożenia a następujących powodów: 
  * każdy fragment jest również datagramem i jako taki może mieć, teoretycznie, do 64 kB wielkości – z premedytacją spreparowane fragmenty przekraczające w sumie 64 kB mogą powodować błędy scalania
  * podobnie manipulacje wartościami pola _Fragment Offset_
  * niektóre stacje IP, w tym zabezpieczenia (filtry pakietów), mogą zachowywać się niepoprawnie atakowane przez niewłaściwie pofragmentowane pakiety – zjawisko to wykorzystuje np. _teardrop attack_ [Ziemba, RFC 1858]
  * często filtry przetwarzają właściwie (np. odrzucają) tylko pierwszy fragment pakietu – wynika to z faktu iż w praktyce informacje niezbędne do przeprowadzenia filtracji znajdują się tylko w pierwszym pakiecie, a ponadto jest to działanie wystarczające do wykluczenia poprawnego scalenia niepożądanego datagramu w węźle odbiorcy, jednak powoduje to mimowolne przepuszczanie kolejnych fragmentów należących do (będących przecież kontynuacją) ruchu sklasyfikowanego jako niepożądany. Fakt przepuszczania takich pakietów może zostać wykorzystany do realizacji niektórych typów ataków.


[![Bsk-m6-01-4.png](https://wazniak.mimuw.edu.pl/images/0/00/Bsk-m6-01-4.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-4.png>)
**Rysunek 4. Schemat fragmentacji IP**
#### Pakiety rozgłoszeniowe
Mechanizmy rozgłoszeniowe oferuje wiele protokołów, również IP. Ukierunkowane rozgłoszenie często jest wykorzystywane do przeprowadzenia ataków na dostępność informacji (typu _Denial of Service – DoS_). Stanowi to najistotniejsze zagrożenie związane z mechanizmem rozgłaszania. Szczęśliwie, wiele routerów posiada funkcję blokowania ruchu rozgłoszeniowego. 
#### Odwzorowanie adresów
Odwzorowanie adresów IP na adresy MAC (np. Ethernet) jest niezbędne dla realizacji operacji nadawczych, a dokładniej do konstrukcji prawidłowej ramki MAC. Zadaniem odwzorowania adresów na ogół zajmuje się protokół ARP (_Address Resolution Protocol_). Stosuje on transmisję rozgłoszeniową zapytań i zbiera odpowiedzi bez zapewnienia poufności i autentyczności. W celu poprawy efektywności, protokół wykorzystuje pamięć podręczną do temporalnego składowania informacji pozyskanych z docierających zapytań i odpowiedzi ARP. 
W efekcie z protokołem ARP wiążą się następujące zagrożenia: 
  * stacja w sieci lokalnej może wysyłać fałszywe zapytania lub odpowiedzi ARP
  * kierując w efekcie inne pakiety w swoim kierunku (ARP spoofing)
  * dzięki czemu napastnik może: 
    * modyfikować strumienie danych
    * podszywać się pod wybrane komputery


Często można skonfigurować lokalne statyczne mapowanie ARP wyłączając przy tym automatyczną obsługę zapytań i odpowiedzi ARP, co uwalnia od w/w problemów. Jednak w praktyce okazuje się, że wyłączenie obsługi komunikacji sieciowej nie jest możliwe w każdej implementacji stacji protokołu ARP. 
[![Bsk-m6-01-5.png](https://wazniak.mimuw.edu.pl/images/b/b8/Bsk-m6-01-5.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-5.png>)
**Rysunek 5. Format zapytania ARP**
### Warstwa transportowa
Jak wiadomo, w rodzinie protokołów internetowych występują 2 protokoły transportowe. Protokół TCP (_Transmission Control Protocol_) jest to protokół strumieniowy zorientowany połączeniowo. Zestawienie komunikacji w protokole TCP wymaga wykonania 3-etapowej procedury nawiązania połączenia (_3-way handshake_). Bodaj najistotniejszym zadaniem tej procedury jest ustalenie inicjalnych numerów sekwencyjnych, rozpoczynających numerowanie bajtów strumienia danych przekazywanego w każdym z dwu kierunków połączenia A-B (rysunek 7). 
[![Bsk-m6-01-6.png](https://wazniak.mimuw.edu.pl/images/f/f3/Bsk-m6-01-6.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-6.png>)
**Rysunek 6. Format segmentu TCP**
Na schemacie z rysunku 7 zastosowano następujące oznaczenia: 
SN = Numer sekwencyjny w nagłówku segmentu określa numer pierwszego oktetu danych przesyłanych w tym segmencie ACK = Numer potwierdzenia – numer sekwencyjny następnego oktetu danych po ostatnim pomyślnie odebranym (numer oczekiwanego oktetu) ISN = Inicjalny numer sekwencyjny (_Initial Sequence Number_) – początkowy numer sekwencyjny danych przesyłanych w danym połączeniu, ustalany w procesie nawiązania połączenia (w segmencie SYN). Każde połączenie może rozpocząć numerację oktetów danych od arbitralnej wartości (jeśli ISN=0, to pierwszy oktet w całym połączeniu ma numer ISN+1=1). Inicjalny numer sekwencyjny jest ustalany oddzielnie dla obu stron połączenia (w ogólności ISNA ≠ ISNB ) 
[![Bsk-m6-01-7.png](https://wazniak.mimuw.edu.pl/images/9/93/Bsk-m6-01-7.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-7.png>)
**Rysunek 7. Schemat nawiązania połączenia (3-way handshake)**
Nawiązanie połączenia TCP charakteryzują następujące cechy: 
  * możliwe jest zdalne wymuszenie połączenia i przechwycenie legalnej komunikacji nawet bez odbioru segmentu SYN+ACK
  * wymaga to odgadnięcia ISN zawartego w tym segmencie
  * na szczęście numery ISN są wybierane pseudolosowo
  * na ogół z rozkładem bardzo dalekim od losowego 
    * wg sugestii z RFC 793 – licznik ISN jest inkrementowany co 4 μs
    * starsze jądra wywodzące się z BSD (4.2) dokonują inkrementacji o wartość stałą co 1 sek i przy każdym nowym połączeniu
  * więc łatwo przewidzieć ISN dla nowych połączeń


Stopień randomizacji wyboru ISN graficznie reprezentuje się wykresem fazowym. Wykresy fazowe prawidłowego generatora ISN zgodny ze standardem RFC 1948 oraz generatorów w popularnych (mniej i bardziej) systemach operacyjnych można znaleźć w <A HREF=”<http://alon.wox.org/tcpseq/”>>[Zalewski]</A>. Jak pokazują przykłady wykresów fazowych, coraz więcej systemów operacyjnych stosuje generatory zbliżone do wzorcowego, jednak nadal wiele jest implementacji dalece od wzorca odbiegających. Skutkuje to możliwością przeprowadzenia pewnych ataków, o których będzie mowa dalej. 
Procedura nawiązania połączenia TCP może być wykorzystana do realizacji następujących ataków: 
  * ataki zalewające ofiarę nowonawiązywanymi połączeniami – dla każdego nawiązanego połączenia system przydziela pewne zasoby, w szczególności pamięć. Zasoby zwalniane są po zamknięciu połączenia. Jeśli zamknięcie nie następuje, wówczas zasoby pozostają zajęte (mimo iż mogły w ogóle nie być wykorzystane). Odpowiednio duża liczba zestawionych połączeń może doprowadzić do przydzielenia im całej dostępnej pamięci nie pozostawiając żadnych dostępnych zasobów do pracy systemu i powodując załamanie jego pracy.
  * ataki zalewające ofiarę segmentami SYN (wykorzystujące stan _half-opened_) – w praktyce system operacyjny przydziela zasoby dla nowozestawianego połączenia, jak tylko pojawia się pierwszy segment SYN, jeszcze zanim 3-etapowa procedura nawiązywania zostanie zakończona. Zasoby zajmowane są zatem nawet jeśli połączenie nie zostanie w pełni zestawione. Duża liczba na wpół nawiązanych połączeń może wyczerpać zasoby i ostatecznie blokuje stację protokołu TCP i cały system. Co więcej, takie ataki są trudno wykrywalne, bowiem typowe implementacje TCP nie raportują wyższym warstwom OSI (systemowi operacyjnemu) żadnych zdarzeń związanych z połączeniem, które nie jest jeszcze w pełni nawiązane.


### Warstwa aplikacyjna
W warstwie aplikacyjnej występują m.in. problemy trywialnego uwierzytelniana na podstawie identyfikacji usług oraz braku odpowiednich zabezpieczeń usług narzędziowych. 
#### Identyfikacja usług
Identyfikacja usług w modelu internetowym odbywa się zwykle jedynie na podstawie numer portu źródłowego lub docelowego. Z wykorzystaniem wartości numeru portu wiążą się następujące obserwacje: 
  * lokalny numer portu klienta jest niemal zawsze wybierany przypadkowo przez system operacyjny (choć klient może go wybrać sam)
  * w systemie Unix występują tzw. porty uprzywilejowane (systemowe) – są to porty o numerach do wartości 1024. Pod tymi portami system pozwala uruchomić proces sieciowy tylko administratorowi (root). Teoretycznie zatem, można domniemywać iż uruchomione pod systemowymi portami procesy należą do zaufanych i bezpiecznych. Jednak w praktyce, nie ma oczywiście pewnego sposobu zweryfikowania prawdziwości tego domniemania zdalnie.
  * niestety nadal w wielu przypadkach systemy zdalne polegają na zaufaniu do asocjacji obejmujących te porty (połączeń z tymi portami)
  * w istocie restrykcja wykorzystania portów uprzywilejowanych tylko przez administratora jest wyłącznie konwencją – nie należy do specyfikacji protokołów usług, a co więcej – nie dotyczy systemów innych niż Unix
  * poleganie na niej absolutnie nie jest bezpieczne


### Usługi narzędziowe infrastruktury sieciowej
Jednym z najpopularniejszych przykładów usług narzędziowych jest DNS (_Domain Name Service_). Jak wiadomo, system DNS to swoista rozproszona baza danych odwzorowań nazwa domenowa - adres sieciowy. Baza DNS ma strukturę drzewiastą, poddrzewa odpowiadają poszczególnym domenom niższego poziomu (poddomenom). Zarządzanie poddrzewami może być delegowane innym serwerom DNS. Aktualizacje bazy DNS mogą obejmować pojedyncze rekordy RR (_resource records_), jak i całe poddrzewa. Poprzez protokół DNS można dokonywać prostych zapytań o pojedyncze odwzorowania, jak i zrealizować pozyskanie pełnej kopii fragmentu obszaru nazw (tzw. transfer stref – _zone transfer_) np. w celu aktualizacji serwerów zapasowych. Protokół DNS dostępny jest poprzez oba internetowe protokoły transportowe: UDP – tak realizowane są proste zapytania DNS, TCP – tak odbywa się transfer stref DNS. Z punktu widzenia bezpieczeństwa istotne jest, iż niektóre zapisy RR dostarczają informacji użytecznych dla włamywaczy, np. HINFO (może zawierać m.in. informacje o systemie operacyjnym), WKS (well-known-services). Pola te, na szczęście, rzadko są dziś stosowane. 
Baza DNS składa się z dwóch oddzielnych drzew mapowań – dla mapowania nazw na adresy (zapytania proste) i adresów na nazwy (zapytania odwrotne – _inverse queries_). Nie ma wymuszonej relacji między drzewami – każde z nich jest w praktyce utrzymywanie niezależnie. Przy tym drzewo mapowań odwrotnych zwykle nie jest równie często aktualizowane a do tego w ogóle jest utrzymywane w gorszym stanie. Niestety stanowi to potencjalne ułatwienie w przejęciu kontroli nad częściami drzewa mapowań odwrotnych i, w efekcie, skutecznym podszywaniu się pod autoryzowane nazwy. 
W przypadku usługi DNS można wyróżnić następujące podstawowe problemy dotyczące bezpieczeństwa: 
  * udostępnianie użytecznych informacji atakującym
  * brak uwierzytelniania w protokole zapytań DNS i transferu stref, co umożliwia fałszowanie danych (_pharming_)
  * podszywanie się pod autoryzowne nazwy kompromituje system uwierzytelniania przez nazwę – w tym przypadku możliwa jest jednak prosta obrona przez dodatkową weryfikację w drzewie mapowań nazw i wykrycie fałszerstwa
  * możliwość „zatruwania” fałszywymi odpowiedziami lokalnej pamięci _cache_ usługi DNS stacji uwierzytelniającej jeszcze zanim wyśle ona zapytanie o mapowanie – wówczas fałszerstwo nie wyjdzie na jaw


Usługi inne popularne usługi narzędziowe BOOTP i DHCP również udostępniają informacje o infrastrukturze sieciowej, i to często bardzo bogate informacje, praktycznie bez uwierzytelniania. Na szczęście dostępne są one na ogół tylko w obrębie sieci lokalnej, zatem mogą być wykorzystane tylko przez atakujących, którzy wdarli się już do atakowanej podsieci. Istotny jest jednak problem bezpiecznej wymiany danych pomiędzy serwerami DHCP a DNS, a ta z kolei może przechodzić przez kilka podsieci. 
### Typowe ataki na infrastrukturę sieciową
Powszechne techniki ataków na infrastrukturę sieciową wykorzystują głównie niedoskonałości protokołów oraz technologii sieciowych w celu: 
  * uzyskania danych (_information recovery_)
  * podszycia się pod inne systemy w sieci (_host impersonation_)
  * manipulacji mechanizmami dostarczania pakietów (_temper with delivery mechanisms_)


Poniżej wymienione zostaną najczęściej spotykane współcześnie techniki ataków zebrane w następujące 4 klasy: 
  * Sniffing/scanning: 
    * _network sniffing_ – jest to pasywny podgląd medium transmisyjnego, np. w celu przechwycenia interesujących ramek (_packet snooping_)
    * _network scanning_ – jest to wykorzystanie specyfiki implementacji protokołów do sondowania (_enumeration_) urządzeń aktywnych w sieci, aktywnych usług, konkretnych wersji systemu operacyjnego i poszczególnych aplikacji (sztandarowym przykładem narzędzi realizujących taki atak jest program _nmap_)
  * Spoofing: 
    * _session hijacking_ – przejmowanie połączeń poprzez „wstrzelenie” odpowiednio dobranych pakietów – wymaga dostępu do uprzednio legalnie zestawionego połączenia TCP
    * _TCP spoofing_ – podszywanie bazujące na oszukaniu mechanizmu generowania numerów ISN; wykorzystanie ataku np. w celu oszukania mechanizmów uwierzytelniania usług r* (które dokonują uwierzytelniania przy użyciu funkcji rusersok())
    * _UDP spoofing_ – prostsze od TCP w realizacji (ze względu na brak mechanizmu szeregowania i potwierdzeń ramek w protokole UDP), użyteczne podczas atakowania usług i protokołów bazujących na UDP np. DNS.
  * Poisoning: 
    * _ARP spoofing/poisoning_ – wykorzystuje zasady działania protokołu ARP, umożliwiając zdalną modyfikację wpisów w tablicach ARP systemów operacyjnych oraz przełączników, a przez to przepełnianie tablic ARP
    * _DNS cache poisoning_ (_pharming_ , także znany jako _birthday attack_) – umożliwia modyfikację wpisów domen w dynamicznym cache DNS, co jest niezwykle dużym zagrożeniem w połączeniu z atakami pasywnymi
    * _ICMP redirect_ – wykorzystanie funkcji ICMP do zmiany trasy routingu dla wybranych adresów sieciowych
    * ataki na urządzenia sieciowe przy pomocy protokołu SNMP
  * Denial of Service (DoS)


w tej kategorii mieszczą się wszystkie te ataki, których ostatecznym celem jest unieruchomienie poszczególnych usług, całego systemu lub całej sieci komputerowej. 
  *     * oto przykłady kilku najpopularniejszych ataków: 
      * SYN flood
      * smurf, fraglle
      * land
      * tribal flood (trin00, trinio, trinity v3)
      * subseven, stacheldracht
      * UDP storms (teardrop, bonk)
      * ICMP destination unreachable
    * istnieją też ataki na wyższe warstwy modelu OSI, np. e-mail bombing.


#### Atak session hijacking
Rysunek 8 przedstawia wyjściowy stan ataku _session hijacking_ , którego celem jest nieuprawnione wpięcie segmentów protokołu transportowego w strumień wymieniany w autoryzowanym (poprawnie zestawionym) połączeniu między systemem A (przyszłą ofiarą ataku) i zaufanym systemem B. Atakujący E, mając wgląd w dotychczasową zawartość strumienia w kierunku do B do A (poprzez _sniffing_), może spreparować poprawny i oczekiwany przez A segment, który podsunie jako rzekomo autentyczny segment wysłany przez B (rysunek 9). 
[![Bsk-m6-01-8.png](https://wazniak.mimuw.edu.pl/images/5/56/Bsk-m6-01-8.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-8.png>)
**Rysunek 8. Schemat ataku session hijacking (1)**
[![Bsk-m6-01-9.png](https://wazniak.mimuw.edu.pl/images/c/c7/Bsk-m6-01-9.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-9.png>)
**Rysunek 9. Schemat ataku session hijacking (2)** – w strumieniu przesyłane są segmenty po 100 B 
#### Atak TCP spoofing
Rysunek 10 przedstawia początek ataku _TCP spoofing_ , którego celem jest nieuprawnione zestawienie połączenia z systemem A (ofiarą ataku) w imieniu zaufanego systemu B. Atakujący E tym razem nie ma wglądu komunikację między A i B, co czyni atak znacznie trudniejszym niż _session hijacking_. Atak wymaga nie tylko sfałszowania adresu źródłowego (w szczególności w pierwszym segmencie SYN, nawiązującym połączenie), ale dodatkowo poprawnego przewidzenia numeru ISNA (który zaproponuje system A w drugim segmencie SYN/ACK) i być może jeszcze zablokowania poprawnej komunikacji z rzeczywistym systemem B (co może wymagać przeprowadzenia ataku DoS skierowanego przeciw B), aby B nie mógł zakończyć (zresetować) niechcianego połączenia. Mimo tych utrudnień E może spreparować poprawny i oczekiwany przez A segment ACK – kończący poprawnie procedurę nawiązania połączenia, (rysunek 11). 
[![Bsk-m6-01-10.png](https://wazniak.mimuw.edu.pl/images/a/a8/Bsk-m6-01-10.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-10.png>)
**Rysunek 10. Schemat ataku TCP spoofing (1)**
Najtrudniejszym krokiem ataku jest wysłanie poprawnego segmentu trzeciego zawierającego potwierdzenie inicjalnego numeru sekwencyjnego ISNA wybranego przez A. Ze względu na brak możliwości podglądu przez E komunikacji z A do prawdziwego B, wymaga to przewidzenia wartości ISNA przez E. Jest to prawdopodobne przy wygenerowaniu relatywnie niedużej liczby segmentów ACK, jeśli system A nie posiada poprawnego generatora ISN. Wówczas jest szansa, iż jeden z wygenerowanych przez E segmentów będzie przenosił poprawną wartość potwierdzenia i zostanie przez A uznany za oczekiwany. 
[![Bsk-m6-01-11.png](https://wazniak.mimuw.edu.pl/images/a/ae/Bsk-m6-01-11.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-11.png>)
**Rysunek 11. Schemat ataku TCP spoofing (2)**
Można wyróżnić następujące elementy ataku TCP spoofing: 
  * wytypowanie właściwego ISNA – np. poprzez uprzednie nawiązanie autoryzowanego połączenia na inny port (pozyskanie wcześniejszego numeru ISN'A)
  * celowe uniemożliwienie przetwarzania segmentu drugiego, zawierającego wartości SYN (ISNA) i ACK (ISNE)


Poczynić można w związku z tym następujące obserwacje: 
  * atakujący nie musi mieć dostępu do segmentów autoryzowanego połączenia
  * jeśli ma (_sniffing_) – może podejrzeć numer sekwencyjny (nie musi zgadywać)
  * i podpiąć się na dowolnym etapie już zestawionego połączenia


#### Atak Denial of Service (DoS)
Celem ataku DoS jest unieruchomienie całego systemu ofiary lub jego komponentów (rysunek 12). W tym celu stosowane są różne techniki ataku. Niektóre z nich zostaną krótko przedstawione poniżej. 
[![Bsk-m6-01-12.png](https://wazniak.mimuw.edu.pl/images/8/84/Bsk-m6-01-12.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-12.png>)
**Rysunek 12. Schemat ataku Denial of Service (DoS)**
Szczególnie niebezpieczną odmianą ataku jest rozproszony DoS (Distributed Denial of Service – DdoS), w którym atakujący nie przeprowadza ataku bezpośrednio, lecz doprowadza do skomasowanego natarcia wykorzystując inne systemy (często w dużej liczbie). Zwykle owe systemy uczestniczące mimowolnie w skomasowanym ataku, zostały wcześniej opanowane przez atakującego i tak odpowiednio zmodyfikowane by ułatwić mu w przyszłości przeprowadzanie ataku DDoS. 
[![Bsk-m6-01-13.png](https://wazniak.mimuw.edu.pl/images/a/a9/Bsk-m6-01-13.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-13.png>)
**Rysunek 13. Schemat ataku Distributed DoS (DDoS)**
##### Atak SYN flood
W przypadku ataku SYN flood atakujący (E) wysyła na adres ofiary (A) dużą liczbę segmentów SYN protokołu TCP adresowanych z dowolnych (nieistniejących) adresów IP. Nieświadomy tego A odpowiada segmentami SYN/ACK i rozpoczyna bezowocne oczekiwanie na segmenty ACK (stacja protokołu TCP ofiary jest w stanie na wpół otwartym). W trakcie oczekiwania wyczerpują się zasoby stacji protokołu TCP i systemu operacyjnego A. 
W 1997 r. atak SYN flood na WebCom wyłączył z użycia ponad 3000 witryn WWW 
##### Ping of Death
Atak ten przeprowadza się poprzez wygenerowanie pofragmentowanych pakietów ICMP przekraczających w sumie 64kB. Wówczas scalanie może w niektórych implementacjach powodować błędy prowadzące do zawieszenia stacji IP. 
##### Smurf attack
Jest to atak DDoS. Polega na wygenerowaniu dużej ilości rozgłoszeniowych (_directed broadcast_) pakietów ICMP echo (ping) z adresem IP ofiary ataku jako źródłowym. Ofiara zostanie zalana odpowiedziami ping. Atak ten jest skuteczny jedynie jeśli brzegowy dla sieci ofiary router przepuszcza ping w ukierunkowanym rozgłoszeniu, a system operacyjny stacji odpowiada na taki ping. 
##### Fraglle attack
To atak posiadający identyczny schemat postępowania, lecz wykorzystuje usługę echo na UDP. 
##### Land attack
W tym przypadku, atakujący wysyła segment SYN na adres ofiary podając jej własny adres jako źródłowy i nadając ten sam numer portu źródłowego i docelowego. Stacja TCP ofiary nigdy nie zestawi połączenia zapętlając się w nieskończoność. W niektórych implementacjach może to prowadzić do jej zawieszenia. 
#### Metody obrony przed atakami DoS/DDoS
Nie ma uniwersalnych metod obrony przez atakami odmowy dostępu. Na ogół wymagają one przygotowania przez producenta systemu operacyjnego odpowiednich poprawek (łat) i zastosowania ich w podatnym na atak systemie. Poniżej przedstawione zostaną dwa mechanizmy obrony przed atakiem SYN flood, które systematycznie zyskują coraz większą popularność. 
Obrona przed atakiem SYN flood – SYN Defender 
SYN Defender jest komponentem kilku kompleksowych systemów ochrony (takich jak np. CheckPoint Firewall-1). Jego ogólna koncepcja działania polega na wprowadzeniu pomiędzy atakującego i ofiarę wyspecjalizowanego obrońcę (na rysunku 14 oznaczonego na czerwono), który przejmuje wszystkie segmenty SYN skierowane do ochranianego systemu i propaguje połączenia dopiero gdy wykluczy atak (czyli, gdy dotrze do obrońcy trzeci segment nawiązania połączenia, co oznacza, że nie mamy do czynienia z atakiem SYN flood). 
[![Bsk-m6-01-14.png](https://wazniak.mimuw.edu.pl/images/f/ff/Bsk-m6-01-14.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-14.png>)
**Rysunek 14. Schemat działania mechanizmu SYN Defender**
Jeśli SYN Defender rozpoznaje atak (nie doczeka się trzeciego segmentu) po prostu zapomina o parametrach połączenia, a system ochraniany nawet nie dowie się o ataku. Jeśli SYN Defender wykluczy atak, to wówczas samodzielnie zestawia nowe połączenie z systemem ochranianym, które posłuży to retransmitowania segmentów odebranych od nadawcy. Oczywiście owo nowe połączenie nie będzie miało identycznych parametrów (np. numer ISN wybrany przez ochranianego będzie z pewnością inny, niż uprzednio zaproponowany nadawcy segmentu SYN przez obrońcę). W związku z tym, segmenty propagowane muszą być poddane konwersji parametrów (nagłówka) przy przejściu przez węzeł obrońcy). 
Istotą ochrony przed atakiem jest przeniesienie punktu obrony z ofiary na zewnętrzny system, który przygotowany na okoliczność ewentualnego ataku nie pozwoli na przeciążenie siebie poprzez zużycie wszystkich zasobów. Właściwie ilość zasobów potrzebna obrońcy na obsługę połączeń jest tu minimalna, a system ofiary obsługuje wyłącznie połączenia, które nie są elementem ataku SYN flood. 
Obrona przed atakiem SYN flood – SYN cookies 
Inną metodą obrony przed atakiem SYN flood jest wykorzystanie dość sprytnego mechanizmu o nazwie SYN cookies. Umożliwia on realizację obrony w samym węźle potencjalnej ofiary. Przy zastosowaniu tego mechanizmu, węzeł broniący się nie musi rezerwować zasobów dla połączenia już w momencie odebrania segmentu SYN. Miast tego, węzeł ten generuje specjalną wartość, przekazywaną nadawcy segmentu SYN, i tak spreparowaną, by po ewentualnym otrzymaniu w przyszłości trzeciego segmentu (ACK), rozpoznać że jest to kontynuacja wcześniej rozpoczętego nawiązywania połączenia. Dopiero po otrzymaniu segmentu ACK rezerwowane są zasoby. 
[![Bsk-m6-01-15.png](https://wazniak.mimuw.edu.pl/images/9/99/Bsk-m6-01-15.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-15.png>)
**Rysunek 15. Schemat działania mechanizmu SYN cookies**
Dla rozpoznania poprawności późniejszego segmentu ACK, broniący po odebraniu segmentu SYN generuje wartość cookie uzależnioną od parametrów segmentu ACK. Wartość ta jest wpisywana następnie jako ISN do segmentu SYN/ACK, a zatem powróci (faktycznie zinkrementowana) w polu potwierdzenia w segmencie ACK, umożliwiając detekcję poprawności procedury zestawiania połączenia. 
Mechanizm SYN cookies posiada niestety pewne ograniczenia, np. nie można korzystać niektórych użytecznych rozszerzeń specyfikacji protokołu TCP, np. Large Window. 
Więcej informacji o SYN cookies można znaleźć pod adresem <http://cr.yp.to/syncookies.html>
### Mechanizmy bezpieczeństwa zdalnego dostępu
Rysunek 16 przedstawia schemat uwierzytelniania przy zdalnym dostępie do sieci komputerowej. Przyjmujemy tu scenariusz, w którym system A uzyskuje dostęp zdalny do sieci poprzez publiczną sieć operatora dostępu do Internetu. Po stronie A wykorzystywany jest adapter łącza do sieci publicznej, wbudowany w system komputerowy A lub zewnętrzny (modem telefoniczny, modem kablowy, adapter ISDN lub modem DSL). Operator posiada infrastrukturę złożoną w łączy i systemów przełączających (np. cyfrowych centralek telefonicznych). Natomiast po stronie sieci docelowej połączenie jest obsługiwane przez serwer dostępowy RAS. Serwer dostępu zezwala tylko na autoryzowane połączenia, które muszą zostać uwierzytelnione. Uwierzytelnieniu podlega na ogół adapter reprezentujący system A wobec serwera RAS. Najprostsze mechanizmy uwierzytelniania (PAP, CHAP) wykorzystują hasła. 
[![Bsk-m6-01-16.png](https://wazniak.mimuw.edu.pl/images/d/d5/Bsk-m6-01-16.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-16.png>)
**Rysunek 16. Schemat uwierzytelniania przy zdalnym dostępie**
#### PAP (_PPP Authentication Protocol_) RFC1334
W protokole PAP, serwer RAS pyta o nazwę (ID) użytkownika, a następnie o hasło i na tej podstawie decyduje o dopuszczeniu do sieci. W tym protokole nazwa użytkownika i hasło są przesyłane tekstem jawnym! Istnieje też odmiana tego protokołu – SPAP (Shiva PAP), która stosuje proste szyfrowanie procedury uwierzytelniania. 
[![Bsk-m6-01-17.png](https://wazniak.mimuw.edu.pl/images/9/94/Bsk-m6-01-17.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-17.png>)
**Rysunek 17. Schemat uwierzytelniania PAP**
#### CHAP (_Challenge Handshake Authentication Protocol_) RFC1994
W przypadku tego protokołu, RAS pyta o ID użytkownika, a następnie przesyła unikalne „zawołanie”. Klient koduje zapytanie hasłem (MD5) i odsyła jako „odzew” decydujący o dopuszczeniu do sieci. 
[![Bsk-m6-01-18.png](https://wazniak.mimuw.edu.pl/images/8/85/Bsk-m6-01-18.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-18.png>)
**Rysunek 18. Schemat uwierzytelniania CHAP**
#### EAP (_PPP Extensible Authentication Protocol_) RFC2284
W tym przypadku RAS wysyła kilka zapytań do uwierzytelnianego podmiotu, każdorazowo specyfikując typ żądania (np. żądanie hasła lub skrótu MD5). Oferuje tym samym możliwość korzystania z wielu protokołów uwierzytelniania bez potrzeby uprzedniego ich negocjowania. Istnieje tez możliwość dwustronnego uwierzytelniania. 
#### Protokół RADIUS (_Remote Access Dial-In User Service_) – RFC2138
Protokół RADIUS oferuje własności AAA (Authentication + Authorization + Accounting) zdalnego dostępu i pozwala na centralizację zarządzania tymi własnościami. Pozwala na przechowywanie jednej globalnej bazy procedur i informacji uwierzytelniających, i umożliwia utrzymywanie wielu punktów dostępowych wykorzystujących tę globalną konfigurację. Ułatwia to tworzenie złożonych sieci z wieloma serwerami dostępowymi RAS. Serwer RADIUS stanowi centrum uwierzytelniania i kontroli dostępu. Natomiast punkty dostępowe RAS realizują proces uwierzytelniania na podstawie informacji pozyskanych z centralnego serwera RADIUS za pomocą protokołu RADIUS. 
[![Bsk-m6-01-19.png](https://wazniak.mimuw.edu.pl/images/3/37/Bsk-m6-01-19.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-19.png>)
**Rysunek 19. Konfiguracja środowiska RADIUS**
Na podobnej zasadzie działają także protokoły TACACS (_Terminal Access Control – Access Control System_), XTACACS czy TACACS+. 
### Uwierzytelnianie stanowisk infrastruktury sieciowej
Standard IEEE 802.1x umożliwia ochronę infrastruktury sieciowej przed nieautoryzowanym dostępem poprzez centralne uwierzytelnianie poszczególnych stacji sieciowych. Przykładowo przy wykorzystaniu tego standardu przełącznik wymusza uwierzytelnienie nowo wpiętej lub właśnie uruchomionej stacji, zanim rozpocznie przełączanie pakietów przez nią wysyłanych. Do zweryfikowania danych uwierzytelniających może wykorzystać protokoły RADIUS czy TACACS+. 
### Bezpieczny system nazw
W 1999 zaproponowano rozszerzenie DNS o mechanizmy kryptograficznego uwierzytelniania i kontroli integralności (RFC 2535). Zaproponowano dodanie rekordów SIG zawierających podpisy cyfrowe podpisujące zbiory rekordów informacyjnych (RRset). Rolę certyfikacji pełni umieszczenie klucza publicznego w samym zbiorze. Klucz przechowują rekordy nowego typu –DNSkey. Usługa DNSsec również może służyć przechowywaniu samych kluczy publicznych dla innych celów, np. PKI. Niestety wdrożenie DNSsec wciąż napotyka trudności. Przykładowym problemem jest m.in. kwestia pełnego lub częściowego podpisywana zbiorów dla dużych domen, takich jak .com) 
### Narzędzia bezpieczeństwa
Niżej przedstawione zostaną dwa wybrane narzędzia ochrony środowisk sieciowych. 
#### DoS guard
DoS guard jest nazwą osobnego narzędzia lub modułu większej aplikacji zabezpieczającej, realizującego ochronę przed atakami DoS. Funkcje DoS guard posiada większość zapór sieciowych (również osobistych), a także wiele systemów operacyjnych routerów, np. TCPintercept w CiscoIOS lub Finesse (PiX). Niektóre z dostępnych narzędzi są nawet dość zaawansowane, np. SYN defender w Checkpoint Firewall-1 lub SYN cookies w PiX-ach. 
#### Kryptograficzne zabezpieczenie komunikacji
Jednym z najbardziej reprezentatywnych przykładów narzędzia kryptograficznej ochrony komunkacji sieciowej jest protokół SSH – Secure Shell. SSH to protokół szyfrowanej transmisji dedykowanej dla emulacji wirtualnego terminala lecz nie tylko. Protokół SSH obsługuje usługa TCP, której przydzielono port 22. W domyślnej konfiguracji zastępuje telnet, rlogin, rsh, rexec, rcp, ftp. Ponadto umożliwia tunelowanie ruchu (VPN – tryb _port forwarding_). 
Protokół SSH to standard _de facto_. Istnieją jego dwie specyfikacje – SSH1 i SSH2). Dostępnych jest wiele implementacji, w tym darmowych dla większości systemów z rodziny Unix/Linux (Open SSH). Natomiast dla systemów MS Windows, MacOS dostępnych jest wielu klientów protokołu SSH. 
[![Bsk-m6-01-20.png](https://wazniak.mimuw.edu.pl/images/3/31/Bsk-m6-01-20.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m6-01-20.png>)
**Rysunek 20. SSH – wykorzystywane algorytmy krytpograficzne.** Implementacje mogą domyślnie używać inne algorytmy niż wskazane w specyfikacji protokołu (np. OpenSSH). 
SSH oferuje różnorodne metody uwierzytelniania, m.in. tradycyjne – hasłem konta systemu zdalnego, kryptograficzne – zapytanie odzew z kluczem publicznym i prywatnym RSA, czy wykorzystanie zewnętrznych systemów uwierzytelniania, jak Kerberos lub S/Key. Istnieją implementacje wykorzystujące tokeny elektroniczne. 
### Pytania problemowe
  1. W bieżącym module stwierdzono, iż często filtry przetwarzają właściwie tylko pierwszy fragment pakietu ponieważ informacje niezbędne do przeprowadzenia filtracji znajdują właśnie w pierwszym pakiecie. Spróbuj wyjaśnić dlaczego.
  2. Dlaczego akurat usługi r* są szczególnie upodobanym celem ataków TCP spoofing?


---


# 

# Bezpieczeństwo systemów komputerowych - wykład 7:
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Podstawowe problemy bezpieczeństwa systemów operacyjnych](https://wazniak.mimuw.edu.pl/<#Podstawowe_problemy_bezpieczeństwa_systemów_operacyjnych>)
    * [1.1 Uwierzytelnianie](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie>)
      * [1.1.1 Uwierzytelnianie w systemie Unix/Linux](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_w_systemie_Unix/Linux>)
      * [1.1.2 Uwierzytelnianie w systemie MS Windows NT 4.0](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_w_systemie_MS_Windows_NT_4.0>)
      * [1.1.3 Uwierzytelnianie w systemie MS Windows 2000, XP, 2003](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_w_systemie_MS_Windows_2000,_XP,_2003>)
      * [1.1.4 Uwierzytelnianie w systemie Novell NetWare](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie_w_systemie_Novell_NetWare>)
      * [1.1.5 Relacja zaufania](https://wazniak.mimuw.edu.pl/<#Relacja_zaufania>)
    * [1.2 Prawa dostępu do zasobów](https://wazniak.mimuw.edu.pl/<#Prawa_dostępu_do_zasobów>)
    * [1.3 Standard POSIX (_Portable Operating System Interface_) 1003.1](https://wazniak.mimuw.edu.pl/<#Standard_POSIX_\(Portable_Operating_System_Interface\)_1003.1>)
      * [1.3.1 Standard POSIX 1003.1e/1003.2c](https://wazniak.mimuw.edu.pl/<#Standard_POSIX_1003.1e/1003.2c>)
      * [1.3.2 Listy dostępu ACL](https://wazniak.mimuw.edu.pl/<#Listy_dostępu_ACL>)
        * [1.3.2.1 ACL w jądrze Linux](https://wazniak.mimuw.edu.pl/<#ACL_w_jądrze_Linux>)
        * [1.3.2.2 Implementacje ACL w systemie Unix](https://wazniak.mimuw.edu.pl/<#Implementacje_ACL_w_systemie_Unix>)
        * [1.3.2.3 Prawa dostępu ACL w MS Windows](https://wazniak.mimuw.edu.pl/<#Prawa_dostępu_ACL_w_MS_Windows>)
    * [1.4 Uprawnienia specjalne w systemie Unix](https://wazniak.mimuw.edu.pl/<#Uprawnienia_specjalne_w_systemie_Unix>)
      * [1.4.1 Flaga _suid_](https://wazniak.mimuw.edu.pl/<#Flaga_suid>)
      * [1.4.2 Redukcja przywilejów (_privilege reduction_)](https://wazniak.mimuw.edu.pl/<#Redukcja_przywilejów_\(privilege_reduction\)>)
      * [1.4.3 Separacja przywilejów (privilege separation)](https://wazniak.mimuw.edu.pl/<#Separacja_przywilejów_\(privilege_separation\)>)
    * [1.5 Malware](https://wazniak.mimuw.edu.pl/<#Malware>)
      * [1.5.1 Wirusy i inne robactwo](https://wazniak.mimuw.edu.pl/<#Wirusy_i_inne_robactwo>)
      * [1.5.2 Ochrona przed wirusami](https://wazniak.mimuw.edu.pl/<#Ochrona_przed_wirusami>)
    * [1.6 Zamaskowane kanały komunikacji](https://wazniak.mimuw.edu.pl/<#Zamaskowane_kanały_komunikacji>)


## Podstawowe problemy bezpieczeństwa systemów operacyjnych
Bieżący moduł przedstawia wybrane zagadnienia bezpieczeństwa dotyczące systemów operacyjnych. Przedstawione zostaną naruszenia bezpieczeństwa systemu operacyjnego, w tym w szczególności typowe formy ataku na system operacyjny oraz komponenty systemu szczególnie podatne na ataki. Omówione zostaną również problemy uwierzytelniania i kontroli dostępu, zagadnienia ochrony antywirusowej oraz zagrożenia związane z zamaskowanymi kanałami komunikacyjnymi. 
Naruszenia bezpieczeństwa systemu operacyjnego przybierają różne formy. Typowo związane są z nimi następujące zagrożenia: 
  * włamania i kradzieże danych
  * destrukcja systemu operacyjnego lub jego komponentów czy aplikacji
  * wykorzystanie systemu operacyjnego do realizacji ataku na inny cel (jako _zombie_)


Różne formy ataku posiadają zwykle nieco odmienne realizacje (przebieg), jednak można wyróżnić pewien ogólny scenariusz ataku na system operacyjny. Obejmuje on zwykle następujące kroki: 
  1. zlokalizowanie systemu do zaatakowania
  2. wtargnięcie na konto legalnego użytkownika (wykorzystując brak hasła, złamanie łatwego hasła, podsłuchanie hasła)
  3. wykorzystanie błędów i luk w komponentach systemu lub w ich konfiguracji w celu uzyskania dostępu do konta uprzywilejowanego
  4. wykonanie nieuprawnionych działań
  5. zainstalowanie furtki dla bieżącego lub przyszłego wykorzystania
  6. zatarcie śladów działalności (usunięcie zapisów z rejestrów systemowych)
  7. ataki na inne komputery


Przyczyny naruszeń bezpieczeństwa tkwią najczęściej w trudności osiągnięcia pełnej kontroli nad poprawnością implementacji i konfiguracji tak złożonego i wielokomponentowego oprogramowania, jakim są współczesne systemy operacyjne. Zwykle trudności te powodują: 
  * błędy i luki bezpieczeństwa („dziury”) w komponentach systemu lub w ich konfiguracji
  * furtki (ang. _backdoor_)
  * konie trojańskie
  * wirusy oraz bomby logiczne i czasowe


Jako konkretne przykłady najczęstszych obszarów błędów implementacyjnych możemy wymienić chociażby sieciowe komponenty systemu, np.: 
  * stos TCP/IP 
    * przykładem może być atak Bonk na implementację stosu protokołów TCP/IP firmy Microsoft, który może spowodować awarię systemu zaatakowanego komputera
  * lub NetBIOS: 
    * WinNuke – atak umożliwiający wywołanie awarii starszych wersji systemu Windows przy użyciu usług systemu NetBIOS
  * albo RPC: 
    * RDS_Shell – metoda wykorzystania składnika Remote Data Services, należącego do MDAC (Microsoft Data Access Components), umożliwiająca zdalnemu napastnikowi uruchamianie poleceń z uprawnieniami systemowymi


Wrażliwe usługi systemowe i narzędziowe nie ograniczają się oczywiście do wymienionych wyżej przypadków i obejmują szerokim kręgiem m.in. usługi informacyjne (jak netstat, systat, nbtstat, finger, rusers, showmount, ident), usługi konfiguracyjne (bootparam, dhcp, zdalne zarządzanie), zdalne wywołanie procdur RPC (rpcinfo, rexec), rozproszone systemy plików (np. NFS), usługi zdalnego dostępu, mechanizm domen zaufania czy usługi komunikacyjne i pocztowe 
W rożnych systemach operacyjnych, a nawet w różnych ich wersjach, można zaobserwować różną podatność komponentów na poszczególne rodzaje ataków. W wielu przypadkach istnieją gotowe i łatwo dostępne narzędzia ataków skierowane na wybrane wersje systemu lub jego konkretnych komponentów. Skuteczne przeprowadzenie ataku staje się rzeczą relatywnie prostą i nie wymagającą praktycznie żadnej wiedzy technicznej. Istotna dla tej skuteczności jest niewątpliwie możliwość zdalnej detekcji systemu operacyjnego, jego wersji i dostępnych w nim komponentów (szczególnie sług dostępnych zdalnie). 
<http://www.insecure.org/nmap/nmap-fingerprinting-article.html>
Metody rozpoznawania systemu możemy podzielić na aktywne i pasywne. Metody aktywne realizowane są poprzez inicjowanie a następnie analizowanie połączeń (na ogół specjalnie spreparowanych) i są wobec tego skierowane wobec konkretnych stanowisk. Natomiast pasywne metody realizowane są poprzez podsłuch pakietów pochodzących z analizowanego systemu. Metody pasywne są naturalnie dużo mniej precyzyjne niż aktywne, lecz są trudno wykrywalne i mogą być skierowane przeciw celom jeszcze nie określonym ostatecznie (np. całej sieci). 
Do zdalnego rozpoznawania systemu operacyjnego najczęściej wykorzystywane są usługi informacyjne dostępne w rozpoznawanym systemie oraz implementacje stosu TCP/IP. 
Usługi informacyjne, jak np. ident oferują typowo charakterystyczne powitanie (_banner_), choć nie tylko informacyjne: dobrym przykładem może być serwer usługi pocztowej sendmail. Powitanie bardzo często zawiera informacje o typie i dokładnej wersji systemu operacyjnego, wersji usługi (co też istotnie przyczynia się do wyboru skutecznego narzędzia ataku). Szczęśliwie problem powitań jest już dobrze znany i coraz więcej usług stara się unikać publicznego podawania newralgicznych informacji o systemie. Z tych też powodów, często świadomie rezygnuje się z oferowania takich nadmiernie „gadatliwych” usług lub ogranicza się zdalny dostęp do nich. Osobnym sposobem ograniczania zagrożenia jest kamuflaż, polegający na spreparowaniu celowo nieprawdziwych informacji w powitaniu, co nie jest niestety gwarancją ochrony systemu przed wprawnym intruzem, jednak może utrudnić i wydłużyć realizację ataku (_security trough obscurity_). 
W przypadku stosu TCP/IP najskuteczniejszą aktualnie metodą zdiagnozowania typu i wersji systemu okazuje się być analizowanie zachowania protokołu implementacji TCP w przypadku retransmisji – tzw. badanie RTO. Badanie RTO (_Retransmission Time-Out_) jest to pomiar czasów pomiędzy retransmisjami pakietów SYN+ACK w trakcie nawiązywania odpowiednio spreparowanego przez atakującego połączenia. Badanie obejmuje ilość retransmisji i odstępy między nimi, co, jak się okazuje, należy do „cech osobniczych” systemu operacyjnego. Przykładowo system MacOS X wysyła po 5 nieskutecznych retransmisjach segment RST, a systemy Windows i Linux milcząco zamykają wpółotwarte połączenie, różniąc się istotnie liczbą i interwałami retransmisji. 
Również w przypadku tej metody detekcji systemu stosować można kamuflaż. Przykladem zaawansowanego narzędzia do kamuflażu jest łata stealth patch na jądro systemu Linux, która m.in.: 
  * blokuje nieprawidłowe pakiety ACK
  * blokuje pakiety z flagami SYN i FIN
  * blokuje pakiety z niepoprawnymi flagami i kombinacjami flag
  * blokuje pakiety ICMP (za wyjątkiem echo)


Podobną funkcjonalność ma pakiet IP Personality – zestaw łat na jądro Linuksa i iptables, niestety już nierozwijany. 
### Uwierzytelnianie
Jednym z najistotniejszych mechanizmów ochrony systemu operacyjnego jest uwierzytelnianie użytkowników, niezbędne dla określania ich uprawnień oraz zdiagnozowania ewentualnej próby niepowołanego dostępu. 
#### Uwierzytelnianie w systemie Unix/Linux
W większości systemów operacyjnych, również w systemach z rodziny Unix/Linux, podstawowym narzędziem uwierzytelniania jest weryfikacja hasła użytkownika. W tym punkcie przedstawimy najpierw klasyczny mechanizm przechowywania haseł w systemie Unix. 
Działanie klasycznego mechanizmu tworzenia i rejestrowania w systemie Unix hasła przebiega następująco: 
  * użytkownik wybiera 8 znakowe hasło
  * hasło jest zamieniane na 56b ciąg za pomocą 7b kodu ASCII
  * powstały 56b ciąg jest kluczem algorytmu DES
  * e-blok algorytmu DES jest modyfikowany za pomocą 12b wartości – ziarna (ang. salt) ustalanego na ogół na podstawie bieżącego czasu
  * tak zmodyfikowany algorytm DES jest wykonywany na 64b bloku złożonym z samych zer
  * wyjście podaje się na wejście kolejnej iteracji (25 iteracji)
  * 64b wynik transformowany na 11-znaków z alfabetu 64 znakowego (A-Z, a-z, 0-9, ‘.’, ‘/’)


Wynikowa postać hasła jest zapamiętywania w pliku konfiguracyjnym (klasycznie był to _/etc/passwd_) i każdorazowo porównywana przez narzędzie login, rejestrujące sesję użytkownika w systemie, z przetransformowanym hasłem wprowadzanym przez logującego się użytkownika. Jak wiemy, mechanizm haseł jest podatny na problem złamania hasła. W przypadku klasycznego mechanizmu uwierzytelniania metoda przeszukiwania wyczerpującego (_brut-force attack_) może być przykładowo wykonana następująco: 
  * 8 znaków z 36-znakowego alfabetu daje 368 czyli ok. 2,8 biliona kombinacji
  * załóżmy moc obliczeniową o wydajności 6,4 miliona iteracji DES na sekundę
  * 25 iteracji dla każdej kombinacji hasła – 1 milion kombinacji w 4 sek.
  * dowolne hasło zostanie złamane (2,8 biliona kombinacji) w 4 miesiące


Przykład ten, aczkolwiek hipotetyczny, jednak obnaża wyraźnie tempo starzenia się haseł oraz uzmysławia dobitnie konieczność i doniosłość systematycznych zmian hasła dla wszystkich kont w systemie operacyjnym. 
Wobec problemu złamania hasła, we współczesnych systemach z rodziny Unix/Linux stosuje się pewne usprawnienia. Obejmują one dodatkowo ochronę haseł przed ich pozyskaniem (w celu utrudnienia przeszukiwania wyczerpującego oraz wymuszanie odpowiednio wysokiego stopnia skomplikowania hasła (w celu utrudnienia ataku słownikowego). Ochrona haseł przed ich pozyskaniem sprowadza się do ukrycia ich postaci składowanej w systemie haseł poza dostępem zwykłego użytkownika – w przypadku systemu Unix/Linux jest to przeniesienie haseł do oddzielnej lokalizacji (pliku /etc/shadow). Realizuje to albo sam system operacyjny (konkretna dystrybucja), albo oddzielne pakiety, np. shadow-in-a-box, Linux Shadow Password Suite, itp. W praktyce okazuje się, iż czasami nadal możliwe ataki na pliki shadow (wykorzystują głównie luki w usługach, obrazy _core dump_), co umożliwia przechwycenie postaci składowanej haseł i ich późniejsze dekodowanie. Rozwiązaniem skuteczniejszym i bardziej uniwersalnym dla ochrony haseł mogą być zatem centralne bazy katalogowe, np. NIS, NIS+, czy bazy dostępne poprzez protokół LDAP. 
W celu kontroli poziomu trudności haseł stosuje się różnorodne testery jakości haseł uaktywniane w momencie ustawiania nowego hasła przez użytkownika. Często spotykane są np. passwd+ (zastępuje passwd) lub anlpasswd, czy npasswd. 
W bieżących wersjach systemów tej rodziny odchodzi się od wykorzystania algorytmu DES na korzyść silniejszych mechanizmów kryptograficznych i pozwalających wybierać hasła bez górnego limitu znaków (lub z wysokim limitem), np. z wykorzystaniem algorytmów MD5 czy Blowfish. 
#### Uwierzytelnianie w systemie MS Windows NT 4.0
W systemie MS Windows NT 4.0 użytkownik otrzymuje losowo wygenerowany SID (Security ID). Procedura logowania wymaga wywołania przerwania sprzętowego (poprzez kombinację Ctrl-Alt-Del), co ułatwia kontrolę nad poprawnym wywołaniem właściwego programu logującego. Ze względu na złożoną ewolucję systemu Windows, hasła w systemie są przechowywane w różnych postaciach. Niezakodowane hasła, przetwarzane przez system, przechowywane są w zastrzeżonym obszarze LSA (Local Security Authority) rejestru: HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets, dostępnym tylko dla usługi Security Accounts Manager. Od wersji NT 4.0 hasła mogą być również zakodowane (w postaci tzw. hash) funkcją MD5 z ziarnem i z 40b kluczem RSA i przechowywane w rejestrze: HKLM\SAM oraz w zastrzeżonym obszarze systemu plików NTFS: %SYSTEMROOT%\SYSTEM32\CONFIG\SAM. Jednak dla zachowania zgodności wstecz (z linią 9x) obok postaci hash MD5 umieszczane są kopie haseł – LM hash – zakodowane autorskim algorytmem LanMan (z protokołu NT Lan Manager), bez ziarna. Postać ta jest dużo mniej bezpieczna i jej dostępność drastycznie podnosi skuteczność złamania hasła. Na szczęście w systemie Windows przechowywanie postaci LM hash można wyłączyć. Rysunek 1 przedstawia obraz ekranu narzędzia Zasad lokalnych zabezpieczeń, które umożliwia uaktywnienie wyłączenia LM hash – tak, widoczną na ekranie opcję trzeba włączyć, aby postać LM hash nie była tworzona i to dopiero od chwili następnej zmiany hasła (do kiedy to dotychczasowe LM hashe pozostają w systemie). 
[![Bsk-m7-01-1.png](https://wazniak.mimuw.edu.pl/images/5/5f/Bsk-m7-01-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m7-01-1.png>)
**Rysunek 1. Uaktywnienie opcji wyłączenia przechowywania postaci LM hash haseł**
W poprawkach serwisowych SP2 i SP3 do systemu wprowadzono następujące usprawnienia: 
  * opcję _syskey_ (SP2) – postacie hash można zaszyfrować kluczem SYSTEM KEY (128b klucz RSA zamiast klucza 40b) co znacznie utrudnia łamanie haseł (jednak nadal dostępne są gotowe narzędzia wyłuskiwania i łamania haseł, choć bardziej złożone niż uprzednio)
  * filtr słabych haseł Passfilt.dll (SP3)
  * dodatkowe restrykcje 
    * ograniczenia czasowe (pory dnia, data ważności konta)
    * ograniczenia stanowisk logowania
    * limit ilości błędnych uwierzytelnień lub korzystania z nieaktualnego hasła
  * rozszerzenia procedury uwierzytelniania 
    * API opublikowane przez Microsoft umożliwia wykorzystanie inteligentnych kart uwierzytelniających lub biometrii


Niestety ciągle istnieje w module zarządzania hasłami wiele luk i dostępnych jest wiele gotowych narzędzi _exploit_ (wykorzystują uprawnienia administracyjne do importu plików SAM, luki w systemie tworzenia kopii zapasowych systemu RDISK, itp.) 
#### Uwierzytelnianie w systemie MS Windows 2000, XP, 2003
W systemie MS Windows 2000 i jego następcach algorytm uwierzytelniania NTLM został zastąpiony przez Kerberos TGP. Ponadto opcja syskey jest domyślnie włączona, a przechowywanie postaci LM hash jest domyślnie wyłączone. Należy jednak mieć na uwadze, iż w środowiskach heterogenicznych istniejące starsze wersje Windows nie obsługują Kerberosa, stąd mogą nadal wymagać obsługi LM hash, co osłabia bezpieczeństwo całego srodowiska. 
#### Uwierzytelnianie w systemie Novell NetWare
W systemie Novell NetWare stosuje się od wczesnych jego wersji dość wyrafinowaną I powszechnie uważaną za bezpieczną procedurę uwierzytelniania. Wykorzystuje ona mechanizmy kryptograficzne i przebiega w uproszczeniu następująco: 
  * w bazie katalogowej NDS (NetWare Directory Service) przechowywany jest skrót hasła użytkownika z ziarnem (jest nim identyfikator użytkownika) oraz para kluczy RSA
  * najpierw stacja sieciowa uwierzytelnia się w imieniu użytkownika wobec wybranego serwera (NetWare od wersji 4 stosuje SSO) metodą zawołanie-odzew
  * następnie serwer przesyła klucz publiczny NDS (KNDS), a stacja losuje klucz jednorazowy K1, który prześle serwerowi zaszyfrowany kluczem KNDS
  * K1 posłuży serwerowi do bezpiecznego przekazania klucza prywatnego RSA użytkownika
  * stacja przekształca klucz RSA do postaci GQ – Gillou-Quisquater (asymetryczny algorytm uwierzytelniania – NetWare od wersji 4 nie stosuje RSA) i natychmiast usuwa z pamięci hasło wraz z kluczem RSA
  * klucz GQ posłuży do uwierzytelniania użytkownika w dostępie do zasobów sieci


#### Relacja zaufania
Jak wiemy z poprzednich modułów, pewnym ograniczeniem ryzyka pozyskania hasła przez intruza, jest zastosowanie mechanizmu SSO (_Single Sign-On_). Systemy Unix/Linux i Windows (w konfiguracji domenowej, od wersji NT Advanced Server) pozwalają wykorzystać mechanizm SSO w postaci tzw. **relacji zaufania**. Dzięki jej istnieniu uwierzytelniony użytkownik systemu (domeny) **zaufanego** może mieć dostęp do zasobów systemu **ufającego** bez konieczności ponownego uwierzytelniania. A wobec tego, hasło nie zostaje ponownie przesyłane ani przetwarzane przy zdalnym dostępie do kolejnego systemu operacyjnego. Relacje zaufania mogą mieć charakter jednostronny lub dwustronny i, co ważne, nie są przechodnie. 
### Prawa dostępu do zasobów
### Standard POSIX (_Portable Operating System Interface_) 1003.1
Standard POSIX 1003.1 jest powszechnie wspierany przez współczesne systemy operacyjne. Wymaga on obsługi następujących elementów procesu autoryzacji i kontroli dostępu do zasobów: 
  * prawa: r (read – odczyt), w (write – zapis), x (execute – wykonanie)
  * kategorie użytkowników: u (user – właściciel zasobu), g (group), o (others)
  * dodatkowo prawa Set User Id, Set Group Id, Sticky, znane z systemu Unix.


Niektóre aplikacje oferują własne rozszerzenia tego modelu uprawnień, np. ProFTPD (<http://proftpd.linux.co.uk/>). Również w samych systemach operacyjnych spotyka się rozszerzone implementacje modelu POSIX. Rozszerzenia te obejmują na ogół: 
  * listy kontroli dostępu ACL: np. w systemach AIX, Solaris
  * model ścisłej kontroli dostępu MAC: w systemach Trusted Solaris, Trusted IRIX, Ultrix, HP-UX czy Xenix.


#### Standard POSIX 1003.1e/1003.2c
Ponieważ wcześniejsza wersja tego standardu dobrze odpowiadała w praktyce tylko klasycznym systemom Unix i w wielu nowszych systemach implementowano różnorodne rozszerzenia standardu, zaproponowano nowe wersje standardu. obejmujące m.in.: 
  * mechanizmy ACL, CAP, RBAC, MAC
  * audyt kontroli dostępu


W implementacji nowego standardu prym wiedzie projekt TrustedBSD (<http://www.trustedbsd.org/>) – dla systemu FreeBSD. Dostępne są również implementacje dużej części standardu w systemie Linux z jądrem w wersjach od 2.5.46 (do jądra 2.4 jest łata obsługująca ACL standardowo dystrybuowana np. w SuSE Linux). Standard POSIX 1003.1e/1003.2c wspierają różne systemy plików Ext2, Ext3, IBM JFS, ReiserFS oraz SGI XFS. Dostępne jest też wsparcie NFS – w wersji NFSv3 możliwe jest przekazywanie list ACL (chociaż brak specyfikacji metody przekazywania skutkuje różnymi implementacjami), a wersja NFSv4 posiada mechanizm NFS ACL, lecz niestety niezgodny z POSIX. Istotne jest zachowanie wymagań standardu również w przypadku takich operacji na zasobach jak archiwizacja i tworzenie kopii zapasowych – tu popularne jest chociażby narzędzie pax (_portable archive interchange_), które zachowuje wszystkie wymagane standardem parametry. 
#### Listy dostępu ACL
Listy ACL są w praktyce dostępne we wszystkich popularnych współcześnie systemach. 
##### ACL w jądrze Linux
System Linux obsługuje dwa rodzaje uprawnień ACL: 
  * _minimal_ ACL – prawa r w x dla u g o
  * _extended_ ACL – rozszerzone prawa i maski praw


Rysunek 2 przedstawia kombinację uprawnień do zasobu KATALOG1 dla użytkownika joe należącego do grupy students. Prawa efektywne są wyznaczane za pomącą algorytmu opisanego niżej. Uprawnienia defaults określają maskę dziedziczenia uprawnień w głąb – ustawianą tylko dla katalogów i dotyczącą tylko nowotworzonych obiektów. 
[![Bsk-m7-01-2.png](https://wazniak.mimuw.edu.pl/images/9/9d/Bsk-m7-01-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m7-01-2.png>)
**Rysunek 2. Schemat wyznaczania uprawnień mechanizmu ACL w systemie Linux**
Rysunek 3 przedstawia przykład wykorzystania narzędzi systemu Linux operujących na uprawnieniach extended ACL. Są to polecenia _getfacl_ i _setfacl_. 
[![Bsk-m7-01-3.png](https://wazniak.mimuw.edu.pl/images/2/21/Bsk-m7-01-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m7-01-3.png>)
**Rysunek 3. Przykładowe wywołanie poleceń _getfacl_ i _setfacl_ w systemie Linux**
System operacyjny weryfikuje po kolei kategorie uprawnionych podmiotów (właściciel zasobu, grupa, wyróżnieni użytkownicy), aby określić, do której kategorii należy podmiot żądający zasobu i jakie prawa z listy ACL należy zaaplikować. Kolejność weryfikacji kategorii uprawnień w celu określenia praw z listy ACL jest następująca: 
  1. właściciel zasobu (_**u** ser_)
  2. wyszczególniony użytkownik (filtrowane przez maskę)
  3. grupa zdefiniowana (jeśli zawiera żądane prawa filtrowane przez maskę)
  4. dowolna z wyszczególnionych grup (jeśli zawiera żądane prawa filtrowane przez maskę)
  5. jeśli żadna dopasowana grupa nie zawiera praw – żądanie jest odrzucane
  6. pozostali użytkownicy (_**o** thers_) bez maski


##### Implementacje ACL w systemie Unix
W systemach z rodziny Unix, listy ACL mogą być przechowywane na różne sposoby. Zwykle definicje ACL przechowuje: 
  * węzeł przysłonięty (_shadow inode_) – wiele i-węzłów może być związanych z tym samym węzłem przysłoniętym (Solaris UFS file system)
  * rozszerzone atrybuty EA obiektów (_Extended Attributes_) – są to struktury informacyjne związane z plikami i in. obiektami w systemie (Linux)


Maksymalna ilość pozycji możliwych do przechowania na liście ACL zależy oczywiście od miejsca przechowywania. Ilość tę dla wybranych systemów plików przedstawia rysunek 4. 
[![Bsk-m7-01-4.png](https://wazniak.mimuw.edu.pl/images/e/e7/Bsk-m7-01-4.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m7-01-4.png>)
**Rysunek 4. Przykładowe wywołanie poleceń _getfacl_ i _setfacl_ w systemie Linux**
##### Prawa dostępu ACL w MS Windows
W systemie Windows wprowadzono mechanizm ACL (odbiegający od POSIX) w systemie plików NTFS. Lista możliwych praw i kategorii uprawnionych podmiotów jest imponująco duża. Wśród ciekawych praw można znaleźć takie atrybuty jak np. append, delete, change permissions, take ownership, change ownership, i in. (istnieją podobne atrybuty dla niektórych systemów plików z rodziny Unix, np. w systemie Linux narzędzie _chattr_ oferuje takie atrybuty dla systemu plików Ext2/Ext3). Dzięki oddzielnie stosowanym przypisaniom GRANT i unieważnieniom DENY praw możliwa jest do osiągnięcia duża elastyczność konfiguracji uprawnień. W definicji uprawnień na liście można wykorzystywać statyczne oraz dynamiczne grupy użytkowników (np. _All Authenticated Users_). Ponadto Windows oferuje dla ACL wsparcie protokołu CIFS (_Common Internet File System_) umożliwiając tym samym tworzenie rozproszonych systemów plików uwzględniających definicje ACL. Z kolei niezależny pakiet Samba dostępny dla systemu Linux, będący implementacją wcześniejszego protokołu współdzielenia zasobów w Windows – SMB, oferuje listy ACL zgodne z POSIX. 
### Uprawnienia specjalne w systemie Unix
#### Flaga _suid_
W systemach z rodziny Unix wykorzystuwana jest często flaga _suid = Set User Id_ oznaczająca specjalne uprawnienie do przejmowania przez proces (uruchomiony z programu z takim atrybutem) praw dostępu zdefiniowanych dla właściciela tego programu. Mechanizm ten jest w niektórych sytuacjach niezbędny do poprawnej pracy systemu, korzystają z niego takie programy narzędziowe jak np. _passwd_. 
Niestety, mechanizm ten może stanowić potencjalne zagrożenie dla bezpieczeństwa systemu operacyjnego, zwłaszcza jeśli właścicielem programu z flagą suid jest administrator. Często spotykany atak polega na wyszukiwaniu programów z atrybutem _suid_ należących do superużytkownika _root_ , w celu wykorzystania błędów lub nieodpowiedniej konfiguracji systemu i uzyskania uprawnień administracyjnych. Zatem programy z ustawionym bitem suid powinny być szczególnie chronione. 
Podobny mechanizm, o podobnym zagrożeniu, wprowadzono również dla grupy – flaga _sgid = Set Group Id_. 
#### Redukcja przywilejów (_privilege reduction_)
Procesy uruchomione z podwyższonymi uprawnieniami (głównie administracyjnymi) stanowią łakomy kąsek dla intruza. Jest to szczególnie istotne w systemie Unix, gdzie przewidziano jedno konto administracyjne – superużytkownika _root_ , które umożliwia wykonanie praktycznie wszelkich działań w systemie. 
Jednak w większości przypadków, nawet ważne dla systemu procesy wymagają wysokich uprawnień tylko przez krótki okres czasu (zwykle początkowy). Koncepcja redukcji przywilejów sprowadza się do ograniczania zagrożenia przejęcia uprawnień procesu mogącego stać się potencjalnym celem ataku. Ograniczenie zagrożenia osiągane jest poprzez świadomą rezygnację z wyższych uprawnień (administracyjnych) natychmiast gdy newralgiczne operacje zostaną przez proces zakończone. W czasie dalszej pracy proces działa z niskimi (możliwie najniższymi) uprawnieniami. 
Innym sposobem ograniczenia zagrożenia, jest wyodrębnienie wielu szczegółowych uprawnień administracyjnych i przydzielanie do procesu tylko niezbędnych, zamiast wszechwładnego prawa superużytkownika. Standard POSIX przewiduje taki mechanizm nazywany capabilities (CAP), dostępny w systemie Linux od jądra 2.2 (<ftp://linux.kernel.org/pub/linux/libs/security/linux-privs>). CAP pozwala na rozdzielenie uprawnień administracyjnych superużytkownika root na zbiór szczegółowych uprawnień i powiązanie ich z systemem plików poprzez dodatkowe bity praw dostępu. 
Popularną implementacją mechanizmu CAP w systemie Linux jest narzędzie LCAP (<http://pweb.netcom.com/~spoon/lcap/>). Oferuje on m.in. następujące uprawnienia szczegółowe: 
  * administrowanie modułami jądra
  * administrowanie siecią
  * dowiązywanie do gniazd numerów portów zarezerwowanych dla serwisów systemowych
  * realizacja komunikacji rozgłoszeniowej i grupowej w sieci
  * omijanie ograniczeń dotyczących kontroli dostępu do plików
  * zmiana informacji o właścicielu i grupie plików
  * kontrola plików specjalnego rodzaju
  * kontrola flag _suid_ oraz _sgid_
  * omijanie ograniczeń dotyczących wysyłania sygnałów do procesów
  * blokowanie stron w pamięci fizycznej
  * omijanie limitów zasobowych


#### Separacja przywilejów (privilege separation)
Kolejnym sposobem ograniczania zagrożeń związanych z nadużyciem praw dostępu jest separacja przywilejów posiadanych przez uruchomiony proces. Koncepcja separacji przywilejów polega na wyodrębnieniu zadań wymagających wysokich uprawnień w postaci odrębnego procesu. Błędy w programie procesu głównego, działającego z uprawnieniami zwykłego użytkownika, nie umożliwiają już tak łatwego uzyskania wysokich uprawnień. Istotne jest, iż ta koncepcja nadaje również się do systemów z klasycznym przydziałem uprawnień administracyjnych (bez CAP). Przykład sztandarowy wykorzystania separacji przywilejów to m.in. OpenSSH. 
### Malware
Pod pojęciem _malware_ należy rozumieć wszelkie niepożądane (złośliwe) w systemie oprogramowanie, którego pojawienie się w systemie było niezamierzone i działanie jego przynosi systemowi wymierne straty. Infekcje systemu operacyjnego mogą być spowodowane różnymi typami oprogramowania malware, do którego należą: 
  * wirusy
  * konie trojańskie
  * spyware
  * dialery


Poniżej zajmiemy się przedstawieniem pierwszej klasy oprogramowania malware – wirusami. 
#### Wirusy i inne robactwo
Wirus (łac. _virus_ – trucizna) to – najprościej definiując – kod samopowielający się w systemie operacyjnym. Istnieje wiele bardzo odmiennych rodzajów wirusów w tym w szczególności tak specyficzne jak: 
  * wirusy skryptowe i w makrodefinicjach (np. w dokumentach edytorów tekstu)
  * wirusy sieciowe (_worms_) – przenoszone poprzez sieć (uruchamiane lokalnie)
  * wirusy w poczcie elektronicznej (przesyłane jako załączniki)
  * wirusy atakujące programy pocztowe (np. Win.Redteam), które przenoszą się tradycyjnie (przez system operacyjny), a jako ofiary wybierają klientów poczty elektronicznej (np. Eudorę) – zarażają klienta, wykonując makrodefinicje i rozsyłając się do wszystkich osób z listy adresowej.
  * wirusy bujdy (hoax-viruses) – udające ostrzeżenia zwykłe żarty rozpowszechniane pocztą elektroniczną (często przez nieświadomych użytkowników).


Efekty działania wirusów to najczęściej: 
  * utrudnienie pracy systemu (zużywanie zasobów: CPU, pamięci, przestrzeni dyskowej, pasma sieci)
  * destrukcja danych
  * wyciek danych na zewnątrz (np. poprzez zamaskowany kanał komunikacyjny).


Obserwacja ewolucji oprogramowania wirusowego w ostatnich latach skłania do wyróżnienia pewnych trendów. Można przykładowo wybrać następujące obserwacje: 
  * 2002 r.: pojawiają się pierwsze wirusy wieloplatformowe, atakujące pliki wykonywalne w popularnych formatach zarówno exe (MS Windows) oraz elf (Linux)
  * 2003 r.: wirusy typu _blended threats_ – łączą cechy różnych klas: wirusów, koni trojańskich, robaków sieciowych (np. MS Blaster)
  * 2004 r.: ataki na systemy wbudowane: np. wirus nazwany Ratter atakujący Windows CE, wirus Cabir atakujący telefony komórkowe z systemem Symbian
  * 2005 r.: wzmaga się aktywność wirusowa w systemach wbudowanych – pojawił się Lasco, wirus telefonów komórkowych z możliwością infekowania plików (od 2005 McAfee i TrendMicro oferują antywirusy dla systemów mobilnych)


W oprogramowaniu wirusowym pojawiają się zaawansowane mechanizmy, takie jak kamuflaż i techniki anty-antywirusowe: 
  * polimorfizm
  * metamorfizm
  * maskowanie (_stealth_) oraz opancerzenie (_armor_) – techniki różnorodnej ochrony kodu, np. uniemożliwienie debugowania.


Wzmaga się aktywność retrowirusów stosujących obronę agresywną przed detekcją, poprzez ataki skierowane przeciw oprogramowaniu antywirusowemu. Najbardziej zaawansowane wirusy sieciowe posiadają strukturę modułową, w której występują moduły zdalnie aktualizowane (przez Internet). 
Oprogramowanie malware może stosować też przeróżne sztuczki w celu ukrycia się w systemie plików i uniemożliwienia skutecznego wyszukania przez oprogramowanie antywirusowe. W tym kontekście ciekawe możliwości oferuje, dotąd mało znany i wykorzystywany mechanizm ADS (_Alternate Data Stream_) w systemie NTFS. Teoretycznie miał on zapewniać wsparcie międzyplatformowe (np. z systemem Macintosh). Jednak istotne z naszego punktu widzenia jest to, iż system Windows w bieżących wersjach pozwala tworzyć pliki (programy) w ADS, choć sam nie zwraca na nie uwagi (nawet ich nie pokazuje), co z kolei pozwala skutecznie ukrywać malware przed użytkownikiem, a nawet przed większością skanerów antywirusowych. 
Nakłady poniesione na usunięcie infekcji i zwalczanie skutków są całkiem pokaźne. Przykładowo wg Computer Economics (2001r.) w roku 1999 osiągnęły w sumie 12,1 mld USD, a w roku 2000 – w sumie 17,1 mld USD. Jedne z najkosztowniejszych pod tym względem wirusów w historii to z pewnością: 
  * Love Bug (łącznie ok. 50 odmian), 2000 r.: 8,7 mld USD
  * Code Red, 2001 r.: 2,6 mld USD
  * Melissa, 1999 r.: 1,2 mld USD
  * Explorer, 1999 r.: 1 mld USD
  * SirCom, 2001 r.: 460 mln USD


#### Ochrona przed wirusami
Ochrona przed wirusami jest realizowana przez różnorodne oprogramowanie nazywane ogólnie antywirusowym, a obejmujące jedną lub kilka z wymienionych poniżej kategorii. 
  * Programy wyszukujące programy zarażone (skanery)


przed ich uruchomieniem 
  *     * wymagające znajomości kodu wirusa 
      * wyszukujące identyfikator wirusa (_fingerprint_)
      * wyszukujące fragment charakterystyczny wirusa
    * nie wymagające znajomości kodu wirusa 
      * stosujące analizę zmian struktury programu


na podstawie efektów 
  *     * metodą "przynęty"
    * poprzez analizę zmian w systemie plików po zakończeniu programu
  * Programy wzbogacające możliwości ochronne systemu 
    * monitory operacji wykonywanych w systemie wyszukujące działania wirusa albo w trakcie instalacji lub powielenia wirusa, albo w trakcie wykonywania zadań 
      * destruktywnych
      * demonstracyjnych
    * skanery usług sieciowych (np. poczty elektronicznej, WWW)
    * system plików zabezpieczony przed zapisem
  * Programy usuwające: 
    * kod wirusa
    * skutki działania wirusa


Poniżej wymienione są przykładowe narzędzia ochrony przed malware. 
  * Zdalne skanery internetowe 
    * <http://skaner.mks.com.pl>
    * <http://hausesall.trendmicro.com>
    * <http://www.bitdefender.com>
    * <http://www.pandasoftware.com/activescan/pol/activatescan_principal.htm>
    * <http://www.kaspersky.pl/serwices.html/s=online_vir_chk>
  * Programy anty-spyware 
    * Ad-aware: <http://www.snapfiles.com/get/adaware.html>
    * Spybot: <http://www.safer-networking.org/pl/download/>
    * Bazooka: <http://www.kephyr.com>
    * SpywareBlaster: <http://javacoolsoftware.com/downloads.html>


### Zamaskowane kanały komunikacji
Zamaskowane kanały komunikacji (_covered channels_) są pojęciem ściśle powiązanym z malware, choć nie ograniczają się wyłącznie do tego przypadku. Poprzez zamaskowany kanał komunikacji (_covered channel_) rozumie się wykorzystanie w celu przekazania informacji takiego mechanizmu systemu operacyjnego, które został opracowany w celu nie związanym z komunikacją i na ogół nie jest z nią w ogóle kojarzony. Kanał ten może być wykorzystywany do nieujawnionego przekazywania wiadomości, tak aby ukryć nie tylko treść tej wiadomości, ale i sam fakt dokonywania transmisji. Przykładami zamaskowanych kanałów komunikacji są: 
  * kanał czasowy (obciążenie systemu) – transmisja bitu następuje poprzez wzmożenie obciążenia systemu w danym kwancie czasu (bit 1) lub obniżenie obciążenia (bit 0)
  * kolejka wydruku (wstawianie do niej i usuwanie określonego zadania wydruku)
  * kanał poprzez tworzenie / usuwanie ogólnodostępnego pliku w systemie plików


---


# 

# Bezpieczeństwo systemów komputerowych - wykład 8:
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Tunele wirtualne VPN](https://wazniak.mimuw.edu.pl/<#Tunele_wirtualne_VPN>)
    * [1.1 Konfiguracje sieci VPN](https://wazniak.mimuw.edu.pl/<#Konfiguracje_sieci_VPN>)
    * [1.2 Protokół IPsec](https://wazniak.mimuw.edu.pl/<#Protokół_IPsec>)
      * [1.2.1 Tryby pracy protokołów IPsec](https://wazniak.mimuw.edu.pl/<#Tryby_pracy_protokołów_IPsec>)
      * [1.2.2 Protokół AH (Authentication Header)](https://wazniak.mimuw.edu.pl/<#Protokół_AH_\(Authentication_Header\)>)
      * [1.2.3 Protokół ESP (Encapsulating Security Payload)](https://wazniak.mimuw.edu.pl/<#Protokół_ESP_\(Encapsulating_Security_Payload\)>)
      * [1.2.4 Asocjacja bezpieczeństwa (_Security Association_)](https://wazniak.mimuw.edu.pl/<#Asocjacja_bezpieczeństwa_\(Security_Association\)>)
      * [1.2.5 Zarządzanie kluczami](https://wazniak.mimuw.edu.pl/<#Zarządzanie_kluczami>)
      * [1.2.6 Protokół IKE (_Internet Key Exchange_)](https://wazniak.mimuw.edu.pl/<#Protokół_IKE_\(Internet_Key_Exchange\)>)
      * [1.2.7 PKI (Public Key Infrastructure)](https://wazniak.mimuw.edu.pl/<#PKI_\(Public_Key_Infrastructure\)>)
      * [1.2.8 Ograniczenia](https://wazniak.mimuw.edu.pl/<#Ograniczenia>)
      * [1.2.9 IPsec w Windows](https://wazniak.mimuw.edu.pl/<#IPsec_w_Windows>)
    * [1.3 Bezpieczeństwo w IPv6](https://wazniak.mimuw.edu.pl/<#Bezpieczeństwo_w_IPv6>)
    * [1.4 Propagowanie połączeń aplikacyjnych (_port forwarding_)](https://wazniak.mimuw.edu.pl/<#Propagowanie_połączeń_aplikacyjnych_\(port_forwarding\)>)
    * [1.5 Tunele SSL](https://wazniak.mimuw.edu.pl/<#Tunele_SSL>)
    * [1.6 Pytania problemowe](https://wazniak.mimuw.edu.pl/<#Pytania_problemowe>)


## Tunele wirtualne VPN
Tunel wirtualny (_Virtual Private Network_ , VPN) jest to kanał komunikacyjny chroniony przez niepowołanym dostępem (odczytem i modyfikacją) poprzez zastosowanie kryptografii. Tunel wirtualny VPN umożliwia chronioną transmisję w obszarze publicznej sieci rozległej, np. w celu realizacji bezpiecznego połączenia pomiędzy różnymi jednostkami, najczęściej geograficznie odległymi (rysunek 1). W sieci publicznej należy się liczyć z potencjalnymi naruszeniami poufności, integralności i autentyczności transmitowanych danych. Poznane we wcześniejszych modułach mechanizmy kryptograficzne umożliwiają skuteczną ochronę wszystkich tych własności informacji. 
[![Bsk-m8-01-1.png](https://wazniak.mimuw.edu.pl/images/2/2b/Bsk-m8-01-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-1.png>)
**Rysunek 1. Schemat sieci publicznej analizowany jako scenariusz zagrożeń**
### Konfiguracje sieci VPN
Konfiguracja host-to-host 
W konfiguracji tej końcami tunelu są pojedyncze stanowiska, wyposażone w odpowiednie oprogramowanie lub sprzęt (karty sieciowe) umożliwiające szyfrowanie i deszyfrowanie transmisji pomiędzy nimi. 
[![Bsk-m8-01-2.png](https://wazniak.mimuw.edu.pl/images/9/91/Bsk-m8-01-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-2.png>)
**Rysunek 2. Konfiguracja host-to-host**
Konfiguracja net-to-net 
W konfiguracji tej końcami tunelu są pojedyncze węzły międzysieciowe (np. dedykowane urządzenia szyfrujące, routery brzegowe z modułami kryptograficznymi). Mogą one szyfrować całą transmisję wychodzącą ze swoich sieci lokalnych lub wybrany ruch sieciowy. Transmisja odbywająca się wewnątrz poszczególnych sieci nie jest szyfrowana. 
[![Bsk-m8-01-3.png](https://wazniak.mimuw.edu.pl/images/2/2f/Bsk-m8-01-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-3.png>)
**Rysunek 3. Konfiguracja net-to-net**
Konfiguracja host-to-net 
W konfiguracji tej jednym z końców tunelu jest pojedyncze stanowisko, które uzyskuje dostęp do zasobów pewnej sieci lokalnej (np. korporacyjnej). Cała komunikacja lub wybrany ruch (wybrane usługi) poddawane są szyfrowaniu. Jest to model typowy dla środowisk pracy zdalnej. 
[![Bsk-m8-01-4.png](https://wazniak.mimuw.edu.pl/images/7/75/Bsk-m8-01-4.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-4.png>)
**Rysunek 4. Konfiguracja host-to-net**
### Protokół IPsec
Jak wiemy w protokole IPv4 brak praktycznie jakichkolwiek mechanizmów bezpieczeństwa. W związku z rosnącymi wymagani bezpieczeństwa, w 1995 r. przedstawiono (IETF) pierwszą wersję specyfikacji protokołu sieciowego IPsec (RFC 1825), zawierającego dwie składowe 
  * Authentication Header (AH) – protokół nr 51
  * Encapsulating Security Payload (ESP) – protokół nr 50


Zadaniem protokołu IPsec operującego w warstwie sieciowej jest transparentne dla aplikacji wykorzystanie narzędzi kryptograficznych w celu osiągnięcia 
  * integralności – poprzez funkcje protokołu AH
  * poufności – poprzez funkcje protokołu ESP


Jednak wkrótce rozszerzono funkcje ESP o ochronę również integralności. W efekcie funkcje ochrony integralności zostały powielone w obu składowych protokołu IPsec. Dlaczego zatem utrzymano oddzielne składniki AH i ESP? Z jednej strony przemawiają za tym trudności merytoryczne, zrozumiałe w tak złożonym projekcie jak ESP. Ponadto przemawiały pierwotnie za tym ograniczenia natury polityczno-prawnej, związane ze stosowaniem kryptografii – AH wykorzystując wyłącznie kryptograficzne funkcje skrótu, z reguły był traktowany bardziej liberalnie. Ostatecznie jednak należy przyznać, iż funkcjonalność AH wystarcza w wielu zastosowaniach, np. w przypadku ochrony usługi DNS, gdzie informacje udostępniane przez tę usługę są z reguły publiczne i nie ma potrzeby ich szyfrowania, ważne jest natomiast by nie zostały one po drodze sfałszowane. 
Ostateczna wersja IPsec (RFC 2401, 1998 r.) obejmuje zatem specyfikacje dwu protokołów: 
<http://www.ipsec.pl/>
  * AH (Authentication Header, RFC 2402) 
    * który realizuje kontrolę integralności i autentyczności datagramu IP oraz umożliwia uwierzytelnianie
  * ESP (Encapsulating Security Payload, RFC 2406) 
    * który zapewnia integralność i poufność treści datagramu


Uwierzytelnianie stron jest realizowane do pewnego stopnia przez sam protokół IPsec i może być rozszerzane przez dodatkowe mechanizmy. 
#### Tryby pracy protokołów IPsec
Tryb transportowy (_transport mode_), inaczej nazywany bezpośrednim, charakteryzuje się tym, że do datagramu dodany jest nagłówek AH / ESP i dane datagramu (ramka TCP, UDP, ICMP, ...) zostają zabezpieczone (podpisane / zaszyfrowane) bezpośrednio za nim. 
[![Bsk-m8-01-5.png](https://wazniak.mimuw.edu.pl/images/9/9b/Bsk-m8-01-5.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-5.png>)
**Rysunek 5. Postać chronionego datagramu w trybie transportowym**
W trybie tunelowym (_tunnel mode_) natomiast oryginalny datagram IP zostanie zabezpieczony (podpisany / zaszyfrowany) w całości z nagłówkiem w ramkę protokołu AH / ESP, a następnie umieszczony w niezabezpieczonym datagramie IP jako jego dane. 
[![Bsk-m8-01-6.png](https://wazniak.mimuw.edu.pl/images/4/47/Bsk-m8-01-6.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-6.png>)
**Rysunek 6. Postać chronionego datagramu w trybie tunelowym**
#### Protokół AH (Authentication Header)
Protokół AH przenosi wartość jednokierunkowej funkcji skrótu treści datagramu oraz stałych pól nagłówka (zarówno w trybie transportowym jak i tunelowym). W tym celu wykorzystywane są funkcje HMAC: MD5, SHA-1, RIPEMD-160 lub inne (negocjowane). Ewentualna fragmentacja datagramu jest dokonywana wcześniej (podpisywany jest każdy fragment oddzielnie). Niezaprzeczalność osiągana jest poprzez silne algorytmy kryptograficzne, np. RSA. 
[![Bsk-m8-01-7.png](https://wazniak.mimuw.edu.pl/images/8/85/Bsk-m8-01-7.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-7.png>)
**Rysunek 7. Schemat budowy datagramu protokołu AH**
#### Protokół ESP (Encapsulating Security Payload)
Protokół ESP Umożliwia podpisywanie datagramu (stosuje te same algorytmy co w AH – uwzględnia w podpisie statyczne pola nagłówka podstawowego IP) oraz zaszyfrowanie datagramu – wykorzystuje szyfry blokowe w trybie CBC, np. DES, 3DES (z 3-ma kluczami), Blowfish, CAST-128 czy Rijndael/AES, aktualnie również 3-IDEA (z 3-ma kluczami). 
Nagłówek ESP jest umieszczany bezpośrednio przed zaszyfrowanymi danymi. Format i długość zaszyfrowanych danych zależy od wybranej metody kryptograficznej. 
[![Bsk-m8-01-8.png](https://wazniak.mimuw.edu.pl/images/8/85/Bsk-m8-01-8.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-8.png>)
**Rysunek 8. Schemat budowy datagramu protokołu ESP**
Możliwe jest połączenie mechanizmów AH i ESP. Przykładowo, najpierw szyfrowane są dane za pomocą ESP, a następnie cały datagram jest zabezpieczony przez AH. Alternatywnie, najpierw wyznacza się nagłówek AH i umieszcza się go datagramie, a następnie szyfruje w całości przez ESP (tuneluje). 
#### Asocjacja bezpieczeństwa (_Security Association_)
Asocjacja bezpieczeństwa SA jest to zbiór parametrów charakteryzujących bezpieczną komunikację między nadawcą a odbiorcą (kontekst), utrzymywany przez nadawcę i unikalnie identyfikowany przez SPI (_Security Parameters Index_). Blok parametrów asocjacji obejmuje następujące dane: 
[![Bsk-m8-01-9.png](https://wazniak.mimuw.edu.pl/images/2/2a/Bsk-m8-01-9.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-9.png>)
Asocjacja bezpieczeństwa (a dokładniej blok parametrów asocjacji) nie jest przesyłana siecią – przesyłany jest tylko numer SPI. Asocjacja bezpieczeństwa jest jednokierunkowa – w łączności obukierunkowej wymagane są dwie asocjacje – daje to dużą elastyczność ruch w każdym kierunku może być szyfrowany innym kluczem i może mieć inny okres ważności. Kanały SA mogą się wzajemnie w sobie zawierać i nie muszą się zaczynać w tych samych miejscach (na tych samych stacjach). 
Poniżej przedstawiony zostanie schemat działania stacji protokołu IPsec. Działania wykonywane przy wysyłaniu pakietu są następujące: 
  1. Sprawdzenie czy i w jaki sposób wychodzący pakiet ma być zabezpieczony: 
    1. sprawdzenie polityki bezpieczeństwa w SPD (_Security Policy Database_)
    2. jeśli polityka bezpieczeństwa każe odrzucić pakiet to pakiet jest odrzucany
    3. jeśli pakiet nie musi być zabezpieczany to jest wysyłany
  2. Ustalenie, które SA powinno być zastosowane do pakietu: 
    1. odszukanie SA w bazie SAD (_SA Database_) lub
    2. nawiązanie odpowiedniego SA jeśli nie jest jeszcze nawiązane
  3. Wykonanie zabezpieczeń wykorzystując algorytmy, parametry i klucze zawarte w SA: 
    1. wynikiem jest stworzenie nagłówka AH lub ESP
    2. dodatkowo może zostać również utworzony nowy nagłówek IP (w trybie tunelowym)
  4. Wysłanie powstałego pakietu IP


Natomiast działania wykonywane przy odbieraniu pakietu są następujące: 
  1. Sprawdzenie nagłówka IPsec: 
    1. odszukanie odpowiedniego SA w SAD na podstawie SPI zawartego w nagłówku
    2. i postępowanie zgodnie z informacjami zawartymi w SA
    3. jeśli SA wskazywany przez SPI nie istnieje, to pakiet jest odrzucany
  2. Sprawdzenie czy i jak pakiet powinien był być zabezpieczony: 
    1. sprawdzenie polityki bezpieczeństwa w SPD
    2. jeśli polityka bezpieczeństwa każe odrzucić pakiet to pakiet jest odrzucany
    3. jeśli zabezpieczenia pakietu nie odpowiadają polityce bezpieczeństwa to pakiet jest odrzucany
    4. jeśli pakiet był zabezpieczony prawidłowo to przekazywany jest wyżej


#### Zarządzanie kluczami
Zarządzanie i dystrybucja kluczy nie są uwzględnione w specyfikacji samego standardu IPsec. Możliwe jest jednak wykorzystanie kluczy dwojakiego typu: 
  * klucze przypisane do użytkownika
  * klucze przypisane do stacji sieciowej


Możliwe są też bardzo różnorodne sposoby dystrybucji: 
  * dystrybucja ręczna – administrator (małej sieci lokalnej) wyznacza wszystkie klucze
  * wykorzystanie istniejących systemów dystrybucji (np. systemu Kerberos)
  * automatyczne – początkowo myślano o DNS jako repozytorium kluczy
  * ostatecznie wprowadzono nowe protokoły i specyfikacje serwerów kluczy (niezależne od IPsec): np. SKIP (Sun), Photuris, IKE (_Internet Key Exchange_)
  * integracja serwerów kluczy z usługami katalogowymi (DNSsec, LDAP)


Protokoły zarządzania kluczami mają na celu wzajemne uwierzytelnianie podmiotów nawiązujących asocjacje IPsec oraz uzgadnianie kluczy sesji na potrzeby poszczególnych kanałów SA. Obie te funkcje realizowane są na podstawie skonfigurowanych na stałe danych uwierzytelniających. Może to być np. hasło wspólne dla pary stacji (_shared secret_), certyfikaty X.509, klucze PGP. Niektóre implementacje (SKIP, Photuris) umożliwiają wyłącznie uwierzytelnienie na podstawie haseł, a popularny protokół IKE obsługuje natomiast wszystkie wyżej wymienione metody i umożliwia jeszcze prywatne rozszerzenia. 
#### Protokół IKE (_Internet Key Exchange_)
Protokół IKE obejmuje 2 składniki: 
  * ISAKMP (_Internet Security Association and Key Management Protocol_) – faktyczny protokół negocjacji parametrów IPSec
  * Oakley – kryptograficzny protokół wymiany kluczy za pomocą algorytmu Diffiego-Hellmana


ISAKMP (RFC 2408) stanowi trzon całości i z tego powodu nazwy tej używa się niekiedy zamiennie z IKE. Protokół ISAKMP korzysta z UDP (port 500). 
Wymiana kluczy następuje dwuetapowo: najpierw ustalana jest tożsamość komunikujących się węzłów i tworzony jest bezpieczny kanał (tzw. ISAKMP SA), utrzymywany przez cały czas trwania sesji i służący następnie do właściwej negocjacji parametrów asocjacji. Negocjacja obejmuje m.in. listę obsługiwanych algorytmów szyfrujących, co ułatwia obsługę środowisk heterogenicznych. 
Uwierzytelnianie może być realizowane na ogół na dwa sposoby. W najprostszym przypadku każda para węzłów musi mieć ustalone wspólne hasło, które służy do obliczania kluczy metodą Diffiego-Hellmana. Oznacza to konieczność konfigurowania haseł na wszystkich węzłach, co jest istotnym ograniczeniem tej metody i może okazać się zbyt pracochłonne w przypadku dużych sieci. Alternatywną metodą jest zastosowanie kluczy publicznych podpisanych przez nadrzędny urząd certyfikujący CA (np. certyfikatów X.509), które jest wolne od ograniczeń ręcznej definicji haseł. 
protokół ISAKMP jest łatwo rozszerzalny. Pewne parametry (_Domain of Interpretation_ , DOI) można przystosować całkowicie do potrzeb własnej instytucji: 
  * własny zestaw szyfrów
  * własne mechanizmy uwierzytelnienia


#### PKI (Public Key Infrastructure)
Protokół IKE pozwala wykorzystać możliwości PKI. Po nawiązaniu komunikacji, ale przed uzgodnieniem ISAKMP SA węzeł może zweryfikować autentyczność certyfikatu drugiej strony dzięki podpisowi CA. W skrajnym przypadku węzeł nie musi wiedzieć nic o innych węzłach z którymi będzie się łączył, lub które będą się łączyć z nim. Wymaga to jedynie lokalnego dostępu (zainstalowania w tym węźle) klucza publicznego urzędu CA – będzie to jeden i ten sam klucz na wszystkich węzłach. Znacznie ułatwia to realizację złożonych topologii. 
Co istotne, IKE umożliwia też automatyczną renegocjację kluczy kryptograficznych co określony interwał (nawet często). W takim przypadku, w razie złamania bieżącego klucza, dane zaszyfrowane poprzednimi kluczami nie są narażone. Cecha ta, określana jako _Perfect Forward Security_ , chroni przed sytuacją gdy atakujący zapisuje wszystkie przechwycone w przeszłości dane w nadziei, że kiedyś uda mu się zdobyć klucz do ich rozszyfrowania. Implementacja obligowana jest by w przypadku renegocjacji klucza poprzedni klucz był usuwany z pamięci. Wówczas włamywacz nie znajdzie go w systemie nawet w przypadku opanowania systemu operacyjnego węzła. 
#### Ograniczenia
Protokół IPsec dobrze nadaje się do realizacji tuneli wirtualnych VPN. Jednak nie jest idealnym rozwiązaniem problemu bezpiecznej komunikacji. Praktycznie od początku był IPsec krytykowany za niekonsekwencje projektowe i nadmierne skomplikowanie. Wytykano, iż np. ochrona integralności zapewniana jest niemal w równym stopniu przez ESP, jak i AH. Niektóre odkryte błędy zostały usunięte w wersji z 1998 r. (np. część potencjalnych furtek do ataków DoS). Gwoli ścisłości należy zaznaczyć, iż zdiagnozowane usterki nie mają raczej charakteru otwartych dziur, grożących złamaniem bezpieczeństwa sieci, ale są za to dość liczne i ułatwiają powstawanie potencjalnych słabości w samych implementacjach. 
Mimo tego jednak, IPsec jest wykorzystywany powszechnie i praktycznie nie ma dla niego alternatywy. Jako reprezentatywną opinię można przytoczyć tu podsumowanie analizy IPsec dokonanej w 1999 r. przez znanych kryptologów Nielsa Fergussona i Bruce’a Schneiera: 
_,,Nawet pomimo dość poważnych zarzutów jakie wysunęliśmy wobec IPSec, jest on prawdopodobnie najlepszym protokołem bezpieczeństwa z obecnie dostępnych._ W przeszłości przeprowadziliśmy podobne analizy innych protokołów o analogicznym przeznaczeniu (w tym PPTP). Żaden ze zbadanych protokołów nie spełnił swojego celu, ale IPSec zbliżył się do niego najbliżej. (...) Mamy ambiwalentne odczucia wobec IPSec. Z jednej strony IPSec jest znacznie lepszy niż jakikolwiek protokół bezpieczeństwa IP stworzony w ostatnich latach: Microsoft PPTP, L2TP itp. Z drugiej strony nie wydaje nam się, by zaowocował on kiedykolwiek stworzeniem w pełni bezpiecznego systemu.” 
#### IPsec w Windows
W Windows 2000 i XP wbudowano obsługę IPsec (ESP) zintegrowaną z usługą Active Directory. Sam IPsec tuneluje tylko ruch IP. 
[![Bsk-m8-01-10.png](https://wazniak.mimuw.edu.pl/images/5/5f/Bsk-m8-01-10.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-10.png>)
**Rysunek 9. Uaktywnienie obsługi protokołu IPsec w Windows**
[![Bsk-m8-01-10-2.png](https://wazniak.mimuw.edu.pl/images/2/2f/Bsk-m8-01-10-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-10-2.png>)
**Rysunek 10. Przykład definicji tunelowania ruchu IP**
[![Bsk-m8-01-11.png](https://wazniak.mimuw.edu.pl/images/0/01/Bsk-m8-01-11.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-11.png>)
**Rysunek 11. Szczegóły definicji tunelowania ruchu (zmienne parametry SA)**
### Bezpieczeństwo w IPv6
Uzupełniając wiadomości o protokole IPsec, należy dodać, iż jest on zintegrowaną częścią specyfikacji protokołu IP w wersji 6. Zatem w protokole IPv6 możliwe jest korzystanie z nagłówków AH i ESP jak z dowolnych innych opcji protokołu. 
### Propagowanie połączeń aplikacyjnych (_port forwarding_)
Aczkolwiek najbardziej uniwersalny tunel wirtualny osiągnąć można na poziomie warstwy sieciowej, to jednak mechanizmy kryptograficznej ochrony komunikacji można zaprząc do pracy w innych warstwach. 
Szyfrowane propagowanie połączeń jest metodą realizacji tuneli wirtualnych na poziomie warstwy aplikacji. Oferuje je np. protokół SSH. Działanie mechanizmu propagowanie połączeń można przedstawić następująco (rysunek 12). 
  * połączenia na port **A bramy 1 są** tunelowane **do bramy 2**
  * i dalej propagowane na port **S serwera** w sieci lokalnej za **bramą 2**
  * tunel między **bramą 1** a **bramą 2** jest szyfrowany
  * komunikacja poza tunelem (w obu sieciach lokalnych – czyli od klienta do **bramy 1** oraz od **bramy 2** do serwera nie jest szyfrowana


[![Bsk-m8-01-12.png](https://wazniak.mimuw.edu.pl/images/7/76/Bsk-m8-01-12.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m8-01-12.png>)
**Rysunek 12. Schemat działania propagacji połączeń**
### Tunele SSL
Tunele wirtualne można realizować na poziomie warstwy sesji. Znanym powszechnie przykładem jest SSL (_Secure Socket Layer_) – połączeniowy protokół oferujący dwupunktowy tunel kryptograficzny z wykorzystaniem certyfikatów, zaprojektowany z myślą o ochronie sesji takich protokołów jak HTTP, POP/IMAP, SMTP. SSL oferuje ochronę poufności, integralności i autentyczności danych. I tak przykładowo HTTPS – protokół HTTP tunelowany poprzez SSL – jest powszechnie wykorzystywaną w sieci internetowej usługą (port 443). Odpowiednio istnieją wersje tunelowane innych usług (POPS, IMAPS). W praktyce SSL potrafi tunelować dowolny ruch (stunnel, OpenVPN). 
Aktualna wersja SSL nosi numer 3.0. Równolegle z tą wersją występuje jego następca – protokół TLS (_Transport Layer Security_). TLS v.1.0 jest standardem IETF – RFC 2246. 
### Pytania problemowe
  1. Który tryb pracy protokołów IPsec – transportowy czy tunelowy – jest dogodniejszy dla konfiguracji: host-to-host, net-to-net, host-to-net?
  2. Wyjaśnij dlaczego najbardziej uniwersalny tunel wirtualny osiągnąć można na poziomie warstwy sieciowej.
---


# 

# Bezpieczeństwo systemów komputerowych - wykład 9:
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Zapory sieciowe (firewall) i translacja adresów](https://wazniak.mimuw.edu.pl/<#Zapory_sieciowe_\(firewall\)_i_translacja_adresów>)
    * [1.1 Podstawowe funkcje systemów firewall](https://wazniak.mimuw.edu.pl/<#Podstawowe_funkcje_systemów_firewall>)
    * [1.2 Podstawowe komponenty systemów firewall](https://wazniak.mimuw.edu.pl/<#Podstawowe_komponenty_systemów_firewall>)
    * [1.3 Router filtrujący](https://wazniak.mimuw.edu.pl/<#Router_filtrujący>)
    * [1.4 Komputer Twierdza](https://wazniak.mimuw.edu.pl/<#Komputer_Twierdza>)
    * [1.5 Filtracja podwójna](https://wazniak.mimuw.edu.pl/<#Filtracja_podwójna>)
    * [1.6 Strefa Zdemilitaryzowana](https://wazniak.mimuw.edu.pl/<#Strefa_Zdemilitaryzowana>)
    * [1.7 Translacja adresów – Network Address Translation (NAT)](https://wazniak.mimuw.edu.pl/<#Translacja_adresów_–_Network_Address_Translation_\(NAT\)>)
      * [1.7.1 Translacja adresów źródłowych (SNAT)](https://wazniak.mimuw.edu.pl/<#Translacja_adresów_źródłowych_\(SNAT\)>)
      * [1.7.2 Translacja adresów docelowych (DNAT)](https://wazniak.mimuw.edu.pl/<#Translacja_adresów_docelowych_\(DNAT\)>)
    * [1.8 Dodatkowa funkcjonalność zapór sieciowych](https://wazniak.mimuw.edu.pl/<#Dodatkowa_funkcjonalność_zapór_sieciowych>)
      * [1.8.1 Filtry kontekstowe](https://wazniak.mimuw.edu.pl/<#Filtry_kontekstowe>)
    * [1.9 Problemy realizacji zapór sieciowych](https://wazniak.mimuw.edu.pl/<#Problemy_realizacji_zapór_sieciowych>)
    * [1.10 Pytania problemowe](https://wazniak.mimuw.edu.pl/<#Pytania_problemowe>)


## Zapory sieciowe (firewall) i translacja adresów
W dziedzinie zabezpieczeń ruchu sieciowego dużą rolę odgrywają systemy kontroli komunikacji nazywane w języku ang. firewall. W języku polskim ścierają się na ogół dwa terminy: zapora sieciowa oraz ściana przeciwogniowa. Drugi z nich jest tłumaczeniem rdzennego pojęcia amerykańskiego (rysunek 1) 
[![Bsk-m9-01-1.png](https://wazniak.mimuw.edu.pl/images/8/82/Bsk-m9-01-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-1.png>)
**Rysunek 1. Etymologia pojęcia firewall**
Inną analogią tego pojęcia jest kontrola paszportowa i celna na granicy – w naszym przypadku granicy sieci komputerowej. 
### Podstawowe funkcje systemów firewall
Podstawowe funkcje systemów firewall obejmują filtrację ruchu oraz pośredniczenie w dostępie do usług sieciowych 
Filtracja pakietów to podstawowa forma zabezpieczenia sieci. Polega na analizie pakietów (a dokładniej parametrów ruchu zawartych w nagłówkach pakietów) warstwa 3 (czasami 2-4) modelu OSI. Możliwa jest: 
  * filtracja pakietów nadchodzących
  * filtracja pakietów wychodzących
  * filtracja pakietów propagowanych przez moduł routingu (dotyczy oczywiście wyłącznie węzłów międzysieciowych)


Ruch sieciowy jest filtrowany (przepuszczany lub blokowany) w zależności od decyzji podjętych na podstawie analizy pakietów, przy zastosowaniu zdefiniowanych reguł (reguł filtracji). 
Pośredniczenie w dostępie do usług jest realizowane poprzez odseparowanie świata wewnętrznego i zewnętrznego względem zapory sieciowej (brak funkcji routingu). Komunikacja poprzez zaporę nie jest możliwa w żadnej warstwie poza aplikacyjną (warstwa 7 modelu OSI). Na zaporze uruchomione są aplikacje pośredniczące (_proxy services_) w komunikacji końcowych aplikacji użytkowych (np. klient-serwer). Oznacza to, iż klient, uruchomiony – przyjmijmy – w sieci wewnętrznej, nie może nawiązać połączenia bezpośrednio z serwerem pracującym w sieci zewnętrznej. Może tylko nawiązać połączenie z aplikacją proxy. Ruch może przechodzić przez zaporę, jedynie gdy zostanie pozytywnie sklasyfikowany przez aplikację proxy. Zaakceptowane połączenie od klienta jest następnie zestawiane w imieniu klienta przez aplikację proxy z serwerem. W istocie zatem utrzymywane są dwa połączenia: klient-proxy i proxy-serwer dolecowy. 
[![Bsk-m9-01-2.png](https://wazniak.mimuw.edu.pl/images/f/f1/Bsk-m9-01-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-2.png>)
**Rysunek 2. Model pośredniczenie w realizacji usług (firewall typu proxy)**
### Podstawowe komponenty systemów firewall
Systemy firewall konstruowane są ze złożenia wymienionych poniżej komponentów. 
  * Specjalizowany węzeł międzysieciowy (router)


Jest to rozwiązanie najprostsze i najłatwiejsze w utrzymaniu. Można je zrealizować przy pomocy następujących urządzeń: 
  *     * router filtrujący (_screening router_)
    * router szyfrujący (_ciphering router_)
  * Komputer Twierdza (_**Bastion Host**_)


Jest to dedykowana stacja lub węzeł międzysieciowy, na którym uruchomione są usługi proxy. 
  * Strefa Zdemilitaryzowana (_**Demilitarized Zone – DMZ**_)


Jest to dedykowana podsieć obejmująca jedno lub kilka stanowisk o złagodzonych wymaganiach względem ochrony. Typowo umieszcza się tam stanowiska oferujące pewne wybrane informacje publicznie, w odróżnieniu od stacji sieciowych pracujących wewnątrz sieci chronionej. 
### Router filtrujący
Podstawowym zagadnieniem dotyczącym realizacji zapory sieciowej tego typu jest kwestia definicji reguł filtracji. Reguły filtracji operują w ogólności na parametrach analizowanych pakietów, takich jak: 
  * adresy z nagłówka protokołu sieciowego (źródłowy i docelowy)
  * typ protokołu (PDU i SDU, np. protokołu transportowego)
  * rodzaj usługi (numer portu z nagłówka protokołu transportowego)


[![Bsk-m9-01-3.png](https://wazniak.mimuw.edu.pl/images/b/ba/Bsk-m9-01-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-3.png>)
**Rysunek 3. Model systemu z zaporą sieciową typu router filtrujący**
Schemat wewnętrznej kompozycji urządzenia filtrującego jest przedstawiony na rysunku 4. Możliwe jest utrzymywanie oddzielnych list filtracji dla ruchu wchodzącego i wychodzącego z zapory sieciowej. 
[![Bsk-m9-01-4.png](https://wazniak.mimuw.edu.pl/images/c/c3/Bsk-m9-01-4.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-4.png>)
**Rysunek 4. Model modułu filtracji**
Filtry można zdefiniować na następujące sposoby: 
  * filtry statyczne – definicje reguł filtracji są dokonane z wyprzedzeniem i obowiązują aż do jawnej ich zmiany
  * filtry kontekstowe – realizują dynamiczne reguły filtracji (SPF = Stateful Packet Filtering) 
    * w trakcie pracy aktualizowane są informacje o bieżących sesjach (asocjacjach protokołu sieciowego)
    * decyzje o filtracji pakietów podejmowane są z uwzględnieniem stanu sesji, do której przynależą
  * filtracja nieliniowa: 
    * elastyczne definiowanie wyrażeń warunkowych (zagnieżdżone reguły logiczne)


Przykład statycznych reguł filtracji pokazuje rysunek 5. Opisuje on filtrację przypadku z rysunku 6. Na nim mamy hipotetyczną sieć wewnętrzną, której stacjom zezwala się na nawiązywanie połączeń tylko wybranej usługi (w przykładzie – telnet) i jedynie z wybranym serwerem zewnętrznym. 
[![Bsk-m9-01-5.png](https://wazniak.mimuw.edu.pl/images/d/d6/Bsk-m9-01-5.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-5.png>)
**Rysunek 5. Przykładowe statyczne reguły filtracji**
Reguły zdefiniowane na statycznej liście filtracji są przeglądane sekwencyjnie do pierwszego trafienia. Dla pasującej reguły jest aplikowane zdefiniowane w niej działanie (na ogół akceptacja lub odrzucenie pakietu). Reguła nr 1 zezwala na ruch wychodzący na zewnątrz jeśli adres nadawcy należy do zakresu adresów sieci wewnętrznej, odbiorcą pakietu jest wyróżniony serwer zewnętrzny, port nadawcy nie jest portem systemowym, a port odbiorcy zgadza się z portem usługi telent. Druga reguła zezwala na ruch w przeciwnym kierunku, pod warunkiem odwrotnej kombinacji parametrów, lecz jedynie pod warunkiem, że w nagłówku TCP ustawiona jest flaga ACK. Natomiast w przypadku, gdy flaga ta jest wyzerowana, ruch wchodzący z serwera jest blokowany. Jest konsekwencją faktu, iż flaga ACK jest wyzerowana jedynie w pierwszym segmencie TCP – nawiązującym połączenie (segment SYN). Nie jest oczywiście naturalne, by serwer usługi telent próbował zestawić połączenie z klientem ochranianej sieci, zatem taką sytuację należy rozpoznać jako podejrzaną i odrzucić pakiet (najprawdopodobniej oprogramowanie podszywające się za serwer próbuje nawiązać połączenie ze stacjami wewnątrz chronionej sieci). Reguła ostatnia jest realizacją zasady domyślnej reguły dostępu – blokuje jakikolwiek ruch, który nie został zdefiniowany w poprzednich regułach. 
[![Bsk-m9-01-6.png](https://wazniak.mimuw.edu.pl/images/4/4e/Bsk-m9-01-6.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-6.png>)
**Rysunek 6. Schemat sieci do przykładu definicji statycznych reguł filtracji**
Statyczne reguły filtracji posiadają kilka ograniczeń. Przykładowo niektóre usługi trudno poddają się filtracji statycznej (np. FTP, X11, DNS). Rozważmy jak w trybie aktywnym pracy serwera FTP (przypomnij sobie jaki to tryb) ochronić się przed nadużyciem, w którym oprogramowanie podszywające się za serwer próbuje nawiązać połączenie ze stacjami wewnątrz chronionej sieci. Z pomocą przychodzą pewne nowe rozwiązania proponowane w samych protokołach aplikacyjnych. Coraz powszechniej wprowadza się i stosuje tryby pracy zmodyfikowane pod kątem usprawnienia filtracji, np. tryb passive w protokole FTP (skądinąd użyteczny także np. przy korzystaniu z dostępu xDSL) 
### Komputer Twierdza
Komputer Twierdza to stacja z odseparowanymi interfejsami sieciowymi (_Dual Homed Host Gateway_) zajmująca miejsce węzła międzysieciowego (rysunek 7). Oferuje fizyczną i logiczną separację prywatnej sieci lokalnej od zewnętrznej sieci publicznej. Dzięki separacji interfejsów tylko Komputer Twierdza jest widoczny z sieci publicznej. Zatem, aby wtargnąć do sieci prywatnej trzeba uprzednio zawładnąć Komputerem Twierdzą. Komputer Twierdza pełni rolę bramy aplikacyjnej – usługi pośredniczące i zastępcze (_proxy_) rozwiązują problem usług trudnych do filtracji. Dzięki temu, iż jest on pełnym stanowiskiem komputerowym, potencjalnie wyposażonym w dowolne żądane oprogramowanie i praktycznie nieograniczone zasoby pamięci masowej, możliwa jest szczegółowa rejestracja zdarzeń (_auditing_), ułatwiająca diagnozowanie ewentualnie pojawiających się nowych zagrożeń i niedoskonałości konfiguracji. 
[![Bsk-m9-01-7.png](https://wazniak.mimuw.edu.pl/images/d/da/Bsk-m9-01-7.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-7.png>)
**Rysunek 7. Model systemu z zaporą sieciową typu Komputer Twierdza**
### Filtracja podwójna
Rysunek 8 pokazuje schematyczne połączenie w jedną linię obrony różnych typów zapór sieciowych, dokładniej jest to brama aplikacyjna poprzedzona routerem filtrującym (_Screened Host Gateway_). 
[![Bsk-m9-01-8.png](https://wazniak.mimuw.edu.pl/images/e/e3/Bsk-m9-01-8.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-8.png>)
**Rysunek 8. Model systemu z filtracją podwójną**
Możliwe jest dalej „rozciągnięcie” Twierdzy na całą dedykowaną podsieć (_Screened Network_), co pokazuje z kolei rysunek 9, a nawet kaskadę podsieci. 
[![Bsk-m9-01-9.png](https://wazniak.mimuw.edu.pl/images/9/92/Bsk-m9-01-9.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-9.png>)
**Rysunek 9. Model systemu z podsiecią ochronną**
### Strefa Zdemilitaryzowana
Konfiguracja która przyjęła się pod nazwą Strefa Zdemilitaryzowana (DMZ = _Demilitarized Zone_) to wydzielona podsieć zawierająca komponenty świadomie wyjęte spod kontroli obejmującej całą resztę sieci wewnętrznej, takie jak np.: 
  * publiczne zasoby (np. ogólnodostępny serwis WWW)
  * przynęty, pułapki


[![Bsk-m9-01-10.png](https://wazniak.mimuw.edu.pl/images/e/e8/Bsk-m9-01-10.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-10.png>)
**Rysunek 10. Model systemu ze Strefą Zdemilitaryzowaną DMZ**
### Translacja adresów – Network Address Translation (NAT)
Translacja adresów jest powszechnym w sieciach komputerowych mechanizmem, który ma różne cele, a są to: 
  * rozszerzenie dostępu do sieci publicznej na stanowiska nie posiadające przydziału adresów publicznych (posiadające tylko adresy prywatne – RFC 1918)
  * wykorzystanie wewnątrz sieci nieprzydzielonych publicznych adresów IP


(za cenę braku możliwości komunikacji z takimi oficjalnymi adresami) 
  * ukrycie wewnętrznej struktury sieci przed światem zewnętrznym
  * przekierowanie ruchu (portów: NAPT = Network Address Port Translation)


Metody wzajemnego odwzorowania adresów są ustandaryzowane i opisane w dokumentach: 
  * RFC1631 (translacja na pojedynczy adres, tj. N:1)
  * RFC1597,1918 (translacja na pulę adresową, tj. N:M)


Wyróżnia się przy tym translację adresów źródłowych – Source NAT (SNAT) – oraz docelowych – Destination NAT (DNAT). 
#### Translacja adresów źródłowych (SNAT)
W tym przypadku pakiety wychodzące z sieci wewnętrznej otrzymują nowy adres źródłowy w nagłówku (rysunek 11). W przykładzie, pakiet wychodzący w rzeczywistości z adresu IP równy 10.1.1.1 otrzymuje po translacji adres źródłowy serwera translacji (jest nim brzegowy węzeł międzysieciowy), mianowicie 150.254.1.100. Numer portu źródłowego też ulega zmianie. 
[![Bsk-m9-01-11.png](https://wazniak.mimuw.edu.pl/images/d/d1/Bsk-m9-01-11.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-11.png>)
**Rysunek 11. Schemat translacji adresów źródłowych (SNAT)**
#### Translacja adresów docelowych (DNAT)
W mechanizmie Destination NAT (DNAT) pakiety przychodzące ze strony inicjującej (na ogół – sieci zewnętrznej) otrzymują nowy adres docelowy (w tym w szczególności – port). Celem może być przekierowanie ruchu określonej usługi pod rzeczywisty, nie ujawniany na zewnątrz, adres wewnętrznego serwera tej usługi. Na rysunku 12 adres serwera (o jaką usługę chodzi w tym przykładzie?) upubliczniony na zewnątrz jest równy 150.254.1.1, podczas gdy rzeczywisty adres to 150.254.1.200. 
[![Bsk-m9-01-12.png](https://wazniak.mimuw.edu.pl/images/4/4c/Bsk-m9-01-12.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-12.png>)
**Rysunek 12. Schemat translacji adresów źródłowych (SNAT)**
### Dodatkowa funkcjonalność zapór sieciowych
Łańcuch funkcji realizowanych przez zapory sieciowe wyglądać może następująco: 
  * jedynie funkcje podstawowe:


[![Bsk-m9-01-12-1.png](https://wazniak.mimuw.edu.pl/images/a/a3/Bsk-m9-01-12-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-12-1.png>)
  * również funkcje dodatkowe:


[![Bsk-m9-01-12-2.png](https://wazniak.mimuw.edu.pl/images/4/47/Bsk-m9-01-12-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-12-2.png>)
Dodatkowymi funkcjami mogą być 
  * obrona przed atakami DoS (_flood-wall_) – specyfikowanie dopuszczalnego rozmiaru strumienia wejściowego (np. w pakietach na sek.)
  * kontrola fragmentacji IP i śledzenie numerów sekwencyjnych TCP (kontrola czy znajdują się w oczekiwanym zakresie)
  * wsparcie dla IPv6: fragmentacja, ICMPv6, ochrona przed atakami DoS analogicznymi jak dla IPv4
  * filtry IPv6, np. ipf (FreeBSD), rozpoznawanie tunelowania IPv6 w IPv4


(tzn. takich protokołów jak 6to4, 6over4, Toredo) 
  * integracja z różnymi zewnętrznymi modułami, np. systemami antywirusowymi, modułami sieciowej detekcji intruzów (IDS), czy ograniczenia dostępu (_parental control_)


#### Filtry kontekstowe
Standardowy przepływ ruchu poddawanego filtracji (round-trip) można przedstawić schematycznie postaci poniższej: 
[![Bsk-m9-01-12-3.png](https://wazniak.mimuw.edu.pl/images/c/c4/Bsk-m9-01-12-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-12-3.png>)
Filtry kontekstowe podejmują dynamicznie zmienne decyzje na podstawie weryfikacji kontekstu (_stateful inspection_): 
  * każda zainicjowana poprawnie sesja jest pamiętana na dynamicznych listach
  * w drodze powrotnej pakiet jest sprawdzany na przynależność do zapamiętanej sesji – filtracja może być pominięta:


Przedstawia to poniższy schemat: 
[![Bsk-m9-01-12-4.png](https://wazniak.mimuw.edu.pl/images/1/1e/Bsk-m9-01-12-4.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m9-01-12-4.png>)
### Problemy realizacji zapór sieciowych
Zapory sieciowe cierpią na wiele problemów, zarówno technologicznych jak i realizacyjnych. Problemy technologiczne dotyczą np. usług takich jak FTP. Przykładowo, jeśli filtr kontekstowy w zaporze obsłuży komendę PORT 23 protokołu FTP, to czy będzie to naruszenie polityki bezpieczeństwa? Problemy technologiczne związane są również z wykorzystaniem w ruchu sieciowym mechanizmów takich jak fragmentacja IP. Z filtracją pakietów pofragmentowanych związane są następujące problemy: 
  * odrzucanie tylko pierwszych fragmentów umożliwia wyciek informacji w strumieniu wyjściowym
  * istnieją narzędzia do tak perfidnego fragmentowania, by flagi ACK i SYN nagłówka TCP nie pojawiały się w pierwszym fragmencie
  * można scalać fragmenty na zaporze – uwaga na błędy przy scalaniu
  * można narzucić wymóg, aby pierwszy fragment zawierał co najmniej 16B danych (a najlepiej cały nagłówek TCP)


Istotne problemy niesie ze sobą pielęgnacja reguł filtracji. Szczególnie trudna jest ona do sprawnego przeprowadzenia w przypadku dużych zbiorów reguł. Dodatkowo potęgują trudności częste na naszym rynku informatycznym zmiany personelu i brak dokumentacji uniemożliwiający pielęgnację starych reguł (odziedziczonych po poprzednim administratorze). Często występują również problemy wewnętrzne: duże organizacje posiadają często złożoną politykę bezpieczeństwa, co implikuje wielość nachodzących na siebie domen bezpieczeństwa i trudności w definicji i pielęgnacji spójnych reguł filtracji. 
Ostrożnie należy też postępować z tunelami wirtualnymi. Autoryzowane tunele VPN mogą być potencjalnym nośnikiem nieautoryzowanych treści poza kontrolą zapór ogniowych. Zatem powinny być zaplanowane i zrealizowane w sposób przemyślany. Podobnie jak VPN, również propagowanie połączeń (_port forwarding_) może przyczynić się do skutecznego ominięcia kontroli na zaporze. Podobnie trudności sprawia dość rozpowszechniony protokół SOAP (_Simple Object Access Protocol_), służący, mówiąc kolokwialnie, do tunelowania jakiegokolwiek ruchu w HTTP. Pod tym względem skrajnie wywrotowy jest httptunnel (<http://www.noccrew.org/software/httptunnel.html>) 
### Pytania problemowe
  1. W przykładzie statycznych reguł filtracji z rysunku 5 zdefiniowano 4 reguły. Jedna z nich jest jednak nadmiarowa i można ją usunąć bez żadnych konsekwencji dla przebiegu filtracji. Która to reguła?

---


# 

# Bezpieczeństwo systemów komputerowych - wykład 10:
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Bezpieczeństwo aplikacji i usług sieciowych](https://wazniak.mimuw.edu.pl/<#Bezpieczeństwo_aplikacji_i_usług_sieciowych>)
    * [1.1 Bezpieczne środowisko aplikacyjne](https://wazniak.mimuw.edu.pl/<#Bezpieczne_środowisko_aplikacyjne>)
    * [1.2 Usługa WWW](https://wazniak.mimuw.edu.pl/<#Usługa_WWW>)
      * [1.2.1 Uwierzytelnianie](https://wazniak.mimuw.edu.pl/<#Uwierzytelnianie>)
      * [1.2.2 Protokół SSL (_Secure Sockets Layer_)](https://wazniak.mimuw.edu.pl/<#Protokół_SSL_\(Secure_Sockets_Layer\)>)
    * [1.3 Luki bezpieczeństwa w usłudze WWW](https://wazniak.mimuw.edu.pl/<#Luki_bezpieczeństwa_w_usłudze_WWW>)
      * [1.3.1 Przeglądarki WWW](https://wazniak.mimuw.edu.pl/<#Przeglądarki_WWW>)
      * [1.3.2 Serwery WWW](https://wazniak.mimuw.edu.pl/<#Serwery_WWW>)
      * [1.3.3 Środowisko wykonania](https://wazniak.mimuw.edu.pl/<#Środowisko_wykonania>)
    * [1.4 Poczta elektroniczna](https://wazniak.mimuw.edu.pl/<#Poczta_elektroniczna>)
    * [1.5 Spam](https://wazniak.mimuw.edu.pl/<#Spam>)
      * [1.5.1 Ochrona kryptograficzna poczty](https://wazniak.mimuw.edu.pl/<#Ochrona_kryptograficzna_poczty>)
      * [1.5.2 System PEM (_Privacy Enhanced Mail_)](https://wazniak.mimuw.edu.pl/<#System_PEM_\(Privacy_Enhanced_Mail\)>)
      * [1.5.3 PGP (_Pretty Good Privacy_)](https://wazniak.mimuw.edu.pl/<#PGP_\(Pretty_Good_Privacy\)>)
      * [1.5.4 S/MIME](https://wazniak.mimuw.edu.pl/<#S/MIME>)
    * [1.6 Pytania problemowe](https://wazniak.mimuw.edu.pl/<#Pytania_problemowe>)


## Bezpieczeństwo aplikacji i usług sieciowych
Bieżący moduł przedstawia wybrane zagadnienia bezpieczeństwa dotyczące aplikacji użytkowych i usług sieciowych. Najpierw omówiony zostanie dość uniwersalny mechanizm ochrony stosowalny wobec dowolnych aplikacji – ograniczanie środowiska wykonania. Następnie przedstawione zostaną najistotniejsze problemy dotyczące popularnych usług aplikacyjnych – WWW i poczty elektronicznej. 
### Bezpieczne środowisko aplikacyjne
Jednym z najważniejszych środków ochrony aplikacji użytkowych przed zagrożeniami płynącymi z zewnątrz i skutkującymi przejęciem kontroli nad aplikacją, a potencjalnie dalej – nad całym systemem operacyjnym, jest stworzenie bezpiecznego środowiska aplikacyjnego, czyli takiego, w którym aplikacja zostaje uruchomiona w specjalnie spreparowanym podsystemie, który minimalizuje zagrożenia. 
Ograniczanie środowiska wykonania aplikacji ma na celu w istocie nie tyle uniemożliwienie ataku w ogóle, co minimalizowanie szkód po ewentualnym ataku. Koncepcja działania tego mechanizmu jest następująca: 
  * zawsze uruchamiamy proces z najmniejszymi wystarczającymi mu uprawnieniami
  * ograniczamy przestrzeń aktywności procesu (dozwolonych modyfikacji) do wybranego zawężonego fragmentu systemu, w szczególności systemu plików – tworząc tzw. piaskownicę (ang. sandbox)


W systemach z rodziny Unix popularnym narzędziem służącym do tworzenia piaskownic jest systemowa funkcja chroot(). Jest to uprzywilejowana funkcja systemowa ograniczająca proces do określonego poddrzewa systemu plików. Blokuje jedynie dostęp do plików, tworząc tzw. więzienie. Uwięziony proces nie może otworzyć (w tym utworzyć) pliku poza ograniczonym obszarem, chociaż może dziedziczyć deskryptory wskazujące na pliki spoza tego obszaru. 
Tworząc piaskownicę w systemie Unix trzeba stworzyć więzionemu procesowi iluzję pracy w pełnoprawnym systemie. W tym celu w piaskownicy należy zainstalować odpowiednie pliki i katalogi potrzebne programowi i używanym przez niego bibliotekom (na ogół bardzo ograniczone fragmenty /etc, /lib czy /usr/lib). 
Mimo ogromnej przydatności funkcji chroot(), związane są z jej wykorzystaniem pewne problemy. Większość z nich dotyczy ataków DoS. I tak przykładowo, mimo ograniczenia środowiska wykonania: 
  * dysk może się przepełnić (np. zrzutami obrazu pamięci, plikami raportów) – na szczęście w systemie Unix możemy ograniczać programy do oddzielnej partycji
  * może nastąpić przepełnienie pamięci – proces może zagarnąć tyle pamięci, że zablokuje to urządzenie z plikiem wymiany – przeważnie możemy ograniczać użycie pamięci
  * zużywanie czasu procesora – tu do obrony mamy do dyspozycji polecenie nice
  * brak automatycznej kontroli nad komunikacją sieciową pozwala potencjalnie wyzwolić się częściowo z uwięzienia


W systemie Unix istnieje polecenie chroot (dostępne z powłoki), które wywołuje funkcję chroot(). Polecenie to ma też pewne ograniczenia, z których najważniejsze to: 
  * polecenie chroot musi znajdować się w piaskownicy
  * chroot wymaga uprawnień superużytkownika
  * brak mechanizmu zmiany UID i GID procesu – proces uwięziony wykonuje się z prawami superużytkownika root (ew. sam musi zmienić efektywny UID/GID)
  * potencjalne luki umożliwią ucieczkę z piaskownicy (prawa superużytkownika)


W nowszych wydaniach systemów Unix/Linux istnieją inne, doskonalsze narzędzia – np. chrootuid, jail – które przed wywołaniem funkcji chroot() pozwalają zmienić UID oraz GID 
```
jail –u nobody –g www –l /tmp/jail.log –d / /usr/apache /bin/httpd

```

### Usługa WWW
#### Uwierzytelnianie
Jednym z ważniejszych problemów zapewnienia podstawowych własności bezpieczeństwa jest, jak wiemy, poprawne uwierzytelnianie. Prosty mechanizm uwierzytelniania został wbudowany w protokół usługi WWW – HTTP. Uwierzytelnianie podstawowe w protokole HTTP przebiega następująco: 
  * serwer WWW może w dowolnym momencie zażądać od przeglądarki dokonania uwierzytelnienia użytkownika
  * przeglądarka wyświetla stosowne okno dialogowe lub podobny obiekt (rysunek 1),


który pozwoli użytkownikowi na wprowadzenie danych uwierzytelniających 
  * po ich pierwszym wpisaniu przeglądarka zapamięta je i automatycznie prześle do serwera na każde następne żądanie
  * dane przesyłane są w postaci jawnej
  * dane te zostaną usunięte z pamięci z chwilą zamknięcia okna przeglądarki


[![Bsk-m10-01-1.png](https://wazniak.mimuw.edu.pl/images/d/dd/Bsk-m10-01-1.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m10-01-1.png>)
**Rysunek 1. Okienko uwierzytelniania wyświetlane w przykładowej przeglądarce www**
Wiele implementacji serwerów usługi www umożliwia automatyzację operacji uwierzytelniania, pozwalając na weryfikację otrzymanych danych uwierzytelniających poprzez zewnętrzne bazy danych, przechowujące konfigurację kont użytkowników. Przykładowo, serwer Apache posiada rodzinę modułów _mod_auth_ służacych do tego celu (np. _mod_auth_mysql_), a serwer IIS pozwala na starowanie automatyzają poprzez ustawienia opcji _Panel Sterowania_ -> _Narzędzia Administracyjne_ -> _Menedżer Usług Internetowych_ (można zdefiniować np. uwierzytelnianie użytkownika przez domenę) 
W standardzie HTTP 1.1 uwzględniono uwierzytelnianie kryptograficzne, realizowane najczęściej z wykorzystaniem algorytmu MD5. Niestety nie przewidziano w specyfikacji dwustronnego uwierzytelniania. 
Rozwiązaniem problemów uwierzytelniania, które przyjęło się w praktyce jest zastosowanie niezależnie od protokołu aplikacyjnego HTTP, protokołu sesji – SSL. 
#### Protokół SSL (_Secure Sockets Layer_)
W istocie protokół SSL tworzy tunel kryptograficzny usługi www. Tak zabezpieczona usługa znana jest pod nazwą https (port 443/tcp). Jednym z podstawowych komponentów protokołu SSL jest protokół uzgadniania, który realizuje zadania uwierzytelniania stron. 
Protokół uzgadniania (_handshake protocol_) działa wg poniższego schematu: 
  * klient wysyła do serwera komunikat ClientHello (wersja protokołu, identyfikator sesji, listę obsługiwanych szyfrów i metod kompresji, dane losowe)
  * serwer odsyła komunikat ServerHello (wersja protokołu, identyfikator sesji, wybrany szyfr i metodę kompresji, dane losowe oraz swój certyfikat X.509) oraz opcjonalnie – żądanie certyfikatu klienta (wraz z losowym zawołaniem)
  * klient uwierzytelnia serwer na podstawie odebranego certyfikatu i w razie niepowodzenia przerywa połączenie
  * po pomyślnym uwierzytelnieniu klient tworzy pierwotny sekret główny (_premaster secret_), który szyfruje kluczem publicznym serwera i wysyła do serwera
  * jeśli serwer żądał uwierzytelnienia klienta, to klient wysyła też swój certyfikat oraz podpisane zawołanie odebrane wcześniej od serwera
  * po ewentualnym uwierzytelnieniu klienta serwer deszyfruje pierwotny sekret główny i na jego podstawie uzyskuje sekret główny (_master secret_), podobnie czyni w tym czasie klient
  * z wygenerowanego sekretu głównego obie strony tworzą (zależny od ustalonego algorytmu szyfrującego) klucz sesji (lub klucze sesji – do szyfrowania i podpisywania)
  * klient i serwer wysyłają do siebie nawzajem zaszyfrowany kluczem sesji komunikat o zakończeniu fazy uzgadniania
  * protokół uzgadniania kończy się i (o ile wzajemna weryfikacja przebiegła pomyślnie) rozpoczyna się sesja SSL


Poprawność procedury uwierzytelniania wynika z następujących obserwacji: 
  * jeśli serwer nie posiadałby klucza prywatnego odpowiadającego kluczowi publicznemu ze swojego certyfikatu: 
    * nie rozszyfruje poprawnie sekretu i nie wygeneruje tego samego klucza sesji co klient
    * wówczas połączenie zastanie przerwane w fazie uzgadniania
    * stąd klient ma pewność, że serwer jest tym, czyją autentyczność poświadcza certyfikat (po weryfikacji jego poprawności)
  * jeśli klient nie posiadałby klucza prywatnego odpowiadającego kluczowi publicznemu ze swojego certyfikatu: 
    * serwer pobierze jego klucz publiczny z certyfikatu i rozszyfruje podpisane kluczem prywatnym klienta zapytanie
    * nie otrzyma tego, które sam wysłał
    * zatem klient nie jest tym, czyją autentyczność poświadcza certyfikat


Newralgiczna w tym procesie jest weryfikacja certyfikatów – SSL jest podatny na atak _man-in-the-middle_. Sposobem redukcji zagrożenia może być np. weryfikacja czy adres IP asocjacji z nawiązanego połączenia zgadza się z adresem IP w certyfikacie. 
### Luki bezpieczeństwa w usłudze WWW
Luki bezpieczeństwa w usłudze WWW dotyczą wielu komponentów systemu, w szczególności klientów (przeglądarek), serwerów czy środowiska wykonania (systemu operacyjnego). 
#### Przeglądarki WWW
Wśród typowych problemów bezpieczeństwa klientów usługi WWW należy wymienić chociażby 
  * problemy z losową generacją kluczy SSL
  * błędy implementacji S/MIME (_Secure/Multi-purpose Internet Mail Extension_)
  * problemy specyficzne dla konkretnych przglądarek, np. Internet Explorer 
    * BHO (_Browser Helper Objects_) – pozwala na integrację z przeglądarką np. toolbarów (praktycznie dowolnych aplikacji) – często wykorzystywane przez malware do cichej instalacji (zagrożenia browser hijacking – podmiana parametrów pracy przeglądarki, takich jak adres strony domowej, tracking – śledzenie pracy użytkownika, niechciane wyskakujące okienka pop-ups)
  * konie trojańskie / wirusy w dokumentach hipertekstowych – ochronę tu stanowić może wiele mechanizmów 
    * zamknięte środowisko uruchomieniowe (_sandbox_)
    * korzystanie wyłącznie z poprawnie zdefiniowanego zbioru zaufanych serwerów źródłowych
    * certyfikaty cyfrowe


Z ostatnim z powyższych problemów związanych jest szereg zagrożeń niesionych przez języki automatyzacji operacji na dokumentach hipertekstowych i definicji dynamicznych stron DHTML czy .NET. Języki te to przede wszystkim Java i ActiveX 
Java charakteryzuje się w tym kontekście następującymi własnościami: 
  * jest to język stosunkowo bezpieczny (brak wskaźników i problemu przepełnienia bufora)
  * jest językiem interpretowanym (aplety mają format byte code) – możliwe są luki bezpieczeństwa w programie interpretera
  * maszyna wirtualna JVM posiada wbudowany system ochronny: analizatory kodu (code verifier i class loader), sandbox, security manager, certyfikacja serwerów


ActiveX posiada następujące istotne w naszych rozważaniach cechy: 
  * program jest dystrybuowany w postaci skompilowanej – praktycznie brak tu możliwości analizy bezpieczeństwa
  * system ochronny: certyfikacja kontrolek ActiveX (mechanizm _authenticode_) – praktyka pokazuje, iż generalnie zaufanie jedynie certyfikacji jest złudne.


W praktyce, najczęściej wbudowane w usługę WWW i dostępne w przeglądarkach mechanizmy ochrony są uzupełniane o filtrację treści ruchu HTTP na zaporze firewall (osobistej lub sieciowej). 
#### Serwery WWW
Do charakterystycznych problemów bezpieczeństwa, na które cierpią implementacje serwerów usługi WWW można zaliczyć w szczególności np.: 
  * tylne furtki
  * błędy przepełnienia bufora, np. w ism.dll (uruchamianym przez IIS dla URL *.htr) pozwala na uruchomienie kodu w kontekście procesu serwera z jego uprawnieniami


#### Środowisko wykonania
Problemy środowiska wykonania szczególnie często ujawniają się w przypadku systemu MS Windows. Tu wymienimy chociażby: 
  * mechanizm LSP (_Layered Service Provider_) oferujący możliwość podpinania się modułów LSP (praktycznie dowolnych aplikacji, w tym malware) pod stos protokołów w bibliotece Winsock 2
  * luki w implementacjach protokołów MHTML, MS-ITS, XMLHTTP i VBScript (wykorzystywane przez Outlook, WindowsUpdate oraz rozliczne malware)


Umożliwiają one instalację niechcianego oprogramowania pobieranego nieświadomie poprzez usługę WWW. 
### Poczta elektroniczna
Rysunek 2 przedstawia model komunikacji systemu internetowej usługi pocztowej standardu SMTP (RFC 821). Wyróżnione na nim elementy systemu to: 
  * _MUA_ = Mail User Agent
  * _MTA_ = Mail Transfer Agent
  * _MDA_ = Mail Delivery Agent


[![Bsk-m10-01-2.png](https://wazniak.mimuw.edu.pl/images/b/ba/Bsk-m10-01-2.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m10-01-2.png>)
**Rysunek 2. Model komunikacji SMTP**
Podstawowe problemy bezpieczeństwa dotyczące poczty obejmują: 
  * niepożądane przesyłki (_spam_)
  * niebezpieczne załączniki (wirusy)
  * potwierdzanie dostarczenia
  * naruszenie poufności / integralności / autentyczności


### Spam
Pojęcie spam dotyczy ogółu niechcianych przesyłek pocztowych zajmujących zasoby pamięciowe (skrzynka pocztowa odbiorcy) i czasowe systemu. Ochrona anty-spamowa sprowadza się do odfiltrowania takich przesyłek z całości ruchu pocztowego i może być realizowana na kilku poziomach modelu komunikacji SMTP. 
Na poziomie MTA filtracja jest dokonywana poprzez analizę nagłówka SMTP, np. 
  * adresów: czy są weryfikowalne w DNS, czy odpowiadają rekordom MX


czy nie jest na czarnej liście 
  * weryfikacja konta nadawcy (komenda VRFY protokołu SMTP)


Posiada ona istotną zaletę – oszczędność zasobów – odrzucamy spam na pierwszej linii obrony. Wadą tego rozwiązania jest mała precyzja wynikająca z faktu, iż na tak wczesnym etapie posiadamy mało informacji do dyspozycji. Stąd występuje duże prawdopodobieństwo pomyłki – sklasyfikowania niechcianej przesyłki jako pożądanej i odwrotnie. 
Stosunkowo dużą skuteczność i małe efekty uboczne (opóźnienie) wykazuje tu mechanizm znany jako szare listy (_greylisting_). Mianowicie, po odebraniu przesyłki MTA odsyła na adres nadawcy kod 452 „czasowa niedostępność” i czeka na powtórną transmisję. Automaty spamerskie z założenia nie retransmitują, stąd akceptowane jako pożądane są wszystkie retransmitowane listy. 
Poziom MDA pozwala stosować do realizacji możliwie skutecznej filtracji takie rozwiązania jak: 
  * analiza heurystyczna (na podstawie przygotowanej bazy danych charakterystycznych)
  * analiza statystyczna (samouczące się filtry Bayesa)


Również klienci pocztowi MUA posiadają często wbudowane narzędzia filtrujące, które, niekiedy automatycznie, pozwalają użytkownikowi klasyfikować wybrane listy jako spam. 
#### Ochrona kryptograficzna poczty
Powszechnie spotykane są następujące standardy ochrony kryptograficznej 
  * PEM – _Privacy Enhanced Mail_
  * PGP – _Pretty Good Privacy_
  * S/MIME – _Secure MIME_


Istnieje wiele kompleksowych systemów i standardów pocztowych wykorzystujących kryptografię, w tym przykładowo: 
  * X.400 MHS – Message Handling System
  * EDI (EDIFACT – X.435) – Electronic Data Interchange


#### System PEM (_Privacy Enhanced Mail_)
PEM to jeden z pierwszych standardów zaproponowanych do ochrony przesyłek protokołu SMTP i posiadający zgodny z pierwotnymi wymaganiami tego protokołu format RFC822 (rysunek 3). W PEM możliwa jest przede wszystkim kontrola integralności przy wykorzystaniu MD2 lub MD5 (128b) – zgodnie ze standardem RFC1421. Opcjonalnie możliwe jest szyfrowanie wiadomości – DES-ECB, 3DES (RFC1423). PEM wspiera zarządzanie kluczami i certyfikację wg ISO X.509 (RFC1422, RFC1424). 
[![Bsk-m10-01-3.png](https://wazniak.mimuw.edu.pl/images/1/12/Bsk-m10-01-3.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsk-m10-01-3.png>)
**Rysunek 3. Schematyczna struktura przesyłki pocztowej zabezpieczonej kryptograficznie**
Przykładowe implementacje to chociażby RIPEM czy TIS-PEM. Jednak w szerszej skali PEM nie uzyskał dużej popularności. 
#### PGP (_Pretty Good Privacy_)
PGP powstał jako projekt akademicki prowadzony przez Phila Zimmermanna (z MIT). Prace uwieńczyły standard IETF RFC1991 (PGP 2.6.x) i wielka popularność jaką zyskał on w Internecie. W 1998 IETF zatwierdził standard OpenPGP (RFC2440) opracowany przez Network Associates, bazujący na PGP 5.x. Istnieje również alternatywny projekt PGPi (www.pgpi.org) = International PGP – przeniesiony poza USA. Z najpopularniejszych implementacji wymienić należy Desktop PGP – jest to komercyjna wersja rozprowadzana przez Network Associates (rozszerzona np. o IDS) – oraz GnuPG – wersję dystrybuowaną na licencji GNU. Ponadto wiele aplikacji wykorzystuje PGP (np. enigmail – rozszerzenie klientów pocztowych Mozilli). 
PGP umożliwia: 
  * szyfrowanie wiadomości pocztowej 
    * wykorzystywany jest jednorazowy klucz symetryczny generowany dla każdego szyfrowanego listu
    * następnie klucz ten szyfrowany jest metodą asymetryczną – kluczem publicznym odbiorcy – Diffie-Hellman/DSS, RSA (768b, 1024b, ...)
    * i tak zaszyfrowany klucz jest dołączany do zaszyfrowanego listu
  * kontrolę integralności – MD5, SHA-1
  * symetryczne szyfrowanie dowolnych plików


#### S/MIME
Standard Secure MIME umożliwia wygodną integrację mechanizmu kryptograficznego zabezpieczenia korespondencji pocztowej z protokołem SMTP, poprzez wykorzystanie rozszerzenia uznanego mechanizmu obsługi załączników MIME. Wersja S/MIME 1 została opracowana przez RSA Security w 1995r. i wykorzystywała mechanizmy kryptograficzne wchodzące w skład PKCS (_Public Key Cryptography Standards_). Wersja S/MIME 2 (RFC2311/12) powstała w 1998r., a wkrótce później S/MIME 3 (RFC 2630-34). S/MIME 3 oferuje m.in. rozszerzone funkcje bazujące na mechanizmach MSP (_Message Security Protocol_ protokołu opracowanego pierwotnie dla _Defense Message System_). 
Należy nadmienić istnienie również protokołów PGP/MIME i OpenPGP/MIME. 
### Pytania problemowe
  1. W przykładzie statycznych reguł filtracji z rysunku 5 zdefiniowano 4 reguły. Jedna z nich jest jednak nadmiarowa i można ją usunąć bez żadnych konsekwencji dla przebiegu filtracji. Która to reguła?


---


# Mechanizmy lokalnej kontroli dostępu

# Bezpieczeństwo systemów komputerowych - laboratorium 1:Mechanizmy lokalnej kontroli dostępu
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Lokalna Kontrola Dostępu w systemie Linux](https://wazniak.mimuw.edu.pl/<#Lokalna_Kontrola_Dostępu_w_systemie_Linux>)
    * [2.1 Algorytm sprawdzania uprawnień dostępu](https://wazniak.mimuw.edu.pl/<#Algorytm_sprawdzania_uprawnień_dostępu>)
    * [2.2 Polecenia](https://wazniak.mimuw.edu.pl/<#Polecenia>)
      * [2.2.1 Polecenie getfacl](https://wazniak.mimuw.edu.pl/<#Polecenie_getfacl>)
      * [2.2.2 Polecenie setfacl](https://wazniak.mimuw.edu.pl/<#Polecenie_setfacl>)
  * [3 Lokalna Kontrola Dostępu w systemie Windows XP](https://wazniak.mimuw.edu.pl/<#Lokalna_Kontrola_Dostępu_w_systemie_Windows_XP>)
  * [4 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [5 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [6 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Mechanizm POSIX ACL został opracowany, aby rozszerzyć standardowy mechanizm uprawnień, który kontroluje dostęp do pliku (lub katalogu) dla właściciela, grupy oraz innych użytkowników w systemach Linux/Unix. Rozszerzenie dotyczy możliwości definiowania uprawnień dla wskazanych użytkowników i/lub grup. W przypadku _minimal_ ACL, dostępnych domyślnie w systemie Unix/Linux, uprawnienia ograniczają się do prawa odczytu (read), zapisu (write) i wykonywania/przeszukiwania (execute). 
Używanie ACL jest możliwe w wielu rodzajach systemów plików w systemie operacyjnym Linux, np.: ext2, ext3, reiserfs, nfs. 
Mechanizm ACL jest również wspierany w systemach firmy Microsoft. Jednak nie zachowują one pełnej zgodności ze standardem POSIX i opierają się jedynie o system plików NTFS. 
Celem ćwiczenia jest przyjrzenie się możliwościom lokalnej kontroli dostępu w systemach Linux oraz Windows. 
## Lokalna Kontrola Dostępu w systemie Linux
### Algorytm sprawdzania uprawnień dostępu
Standard POSIX ACL oferuje możliwość maskowania uprawnień poprzez pole maski. Efektywnie uprawnienia do pliku są sumą bitową uprawnień użytkownika/grupy i maski. 
Kolejne kroki algorytmu sprawdzenia uprawnień dostępu: 
  * jeśli użytkownik jest właścicielem pliku - dopuść,
  * jeżeli użytkownik jest na liście nazwanych użytkowników i ma odpowiednie efektywne uprawnienia - dopuść,
  * jeżeli jedna z grup użytkownika jest grupą właściciela i posiada odpowiednia efektywne prawa - dopuść,
  * jeżeli jedna z grup użytkownika występuje jako grupa nazwana i posiada odpowiednie efektywne prawa - dopuść,
  * jeżeli jedna z grup użytkownika jest grupą właściciela lub należy do grup nazwanych, ale nie posiada dostatecznych efektywnych uprawnień - dostęp jest zabroniony,
  * następnie uprawnienia innych (others) określają możliwość dostępu.


### Polecenia
Dostępne są dwa polecenia, jedno służy do odczytu rozszerzonych praw, drugie do ich ustawiania: 
  * getfacl
  * setfacl


#### Polecenie getfacl
Program wypisuje rozszerzone uprawnienia do plików i katalogów. 
```
 % ls -l
 -rw-r--r-- 1 user group 1000 2004-10-01 09:00 plik.txt
 
 % getfacl plik.txt
 # file: plik.txt
 # owner: user
 # group: group
 user::rw-
 group::r--
 other::r--
 
 % getfacl plik.txt –-omit-header
 user::rw-
 group::r--
 other::r--

```

#### Polecenie setfacl
Polecenie pozwala zmienić, dodać lub usunąć uprawnienia z rozszerzonych uprawnień. 
Dodanie uprawnień: 
```
 % setfacl -m user:kowalski:rwx plik.txt
 % getfacl plik.txt –-omit-header
 user::rw-
 user:kowalski:rwx
 group::r--
 mask::rwx
 other::r--

```

Zmiana uprawnień: 
```
 % setfacl -m u:kowalski:r plik.txt
 % getfacl plik.txt –-omit-header
 user::rw-
 user:kowalski:r
 group::r--
 mask::rwx
 other::r--

```

Usunięcie uprawnień: 
```
 % setfacl -x u:kowalski plik.txt
 % getfacl plik.txt –-omit-header
 user::rw-
 group::r--
 mask::r--
 other::r--

```

Uprawnienia domyślne dotyczą tylko katalogów i umożliwiają automatyczne nadawanie rozszerzonych uprawnień do nowotworzonych plików/katalogów w katalogu, któremu nadaliśmy uprawnienia domyślne. 
Dodanie uprawnień domyślnych: 
```
 % setfacl -d -m group:students:wx katalog
 % getfacl katalog –-omit-header
 user::rwx
 group::r-x
 other::r-x
 default:user::rwx
 default:group::r-x
 default:group:students:-wx
 default:mask::rwx
 default:other::r-x

```

Modyfikacja i usuwanie domyślnych uprawnień jest analogiczne. 
Możliwość ustawiania pola maski jest możliwa poprzez następujące polecenie: 
```
 % setfacl -m mask::rwx plik.txt

```

Istnieją jeszcze opcje pozwalające całkowicie skasować rozszerzone uprawnienia (-b) oraz domyślne uprawnienia (-k). 
## Lokalna Kontrola Dostępu w systemie Windows XP
System plików NTFS umożliwia związanie z każdym zasobem plikowym (w tym: katalogiem) list kontroli dostępu ACL (_Access Control List_). Dostęp do prostych ustawień ACL pliku (katalogu) jest możliwy z poziomu np. Eksploratora Windows w opcji Właściwości (menu Plik lub kontekstowe). 
[![Bsi 01 01.png](https://wazniak.mimuw.edu.pl/images/5/51/Bsi_01_01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_01_01.png>)
Rozszerzone listy ACL są dostępne po wyborze uprawnień Zaawansowanych. 
[![Bsi 01 02.png](https://wazniak.mimuw.edu.pl/images/6/6f/Bsi_01_02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_01_02.png>)
## Zadania
  * Stworzyć katalog z prawami 0750 i zobaczyć listę rozszerzonych praw do tego katalogu.
  * Dodać uprawnienia do zapisu i przeszukiwania do powyższego katalogu koledze siedzącemu przy sąsiednim komputerze.
  * Sprawdź czy możesz zapisać jakiś plik do katalogu kolegi. Jeśli nie - sprawdź przyczynę.
  * Wykonać chmod g-w <katalog>, następnie sprawdzić czy kolega może stworzyć plik w tym katalogu. Sprawdzić rozszerzone uprawnienia dla tego katalogu.
  * Wykonać chmod g+w <katalog> i ponownie wykonać punkt poprzedni.
  * Nadać katalogowi uprawnienia domyślne. Stworzyć w katalogu kolegi plik, katalog. Sprawdzić rozszerzone uprawniania nowo utworzonego pliku i katalogu.
  * Utworzyć nowy katalog ~/public z uprawnieniami "wx" dla grupy "students" oraz "rwx" dla grupy "staff". Dodać domyślne uprawnienia dla samego siebie.
  * Utworzyć w katalogu _Moje dokumenty_ plik _Test.txt_. Dla tego pliku wykonać następujące operacje:
  * korzystając z prostych ACL nadać uprawnienia do odczytu dla użytkownika **scott**
  * sprawdzić rozszerzone ACL dla tego użytkownika
  * sprawdzić jakie czynne uprawnienia posiada ten użytkownik
  * Następnie dla pliku Test.txt:
  * sprawdzić jakie czynne uprawnienia posiada użytkownik **gość**
  * korzystając z prostych ACL odebrać uprawnienia do zapisu użytkownikowi **gość**
  * sprawdzić rozszerzone ACL dla tego użytkownika
  * sprawdzić jakie czynne uprawnienia posiada ten użytkownik
  * Sprawdzić czy dla obu tych użytkowników, rzeczywiście mogą oni skorzystać z odpowiednich praw dostępu do analizowanego pliku. Co należy dodatkowo zrobić, aby dostęp ten był możliwy?


## Problemy do dyskusji
  * Porównać mechanizmy ACL systemu Linux i Windows.
  * Jakie są wady, zalety poszczególnych mechanizmów ACL?
  * Czy warto wykorzystywać bardziej zaawansowane funkcje mechanizmów ACL?
  * Czy istnieje lepszy mechanizm ACL niż przedstawione powyżej, jakie?


---


# Domeny zaufania, mechanizmy kontroli zdalnego dostępu

# Bezpieczeństwo systemów komputerowych - laboratorium 2:Domeny zaufania, mechanizmy kontroli zdalnego dostępu
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
Domeny zaufania i zabezpieczanie usług sieciowych w systemie Linux za pomocą programu tcpd 
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Zastosowanie domen zaufania](https://wazniak.mimuw.edu.pl/<#Zastosowanie_domen_zaufania>)
  * [3 Przykładowa domena zaufania](https://wazniak.mimuw.edu.pl/<#Przykładowa_domena_zaufania>)
    * [3.1 Polecenie rlogin w systemie Linux](https://wazniak.mimuw.edu.pl/<#Polecenie_rlogin_w_systemie_Linux>)
  * [4 Zabezpieczanie usług sieciowych programem tcpd](https://wazniak.mimuw.edu.pl/<#Zabezpieczanie_usług_sieciowych_programem_tcpd>)
    * [4.1 Podstawy](https://wazniak.mimuw.edu.pl/<#Podstawy>)
    * [4.2 Przykład zabezpieczania usługi tftp programem tcpd](https://wazniak.mimuw.edu.pl/<#Przykład_zabezpieczania_usługi_tftp_programem_tcpd>)
  * [5 Podsumowanie](https://wazniak.mimuw.edu.pl/<#Podsumowanie>)
  * [6 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [7 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [8 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
W rozbudowanych środowiskach sieciowych, w których istnieje wiele usług, wielu użytkowników oraz potencjalnie wiele różnych mechanizmów kontroli dostępu, praca użytkowników obarczona zostaje potrzebą wielokrotnego uwierzytelniania się przed różnymi serwerami usługowymi. Taki stan rzeczy nie jest pożądany co najmniej z kilku powodów. Po pierwsze zabiera czas przewidziany na efektywną pracę. Po drugie wielokrotne uwierzytelnianie się budzi niechęć użytkowników, dla których kwestie bezpieczeństwa w większości sytuacji nie są priorytetowe. Po trzecie wielokrotne uwierzytelnianie może prowadzić do sytuacji, w której użytkownicy zamiast pamiętać wszystkie klucze, hasła itd. zwyczajnie zapisują je na różnych nośnikach informacji i robią to najczęściej bez zachowania należytych środków ostrożności. 
Mechanizm domeny zaufania, w którym wykorzystywana jest idea jednokrotnego uwierzytelniania (_ang. single sign-on_), stanowi receptę na opisane powyżej problemy. 
Druga część niniejszego opracowania będzie dotyczyła programu określanego mianem TCP Wrapper. W systemie Linux jest to program wykonywalny tcpd oraz dwa pliki konfiguracyjne, w których zapisywane są reguły bezpieczeństwa dla programu tcpd. Mechanizm TCP Wrapper, mimo że nie jest ani najnowszy, ani bardzo skomplikowany opiera się na prostej zasadzie, według której ruch sieciowy nadchodzący, jaki ma trafić do odpowiedniego programu, jest najpierw transparentnie dla tego programu sprawdzany na wypadek niezgodności z regułami bezpieczeństwa zapisanymi w plikach konfiguracyjnych. Naruszenie reguł spowoduje zablokowanie ruchu sieciowego skierowanego do danego programu i tym samym niedopuszczenie do potencjalnego nadużycia programu. 
Słowa kluczowe: domena zaufania, jednokrotne uwierzytelnianie, tcpd, xinetd, bastion, twierdza. 
## Zastosowanie domen zaufania
Domena zaufania to środowisko sieciowe wraz z działającymi w nim usługami, w którym występuje jednolity mechanizm kontroli dostępu. W wypadku opisywanej niżej domeny zaufania mechanizm kontroli opiera się na zaufaniu, jakim darzą wyszczególnionego hosta pozostałe hosty, jeżeli chodzi o uwierzytelnianie użytkowników. W tak zorganizowanej domenie grupa hostów/serwerów/usług ufa wyszczególnionemu hostowi, że ten przeprowadzi silne uwierzytelnianie. Zaufanie grupy hostów opiera się na idei, według której, jeśli użytkownik uwierzytelnił się w wystarczający sposób przed wybranym hostem, to znaczy, że jest tym, za kogo się podaje, i nie ma potrzeby ponownie przeprowadzać procedury uwierzytelniania przy dostępie do innych hostów. Wybrany host, który jest odpowiedzialny za silne uwierzytelnianie użytkowników, określany jest mianem twierdzy lub bastionu. 
Utworzenie domeny zaufania i wprowadzenie mechanizmu jednokrotnego uwierzytelniania pozwoli zmniejszyć uciążliwość korzystania z rozproszonego środowiska sieciowego, w którym jest zlokalizowanych wiele usług wymagających kontroli dostępu. Myśląc o wadach, należy wziąć pod uwagę, co się stanie, gdy wybrany host przeprowadzający uwierzytelnianie przestanie być dostępny dla użytkowników. Prawdopodobnie spowoduje to efekt odmowy usługi (_ang. Denial of Service_). Kolejny ważny problem to kompromitacja wybranego hosta, który zapewnia silne uwierzytelnianie. Czy spowoduje to natychmiastową kompromitację całej domeny? Przed wprowadzeniem mechanizmu jednokrotnego uwierzytelniania należy dokładnie rozpatrzyć wszystkie zalety i wady takiego rozwiązania. 
## Przykładowa domena zaufania
[![Przykladowa domena zaufania.png](https://wazniak.mimuw.edu.pl/images/f/f7/Przykladowa_domena_zaufania.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Przykladowa_domena_zaufania.png>)
### Polecenie rlogin w systemie Linux
Komenda rlogin pozwala na zdalny dostęp do konta systemu operacyjnego. Podejmuje próbę zalogowania bieżącego użytkownika lokalnego systemu operacyjnego na wskazanym systemie zdalnym. Jeśli nie wyspecyfikowano inaczej, wybrane zostaje zdalne konto użytkownika o takiej samej nazwie jak bieżąca nazwa użytkownika w systemie lokalnym. Po zalogowaniu, uruchamiana jest w trybie interaktywnym domyślna powłoka zdefiniowana dla konta zdalnego, np. sh, csh, tcsh itp. Poniżej zaprezentowano użycie polecenia rlogin: 
```
localhost>rlogin remotehost

```

Dalsza praca z systemem zdalnym odbywa się podobnie jak w przypadku usługi sieciowej TELNET. Jeśli wymagane jest podanie hasła dla konta zdalnego, rlogin poprosi użytkownika o podanie go przed zalogowaniem: 
```
localhost> rlogin remotehost
Password: 
remotehost> 

```

Polecenie rlogin umożliwia również dostęp do konta użytkownika o innej nazwie niż bieżący użytkownik. Wówczas nazwę użytkownika zdalnego konta należy podać po opcji: -l: 
```
localhost>rlogin -l username remotehost
username's Password:
remotehost>

```

Hasło jest transmitowane tekstem jawnym, podobnie jak w protokole TELNET, co stanowi poważne zagrożenie poufności hasła do zdalnego konta. Jednak istnieje możliwość wykorzystania procedury jednokrotnego uwierzytelniania (_ang. single sign-on_) zalogowania użytkownika bez potrzeby podawania hasła dostępu do konta. Umożliwia to mechanizm zaufania do systemów, z których nawiązywane są sesje rlogin. W systemowym pliku /etc/hosts.equiv umieszczona jest lista nazw komputerów, z których dozwolony jest zdalny dostęp na lokalne konto użytkownika bez pytania o hasło. Lista ta dotyczy wszystkich kont lokalnych. Oto zawartość przykładowego pliku /etc/hosts.equiv na komputerze uran: 
```
saturn
mars
neptun

```

Tak zdefiniowana lista zaufanych systemów pozwala każdemu użytkownikowi posiadającemu konto na dowolnym z wymienionych na niej systemów, a więc na saturnie, marsie lub neptunie (w tym w szczególności na wszystkich trzech), zalogować się na własne konto w systemie uran, bez wymogu podania hasła. Istotne jest, aby konto na które użytkownik uzyskuje dostęp nazywało się identycznie jak zdalne konto, z którego ten użytkownik nawiązuje połączenie. 
Każdy z użytkowników może również zdefiniować w pliku ~/.rhosts własną dodatkową listę obejmującą nazwy komputerów(i ewentualnie nazwy użytkowników na tych komputerach), które on obdarza zaufaniem i umożliwia im zdalny dostęp na swoje konto bez podania hasła. Jest to użyteczne, gdy ten sam użytkownik posiada różne konta(być może o różnych nazwach użytkownika) na kilku systemach i nie chce wystawiać swojego hasła na transmisje niechronionym kanałem lub chce umożliwić zdalne wywoływanie poleceń na swoim koncie. Poniżej zaprezentowano przykładową konfigurację pliku ~/.rhosts na koncie Michal w systemie Uran: 
```
jowisz
dcslab iksinski

```

Taka lista pozwala zalogować się bez wymogu podania hasła użytkownikowi systemu jowisz posiadającemu konto o identycznej nazwie(czyli michal) oraz użytkownikowi iksinski z systemu dcslab. 
Mechanizm tak skonfigurowanego zaufania jest jednak bardzo niebezpieczny, gdyż wystawia konto na ataki podszywania się pod zaufanego hosta. 
## Zabezpieczanie usług sieciowych programem tcpd
W systemie Linux istnieje szereg prostych usług sieciowych, które nie posiadają rozbudowanych mechanizmów kontroli dostępu lub w ogóle nie posiadają żadnych. Do grupy takich usług można zaliczyć tzw. small services np. finger, chargen, rlogin, echo czy tftp. 
W większości sytuacji usługi te w obecnych systemach Linux/Unix są domyślnie wyłączone więc zagrożenie z ich strony jest nikłe. Czasami zdarzają się jednak sytuacje, gdy niektóre usługi z tej grupy pełnią ważną rolę w systemach komputerowych i należy wdrożyć mechanizm kontroli dostępu dla takiej usługi. Nie tylko proste usługi sieciowe mogą być chronione przez program tcpd. Usługa bez której nie byłaby możliwa praca zdalna na maszynach Linux/Unix czyli ssh również może posiadać dodatkowe zabezpieczenie w formie reguł bezpieczeństwa dla programu tcpd. W większości sytuacji jednak program tcpd stosuje się jako mechanizm kontroli dostępu usług sieciowych, które nie posiadają wystarczających wbudowanych mechanizmów kontroli dostępu. Dlatego też znajomość obsługi programu tcpd może być konieczna w niektórych systemach komputerowych. 
### Podstawy
Program tcpd służy do zabezpieczania usług sieciowych poprzez sprawdzanie zgodności przychodzącego ruchu sieciowego z regułami bezpieczeństwa zdefiniowanymi w dwóch plikach konfiguracyjnych: /etc/hosts.allow i /etc/hosts.deny. W pierwszej kolejności należy zrozumieć w jaki sposób program tcpd podejmuje decyzje odnośnie przepuszczania i blokowania ruchu sieciowego skierowanego do danych usług sieciowych: 
  * dostęp zostanie przyznany gdy w pliku /etc/hosts.allow znajdzie się odpowiednia reguła bezpieczeństwa
  * w przeciwnym wypadku dostęp zostanie zablokowany, gdy w pliku /etc/hosts.deny znajdzie się odpowiednia reguła bezpieczeństwa
  * w przeciwnym wypadku dostęp zostanie przyznany.


Należy zauważyć, że tak skonstruowany mechanizm sprawdzania możliwości przyznania dostępu powoduje, że brak dopasowania w obu plikach konfiguracyjnych spowoduje przyznanie dostępu. 
Komplet niezbędnych informacji o programie tcpd i jego możliwościach można znaleźć w podręczniku systemowym systemu Linux/Unix wykonując polecenia: 
  * man tcpd - ogólne informacje o programie tcpd
  * man 5 hosts_access - informacje o plikach konfiguracyjnych dla programu tcpd
  * man 5 hosts_options - informacje o możliwych opcjach jakie można użyć w plikach konfiguracyjnych


### Przykład zabezpieczania usługi tftp programem tcpd
Konfiguracja programu tcpd zostanie pokazana na przykładzie zabezpieczania usługi tftp. Usługa tftp jest prostszą wersją protokołu ftp wykorzystywaną przez wiele urządzeń sieciowych. Dlatego też ta usługa posłuży jak przykład. Usługa tftp oprócz aktywnych urządzeń sieciowych jest również wykorzystywana do tzw. provisioningu. Provisioning jest to możliwość dostarczania usług, różnego rodzaju zasobów użytkownikom lub urządzeniem np. modemom kablowym, które w ten sposób pobierają plik z konfiguracją. Dlatego też usługa tftp jest nadal aktywnie wykorzystywana w rozbudowanych środowiskach sieciowych np. w sieciach ISP(_ang. Internet Service Provider_). 
Usługę tftp można uruchomić jako samodzielną usługę sieciową(tryb _standalone_) lub po przez superdemona inetd lub xinetd. W niniejszym opracowaniu usługa tftp będzie uruchomiona za pomocą superdemona xinetd. Poniżej zaprezentowano przykładową zawartość pliku konfiguracyjnego dla demona xinetd do uruchomienia usługi tftp: 
```
service tftp
{
	per_source	= 5
	socket_type = dgram
	protcol	= udp
	wait		= yes
	user 		= root
	server	= /usr/sbin/tcpd
	server_args	= in.tftpd -t 60 -s /var/tftp -u tftpd 
	disable	= no
	banner_fail	= /etc/xinetd/fail.banner
	cps		= 100 10
}

```

W konfiguracji przedstawionej powyżej należy w szczególności zwrócić uwagę na dwa parametry. Parametr server wskazuje na plik wykonywalny programu usługi sieciowej, którą ma uruchomić xinetd np. tftp, finger, rlogin. Z uwagi, że zależy nam aby usługa tftp była chroniona przez program tcpd w parametrze server podajemy ścieżkę do pliku wykonywalnego tcpd a nie faktycznej usługi która ma być uruchomiona przez demona xinetd. Parametr server_args zawiera parametry jakie mają być przekazane do programu podanego w parametrze server. W tym przypadku są to parametry dla programu tcpd oraz zestaw parametrów dla usługi tftp, którą uruchomi program tcpd. W przedstawionym powyżej przykładzie parametr server_args zawiera nazwę wykonywalnego pliku serwera usługi tftp, plik in.tftpd. Drugi parametr określa jak długo po uruchomieniu programu in.tftpd ma on być aktywny. Trzeci parametr wymusza przejście do katalogu /var/tftp z zastosowaniem mechanizmu chroot. Ostatni parametr wymusza zmianę użytkownika z jakim będzie działał program in.tftpd na użytkownika tftpd. Superdemon xinetd posiada szereg przydatnych funkcjonalności odnośnie kwestii bezpieczeństwa uruchamianych usług sieciowy. Autor niniejszego opracowania zaleca zapoznanie się z nimi w celu lepszego zrozumienia możliwości xinetd. Komplet informacji na temat superdemona xinetd można znaleźć na stronie domowej projektu xinted[1]. 
Druga etap zabezpieczania usługi tftp to przygotowanie reguł bezpieczeństwa dla programu tcpd. W pierwszej kolejności należy zastanowić się, komu będzie przyznawany dostęp do usługi tftp i czy chcemy aby działanie usługi tftp było zapisywanie w plikach logu a jeśli tak to w jaki sposób. Powinno nam zależeć na możliwe ścisłym określeniu, kto może korzystać z usługi tftp oraz powinniśmy posiadać informacje o działaniu samej usługi. Poniżej zaprezentowano przykładowe pliki /etc/hosts.allow i /etc/hosts.deny, które poruszają wyżej wymienione kwestie: 
```
#plik /etc/hosts.allow
in.tftpd: 192.168.1. : spawn (logger -p auth.notice -t %d access_granted to hostname %c ip %a ) & 
#lub prostrza wersja bez logowania 
in.tftpd: 192.168.1.

```
```
#plik /etc/hosts.deny
in.tftpd: ALL EXCEPT 192.168.1. : spawn (logger -p auth.notice -t %d permission denied to hostname %c ip %a ) &
#lub globalne zablokowanie dostepu
ALL: ALL

```

W powyższych przykładach pokazano w jaki sposób można ograniczyć dostęp do usługi tftp tylko dla hostów z adresami 192.168.1. Brak ostatniego oktetu w adresie IP 192.168.1 sugeruje, że będzie on pomijany przy sprawdzaniu możliwości dostępu do usługi, liczą się tylko pierwsze trzy oktety. W powyższych przykładach każda akcja dostępu do usługi tftp zakończona otrzymaniem dostępu bądź odmową jest odnotowywana w plikach logu poprzez tworzenie odpowiedniego wpisu. Należy zauważyć, że w środowiskach sieciowych w których usługa tftp jest intensywnie używana odnotowywanie każdej udanej próby dostępu do usługi tftp będzie prowadzić do tworzenia wielu wpisów w pliku logów systemowych, co z kolei będzie prowadziło do utrudnionej analizy działania usługi tftp z uwagi na ilość zgromadzonych danych. Dlatego w uzasadnionych przypadkach zalecane jest ograniczenie odnotowywania udanych prób uzyskania połączenia lub nawet zaprzestanie zbierania takich informacji. Zalecane jest jednak zbieranie informacji o nieudanych próbach uzyskania dostępu do usługi tftp z uwagi na potencjalny atak na tą usługę lub na demona xinted prowadzący w skrajnych przypadkach do efektu odmowy dostępu(atak typu DOS) dla uprawnionych hostów z uwagi na wyczerpanie zasobów systemowych przyznanych usłudze tftp. 
## Podsumowanie
Domeny zaufania mogą w wydatny sposób pomóc w ułatwieniu korzystania z usług sieciowych w rozbudowanych środowiskach sieciowych. Duże ułatwienie niesie za sobą również duże ryzyko kompromitacji serwerów usługowych z uwagi na brak niezależnej procedury uwierzytelniania użytkowników. Dlatego też przed wdrożeniem takiego rozwiązania należy szczegółowo rozważyć wszystkie za i przeciw gdyż kompromitacja usług, ujawnienie poufnych danych lub ich kradzież mogą okazać się bardzo kosztowne. 
W wielu środowiskach sieciowych nadal działają usługi, które wydawałoby się odeszły w zapomnienie gdyż przeważająca większość użytkowników nie korzysta z nich. Niektóre z tych usług pełnia krytyczną role w swoich środowiskach i należy dbać o ich bezpieczeństwo. Program tcpd może okazać się pomocny w zabezpieczaniu takich usług. 
## Zadania
  * Zapoznanie się w możliwościami programu rlogin
  * Utworzenie przykładowej domeny zaufania i wykorzystanie programu rlogin do zdalnego dostępu w hosta Bastion do dowolnego hosta w domenie zaufania.
  * Zapoznanie się z możliwościami programu xinted.
  * Zapoznanie się z możliwościami usługi tftp.
  * Zapoznanie się z możliwościami programu tcpd
  * Konfiguracja usługi tftp w oparciu o program tcpd i pliki konfiguracyjne hosts.allow i hosts.deny.
  * Zapoznanie się z programem logger.


## Problemy do dyskusji
  * Jakie zagrożenia i ułatwienia niesie utworzenie domeny zaufania w oparciu o mechanizm jednokrotnego uwierzytelniania i program rlogin.
  * Czy możliwe jest zablokowanie możliwości samodzielnego dodawania zaufanych hostów w domenie zaufania przez nieuprzywilejowanych użytkowników?
  * Jakie wbudowane mechanizmy bezpieczeństwa posiada usługa tftp?
  * Jakie mechanizmy bezpieczeństwa posiada superdemon xinetd?
  * Czy używając programu tcpd można odesłać jakąś wiadomość użytkownikowi próbującemu uzyskać dostęp, jeśli tak to w jaki sposób?
  * Do czego służy mechanizm chroot?


## Bibliografia
  * [1] Strona domowa projektu xinted: <http://www.xinted.org>
  * Strona podręcznika systemowego dla programu logger: man logger
  * Strona podręcznika systemowego dla programu rlogin i in.rlogind: man rlogin, man in.rlogind
  * Strona podręcznika systemowego dla programu tcpd: man tpcd
  * Strona podręcznika systemowego dla programu chroot: man chroot


---


# Umacnianie ochrony systemu opearacyjnego serwerowych środowisk MS Windows

# Bezpieczeństwo systemów komputerowych - laboratorium 3:Umacnianie ochrony systemu opearacyjnego serwerowych środowisk MS Windows
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
Umacnianie ochrony systemu operacyjnego MS Windows 
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Konta użytkowników](https://wazniak.mimuw.edu.pl/<#Konta_użytkowników>)
    * [2.1 Inspekcja zdarzeń logowania](https://wazniak.mimuw.edu.pl/<#Inspekcja_zdarzeń_logowania>)
    * [2.2 Dezaktywacja kont](https://wazniak.mimuw.edu.pl/<#Dezaktywacja_kont>)
    * [2.3 Konta użytkowników uprzywilejowanych](https://wazniak.mimuw.edu.pl/<#Konta_użytkowników_uprzywilejowanych>)
  * [3 System plików](https://wazniak.mimuw.edu.pl/<#System_plików>)
    * [3.1 Szyfrowanie danych](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_danych>)
    * [3.2 Archiwa z ochroną kryptograficzną](https://wazniak.mimuw.edu.pl/<#Archiwa_z_ochroną_kryptograficzną>)
  * [4 Poczta elektroniczna](https://wazniak.mimuw.edu.pl/<#Poczta_elektroniczna>)
    * [4.1 Certyfikaty adresów pocztowych](https://wazniak.mimuw.edu.pl/<#Certyfikaty_adresów_pocztowych>)
  * [5 Środowisko sieciowe](https://wazniak.mimuw.edu.pl/<#Środowisko_sieciowe>)
    * [5.1 Otoczenie sieciowe i udziały sieciowe](https://wazniak.mimuw.edu.pl/<#Otoczenie_sieciowe_i_udziały_sieciowe>)
    * [5.2 Ukrycie komputera w otoczeniu sieciowym](https://wazniak.mimuw.edu.pl/<#Ukrycie_komputera_w_otoczeniu_sieciowym>)
    * [5.3 Połączenia sieciowe](https://wazniak.mimuw.edu.pl/<#Połączenia_sieciowe>)
    * [5.4 Zapory sieciowe](https://wazniak.mimuw.edu.pl/<#Zapory_sieciowe>)
  * [6 Podsumowanie](https://wazniak.mimuw.edu.pl/<#Podsumowanie>)
  * [7 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [8 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Systemy operacyjne w rodziny Microsoft Windows należą niewątpliwie do liderów popularności na rynku systemów operacyjnych. W większości zastosować domowych popularne Windowsy sprawdzają się bardzo dobrze, co owocuje dużym przywiązaniem użytkowników do tych produktów. Istnieją zastosowania w których systemy te słabo bądź w ogóle nie sprawdzają się jednakże z powodu wygody użytkowania i przystępnego środowiska graficznego są liderem na rynku systemów biurkowych. Systemy MS Windows posiadają wbudowane mechanizmy podwyższające bezpieczeństwo i znajomość tych podstawowych rozwiązań powinna być znana każdemu użytkownikowi tych systemów. W niniejszym opracowaniu zostaną przedstawione różne aspekty odnośnie podnoszenia poziomu bezpieczeństwa pracy w systemach MS Windows XP. Rozwiązania prezentowane należą do grupy zabiegów określanych mianem utwardzania systemu(_ang. system hardening_) i mają na celu podnieść poziom bezpieczeństwa oferowanego przez system. Posługując się określeniem system Windows autor ma na myśli system Microsoft Windows XP Professional z dodatkiem SP2. 
## Konta użytkowników
Pierwszą czynnością podczas pracy z systemem Windows XP jest zalogowanie się do systemu. W większości przypadków konto na które następuje logowanie jest chronione hasłem użytkownika. Możliwe jest również automatyczne logowanie na konto danego użytkownika bez podawania hasła. Jednak taka konfiguracja jest niezalecana. System Windows posiada rozbudowane możliwości konfiguracji różnych aspektów odnośnie kont użytkowników i procedury logowania. Opcje konfiguracyjne zlokalizowane są w oknie _Ustawienia zabezpieczeń lokalnych_ i podgrupach _Zasady konta_ i _Zasady haseł_. Poniżej zaprezentowano zrzut ekranowy prezentujący okno ustawień zabezpieczeń lokalnych: 
[![1 windows hardening.png](https://wazniak.mimuw.edu.pl/images/5/51/1_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:1_windows_hardening.png>)
Zadania: 
  1. Zweryfikuj trudność złamania haseł w systemie za pomocą wybranego narzędzia typu reactive password checking(np. LC4)
  2. Włącz opcję hasło ma spełniać wymagania co do złożoności i ustaw następujące parametry: 
    1. maksymalny wiek hasła: 42 dni
    2. minimalna długość hasła: 8 znaków
    3. minimalny okres ważności hasła: 2 dni
    4. 24 ostatnie hasła pamiętane w historii
    5. wyłączone odwracalne szyfrowanie haseł
  3. Ustaw następujące parametry blokady konta: 
    1. próg blokady: 4 próby
    2. czas trwania blokady: 30 minut
    3. zerowanie licznika prób: po 30 minutach
  4. Wyłącz przechowywanie skrótów kryptograficznych haseł w postaci LMhash: 
    1. Znajdź odpowiednią opcję(Zasady zabezpieczeń lokalnych, grupa Opcje zabezpieczeń, atrybut: „Zabezpieczenia sieci: nie przechowuj wartości hash programu LAN Manager).
    2. Sprawdź ponownie programem LC4 czy skróty Lmhash są dostępne


### Inspekcja zdarzeń logowania
Inspekcję(_ang. Logging_) zdarzeń logowania można włączyć poprzez _Ustawienia zabezpieczeń lokalnych_. Inspekcja ta jest jednym z elementów _Zasad lokalnych_. Zarejestrowane zdarzenia można przeglądać przy pomocy programu _Podgląd zdarzeń_ w pozycji _System_. 
Zadania: 
  * Włącz i przetestuj inspekcję zdarzeń logowania zakończonych sukcesami i niepowodzeniem.


### Dezaktywacja kont
Wszelkie konta (w tym szczególnie konta zakładane domyślnie przez system lub aplikacje) poza rzeczywiście niezbędnymi powinny być zablokowane (lub usunięte). Poniżej zaprezentowano okno konsoli zarządzania komputerem z uaktywnionym podglądem właściwości dla użytkownika „ _Gość_ ": 
[![2 windows hardening.png](https://wazniak.mimuw.edu.pl/images/b/b1/2_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:2_windows_hardening.png>)
Zadania: 
  * Zidentyfikuj i wyłącz nieużywane konta.


### Konta użytkowników uprzywilejowanych
Konta użytkowników uprzywilejowanych należy szczególnie starannie chronić przed wykorzystaniem przez osoby nieuprawnione. W pewnym stopniu można utrudnić nielegalne wykorzystanie konta Administratora (włamanie) poprzez zmianę standardowej nazwy tego konta, często oczekiwanej przez intruzów. Jednak wszelkie konta w systemie posiadają oprócz nazw także identyfikatory numeryczne, które nie ulegają zmianie nawet po ewentualnej zmianie nazwy konta (zaawansowane metody ataku korzystają z takich identyfikatorów). Poniżej zaprezentowano zrzut ekranowy pokazując w jaki sposób można zmienić nazwę użytkownika uprzywilejowanego: 
[![3 windows hardening.png](https://wazniak.mimuw.edu.pl/images/8/88/3_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:3_windows_hardening.png>)
Zadania: 
  * Zmień nazwę konta Administratora. Zweryfikuj zdalnie (np. za pomocą narzędzia _wininfo_) dostępne informacje o kontach w swoim systemie.


## System plików
System plików NTFS umożliwia związanie z każdym zasobem plikowym (w tym: katalogiem) list kontroli dostępu ACL (_Access Control List_). Dostęp do prostych ustawień ACL pliku (katalogu) jest możliwy z poziomu np. Eksploratora Windows w opcji Właściwości (menu Plik lub kontekstowe). Poniżej zaprezentowano okno właściwości dla wybranego pliku: 
[![4 windows hardening.png](https://wazniak.mimuw.edu.pl/images/7/7f/4_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:4_windows_hardening.png>)
Rozszerzone listy ACL są dostępne po wyborze uprawnień zaawansowanych: 
[![5 windows hardening.png](https://wazniak.mimuw.edu.pl/images/b/b6/5_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:5_windows_hardening.png>)
Zadania: 
  * Zaloguj się na konto administratora (Szef).
  * Utwórz w katalogu _Moje dokumenty_ plik _test.txt_. Dla tego pliku wykonaj następujące operacje:


  1. korzystając z prostych ACL nadaj uprawnienia do odczytu dla użytkownika Sherlock Holmes
  2. sprawdź rozszerzone ACL dla tego użytkownika
  3. sprawdź jakie czynne uprawnienia posiada ten użytkownik


  * Następnie dla pliku Test.txt:


  1. sprawdź jakie czynne uprawnienia posiada użytkownik James Bond
  2. korzystając z prostych ACL odbierz uprawnienia do zapisu użytkownikowi James Bond
  3. sprawdź rozszerzone ACL dla tego użytkownika
  4. sprawdź jakie czynne uprawnienia posiada ten użytkownik


### Szyfrowanie danych
System plików NTFS umożliwia również ochronę kryptograficzną zasobów plikowych, metodą szyfrowania symetrycznego (algorytmem DESX). Poniżej zaprezentowano zrzut ekranowy z oknem właściwości dotyczących szyfrowania: 
[![6 windows hardening.png](https://wazniak.mimuw.edu.pl/images/9/94/6_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:6_windows_hardening.png>)
Użyty do szyfrowania klucz właściciela pliku przechowywany jest w certyfikacie użytkownika. Razem z nim system operacyjny utrzymuje też klucz uniwersalny usługi systemowej _Data Recovery Agent_. Klucze te są widoczne w aplikacji Microsoft Management Console (program **mmc**). Poniżej zaprezentowano okno konsoli zarządzania certyfikatami: 
[![7 windows hardening.png](https://wazniak.mimuw.edu.pl/images/3/3c/7_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:7_windows_hardening.png>)
Po uruchomieniu konsoli należy z menu Plik wybrać opcję Dodaj/Usuń przystawkę (np. klawiszem ^M), a następnie dodać przystawkę _Certyfikaty – bieżący użytkownik_ : 
[![8 windows hardening.png](https://wazniak.mimuw.edu.pl/images/f/fc/8_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:8_windows_hardening.png>)
Zadania: 
  * Utwórz plik tekstowy _tajne.txt_ o dowolnej treści. Wyświetl jego zawartość w Eksploratorze oraz w konsoli tekstowej (np. poleceniem _type_).
  * Następnie zaszyfruj ten plik i spróbuj ponownie wyświetlić jego zawartość.
  * Wyświetl informacje o zaszyfrowanym pliku poleceniem _efsinfo_.
  * Odszukaj certyfikat EFS klucza szyfrowania.
  * Zaloguj się jako inny użytkownik i spróbuj wyświetlić zawartość tego pliku.


### Archiwa z ochroną kryptograficzną
Wiele programów kompresujących i archiwizujących posiada możliwość zabezpieczania spakowanych danych hasłem dostępu. Wśród takich produktów wyróżnia się BCarchive (firmy Jetico) oferujący profesjonalną ochronę kryptograficzną z wykorzystaniem szyfrowania asymetrycznego i certyfikatami kluczy publicznych. Umożliwia to bezpieczny dostęp do zawartości archiwum np. odbiorcy pocztowemu bez potrzeby uprzedniego ustalania hasła lub klucza. Poniżej zaprezentowano okno programu BCarchive: 
[![9 windows hardening.png](https://wazniak.mimuw.edu.pl/images/a/ab/9_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:9_windows_hardening.png>)
## Poczta elektroniczna
Niektóre programy klientów posiadają możliwość wykorzystania mechanizmów kryptograficznych: szyfrowania i / lub podpisywania korespondencji pocztowej. Taką możliwość posiadają np. popularne produkty z rodziny Mozilla (Mozilla Mail lub Thunderbird) z rozszerzeniem Enigmail (na platformę Windows to rozszerzenie trzeba zainstalować oddzielnie). Enigmail integruje klienta pocztowego z popularnym i powszechnie stosowanym w Internecie systemem PGP (np. pakiet OpenPGP lub GnuPG, niezależnie instalowane w systemie). System PGP umożliwia m.in. certyfikację kluczy pocztowych metodą wzajemnego zaufania (Web of Trust). Poniżej zaprezentowano okno klienta poczty Mozilla Mail zintegrowanego z dodatkiem Enigmail: 
[![10 windows hardening.png](https://wazniak.mimuw.edu.pl/images/5/51/10_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:10_windows_hardening.png>)
Zadania: 
  * Zainstaluj system GnuPG oraz rozszerzenie Enigmail klienta pocztowego Mozilla Thunderbird.
  * Korzystając w programie Thunderbird z funkcji OpenPGP Key Management wygeneruj swoją parę kluczy kryptograficznych.
  * Wyślij podpisany list do siebie samego. Sprawdź reakcję systemu.
  * Wyślij podpisany list do innego użytkownika ze swojej grupy i odbierz jego list.
  * Zweryfikuj poprawność podpisu otrzymanego listu.
  * Zrealizuj komunikację z szyfrowaniem całej przesyłki pocztowej.


### Certyfikaty adresów pocztowych
Jednym z bardziej popularnych ośrodków certyfikacji w Internecie jest firma Thawte. Wiele przeglądarek WWW i aplikacji pocztowych zawiera certyfikat głównego urzędu certyfikacji tej firmy, co pozwala ufać podpisom tego urzędu. Poniżej zaprezentowano certyfikat firmy Thawte: 
[![11 windows hardening.png](https://wazniak.mimuw.edu.pl/images/d/d6/11_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:11_windows_hardening.png>)
Korzystając ze strony <http://www.thawte.com> można pozyskać darmowy certyfikat poświadczający własny adres pocztowy: 
[![12 windows hardening.png](https://wazniak.mimuw.edu.pl/images/9/9a/12_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:12_windows_hardening.png>)
## Środowisko sieciowe
Rdzennymi w środowisku MS Windows protokołami sieciowymi obsługującymi zasoby udostępniane w otoczeniu sieciowym są NetBIOS i SMB (Server Message Block). Nie są to, niestety, wyrafinowane protokoły, szczególnie pod względem bezpieczeństwa. 
### Otoczenie sieciowe i udziały sieciowe
Udziałami nazywa się w protokole SMB udostępnione poprzez sieć zasoby systemu operacyjnego. Polecenie net z argumentem share pozwala wyświetlić listę udziałów bieżącego systemu: 
[![13 windows hardening.png](https://wazniak.mimuw.edu.pl/images/e/ec/13_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:13_windows_hardening.png>)
Systemy MS Windows bezpośrednio po instalacji tworzą pewne udziały domyślne (dla Windows XP są to np. C$ oraz ADMIN$), które, jakkolwiek na ogół nie stanowią istotnej luki bezpieczeństwa, często nie są potrzebne i powinny być wyłączone. W tym celu niezbędna jest modyfikacja rejestru systemowego. Dla systemu Windows XP w gałęzi _HLM\SYSTEM\CurrentControlSet\Services\LanManServer_ w kluczu parameters należy dodać wartość _AutoShareWks_ typu DWORD równą 0: 
[![14 windows hardening.png](https://wazniak.mimuw.edu.pl/images/3/32/14_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:14_windows_hardening.png>)
Po załadowaniu tak zmodyfikowanego rejestru (po restarcie) udziały domyślne nie są widoczne: 
[![15 windows hardening.png](https://wazniak.mimuw.edu.pl/images/6/62/15_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:15_windows_hardening.png>)
Zadania: 
  * Usuń udziały domyślne swojego stanowiska komputerowego. Zweryfikuj rezultat.


### Ukrycie komputera w otoczeniu sieciowym
W systemie Windows XP istnieje możliwość ukrycia nazwy bieżącego komputera w otoczeniu sieciowym, z zachowaniem jednocześnie możliwości udostępniania zasobów. Ukrycie takie w czasie bieżącej sesji umożliwia polecenia net z argumentem _config server_ : 
```
C:\> net config server /hidden:yes

```

_/hidden_ – opcja ukrycia nazwy w otoczeniu sieciowym, możliwe wartości yes oraz no Aby trwale uczynić nazwę bieżącego komputera niewidoczną w otoczeniu sieciowym należy zmodyfikować wpis w rejestrze systemowym w gałęzi _HLM\SYSTEM\CurrentControlSet\Services\LanManServer_ w kluczu parameters należy dodać wartość Hidden typu DWORD równą 1. 
Zadania: 
  * Sprawdź widoczność swojego stanowiska w otoczeniu sieciowym. Przetestuj ukrywanie jego nazwy. Czy cały czas możliwe jest korzystanie z udostępnianych zasobów?


### Połączenia sieciowe
Szczegółowe informacje o stanie komunikacji sieciowej (np. informacje o aktywnych bieżąco usługach, nawiązanych połączeniach, statystyki dotyczące ruchu sieciowego) można uzyskać za pomocą polecenia _netstat_ : 
[![16 windows hardening.png](https://wazniak.mimuw.edu.pl/images/5/50/16_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:16_windows_hardening.png>)
### Zapory sieciowe
W systemie Windows XP SP 2 dostępne jest Centrum zabezpieczeń zawierające m.in. zaporę sieciową: 
[![17 windows hardening.png](https://wazniak.mimuw.edu.pl/images/a/a1/17_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:17_windows_hardening.png>)
Zapora wbudowana w system Windows jest bardzo prymitywna i nie daje użytkownikowi wielu możliwości: 
[![18 windows hardening.png](https://wazniak.mimuw.edu.pl/images/9/9f/18_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:18_windows_hardening.png>)
Zadania: 
  * Zablokuj całkowicie komunikację z wykorzystaniem protokołu ICMP. Przetestuj konfigurację za pomocą polecenia _ping_.


Niestety, ta prosta zapora nie umożliwia precyzyjnej kontroli ruchu sieciowego. Z tego powodu nieodzowne stają się oddzielne produkty typu Personal Firewall. Dobrym przykładem może być Kerio Personal Firewall (firmy Kerio), który pozwala na wielopoziomowe filtrowanie ruchu sieciowego: 
[![19 windows hardening.png](https://wazniak.mimuw.edu.pl/images/0/0f/19_windows_hardening.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:19_windows_hardening.png>)
## Podsumowanie
Systemy z rodziny MS Windows są bardzo popularne. Nie wszystkie elementy systemu stoją na tak wysokim poziomie jak graficzny interfejs użytkownika. W Internecie można znaleźć wiele przykładów na to iż systemy te są podatne na wiele groźnych ataków dzięki którym użytkownicy mogą być narażeni na utratę dany, szantaże i straty materialne spowodowane kradzieżą numerów kont, haseł itp. Firma Microsoft dokłada starań aby jej produkty były coraz mniej podatne na różnego typu ataki jednak nie zwalnia to użytkowników od interesowania się bezpieczeństwem systemu operacyjnego którego używają na co dzień. Dlatego też podstawowa wiedza z dziedziny szeroko rozumianego bezpieczeństwa systemów komputerowych i informacji jest konieczna do przyswojenia jeśli użytkownicy nie chcą być biernymi obserwatorami nadużyć komputerowych popełnianych na ich systemach operacyjnych. 
## Problemy do dyskusji
  * Jakie znasz ataki na które podatne są systemy z rodziny MS Windows?
  * Czy wiesz jak się bronić przed najczęstszymi atakami takim jak wirusy, robaki internetowe, programy szpiegujące i spam?
  * Czy znasz i używasz popularne zamienniki programów stosowanych na platformie MS Windows które są często powodem problemów z bezpieczeństwem? Czy potrafisz wymienić takie programy?


---


#  RSBAC

# Bezpieczeństwo systemów komputerowych - laboratorium 4:Utwardzanie ochrony systemu operacyjnego serwerowych środowisk Linuksowych: RSBAC
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Informacje o systemie RSBAC](https://wazniak.mimuw.edu.pl/<#Informacje_o_systemie_RSBAC>)
  * [3 Utwardzanie ochrony systemu na podstawie zabezpieczenia serwera Apache przy wykorzystaniu RSBAC](https://wazniak.mimuw.edu.pl/<#Utwardzanie_ochrony_systemu_na_podstawie_zabezpieczenia_serwera_Apache_przy_wykorzystaniu_RSBAC>)
    * [3.1 Instalacja systemu RSBAC oraz podstawowe polecenia](https://wazniak.mimuw.edu.pl/<#Instalacja_systemu_RSBAC_oraz_podstawowe_polecenia>)
      * [3.1.1 Pierwsze uruchomienie](https://wazniak.mimuw.edu.pl/<#Pierwsze_uruchomienie>)
      * [3.1.2 2.Przygotowanie systemu do bezpiecznego używania serwera apache2](https://wazniak.mimuw.edu.pl/<#2.Przygotowanie_systemu_do_bezpiecznego_używania_serwera_apache2>)
        * [3.1.2.1 Dodanie możliwości zmiany uprawnień (użytkownika) na uid=30 (wwwrun) oraz gid=9 (www) przez aplikację /usr/sbin/apache2-prefork](https://wazniak.mimuw.edu.pl/<#Dodanie_możliwości_zmiany_uprawnień_\(użytkownika\)_na_uid=30_\(wwwrun\)_oraz_gid=9_\(www\)_przez_aplikację_/usr/sbin/apache2-prefork>)
        * [3.1.2.2 Ustawienie typów RC (Role Compatibility)](https://wazniak.mimuw.edu.pl/<#Ustawienie_typów_RC_\(Role_Compatibility\)>)
          * [3.1.2.2.1 Stworzenie typów](https://wazniak.mimuw.edu.pl/<#Stworzenie_typów>)
          * [3.1.2.2.2 Przypisanie typów do zasobów](https://wazniak.mimuw.edu.pl/<#Przypisanie_typów_do_zasobów>)
        * [3.1.2.3 Ustawienie ról RC](https://wazniak.mimuw.edu.pl/<#Ustawienie_ról_RC>)
          * [3.1.2.3.1 Stworzenie ról](https://wazniak.mimuw.edu.pl/<#Stworzenie_ról>)
          * [3.1.2.3.2 Przypisanie ról](https://wazniak.mimuw.edu.pl/<#Przypisanie_ról>)
        * [3.1.2.4 Utworzenie szablonu gniazdka](https://wazniak.mimuw.edu.pl/<#Utworzenie_szablonu_gniazdka>)
        * [3.1.2.5 Ustawienie uprawnień](https://wazniak.mimuw.edu.pl/<#Ustawienie_uprawnień>)
          * [3.1.2.5.1 dla roli WWW_Server:](https://wazniak.mimuw.edu.pl/<#dla_roli_WWW_Server:>)
          * [3.1.2.5.2 dla roli WWW_User:](https://wazniak.mimuw.edu.pl/<#dla_roli_WWW_User:>)
      * [3.1.3 Uruchomienie serwera apache2](https://wazniak.mimuw.edu.pl/<#Uruchomienie_serwera_apache2>)
  * [4 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [5 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [6 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)
  * [7 Dodatek A](https://wazniak.mimuw.edu.pl/<#Dodatek_A>)
  * [8 Dodatek B](https://wazniak.mimuw.edu.pl/<#Dodatek_B>)


## Wprowadzenie
Utwardzanie ochrony systemu operacyjnego jest szczególnie ważne dla serwerów pracujących bezustannie oraz dla serwerów o zakładanym wysokim poziomie bezpieczeństwa przechowującym tajne dane. System taki powinien być odporny na większość (jeśli nie wszystkie) możliwe próby ataku, włamania. Oczywiście jest to bardzo trudne do osiągnięcia, jeśli w ogóle jest to możliwe. Już w latach 80-tych zaczęto się zastanawiać nad zwiększeniem bezpieczeństwa systemów serwerowych, głównym organizatorem tych rozszerzeń były organizacje wojskowe i rządowe, które musiały dobrze chronić informacje. Zaproponowano wówczas nowy model bezpieczeństwa - **Obowiązkową Kontrolę Dostępu (MAC),** zamiast aktualnie wykorzystywanej **Uznaniowej Kontroli Dostępu (DAC).**
Rozwój systemów wykorzystujących politykę MAC jest dosyć powolny, głównie ze względu na trudności administracyjne tych systemów. Jednak jako ich bardzo duży plus jest odporność na większość ataków, włamań - warunkiem jednakże jest poprawne skonfigurowanie polityki, co jest zadaniem bardzo trudnym. 
Niniejsze ćwiczenie ma zaznajomić z utwardzaniem ochrony na podstawie systemu wykorzystującego politykę MAC o nazwie RSBAC (Rule-set Based Access Control). 
## Informacje o systemie RSBAC
System RSBAC został stworzony przez Amon Ott w 1996-97 jako praca magisterska. RSBAC jest cały czas rozwijany przez jego twórcę oraz grono jego współpracowników. Projekt ten jest całkowicie otwarty, jednak jego rozwój nie jest bardzo szybki ze względu na wysoki poziom bezpieczeństwa, który ma zapewniać. 
RSBAC to zestaw łat na jądro systemu Linux rozszerzających bezpieczeństwo systemu. Wspiera on mechanizmy takie jak: 
  * ścisła kontrola dostępu (MAC - Mandatory Access Control),
  * rozszerzone prawa do plików,
  * listy kontroli dostępu (ACL - Access Control Lists),
  * role,
  * typy,
  * piaskownice (rozszerzone polecenie chroot),
  * wiele innych.


Dzięki modułowej budowie, RSBAC jest bardzo elastyczny. Każdy moduł daje pewne możliwości zapewniania bezpieczeństwa, ale często dany problem można rozwiązać na kilka sposobów przy użyciu różnych modułów. Wybór odpowiedniego modułu/rozwiązania należy do administratora. 
## Utwardzanie ochrony systemu na podstawie zabezpieczenia serwera Apache przy wykorzystaniu RSBAC
### Instalacja systemu RSBAC oraz podstawowe polecenia
Na zainstalowany system Linux powinno się skompilować nowe jądro systemu wykorzystujące system RSBAC oraz zainstalować (wpierw skompilować) narzędzia niezbędne do konfiguracji systemu RSBAC. 
Istnieją dwa rodzaje narzędzi, polecenia w trybie tekstowym oraz polecenia z interfejsem użytkownika. Największym narzędziem jest rsbac_menu, który umożliwia dostęp do wszystkich możliwych ustawień wszystkich modułów, jest to narzędzie z interfejsem użytkownika. 
Każde inne narzędzie wprowadza użytkownika bezpośrednio do dokładniejszych informacji/ustawień. 
#### Pierwsze uruchomienie
Pierwsze uruchomienie spowoduje utworzenie domyślnych reguł, które pozwalają na uruchomienie systemu, jednak nie pozwalają na zalogowanie się. Jest to spowodowane zablokowaniem możliwości zmiany użytkownika przez wszystkie programy (między innymi przez login), można to ominąć dodając przy starcie opcję rsbac_auth_enable_login. Jednak zaraz po zalogowaniu się należy stworzyć użytkownika _security officer_ : secoff (uid=400), który będzie ukrytym zarządcą systemu i do jego zadań należy konfiguracja zabezpieczeń systemu w wykorzystaniem rozszerzeń RSBAC. 
Ustawienie uprawnień do zmiany uprawnień dla programu /bin/login: 
```
 attr_set_fd FILE auth_may_setuid 1 /bin/login

```

#### 2.Przygotowanie systemu do bezpiecznego używania serwera apache2
Na początku należy ustalić w jaki sposób będziemy zabezpieczać serwer. Po pierwsze należy określić, które katalogi będą podlegały restrykcją: 
  * konfiguracja serwera apache2 - /etc/apache2/*
  * katalog z logami - /var/log/apache2/*
  * plik blokady - /var/run/apache2.pid
  * katalog ze stronami www - /srv/www/htdocs, /usr/share/apache2/error, /usr/share/apache2/icons
  * katalog ze skryptami - /srv/www/cgi-bin
  * katalog plików tymczasowych - /tmp
  * katalog z globalną konfiguracją - /etc


Rozdzielenie katalogów ze skryptami i stronami www pozwala nam zwiększyć bezpieczeństwo. 
##### Dodanie możliwości zmiany uprawnień (użytkownika) na uid=30 (wwwrun) oraz gid=9 (www) przez aplikację /usr/sbin/apache2-prefork
```
 auth_set_cap FILE add /usr/sbin/httpd2-prefork 30
 auth_set_cap -g FILE add /usr/sbin/httpd2-prefork 8

```

##### Ustawienie typów RC (Role Compatibility)
###### Stworzenie typów
Korzystając z aplikacji rsbac_rc_type_menu tworzymy typy FD. Należy wybrać "New Type", zaakceptować numer, a następnie zmienić nazwę na: 
  * WWW_Config
  * WWW_Logfile
  * WWW_LockFiles
  * WWW_Files
  * WWW_Cgi-bin
  * Configfiles
  * Tempfiles


Następnie należy skopiować uprawnienia z "General FD" do wszystkich powyższych nowo utworzonych typów, poprzez "Copy Rights to Type". Należy jeszcze stworzyć typ NETOBJ o nazwie HTTP_NETOBJ (oraz UNIX_NETOBJ) i skopiować uprawnienia z "General_NETOBJ" 
###### Przypisanie typów do zasobów
Wykorzystać program rsbac_fd_menu do przyporządkowania typów do odpowiednich katalogów: 
  * typ Configfiles do katalogu /etc
  * typ Tempfiles do katalogu /tmp
  * typ WWW_Config do katalogu /etc/apache2
  * typ WWW_Logfile do katalogu /var/log/apache2
  * typ WWW_LockFiles do katalogu /var/run/apache2 (należy go wcześniej utworzyć)


Nie można przypisać typu do pliku (PidFile), gdyż plik ten jest usuwany przy wyłączeniu serwera, a uprawnienia są przypisywane do konkretnych i-węzłów, a nie do nazw. 
Dodatkowo trzeba zmodyfikować konfigurację serwera, aby wykorzystywał ten katalog, w pliku /etc/apache2/httpd.conf należy dopisać linię: PidFile /var/run/apache2/httpd2.pid oraz w pliku /etc/init.d/apache2 zmodyfikować linię pidfile=... tak aby odpowiadała temu samemu plikowi. 
  * typ WWW_Files do katalogu /srv/www/htdocs
  * typ WWW_Cgi-bin do katalogu /srv/www/cgi-bin


Przed restartowaniem systemu należy sprawdzić, czy wszystkie pliki i katalogi, które miały zmieniane uprawnienia, posiadają prawa dostępu dla użytkownika root. Dopiero tak ustawiony system można restartować. 
##### Ustawienie ról RC
###### Stworzenie ról
Wykorzystać program rsbac_rc_role_menu, aby utworzyć dwie nowe role, tworzymy je poprzez kopiowanie z General User, a następnie należy zmienić nazwy na: 
  * WWW_Server - potrzebny do startu serwera
  * WWW_User - potrzebny do dalszego działania serwera


###### Przypisanie ról
  * WWW_Server należy przyporządkować jako RC Initial Role do pliku /usr/sbin/httpd2-prefork programem rsbac_fd_menu
  * WWW_User należy przyporządkować jako RC Default Role użytkownikowi wwwrun (30) przy użyciu programu rsbac_user_menu


To przyporządkowanie ról zapewni samoczynną zmianę roli wykorzystywanej przez serwer, gdyż na początku uruchamia się z prawami użytkownika root oraz rolą WWW_Server, następnie zmienia uprawnienia na uprawnienia użytkownika wwwrun, któremu została przyporządkowana rola WWW_User i tym samym rola zostanie zmieniona. 
##### Utworzenie szablonu gniazdka
Wykorzystać program rsbac_nettemp_def_menu. Stworzyć nowy szablon gniazdka [New Template] (z numerem mniejszym niż domyślne szablony, gdyż rsbac sprawdza od najniższego numeru, aż do pierwszego znalezionego). Szablon powinien być skonfigurowany następująco: 
```
 Template: 20000
 Name: HTTP
 Address Family: INET
 Socket Type: STREAM
 Address: 0.0.0.0 (można podać adres IP konkretnego interfejsu)
 Valid Length: 32
 Protocol: TCP
 Network Device:
 Min Port: 80
 Max Port: 80

```

wybrać NetTemp Attributes: 
```
 Template number: 20000/HTTP
 RC Type: HTTP_NETOBJ (jedyny RC który jeszcze nie był przyporządkowany)
 RC Type NT: 0/General NETTEMP

```

Stworzyć drugi szablon: 
```
 Template: 10000
 Name: UNIX
 Address Family: UNIX
 Socket Type: STREAM
 Address:
 Valid Length:
 Protocol:
 Network Device:
 Min Port:
 Max Port:

```

wybrać NetTemp Attributes: 
```
 Template number: 10000/UNIX
 RC Type: UNIX_NETOBJ (jedyny RC który jeszcze nie był przyporządkowany)
 RC Type NT: 0/General NETTEMP

```

##### Ustawienie uprawnień
Wykorzystać program rsbac_rc_role_menu do ustawienia uprawnień dwóm stworzonym rolom: 
###### dla roli WWW_Server:
```
 Type Comp FD -> General_FD -> R + Exec + Map_exec
 Type Comp FD -> WWW_Config -> R
 Type Comp FD -> WWW_Logfiles -> R + Append_open + Write (opcjonalnie)
 Type Comp FD -> WWW_LockFiles -> R + Create + Delete + Write_Open + Write + Truncate
 Type Comp FD -> WWW_Files -> R
 Type Comp FD -> WWW_Cgi-bin -> R
 Type Comp FD -> Tempfiles -> R + W + Create
 Type Comp FD -> Configfiles -> R
 Type Comp NETOBJ -> General_NETOBJ -> Create + Modify_system_data
 Type Comp NETOBJ -> HTTP_NETOBJ -> Bind + Listen + Close
 Type Comp NETOBJ -> UNIX_NETOBJ -> Create + Close + Connect

```

###### dla roli WWW_User:
```
 Type Comp FD -> General_FD -> R + Execute + Map_exec
 Type Comp FD -> WWW_Config -> R
 Type Comp FD -> WWW_Logfiles -> R + Append_open
 Type Comp FD -> WWW_LockFiles -> R
 Type Comp FD -> WWW_Files -> R
 Type Comp FD -> WWW_Cgi-bin -> R + Execute
 Type Comp FD -> Tempfiles -> R + W + Create
 Type Comp FD -> Configfiles -> Search (Opcjonalnie)
 Type Comp NETOBJ -> General_NETOBJ -> Accept + Send + Receive + Net_shutdown + Write + Read + Get_status_data
 Type Comp NETOBJ -> HTTP_NETOBJ -> –
 Type Comp NETOBJ -> UNIX_NETOBJ -> –

```

#### Uruchomienie serwera apache2
Po uprzednim skonfigurowaniu serwera oraz przypisaniu mu uprawnień należy uruchomić serwer poprzez skrypt /etc/rc.d/apache2 start. 
Dla celów testowych można w trakcie ustawiania próbować uruchamiać serwer apache2 jednocześnie obserwując plik /var/log/messages, gdzie są umieszczane wszystkie komunikaty o błędach. 
## Zadania
  * Uruchomić system Linux wykorzystując nowe jądro (RSBAC), w trybie rsbac_auth_enable_login - wybrać przy starcie komputera z menu bootloadera.
  * Uruchomić serwer apache2 i sprawdzić czy poprawnie działa, jeśli nie należy sprawdzić dlaczego (komunikaty błędów systemu) i umożliwić zmianę uprawnień.
  * Napisać prosty skrypt php, który odczytuje plik /etc/passwd i przesyła poprzez www.
  * Sprawdzić działanie oraz sprawdzić komunikaty błędów systemu (konsola 10'ta).
  * Zalogować się jako użytkownik secoff i uruchomić skrypt "apache_rsbac.sh".
  * Powtórnie sprawdzić poprawność działania skryptu oraz komunikaty błędów.
  * Napisać "rc_set_item ROLE 5 type_comp_fd 9 R", a następnie sprawdzić działanie skryptu i komunikaty błędów.
  * Następnie należy zapoznać się ze skryptem "apache_rsbac.sh".


Następnie należy stworzyć katalog /srv/www/htdocs/tajne/ oraz plik index.html w tym katalogu i zablokować dostęp do tego katalogu z poziomu zabezpieczeń RSBAC, korzystając z już utworzonej polityki, jedynie dopisując lub modyfikując ją. Rozwiązanie należy przedstawić prowadzącemu zajęcia. 
## Problemy do dyskusji
  * Wady, zalety systemu RSBAC.
  * Polityka MAC, a polityka DAC.
  * Czy potrzebne są systemy wspierające politykę MAC?
  * Co rozumiemy przez błąd dnia zerowego?


## Bibliografia
[WWW] Projekt RSBAC - <http://www.rsbac.org>
## Dodatek A
Wszystkie polecenia można wykonywać bez pośrednictwa menu, poniżej zostaną zaprezentowane wszystkie polecenia wykorzystywane podczas ćwiczenia. 
Umożliwienie zmiany uprawnień serwerowi Apache z praw administratora "root" (oraz grupy root) na użytkownika wwwrun(30) i grupę www(8): 
```
 (zmiana grupy)	auth_set_cap -g FILE add /usr/sbin/httpd2-prefork 8
 (zmiana użytkownika)auth_set_cap FILE add /usr/sbin/httpd2-prefork 30

```

Utworzenie nowych (o nowych numerach) typów poprzez skopiowanie domyślnego typu (General FD ‑ 0 lub General NETOBJ - 0), wykorzystujemy dwa rodzaje typów FD i NETOBJ: 
```
 rc_copy_type FD 0 4
 rc_copy_type FD 0 5
 rc_copy_type NETOBJ 0 4

```

Zmiana nazwy nowo utworzonym typom: 
```
 rc_set_item TYPE 4 type_fd_name WWW_Config
 rc_set_item TYPE 4 type_netobj_name HTTP_NETOBJ

```

Przypisanie plików i katalogów do konkretnych typów: 
```
 (Katalog) attr_set_file_dir RC DIR /etc/apache2 rc_type_fd 4
 (Plik) attr_set_file_dir RC FILE /etc/localtime rc_type_fd 4

```

Utworzenie nowych ról poprzez skopiowanie ich z domyślnej roli (General User): 
```
 rc_copy_role 0 4
 rc_copy_role 0 5

```

Zmiana nazwy nowo utworzonym rolom: 
```
 rc_set_item ROLE 4 name WWW_Server
 rc_set_item ROLE 5 name WWW_User

```

Przypisanie użytkownikowi wwwrun domyślnej roli WWW_User (5): 
```
 attr_set_user RC wwwrun rc_def_role 5

```

Przypisanie programowi (plikowi) roli WWW_Server (4), jaką otrzyma w przypadku uruchomienia: 
```
 attr_set_file_dir RC FILE /usr/sbin/httpd2-prefork rc_initial_role 4

```

Utworzenie nowego szablonu gniazdka o numerze 20000 i nazwie HTTP: 
```
 net_temp new_template 20000 HTTP

```

Przypisanie typu adresu na Internetowy: 
```
 net_temp set_address_family 20000 INET

```

Ustalenie wielkości adresu na 32 bity: 
```
 net_temp set_valid_len 20000 32

```

Ustalenie typu gniazdka na strumieniowe: 
```
 net_temp set_type 20000 STREAM

```

Ustalenie protokołu na TCP: 
```
 net_temp set_protocol 20000 TCP

```

Ustalenie minimalnego portu, który będzie miał prawo wykorzystać: 
```
 net_temp set_min_port 20000 80

```

Ustalenie maksymalnego portu, który będzie miał prawo wykorzystać: 
```
 net_temp set_max_port 20000 80

```

Przypisanie szablonu gniazdka do typu NETOBJ o nazwie HTTP_NETOBJ (4): 
```
 attr_set_net RC NETTEMP rc_type 4 20000

```

Ustalanie uprawnień dla poszczególnych typów i ról: 
ustalenie dla roli WWW_Server (4), typu General FD (0) praw odczytu, wykonywanie: 
```
 rc_set_item ROLE 4 type_comp_fd 0 R EXECUTE MAP_EXEC

```

ustalenie dla typu WWW_Config (4) przy korzystaniu z roli WWW_Server (4) praw odczytu: 
```
 rc_set_item ROLE 4 type_comp_fd 4 R

```

ustalenie dla typu General NETOBJ (0) przy korzystaniu z roli WWW_Server (4) praw tworzenia i modyfikacji danych systemowych: 
```
 rc_set_item ROLE 4 type_comp_netobj 0 CREATE MODIFY_SYSTEM_DATA

```

## Dodatek B
Skrypt ustanawiający politykę bezpieczeństwa określoną w powyższym ćwiczeniu. 
_rsbac_apache2_ : 
```
 export LANG=C
 auth_set_cap -g FILE add /usr/sbin/httpd2-prefork 8
 auth_set_cap FILE add /usr/sbin/httpd2-prefork 30
 
 rc_copy_type FD 0 4
 rc_copy_type FD 0 5
 rc_copy_type FD 0 6
 rc_copy_type FD 0 7
 rc_copy_type FD 0 8
 rc_copy_type FD 0 9
 rc_copy_type FD 0 10
 rc_copy_type NETOBJ 0 4
 rc_set_item TYPE 4 type_fd_name WWW_Config
 rc_set_item TYPE 5 type_fd_name WWW_Logfiles
 rc_set_item TYPE 6 type_fd_name WWW_Lockfiles
 rc_set_item TYPE 7 type_fd_name WWW_Files
 rc_set_item TYPE 8 type_fd_name WWW_Cgi-bin
 rc_set_item TYPE 9 type_fd_name ConfigFiles
 rc_set_item TYPE 10 type_fd_name TempFiles
 rc_set_item TYPE 4 type_netobj_name HTTP_NETOBJ
 rc_set_item TYPE 5 type_netobj_name UNIX_NETOBJ
 
 attr_set_file_dir RC DIR /etc/apache2 rc_type_fd 4
 attr_set_file_dir RC FILE /etc/localtime rc_type_fd 4
 attr_set_file_dir RC DIR /var/log/apache2 rc_type_fd 5
 attr_set_file_dir RC DIR /var/run/apache2 rc_type_fd 6
 attr_set_file_dir RC DIR /srv/www/htdocs rc_type_fd 7
 attr_set_file_dir RC DIR /srv/www/cgi-bin rc_type_fd 8
 attr_set_file_dir RC DIR /etc rc_type_fd 9
 attr_set_file_dir RC DIR /tmp rc_type_fd 10
 
 rc_copy_role 0 4
 rc_copy_role 0 5
 rc_set_item ROLE 4 name WWW_Server
 rc_set_item ROLE 5 name WWW_User
 attr_set_user RC wwwrun rc_def_role 5
 attr_set_file_dir RC FILE /usr/sbin/httpd2-prefork rc_initial_role 4
 
 net_temp new_template 20000 HTTP
 net_temp set_address_family 20000 INET
 net_temp set_valid_len 20000 32
 net_temp set_type 20000 STREAM
 net_temp set_protocol 20000 TCP
 net_temp set_min_port 20000 80
 net_temp set_max_port 20000 80
 attr_set_net RC NETTEMP rc_type 4 20000
 
 net_temp new_template 10000 UNIX
 net_temp set_address_family 10000 UNIX
 net_temp set_type 10000 STREAM
 attr_set_net RC NETTEMP rc_type 5 10000
 
 rc_set_item ROLE 4 type_comp_fd 0 R EXECUTE MAP_EXEC
 rc_set_item ROLE 4 type_comp_fd 4 R
 rc_set_item ROLE 4 type_comp_fd 5 R APPEND_OPEN WRITE
 rc_set_item ROLE 4 type_comp_fd 6 R CREATE DELETE \
  WRITE_OPEN WRITE TRUNCATE
 rc_set_item ROLE 4 type_comp_fd 7 R
 rc_set_item ROLE 4 type_comp_fd 8 R
 rc_set_item ROLE 4 type_comp_fd 9 R
 rc_set_item ROLE 4 type_comp_fd 10 R W CREATE
 
 rc_set_item ROLE 4 type_comp_netobj 0 CREATE \
  MODIFY_SYSTEM_DATA
 rc_set_item ROLE 4 type_comp_netobj 4 BIND LISTEN CLOSE
 rc_set_item ROLE 4 type_comp_netobj 5 CREATE CLOSE CONNECT
 
 rc_set_item ROLE 5 type_comp_fd 0 R EXECUTE MAP_EXEC
 rc_set_item ROLE 5 type_comp_fd 4 R
 rc_set_item ROLE 5 type_comp_fd 5 R APPEND_OPEN
 rc_set_item ROLE 5 type_comp_fd 6 R
 rc_set_item ROLE 5 type_comp_fd 7 R
 rc_set_item ROLE 5 type_comp_fd 8 R EXECUTE
 rc_set_item ROLE 5 type_comp_fd 9 SEARCH
 rc_set_item ROLE 5 type_comp_fd 10 R W CREATE
 
 rc_set_item ROLE 5 type_comp_netobj 0 ACCEPT SEND RECEIVE \
  NET_SHUTDOWN READ WRITE GET_STATUS_DATA
 rc_set_item ROLE 5 type_comp_netobj 4

```

_rsbac_apache2_full_ : 
```
 export LANG=C
 auth_set_cap -g FILE add /usr/sbin/httpd2-prefork 8
 auth_set_cap FILE add /usr/sbin/httpd2-prefork 30
 
 rc_copy_type FD 0 4
 rc_copy_type FD 0 5
 rc_copy_type FD 0 6
 rc_copy_type FD 0 7
 rc_copy_type FD 0 8
 rc_copy_type FD 0 9
 rc_copy_type FD 0 10
 rc_copy_type FD 0 11
 rc_copy_type NETOBJ 0 4
 rc_set_item TYPE 4 type_fd_name WWW_Config
 rc_set_item TYPE 5 type_fd_name WWW_Logfiles
 rc_set_item TYPE 6 type_fd_name WWW_Lockfiles
 rc_set_item TYPE 7 type_fd_name WWW_Files
 rc_set_item TYPE 8 type_fd_name WWW_Cgi-bin
 rc_set_item TYPE 9 type_fd_name ConfigFiles
 rc_set_item TYPE 10 type_fd_name TempFiles
 rc_set_item TYPE 11 type_fd_name Library
 rc_set_item TYPE 4 type_netobj_name HTTP_NETOBJ
 rc_set_item TYPE 5 type_netobj_name UNIX_NETOBJ
 
 attr_set_file_dir RC DIR /etc/apache2 rc_type_fd 4
 attr_set_file_dir RC FILE /etc/localtime rc_type_fd 4
 attr_set_file_dir RC DIR /var/log/apache2 rc_type_fd 5
 attr_set_file_dir RC DIR /var/run/apache2 rc_type_fd 6
 attr_set_file_dir RC DIR /srv/www/htdocs rc_type_fd 7
 attr_set_file_dir RC DIR /srv/www/cgi-bin rc_type_fd 8
 attr_set_file_dir RC DIR /etc rc_type_fd 9
 attr_set_file_dir RC DIR /tmp rc_type_fd 10
 attr_set_file_dir RC DIR /lib rc_type_fd 11
 #attr_set_file_dir RC DIR /usr/lib rc_type_fd 11
 #
 # biblioteki potrzebne dla servera apache
 attr_set_file_dir RC DIR /usr/lib/apache2 rc_type_fd 11
 attr_set_file_dir RC DIR /usr/lib/php/extensions \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libaprutil-0.so.0.9.6 \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libgdbm.so.3.0.0 \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libdb-4.3.so \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libexpat.so.0.5.0 \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libapr-0.so.0.9.6 \
  rc_type_fd 11
 attr_set_file_dir RC FILE \
  /usr/lib/apache2-prefork/mod_cgi.so rc_type_fd 11
 attr_set_file_dir RC FILE \
  /usr/lib/apache2-prefork/mod_ssl.so rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libssl.so.0.9.7 \
  rc_type_fd 11
 attr_set_file_dir RC FILE /usr/lib/libcrypto.so.0.9.7 \
  rc_type_fd 11
 attr_set_file_dir RC FILE \
  /usr/lib/apache2-prefork/libphp4.so rc_type_fd 11
 
 rc_copy_role 0 4
 rc_copy_role 0 5
 rc_set_item ROLE 4 name WWW_Server
 rc_set_item ROLE 5 name WWW_User
 attr_set_user RC wwwrun rc_def_role 5
 attr_set_file_dir RC FILE \
  /usr/sbin/httpd2-prefork rc_initial_role 4
 
 net_temp new_template 20000 HTTP
 net_temp set_address_family 20000 INET
 net_temp set_valid_len 20000 32
 net_temp set_type 20000 STREAM
 net_temp set_protocol 20000 TCP
 net_temp set_min_port 20000 80
 net_temp set_max_port 20000 80
 attr_set_net RC NETTEMP rc_type 4 20000
 
 net_temp new_template 10000 UNIX
 net_temp set_address_family 10000 UNIX
 net_temp set_type 10000 STREAM
 attr_set_net RC NETTEMP rc_type 5 10000
 
 rc_set_item ROLE 4 type_comp_fd 0 SEARCH GET_STATUS_DATA
 rc_set_item ROLE 4 type_comp_fd 4 R
 rc_set_item ROLE 4 type_comp_fd 5 R APPEND_OPEN WRITE
 rc_set_item ROLE 4 type_comp_fd 6 R CREATE DELETE \
  WRITE_OPEN WRITE TRUNCATE
 rc_set_item ROLE 4 type_comp_fd 7 R
 rc_set_item ROLE 4 type_comp_fd 8 R
 rc_set_item ROLE 4 type_comp_fd 9 R
 rc_set_item ROLE 4 type_comp_fd 10 R W CREATE
 rc_set_item ROLE 4 type_comp_fd 11 R MAP_EXEC
 
 rc_set_item ROLE 4 type_comp_netobj 0 CREATE \
  MODIFY_SYSTEM_DATA
 rc_set_item ROLE 4 type_comp_netobj 4 BIND LISTEN CLOSE
 rc_set_item ROLE 4 type_comp_netobj 5 CREATE CLOSE CONNECT
 
 rc_set_item ROLE 5 type_comp_fd 0 SEARCH GET_STATUS_DATA
 rc_set_item ROLE 5 type_comp_fd 4
 rc_set_item ROLE 5 type_comp_fd 5 APPEND_OPEN WRITE \
  CHDIR CLOSE GET_PERMISSIONS_DATA GET_STATUS_DATA SEARCH
 rc_set_item ROLE 5 type_comp_fd 6
 rc_set_item ROLE 5 type_comp_fd 7 R
 rc_set_item ROLE 5 type_comp_fd 8 R EXECUTE
 rc_set_item ROLE 5 type_comp_fd 9 SEARCH
 rc_set_item ROLE 5 type_comp_fd 10 R W CREATE
 rc_set_item ROLE 5 type_comp_fd 11 
 
 rc_set_item ROLE 5 type_comp_netobj 0 ACCEPT SEND \
  RECEIVE NET_SHUTDOWN READ WRITE GET_STATUS_DATA
 rc_set_item ROLE 5 type_comp_netobj 4

```

---


# Modularne systemy uwierzytelniania i kontroli dostępu do systemu operacyjnego

# Bezpieczeństwo systemów komputerowych - laboratorium 5:Modularne systemy uwierzytelniania i kontroli dostępu do systemu operacyjnego
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Informacje o mechanizmie PAM](https://wazniak.mimuw.edu.pl/<#Informacje_o_mechanizmie_PAM>)
    * [2.1 Ogólne założenie uwierzytelniania w systemie Linux](https://wazniak.mimuw.edu.pl/<#Ogólne_założenie_uwierzytelniania_w_systemie_Linux>)
    * [2.2 System PAM](https://wazniak.mimuw.edu.pl/<#System_PAM>)
    * [2.3 Wybrane wtyczki mechanizmu PAM](https://wazniak.mimuw.edu.pl/<#Wybrane_wtyczki_mechanizmu_PAM>)
    * [2.4 Wpływ działania wtyczki na proces uwierzytelniania](https://wazniak.mimuw.edu.pl/<#Wpływ_działania_wtyczki_na_proces_uwierzytelniania>)
    * [2.5 Podsumowanie mechanizmu PAM](https://wazniak.mimuw.edu.pl/<#Podsumowanie_mechanizmu_PAM>)
  * [3 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [4 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [5 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Modularne systemy uwierzytelniania mają za zadanie ułatwić kontrolę dostępu do systemu operacyjnego. Kontrola to zarządzanie kontami użytkowników, a także ustawianie ograniczeń dla tych kont. 
Mechanizm PAM jest szeroko stosowanym mechanizmem w systemach Linux i posiada bardzo dużą rozbudowę, poprzez rozbudowę należy rozumieć wiele dostępnych modułów rozszerzających. 
Celem ćwiczenia jest zrozumienie mechanizmu PAM i zastosowanie kilku modułów w praktyce. 
## Informacje o mechanizmie PAM
System uwierzytelniania w systemie Linux wykorzystuje mechanizm PAM (Pluggable Authentication Modules - Dołączalne Wtyczki Uwierzytelniające). Implementację dla systemu Linux stworzył i cały czas rozwija Andrew G.Morgan. 
System PAM to zestaw bibliotek i wtyczek, które są wykorzystywane do uwierzytelniania użytkowników w systemie. Biblioteka jest wykorzystywana przez aplikację, aby wywołać procedurę uwierzytelniającą. Wtyczki określają możliwości systemu uwierzytelniającego, możliwościami taki są ograniczenie czasu logowania do konkretnych godzin, określenie różnych źródeł danych o użytkownikach (na przykład baza LDAP, MySQL i inne). 
### Ogólne założenie uwierzytelniania w systemie Linux
Każdy użytkownik w systemie jest jednoznacznie identyfikowany poprzez identyfikator użytkownika (ang. User Identifier - UID), każdy użytkownik należy do conajmniej jednej grupy użytkowników, która również posiada unikalny identyfikator grupy (ang. Group Identifier - GID); oczywiście liczba grup do której należy użytkownik może być dowolnie długa. 
Obiekty w systemie również mają przypisane UID i GID, dokładniej właściciela, którego UID jest przypisane plikowi i grupę - GID, do której należą użytkownicy danego obiektu. Oprócz właściciela i grupy wyróżniamy opcje dla pozostałych użytkowników, którzy nie kwalifikują się w żadnej z powyższych grup. Opcjami określanymi dla każdego obiektu i każdego poziomu dostępu są uprawnienia zaprezentowane w mechanizmach lokalnej kontroli dostępu. 
### System PAM
System uwierzytelniania PAM. Koncepcja i pierwsza implementacja dla systemu Solaris wykonana przez V.Samara i R.Schemersa w dokumencie _OSF RFC 86.0. "Unified Login with Pluggable Authentication Modules (PAM)"_ [SS95]. 
System PAM składa się z czterech komponentów: 
  * zarządzanie uwierzytelnianiem,
  * zarządzanie kontami,
  * zarządzanie sesjami,
  * zarządzania hasłami.


Każdy z powyższych komponentów może być ustawiony w indywidualny sposób dla różnych aplikacji. Możliwości zarządzania powyższymi komponentami są praktycznie nieograniczone, gdyż zależą od zastosowanych wtyczek systemu PAM. Liczba wtyczek dostarczanych z główną biblioteką PAM jest ograniczone, jednak nie jest problemem napisanie nowej wtyczki systemu PAM w celu stworzenia nowego zastosowania. 
Wszystkie aplikacje, które chcą wykorzystywać uwierzytelniania poprzez system PAM muszą zostać do tego przystosowane. Muszą posiadać odwołania do biblioteki systemu PAM, która jest odpowiedzialna za komunikację pomiędzy aplikacją a systemem PAM. System PAM po otrzymaniu zgłoszenia od aplikacji czyta plik konfiguracyjny dotyczący danej aplikacji i wczytuje wszystkie wtyczki, które zostały tam wymienione. Wtyczki te mają rozpocząć proces uwierzytelniania użytkownika i jeśli proces się powiedzie (lub nie) biblioteka zwróci odpowiednią odpowiedź aplikacji. 
### Wybrane wtyczki mechanizmu PAM
  * access - wtyczka określająca kto ma mieć dostęp do systemu oraz w jaki sposób może uzyskać dostęp,
  * cracklib - wtyczka sprawdzająca siłę hasła użytkownika, który dokonuje zmiany hasła; wtyczka dodatkowo może sprawdzać czy hasło nie jest którymś z poprzednich lub jak bardzo różni się od poprzedniego,
  * locking-out - wtyczka blokująca dostęp, zawsze zwraca nie poprawność logowania,
  * anonymous access - wtyczka umożliwiająca stworzenie anonimowego dostępu do serwera ftp,
  * resource limits - określa limity wykorzystania systemu przez użytkownika, limitami takimi można objąć wykorzystanie pamięci operacyjnej dla pojedyńczego procesu i dla wszystkich procesów użytkownika, maksymalna czas procesora, maksymalną liczbę logować użytkownika i wiele innych,
  * radius session - uwierzytelniania użytkownika przy wykorzystaniu zdalnego serwera Radius,
  * time control - określa dostęp użytkownika do systemu w zależności od czasu w którym próbuje on uzyskać dostęp,
  * kerberos - uwierzytelnianie użytkownika przy wykorzystaniu systemu Kerberos,
  * smart card - uwierzytelnianie użytkownika na podstawie karty chipowej,
  * One-time password authentication - uwierzytelnianie użytkownika na podstawie jednorazowych haseł,
  * SQL database based authentication - uwierzytelnianie użytkownika na podstawie wpisów w bazie danych; istnieją wtyczki do większość baz danych,
  * SecurID - uwierzytelnianie użytkownika poprzez tokeny, potrzebny jest do tego serwer, w którym tokeny są zarejestrowane,
  * voiceauth - uwierzytelnianie użytkownika na podstawie jego głosu,
  * LDAP - uwierzytelnianie użytkownika na podstawie wpisów w bazie LDAP,


### Wpływ działania wtyczki na proces uwierzytelniania
  * wymagana _(ang. required)_ - wtyczka musi zwrócić sukces,
  * wymagana _(ang. requisite)_ - wtyczka musi zwrócić błąd,
  * wystarczająca _(ang. sufficient)_ - wtyczka powinna zwrócić sukces, jednak jej porażka nie oznacza nie przyznania dostępu,
  * opcjonalna _(ang. optional)_ - wtyczka może zwrócić dowolną wartość, jednak znaczenie może być przy przekazywaniu uprawnień do aplikacji.


### Podsumowanie mechanizmu PAM
Możliwości systemu PAM są bardzo duże, umożliwiają ustawienie innych systemów uwierzytelniających różnym aplikacjom lub dla wszystkich aplikacji zastosowanie jednego systemu uwierzytelniania. 
Oczywiście uwierzytelnianie to jedna z części potrzebna do działania, potrzebne są jeszcze uprawnienia do obiektów, listy kontroli dostępu zostały omówione wcześniej. 
## Zadania
Wykorzystać zaprezentowane powyżej wtyczki w celu: 
  * ograniczenia czasowego logowania się użytkownika _guest_ do systemu do godzin 8:00 - 9:00 w poniedziałki (lub inny termin, którego weryfikację uda się przeprowadzić),
  * ograniczenie dostępu do systemu poprzez zdalne logowanie (na przykład przy użyciu SSH) użytkownika _root_ i zweryfikowanie poprawności działania,
  * ustawienie weryfikacji haseł oraz zablokowanie ustawianie identycznego hasła jak poprzednie 2 - zweryfikować poprawność działania,
  * ustawić wymuszanie limitów zasobowych (polecenie ulimit) dla użytkowników grupy _guest_ i zweryfikować poprawność tego wymuszania,
  * ustawienie więzienia (chroot) dla użytkownika _guest_ i sprawdzenie czy działa poprawnie,
  * ustawić system do wykonania uwierzytelniania przy użyciu zdalnego źródła użytkowników, na przykład usługi katalogowej LDAP, bazy danych MySQL.


## Problemy do dyskusji
  * czy mechanizm PAM posiada wady, jakie?
  * jakie są zalety mechanizmu PAM?
  * czy mechanizm PAM jest skalowalny?
  * dlaczego mechanizm PAM stał się podstawowym systemem uwierzytelniania w systemie Linux?
  * czy aplikacje mogą pomijać mechanizm PAM podczas uwierzytelniania użytkowników? jeśli tak to w jaki sposób? oraz czy jest to słuszne podejście?
  * czy istnieją inne rozwiązania uwierzytelniania w systemach Linux/Unix oraz czy dają lepsze/gorsze możliwości uwierzytelniania?


---


# Ograniczone środowiska wykonywania aplikacji, ograniczone powłoki systemu operacyjnego środowisk serwerowych, delegacja uprawnień administracyjnych

# Bezpieczeństwo systemów komputerowych - laboratorium 6:Ograniczone środowiska wykonywania aplikacji, ograniczone powłoki systemu operacyjnego środowisk serwerowych, delegacja uprawnień administracyjnych
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Informacje o mechanizmie limitów](https://wazniak.mimuw.edu.pl/<#Informacje_o_mechanizmie_limitów>)
    * [2.1 Możliwości mechanizmu limitów](https://wazniak.mimuw.edu.pl/<#Możliwości_mechanizmu_limitów>)
    * [2.2 Podsumowanie mechanizmu limitów](https://wazniak.mimuw.edu.pl/<#Podsumowanie_mechanizmu_limitów>)
  * [3 Informacje o mechanizmie SUDO](https://wazniak.mimuw.edu.pl/<#Informacje_o_mechanizmie_SUDO>)
    * [3.1 Możliwości mechanizmu na podstawie pliku konfiguracyjnego](https://wazniak.mimuw.edu.pl/<#Możliwości_mechanizmu_na_podstawie_pliku_konfiguracyjnego>)
    * [3.2 Podsumowanie mechanizmu SUDO](https://wazniak.mimuw.edu.pl/<#Podsumowanie_mechanizmu_SUDO>)
  * [4 Informacje o mechanizmie SUID i SGID](https://wazniak.mimuw.edu.pl/<#Informacje_o_mechanizmie_SUID_i_SGID>)
  * [5 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [6 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [7 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Ograniczanie środowiska wykonywania aplikacji i powłoki systemu umożliwia ograniczanie zasobów wykorzystywanych przez aplikację oraz przez konkretnych użytkowników. Wykorzystywany do tego celu jest mechanizm limitów w systemach Linux/Unix. 
Delegacja uprawnień administracyjnych wykorzystuje dwa mechanizmy. Pierwszym z nich jest mechanizm bitów SUID i SGID, drugim mechanizm SUDO. 
Celem ćwiczenia jest zrozumienie wszystkich wymienionych powyżej mechanizmów i zastosowanie ich w praktyce. 
## Informacje o mechanizmie limitów
Mechanizm limitów wykorzystywany w systemie Linux umożliwia ograniczanie liczby otwartych plików, liczby aktywnych procesów i wiele innych dla każdego z użytkowników. Jednocześnie wiele aplikacji korzysta ze osobnych kont użytkowników i dzięki temu możemy ograniczyć konkretne aplikacje. 
Mechanizm ten często nazywamy ulimit (_eng. user limit),_ czyli limity użytkownika. 
Limity narzucane są przez administratora systemu, aczkolwiek, użytkownik może je troszkę modyfikować, dokładniej może jedynie jeszcze bardziej siebie ograniczyć. 
### Możliwości mechanizmu limitów
Mechanizm limitów może ograniczać następujące zasoby: 
  * wielkość pliku core,
  * wielkość pamięci zajmowanej przez dane,
  * maksymalną wielkość pliku,
  * maksymalną ilość zajmowanej pamięci,
  * maksymalną liczbę jednocześnie otwartych plików,
  * maksymalną wielkość zajmowanych zasobów,
  * maksymalną wielkość stosu,
  * maksymalny czas procesora, który może wykorzystać,
  * maksymalną liczbę równoczesnych procesów,
  * ograniczenie przestrzeni adresowej(*),
  * maksymalną liczbę jednoczesnego zalogowania się użytkownika do systemu(*),
  * maksymalną liczbę zalogowań się do systemu(*),
  * priorytet z jakim mają być uruchamiane procesy użytkownika(*),
  * maksymalna liczba blokad na pliki,
  * maksymalna liczba oczekujących sygnałów do wysłania,
  * maksymalna ilość pamięci użyta dla kolejek typu POSIX,
  * maksymalny priorytet, do którego może być zwiększony priorytet procesu użytkownika(*),
  * maksymalny priorytet czasu rzeczywistego(*).


Ograniczenia z gwiazdkami (*) są jedynie dostępne z poziomu konfiguracji limitów poprzez PAM. 
Ograniczenia te można nadawać wykorzystując aplikację **ulimit** z odpowiednimi przełącznikami, jak również można wykorzystać mechanizm PAM, który umożliwia proste skonfigurowanie limitów dla użytkowników oraz grup systemu operacyjnego. 
### Podsumowanie mechanizmu limitów
Mechanizm limitów może znacznie ograniczyć środowisko dostępne dla użytkownika, można go używać pod warunkiem posiadania wiedzy, którzy użytkownicy wymagają jakich uprawnień. Oczywiście często trudno jest to w prosty sposób zdefiniować, poza tym trzeba brać pod uwagę, że użytkownicy nie lubią żadnych ograniczeń, więc nie można ich się pytać jak bardzo można ich ograniczyć, tylko dochodzić do tego co użytkownik powinien móc robić w systemie. Aplikacje również można w ten sposób ograniczać, na przykład serwer WWW działa na uprawnieniach konta _wwwrun_ , w ten sposób można ograniczyć to konto jednocześnie ograniczając serwer WWW. 
## Informacje o mechanizmie SUDO
Mechanizm SUDO ma za zadanie umożliwienie wykonywania aplikacji z innymi uprawnieniami, na przykład z uprawnieniami użytkownika _root_. Mechanizm ten opiera się na aplikacji poprzez którą mogą być uruchamiane inne aplikacje z innymi uprawnieniami. Aplikacja SUDO jest konfigurowalna przez administratora systemu i to on może ustalić jakie aplikacje mogą być uruchamiane z innymi uprawnieniami, a nawet z jakimi uprawnieniami oraz przez jakiego użytkownika. 
### Możliwości mechanizmu na podstawie pliku konfiguracyjnego
Plik konfiguracyjny znajduje się w _/etc/sudoers_ i jest dostępny jedynie dla administratora systemu. Dodatkowo powinien być on edytowany za pomocą polecenia _visudo_. 
Plik ten składa się z dwóch części: 
  * aliasy (podstawowe zmienne);
  * specyfikację użytkownika (które określają kto może co uruchomić).


Wyróżniamy 4 typy aliasów: 
  * user_alias
  * runas_alias
  * host_alias
  * cmnd_alias


Każdy z typów może zawierać troszkę inne wartości, jednak w ogólności są one proste do zapamiętania, na przykład user_alias może zawierać nazwy użytkowników, nazwy grup oraz inne. Szczegóły dotyczące aliasy znajdują się z podręczniku użytkownika SUDOERS(5). Poniżej kilka przykładów: 
```
User_alias	FULLTIMERS = adam, adrian, ania
User_alias	ADVUSER = bartek, piort
Runas_alias OP = root
Runas_alias DB = oracle
Host_alias	ORACLE = dblab, oracle, baza
Host_alias	CS = 150.254.0.0/16
Cmnd_alias	KILL = /usr/bin/kill
Cmnd_alias	SHELLS = /usr/bin/sh, /usr/bin/bash

```

Specyfikacja użytkownika określa jaki użytkownik może wykonać określone aplikacje z określonymi uprawnieniami. Domyślnie każda aplikacja będzie uruchamiana z uprawnieniami administratora, chyba, że podamy inaczej. Również można określić czy użytkownik będzie musiał podawać hasło, aby uzyskać dostęp do danej komendy. 
Przykłady: 
```
FULLTIMERS	CS = NOPASSWD: SHELLS, KILL

```

określa, że użytkownicy "FULLTIMERS" mogą na komputerach "CS" bez hasła wykonać komendy "SHELLS" i "KILL" z uprawnieniami _root_. 
```
bartek	ALL = (DB) NOPASSWD: SHELLS

```

użytkownik _bartek_ może na wszystkich komputerach wykonać bez hasła komendy "SHELLS" z uprawnieniami "DB" 
```
piotr	ALL, !ORACLE = (www) ALL, (OP) KILL, (DB) /usr/bin/ls

```

użytkownik _piotr_ może na wszystkich komputerach za wyjątkiem komputerów "ORACLE" wykonywać wszystkie komendy z uprawnieniami _www_ , natomiast komendy "KILL" z uprawnieniami "OP", a komendę "/usr/bin/ls" z uprawnieniami "DB" 
Większą liczbę przykładów i opisy można znaleźć w podręczniku użytkownika SUDOERS(5). 
### Podsumowanie mechanizmu SUDO
Mechanizm SUDO pozwala dopuszczać użytkowników do wykonywania aplikacji z innymi uprawnieniami, przy czym nie ma znaczenia czy aplikacja na to pozwala czy nie, gdyż jest to on niej nie zależne. Dodatkowo administrator systemu ma pełną kontrolę nad użytkownikami, którzy mogą posiadać możliwości wykorzystywania tego mechanizmu oraz ścisłe ograniczenia w jaki sposób mogą z nich korzystać. 
## Informacje o mechanizmie SUID i SGID
Mechanizm SUID i SGID jest najprostszym z wyżej wymienionych. Jest on także bardzo prosty i opiera się na systemie plików, gdyż z każdym plikiem możemy określić dodatkowy bit uprawnień, określający SUID i SGID. Na podstawie ustawionego tego bitu system operacyjny wykonuje aplikację z innymi uprawnieniami, dokładniej wykonuje ją z uprawnieniami właściciela aplikacji. 
Jeśli ustawimy bit SUID to aplikacja zostanie wykonana z uprawnieniami właściciela aplikacji, niezależnie od tego kto ją wykona, pod warunkiem, że posiada uprawnienia do jej wykonania. 
Natomiast bit SGID określa, że aplikacja zostanie wykonana z uprawnieniami grupy właściciela aplikacji, która to jest określona jako grupa danego pliku. 
Niestety mechanizm ten nie posiada żadnej kontroli, dlatego uważany jest za bardzo niebezpieczny i jedynie niektóre komendy powinny mieć ustawiony bit SUID, przykładem takiej aplikacji jest _/bin/ping_ lub inne komendy wymagające wysokich uprawnień. 
Przypisanie bitu SUID i SGID do pliku wykonywane jest za pomogą programu _chmod_ , na przykład _chmod u+s plik_ spowoduje dodanie bitu SUID, natomiast _chmod g+s plik_ spowoduje przypisanie bitu SGID. 
## Zadania
Wykorzystać zaprezentowane powyżej mechanizmy w celu: 
  * wykorzystaj mechanizm limitów do ograniczenia użytkownika _secoff_ w następujący sposób: ustal możliwość jednokrotnego logowana do systemu, dopisz ograniczenie na liczbę procesów oraz maksymalną wielkość nowo tworzonego pliku. Zweryfikuj poprawność działania wpisanych limitów,
  * wykorzystaj mechanizm SUDO, aby umożliwić użytkownikowi _secoff_ uruchamiać z uprawnieniami administratorskimi aplikacji _ls_ oraz aplikacji find z uprawnieniami użytkownika _wwwrun_ ,
  * wykorzystaj mechanizm SUDO do ustanowienia uprawnień dla _users_ do wykonywania polecenia ls z uprawnieniami użytkownika secoff oraz aplikacji minicom z uprawnieniami administratorskimi,
  * wykorzystaj mechanizm SUID i SGID do ustanowienia podobnych uprawnień jak w powyższych dwóch punktach, odpowiedz na pytanie na ile jest to możliwe i czy na pewno daliśmy tylko takie uprawnienia?
  * wykorzystaj aplikację _find_ do znalezienie wszystkich aplikacji posiadających ustawiony jeden z bitów SUID lub SGID, przedstaw listę prowadzącemu wraz z uzasadnieniem dlaczego akurat te aplikacje mają ustawiony ten bit.


## Problemy do dyskusji
  * czy przestawione powyżej mechanizmy posiada wady, jakie?
  * jakie są zalety powyższych mechanizmów?
  * czy można by rozbudować któryś z mechanizmów, jeśli tak to o jaką funkcjonalność?
  * które z mechanizmów powinien wykorzystywać administrator systemu chcący zapewnić bezpieczeństwo systemu, a których powinien się wystrzegać?


---


# Systemy kryptograficznej ochrony komunikacji warstwy aplikacyjnej

# Bezpieczeństwo systemów komputerowych - laboratorium 7:Systemy kryptograficznej ochrony komunikacji warstwy aplikacyjnej
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Aplikacja SSH w systemie Linux/Unix](https://wazniak.mimuw.edu.pl/<#Aplikacja_SSH_w_systemie_Linux/Unix>)
    * [2.1 Metody uwierzytelniania użytkownika.](https://wazniak.mimuw.edu.pl/<#Metody_uwierzytelniania_użytkownika.>)
    * [2.2 Stosowane algorytmy szyfracji](https://wazniak.mimuw.edu.pl/<#Stosowane_algorytmy_szyfracji>)
    * [2.3 Zarządzanie kluczami kryptograficznymi](https://wazniak.mimuw.edu.pl/<#Zarządzanie_kluczami_kryptograficznymi>)
    * [2.4 Tunele wirtualne warstwy aplikacji (TCP port forwarding)](https://wazniak.mimuw.edu.pl/<#Tunele_wirtualne_warstwy_aplikacji_\(TCP_port_forwarding\)>)
  * [3 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [4 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [5 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Kryptograficzna ochrona komunikacji coraz częściej wymagana jest przy przesyłaniu różnego rodzaju danych. W szczególności tymi danymi może być interaktywne połączenie w powłoką zdalnego systemu operacyjnego. Systemy nie wykorzystujące kryptograficznej ochrony komunikacji cały czas istnieją i są używane w sieci Internet, jednak coraz częstsze przechwytywanie ruchu, jego podsłuchiwanie wymusza zaczęcie stosowania bezpiecznych metod transmisji. Kryptografia to jedyna możliwość ochrony przed przypadkowym podsłuchaniem. Oczywiście nie można mieć pewności, że podsłuchujący nie będzie w stanie odszyfrować naszej transmisji, jednak trzeba starać mu się to utrudnić. 
Protokół SSH umożliwia bezpieczny dostęp do zdalnego konta. Protokół pozwala na zastosowanie bezpiecznego uwierzytelniania użytkownika i szyfrowanie transmisji. Korzysta z portu TCP o numerze 22. Ponadto możliwe jest też szyfrowane tunelowanie ruchu pomiędzy arbitralnymi portami TCP, co umożliwia tworzenie tuneli wirtualnych. Transmitowane dane mogą podlegać automatycznej kompresji. 
## Aplikacja SSH w systemie Linux/Unix
Program ssh zastępuje w działaniu program rlogin i rsh. 
```
 local> ssh –l username remotehost ls

```

Umożliwia jednakże osiągnięcie podwyższonego stopnia bezpieczeństwa przy dostępie do zdalnego konta. Cała transmisja jest bowiem szyfrowana (łącznie w procedurą logowania, a więc i ewentualnym przesłaniem hasła), a do weryfikacji tożsamości użytkownika również stosowane są mechanizmy kryptograficzne. 
#### Metody uwierzytelniania użytkownika.
Program ssh podejmuje próby uwierzytelnienia użytkownika w następującej kolejności: 
  * uwierzytelnianie przez mechanizm zaufania do systemów zdalnych połączony z kryptograficznym uwierzytelnieniem obu systemów metodą klucza asymetrycznego wraz z ustaleniem symetrycznego klucza sesji (metodą Dieffiego-Hellmana);
  * uwierzytelnienie użytkownika kryptograficzną metodą klucza asymetrycznego, typu _challenge-response_ (algorytm RSA lub DSA)
  * uwierzytelnianie klasyczne poprzez hasło systemowe użytkownika zdalnego (komunikacja jest jednak szyfrowana, więc hasło nie jest transmitowane tekstem jawnym).


Mechanizm zaufania może być identyczny, jak dla poleceń r (bazujący na plikach /etc/hosts.equiv oraz ~/.rhosts). Jednak, z powodu wysokiego niebezpieczeństwa jego stosowania, protokół SSH stosuje swój własny system zaufania, wykorzystujący pliki, odpowiednio, /usr/local/etc/shosts.equiv oraz ~/.shosts. Mimo tego, stosowanie mechanizmu zaufania nie jest rekomendowane i niektóre implementacje protokołu SSH nie obsługują tego mechanizmu (w szczególności w standardzie SSH2 nie przewiduje się już tego mechanizmu). 
Kryptograficzne uwierzytelnianie systemu zdalnego wykorzystuje zbiór kluczy publicz­nych zdalnych systemów znanych systemowi lokalnemu, przechowywanych w plikach /usr/local/etc/ssh_known_hosts oraz ~/.ssh/known_hosts. Mechanizm szyfrowania asymetrycz­nego i tajność kluczy prywatnych wystarcza do obrony systemu przed atakami typu DNS spoofing, IP spoofing czy routing spoofing. 
Kryptograficzne uwierzytelnianie zdalnego użytkownika wykorzystuje zbiór kluczy publicznych zaufanych użytkowników, przechowywanych w pliku ~/.ssh/authorized_keys. Weryfikacja tożsamości metodą _challenge-response_ , przy zachowaniu tajności kluczy prywatnych użytkowników, umożliwia bezpieczne uwierzytelnianie. 
Ssh dokonuje uwierzytelnienia przy pomocy algorytmu RSA. 
#### Stosowane algorytmy szyfracji
W aktualnej wersji SSH v.2 obsługiwane są następujące symetryczne algorytmy szyfracji komunikacji: 
  1. 3DES (wybierany domyślnie),


  * Arcfour - bardzo szybki algorytm, pochodny RC4,
  * Blowfish i CAST128 - algorytmy 128-bitowe


a także algorytmy podpisu elektronicznego (do zapewnienia integralności komunikacji): 
  * HMAC-MD5 oraz HMAC-SHA1.


### Zarządzanie kluczami kryptograficznymi
Do tworzenia pary kluczy kryptograficznych służy program ssh-keygen. Zapisuje on klucz prywatny użytkownika wygenerowany dla algorytmu DSA (lub RSA) w pliku ~/.ssh/id_dsa (odpowiednio ~/.ssh/id_rsa), a klucz publiczny w pliku ~/.ssh/id_dsa.pub (~/.ssh/id_rsa.pub). Dla dodatkowego zabezpieczenia, klucz prywatny może być zapisany w pliku w postaci zaszyfrowanej, domyślnie algorytmem 3DES. Posługiwanie się wówczas tym kluczem wymaga każdorazowo podania sekwencji traktowanej jako rodzaj hasła. 
```
 local> ssh–keygen –t dsa
 Generating public/private dsa key pair.
 Enter file in which to save the key (~/.ssh/id_dsa): 
 Enter passphrase (empty for no passphrase): 
 Enter same passphrase again: 
 Your identification has been saved in ~/.ssh/id_dsa.
 Your public key has been saved in ~/.ssh/id_dsa.pub.
 The key fingerprint is:
 5c:13:fc:48:75:19:9b:27:ec:5c:4f:d3:b1:a2:6c:da user@host.domain
 

```

Program ten jest również wykorzystywany do generacji kluczy systemu, prywatnego oraz publicznego, odpowiednio w plikach: /usr/local/etc/ssh_hosts_key i /usr/local/etc/ssh_hosts_key.pub. 
### Tunele wirtualne warstwy aplikacji (TCP port forwarding)
Istnieje możliwość zbudowania tunelu wirtualnego pomiędzy dwoma komputerami (np. bramami typu BastionHost), przechodzącego przez sieć niezabezpieczoną (np. publiczną), Tunel ten może być następnie wykorzystywany do bezpiecznej komunikacji w warstwie aplikacyjnej pomiędzy innymi komputerami (np. klientem znajdującym się przed pierwszą bramą i serwerem za drugą bramą). 
```
 gate1> ssh –L localport:server:serviceport gate2

```

Takie polecenie utworzy tunel pomiędzy bramami gate1 i gate2, który umożliwi komunikację poprzez port localport z usługą serviceport na komputerze server (‑L = Local port forwarding). Komunikacja jest zaszyfrowana na odcinku gate1-gate2. 
'_localport'_ - port TCP lokalnego systemu (bramy gate1) 
'_server'_ - nazwa (domenowa) lub adres (IP) komputera, którego port udostępniamy poprzez tunel wirtualny (za bramą gate1) 
'_serviceport'_ - udostępniany zdalnie port TCP na serwerze server 
Propagowanie połączeń w tunelu przedstawia schematycznie poniższy rysunek. 
[![Bsi 07 01.png](https://wazniak.mimuw.edu.pl/images/e/e6/Bsi_07_01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_07_01.png>)
Identyczny efekt do poprzedniego ma kolejne polecenie: 
```
 gate2> ssh –R remoteport:server:serviceport gate1

```

(‑R = Remote port forwarding). 
'_remoteport'_ - port TCP zdalnego systemu (bramy gate1) 
'_server'_ - nazwa (domenowa) lub adres (IP) komputera, którego port udostępniamy poprzez tunel wirtualny (przed bramą gate2) 
'_serviceport'_ - udostępniany zdalnie port TCP na serwerze server 
## Zadania
  * Za pomocą narzędzi z pakietu OpenSSH nawiąż połączenie ze wskazanym serwerem (np. gumis).
  * Wykonaj zdalnie w systemie tego serwera polecenie cat /etc/HOSTNAME.
  * Dokonaj skopiowania lokalnego pliku do wybranego podkatalogu na koncie w systemie zdalnym.
  * Wygeneruj parę kluczy kryptograficznych szyfrowania asymetrycznego dla swojego lokalnego konta (bez zabezpieczania hasłem pliku z kluczem prywatnym). Wykorzystaj klucze do uwierzytelniania użytkownika w systemie zdalnym.
  * Zabezpiecz hasłem plik ze swoim kluczem prywatnym.
  * Uruchom lokalne propagowanie połączeń (port forwarding) tylko dla lokalnych połączeń (_loopback_) z portu 8080 na port 80 serwera www (www.cs.put.poznan.pl) w tunelu wirtualnym pomiędzy swoim lokalnym systemem a serwerem unixlab.
  * Uruchom lokalne propagowanie połączeń lokalnych i zdalnych (z sieci lokalnej) w konfiguracji jak powyżej.


## Problemy do dyskusji
  * Wady, zalety aplikacji SSH.
  * Braki możliwości w aplikacji SSH.
  * Czy SSH jest wszechstronną aplikacją?
  * Czy dzięki SSH mogę być pewien, że łączę się z konkretnym serwerem zdalnym?
  * Czy SSH wspiera możliwość uwierzytelniania przy użyciu certyfikatów X.509?

---


# Zabezpieczanie komunikacji pocztowej, integracja mechanizmów kryptograficznych z usługami pocztowymi

# Bezpieczeństwo systemów komputerowych - laboratorium 8:Zabezpieczanie komunikacji pocztowej, integracja mechanizmów kryptograficznych z usługami pocztowymi
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Mechanizm OpenPGP](https://wazniak.mimuw.edu.pl/<#Mechanizm_OpenPGP>)
    * [2.1 Zarządzanie kluczami kryptograficznymi](https://wazniak.mimuw.edu.pl/<#Zarządzanie_kluczami_kryptograficznymi>)
    * [2.2 Wygenerowanie klucza](https://wazniak.mimuw.edu.pl/<#Wygenerowanie_klucza>)
    * [2.3 Pozyskanie czyjegoś klucza publicznego](https://wazniak.mimuw.edu.pl/<#Pozyskanie_czyjegoś_klucza_publicznego>)
    * [2.4 Podpisywanie i szyfrowanie wiadomości](https://wazniak.mimuw.edu.pl/<#Podpisywanie_i_szyfrowanie_wiadomości>)
    * [2.5 Deszyfracja i weryfikacja wiadomości](https://wazniak.mimuw.edu.pl/<#Deszyfracja_i_weryfikacja_wiadomości>)
    * [2.6 Szyfrowanie plików](https://wazniak.mimuw.edu.pl/<#Szyfrowanie_plików>)
  * [3 Integracja mechanizmów kryptograficznych z popularnymi klientami poczty elektronicznej](https://wazniak.mimuw.edu.pl/<#Integracja_mechanizmów_kryptograficznych_z_popularnymi_klientami_poczty_elektronicznej>)
    * [3.1 Certyfikaty adresów pocztowych](https://wazniak.mimuw.edu.pl/<#Certyfikaty_adresów_pocztowych>)
  * [4 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [5 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [6 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Coraz częściej w Internecie zdarzają się próby podszywania pod inne osoby (konta pocztowe innych osób), rozsyłane są wiadomości reklamowe oraz tak zwany SPAM. Istnieje wiele sposobów przeciwdziałania tego typu poczcie i co pewien czas jakaś firma postanawia zaproponować nowe rozwiązanie. Niestety jak dotychczas żadne rozwiązanie nie wyeliminowało całkowicie problemy niechcianej poczty (SPAMu). Natomiast jest na to bardzo proste rozwiązanie, które jest już zauważane przez ludzi, jednak oczywiście jest to w pewnym stopniu problematyczne. Mianowicie rozwiązanie to polega na zastosowaniu podpisu elektronicznego, który byłby stosowany do podpisu każdej wiadomości. Jednak jak wszystkim wiadomo podpis elektroniczny jest dosyć drogi, dlatego można wykorzystać inne metody podpisywania poczty nie korzystający z typowego podpisu elektronicznego, przykładami darmowych rozwiązań tego typu jest pakiet PGP (Pretty Good Privacy), jeszcze innym rozwiązaniem jest stosowanie certyfikatów poświadczających wiarygodność adresu poczty elektronicznej. 
Wadą przedstawionego powyżej rozwiązania jest to, że aby w pełni wykorzystać z takiego sposobu obrony przed niechcianą pocztą jest posiadanie kluczy publicznych wszystkich osób, od których możemy otrzymać pocztę, a to może być trudne do wykonania. Bardzo często użytkownicy nie chcą przekonać się do stworzenia swoich kluczy i podpisywania wszystkich wiadomości. 
Celem ćwiczenia jest zapoznanie się z mechanizmem PGP oraz z certyfikatami dla adresów e-mail. 
## Mechanizm OpenPGP
Standardy PGP (RFC 1991) i OpenPGP (RFC 2440) umożliwiają podpisywanie oraz szyfrowanie plików (w tym korespondencji pocztowej) metodami asymetrycznymi i symetrycznymi. W implementacji GnuPG stosowane są szyfry RSA, DSA lub ElGamal dla szyfrowania asymetrycznego oraz 3DES, CAST5, Blowfish, Twofish, i AES (128b, 192b i 256b) dla szyfrowania symetrycznego. Podpis elektroniczny obsługują algorytmy MD5, SHA-1 i SHA-256 oraz RIPEMD-160. Ponadto w implementacji tej możliwe jest dokonywanie kompresji szyfrowanej treści algorytmami ZIP lub ZLIB. 
### Zarządzanie kluczami kryptograficznymi
Wszystkie operacje w systemie GnuPG wykonuje uniwersalne narzędzie gpg. Program ten umożliwia użytkownikowi m.in. wygenerowanie pary kluczy asymetrycznych o wybranej długości oraz utrzymuje zbiory („pęki") kluczy publicznych innych użytkowników. 
### Wygenerowanie klucza
```
 local> gpg --gen-key

```

Pęki kluczy przechowywane są domyślnie w katalogu ~/.gnupg w plikach: pubring.gpg oraz secring.gpg. Bieżącą zawartość pęku posiadanych kluczy publicznych można wyświetlić poleceniem : 
```
 local> gpg –-list-keys

```

lub dla kluczy prywatnych: 
```
 local> gpg –-list-secret-keys

```

Przykładowy wynik działania pierwszego z tych dwóch poleceń może wyglądać następująco: 
```
 /home/jbond/.gnupg/pubring.gpg
 --------------------------------
 pub 1024D/3BF84E43 2004-06-25 James Bond <spsk007@cs.put.poznan.pl>
 sub 1024g/8B423A22 2004-06-25

```

Wygenerowany klucz publiczny można udostępnić, np. eksportując do pliku tekstowego w formacie ASCII: 
```
 local> gpg –-export –a –o ~/.gpgkey

```

### Pozyskanie czyjegoś klucza publicznego
Pozyskanie klucza prywatnego może nastąpić: 
  * z pliku przesłanego lub pobranego (np. poprzez WWW) od właściciela klucza:

```
 local> gpg –-import plik_z_kluczem

```

  * lub z serwera kluczy:

```
 local> gpg --keyserver certserver.pgp.com --recv-key 0xBB7576AC

```

### Podpisywanie i szyfrowanie wiadomości
Program gpg pozwala podpisać dowolny plik, w szczególności list, swoim kluczem prywatnym: 
```
 local> gpg –-sign plik

```

W powyższym przykładzie wynik pojawi się w postaci skompresowanej w pliku o nazwie plik.pgp. Aby uzyskać podpis w postaci czytelnej (bez kompresji) należy wykonać polecenie: 
```
 local> gpg –-clearsign plik

```

Wówczas powstanie plik tekstowy w formacie ACII o nazwie plik.asc. Nazwę pliku wynikowego możemy zmieniać opcją -o nazwa_pliku. 
Program gpg pozwala też zaszyfrować wiadomość kluczem publicznym konkretnego odbiorcy: 
```
 local> gpg –-recipient odbiorca –at –o list.txt plik

```

a także połączyć szyfrowanie z podpisem elektronicznym: 
```
 local> gpg -se –r odbiorca –at –o list.txt plik

```

### Deszyfracja i weryfikacja wiadomości
Do deszyfrowania i weryfikowania podpisu służą opcje, odpowiednio, -d (--decrypt) oraz ‑‑verify: 
```
 local> gpg –d list
 local> gpg –-verify list

```

### Szyfrowanie plików
Do symetrycznego szyfrowania plików służy opcja -c programu gpg: 
```
 local> gpg –c -o szyfrogram plik.txt

```

lub: 
```
 local> gpg –symmetric --cipher-algo AES256 -o szyfrogram plik.txt

```

## Integracja mechanizmów kryptograficznych z popularnymi klientami poczty elektronicznej
Niektóre programy klientów posiadają możliwość wykorzystania mechanizmów kryptograficznych: szyfrowania i / lub podpisywania korespondencji pocztowej. Taką możliwość posiadają np. popularne produkty z rodziny Mozilla (Mozilla Mail lub Thunderbird) z rozszerzeniem enigmail (na platformę Windows to rozszerzenie trzeba zainstalować oddzielnie). Enigmail integruje klienta pocztowego z popularnym i powszechnie stosowanym w Internecie systemem PGP (np. pakiet OpenPGP lub GnuPG, niezależnie instalowane w systemie). System PGP umożliwia m.in. certyfikację kluczy pocztowych metodą wzajemnego zaufania (_Web of Trust_). 
[![Bsi 08 01.png](https://wazniak.mimuw.edu.pl/images/8/88/Bsi_08_01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_01.png>)
Niestety nie wszystkie programy klienckie poczty elektronicznej posiadają rozszerzenia umożliwiające bezpośrednie korzystanie z podpisywania wiadomości przy użyciu mechanizmu PGP. Dosyć popularny klient poczty (MS Outlook Express) niestety nie posiada darmowych dobrze pracujących rozszerzeń zapewniających integrację z PGP. Zamiast tego wszystkie wiadomości podpisane z wykorzystaniem tego mechanizmu są pokazywane jako lista załączników do poczty. Aby jednak móc wykorzystywać mechanizm PGP można wykorzystać mechanizm pośrednika, który będzie pośrednikiem przy wysyłaniu i odbieraniu poczty elektronicznej (w ten sposób całkowicie uniezależniamy się od konkretnego klienta poczty elektronicznej, gdyż każdy klient może korzystać z takiego pośrednika). 
Przykładowym programem zapewniającym stworzenie mechanizmu pośrednika jest program GnuPGRelay [GR] instalacje jego wymaga wcześniej zainstalowania aplikacji GnuPG [GPG] dostępnej w internecie, często również w innych pakietach programów, polecić można pakiet WinPT [WPT] zawierającą oprócz GnuPG szereg innych aplikacji umożliwiających szyfrowanie plików, katalogów itp. 
Po zainstalowaniu pakietu WinPT należy utworzyć własną parę kluczy PGP 
[![Bsi 08 02.png](https://wazniak.mimuw.edu.pl/images/e/ec/Bsi_08_02.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_02.png>)
W aplikacji tej również można dodawać klucze publiczne zaufanych osób, od których będziemy otrzymywać podpisaną pocztę celem weryfikacji podpisów. 
Następnie instalujemy aplikacje GnuPGRelay, którą musimy skonfigurować do wysyłania i odbierania poczty. Dokładniej należy ustawić serwery poczty przychodzącej (POP3) i wychodzącej (SMTP), aby móc korzystać z pośrednika, dodatkowo wymaga to przekonfigurowania aplikacji klienta poczty, aby kontaktował się z pośrednikiem lokalnym jako serwerem poczty przychodzącej i wychodzącej. 
Poniższy rysunek przedstawia konfigurację serwerów poczty w pośredniku: 
[![Bsi 08 03.png](https://wazniak.mimuw.edu.pl/images/thumb/a/a9/Bsi_08_03.png/300px-Bsi_08_03.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_03.png>)
Po skonfigurowaniu pośrednika i klienta poczty, należy ustawić preferencję wykorzystywania mechanizmu PGP - należy ustawić profile i przypisać do nich odpowiednie klucze. Klucze pobierane są z głównej aplikacji GnuPG. Wybór i edycja profilu pozwala określić czy poczta ma być podpisywana, czy szyfrowana, czy obie akcje równocześnie lub w ostateczności nie musimy nic z pocztą robić. 
Poniższy rysunek przedstawia konfiguracje profili: 
[![Bsi 08 04.png](https://wazniak.mimuw.edu.pl/images/thumb/0/0f/Bsi_08_04.png/300px-Bsi_08_04.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_04.png>)
Klucze PGP są zaszyfrowane dlatego pośrednik musi znać hasło do klucza prywatnego właściciela klucza, lub każdorazowo może się pytać o to hasło. Ekran pytania się o hasło poniżej: 
[![Bsi 08 05.png](https://wazniak.mimuw.edu.pl/images/0/06/Bsi_08_05.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_05.png>)
Możliwości wykorzystywania pośrednika nie ograniczają się do konkretnego klienta poczty elektronicznej. Oczywiście pośrednik taki ma również ograniczenia, gdyż na etapie tworzenia wiadomości nie możemy określić czy wiadomość ma być podpisywania i/lub szyfrowana, tylko musimy określić to poprzez profile w pośredniku. 
### Certyfikaty adresów pocztowych
Jednym z bardziej popularnych ośrodków certyfikacji w Internecie jest firma Thawte. Wiele przeglądarek WWW i aplikacji pocztowych zawiera certyfikat głównego urzędu certyfikacji tej firmy, co pozwala ufać podpisom tego urzędu: 
[![Bsi 08 06.png](https://wazniak.mimuw.edu.pl/images/e/ef/Bsi_08_06.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_06.png>)
Korzystając ze strony <http://www.thawte.com> można pozyskać darmowy certyfikat poświadczający własny adres pocztowy: 
[![Bsi 08 07.png](https://wazniak.mimuw.edu.pl/images/1/1a/Bsi_08_07.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_08_07.png>)
## Zadania
  1. Za pomocą narzędzi pakietu GnuPG wygeneruj pęki kluczy kryptograficznych szyfrowania asymetrycznego dla swojego konta pocztowego, a następnie udostępnij klucz publiczny poprzez usługę finger.
  2. Wykorzystaj pakiet GnuPG do ochrony korespondencji z wybranym użytkownikiem.
  3. Dokonaj zaszyfrowania wybranego pliku metodą szyfrowania symetrycznego narzędziami pakietu GnuPG.
  4. Zainstaluj system GnuPG (jeśli korzystasz z systemu Windows) oraz rozszerzenie Enigmail klienta pocztowego Mozilla Thunderbird.
  5. Korzystając w programie Thunderbird z funkcji OpenPGPKey Management wygeneruj swoją parę kluczy kryptograficznych.
  6. Wyślij podpisany list do siebie samego. Sprawdź reakcję systemu.
  7. Wyślij podpisany list do innego użytkownika ze swojej grupy i odbierz jego list.
  8. Zweryfikuj poprawność podpisu otrzymanego listu.
  9. Zrealizuj komunikację z szyfrowaniem całej przesyłki pocztowej
  10. Wykonać instalację pośrednika GnuPGRelay wraz z WinPT oraz przekonfigurowanie dowolnego klienta poczty elektronicznej do korzystania z pośrednika i przetestowanie jego możliwości.
  11. Wykorzystując stronę firmy thawte.com utworzyć darmowy certyfikat do poczty elektronicznej i zapisać go w klienci poczty elektronicznej (Thunderbird), a następnie wysłać list podpisany przy użyciu certyfikatu.
  12. Zweryfikować otrzymaną pocztę podpisaną przy użyciu certyfikatu, sprawdzić poprawność podpisu.


## Problemy do dyskusji
  * Dlaczego podpisy PGP nie są zbyt często wykorzystywane przez zwykłego użytkownika?
  * Dlaczego klient poczty elektronicznej wymaga podania certyfikatu lub klucza publicznego nadawcy poczty?
  * Dlaczego popularny klient poczty Ms Outlook bardzo dziwnie odbiera pocztę podpisaną z wykorzystaniem mechanizmu PGP, pod warunkiem, że nie posiada mechanizmu do obsługi tego mechanizmu?
  * Który z wymienionych wyżej systemów jest lepszy i dlaczego (PGP czy certyfikaty)?
  * Czy istnieje prosta metoda wykorzystania mechanizmów kryptograficznych do zabezpieczenia poczty elektronicznej?
  * Przykłady innych mechanizmów zapewniających bezpieczeństwo przesyłanych danych pocztowych (o ile takowe istnieją)


---


# Zabezpieczanie serwerów usług aplikacyjnych na przykładzie WWW (uwięzienie w piaskownicy)

# Bezpieczeństwo systemów komputerowych - laboratorium 9:Zabezpieczanie serwerów usług aplikacyjnych na przykładzie WWW (uwięzienie w piaskownicy)
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Uwięzienie w piaskownicy](https://wazniak.mimuw.edu.pl/<#Uwięzienie_w_piaskownicy>)
    * [2.1 Podsumowanie mechanizmu piaskownicy](https://wazniak.mimuw.edu.pl/<#Podsumowanie_mechanizmu_piaskownicy>)
  * [3 Umieszczenie serwera Apache w środowisku uwięzienia w piaskownicy.](https://wazniak.mimuw.edu.pl/<#Umieszczenie_serwera_Apache_w_środowisku_uwięzienia_w_piaskownicy.>)
  * [4 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [5 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [6 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Zabezpieczanie serwerów usług aplikacyjnych polega głównie na ograniczeniu jego środowiska oraz ograniczenie dostępu do zasobów systemu operacyjnego i plików w systemie. Wiele z metod służących do ograniczanie aplikacji zostało już omówiona we wcześniejszych materiałach, poprzez mechanizm PAM i limity. W tym laboratorium należy zaznajomić się z możliwością ograniczenia systemu plików i dostępu do jego zasobów aplikacji serwerowej. 
Uwięzienie w piaskownicy jest jedną z metod ograniczania dostępu do systemu plików systemu operacyjnego. Ponieważ jest to jedyne zadanie tego mechanizmu nie wpływa on na zwiększenie bezpieczeństwa samej aplikacji serwerowej, a jedynie zwiększa bezpieczeństwo systemu operacyjnego. 
Celem ćwiczenia jest uruchomienie serwera apache w środowisku uwięzionym w piaskownicy. 
## Uwięzienie w piaskownicy
Mechanizm ten bardzo często nazywany jest więzieniem, jednak nie jest on aż tak bezpieczny, dlatego nie powinno używać tej nazwy. 
Mechanizm ten może być wykorzystywany przez każdą dowolną aplikację, jak również przez aplikacje przystosowane do wykorzystywania tego mechanizmu. Oczywiście występują duże różnice między tymi podejściami. 
Aplikacje posiadające wsparcie dla tego mechanizmu same mogą uwięzić się w piaskownicy, jednak zanim uwięzią się wczytują wszystkie potrzebne biblioteki systemowe i pliki konfiguracyjne, w piaskownicy nie będą miały już do nich dostępu. Piaskownica ogranicza się wtedy do plików, które muszą być stale dostępne aplikacji (w przypadku serwera www będą to strony www). 
Natomiast aplikacje nie posiadające wsparcie dla mechanizmu mogą z niego korzystać w sposób niezauważalny dla nich. Jest to możliwe pod warunkiem, że aplikacja w piaskownicy będzie posiadała dostęp do wszystkich bibliotek i plików, które są wymagane przy starcie aplikacji. 
Piaskownica jest strukturą katalogową, do której będzie miała dostęp aplikacja, zazwyczaj jest to struktura wymagana przez aplikacje wraz ze wszystkimi plikami. 
### Podsumowanie mechanizmu piaskownicy
Mechanizm uwięzienie w piaskownicy jest stosowany jeśli chcemy ograniczyć dostęp do plików serwerom aplikacyjnym, dzięki temu możemy ograniczyć szkody, jeśli komuś uda się przełamać zabezpieczenia danej aplikacji serwerowej, jednak wtedy uzyskuje jedynie dostęp do ograniczonego środowiska piaskownicy.. 
## Umieszczenie serwera Apache w środowisku uwięzienia w piaskownicy.
Po pierwsze należy stworzyć strukturę katalogową piaskownicy w jakimś katalogu systemu operacyjnego. Przykładowo stworzymy katalog /chroot/apache/. W katalogu tym musimy stworzyć następujące katalogi: 
  * etc/apache2
  * srv/www/htdocs
  * srv/www/icons
  * srv/www/cgi-bin
  * lib (lub lib64)
  * usr/lib (lub usr/lib64)
  * usr/sbin
  * var/log/apache2 (należy umożliwić zapis użytkownikowi _wwwrun_)
  * var/run
  * dev


Następnie należy przegrać z głównego środowiska do piaskownicy całe katalogi: 
  * /etc/apache2 do /chroot/apache/etc/apache2
  * /srv/www/htdocs do /chroot/apache/srv/www/htdocs
  * /srv/www/icons do /chroot/apache/srv/www/icons
  * /srv/www/cgi-bin do /chroot/apache/srv/www/cgi-bin
  * /usr/lib[64]/apache2* do /chroot/apache/usr/lib[64]/


Następnie należy przegrać kilka plików apache2 oraz podstawowych plików konfiguracyjnych systemu operacyjnego: 
  * /usr/sbin/apache* do /chroot/apache/usr/sbin/
  * /dev/null do /chroot/apache/dev/
  * /dev/random do /chroot/apache/dev/
  * /dev/urandom do /chroot/apache/dev/
  * /etc/mime.types do /chroot/apache/etc/
  * /etc/resolv.conf do /chroot/apache/etc/
  * /etc/passwd do /chroot/apache/etc/
  * /etc/group do /chroot/apache/etc/
  * /usr/sbin/apache2* do /chroot/usr/sbin/


Dodatkowo pliki passwd i group należy tak zmodyfikować, aby zostały tam jedynie informacje na temat użytkownika _wwwrun_ i grupy _www_. 
Jedynie brakuje jeszcze bibliotek, których wymaga serwer apache, listę tych bibliotek otrzymamy wykonując następujące polecenie _ldd /usr/sbin/httpd2-prefork_. Następnie wszystkie wypisane biblioteki wraz z linkami symbolicznymi do nich należy skopiować do odpowiednich katalogów w piaskownicy. 
Po ustawieniu wszystkich powyższych czynności możemy przystąpić do uruchomienia aplikacji Apache wywołując ją w następujący sposób _chroot /chroot/apache /usr/sbin/httpd2-prefork_
Przedstawione powyżej rozwiązanie nie oferuje przygotowania do obsługi skryptów PHP, jest to jedynie uwięzienie w piaskownicy samego serwera apache 
## Zadania
Wykorzystać zaprezentowane powyżej mechanizm uwięzienia aplikacji w piaskownicy w celu przygotowania aplikacji Apache do działania w uwięzionym środowisku i zweryfikowania poprawności działania serwera WWW. 
## Problemy do dyskusji
  * Czy uwięzienia w piaskownicy jest dobrym mechanizmem obrony przed atakami?
  * Czy mechanizm ten w ogóle służy do zabezpieczania serwera aplikacyjnego, czy raczej do zabezpieczania systemu operacyjnego?
  * Czy możliwe jest obejście mechanizmu piaskownicy w podstawowej wersji wykorzystywanej w systemie Linux?
  * Czy istnieją inne lepsze rozwiązania uwięzienia aplikacji w ograniczonym środowisku, jeśli tak to jakie?


---


# Konstrukcja urzędów certyfikacji standardu OpenSSL, zarządzanie certyfikatami

# Bezpieczeństwo systemów komputerowych - laboratorium 10:Konstrukcja urzędów certyfikacji standardu OpenSSL, zarządzanie certyfikatami
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
Konstrukcja urzędów certyfikacji standardu OpenSSL, zarządzanie certyfikatami 
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Protokół SSL](https://wazniak.mimuw.edu.pl/<#Protokół_SSL>)
    * [2.1 Etap nawiązania sesji SSL](https://wazniak.mimuw.edu.pl/<#Etap_nawiązania_sesji_SSL>)
  * [3 Infrastruktura klucza publicznego i certyfikaty cyfrowe](https://wazniak.mimuw.edu.pl/<#Infrastruktura_klucza_publicznego_i_certyfikaty_cyfrowe>)
    * [3.1 Zarządzanie PKI](https://wazniak.mimuw.edu.pl/<#Zarządzanie_PKI>)
  * [4 Oprogramowanie OpenSSL](https://wazniak.mimuw.edu.pl/<#Oprogramowanie_OpenSSL>)
    * [4.1 Tworzenie własnego centrum certyfikacji](https://wazniak.mimuw.edu.pl/<#Tworzenie_własnego_centrum_certyfikacji>)
    * [4.2 Generowanie prośby o wystawienie certyfikatu](https://wazniak.mimuw.edu.pl/<#Generowanie_prośby_o_wystawienie_certyfikatu>)
    * [4.3 Wystawienie certyfikatu](https://wazniak.mimuw.edu.pl/<#Wystawienie_certyfikatu>)
  * [5 Podsumowanie](https://wazniak.mimuw.edu.pl/<#Podsumowanie>)
  * [6 Zadanie](https://wazniak.mimuw.edu.pl/<#Zadanie>)
  * [7 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [8 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Technologia SSL(_Secure Sockets Layer_) zaproponowana przez firmę Netscape Communications na potrzeby szyfrowania i uwierzytelniania komunikacji została bardzo dobrze przyjęta przez wszystkich zainteresowanych. Obecnie technologia SSL jest szeroko wykorzystywana jako mechanizm bezpiecznej komunikacji nie tylko w obrębie protokołu HTTP ale służy również do tworzenia sieci VPN(Virtual Private Network). Najnowsza wersja protokołu SSL to wersja 3.0. U podstaw protokołu SSL leży praktyczne wykorzystanie kryptografii asymetrycznej oraz symetrycznej. Celem ćwiczenia jest zrozumienie działania protokołu SSL oraz poznanie pakietu OpenSSL. 
Słowa kluczowe: ssl, openssl, PKI, certyfikat cyfrowy, vpn 
## Protokół SSL
Zadaniem protokołu SSL jest zapewnienie szyfrowanego i/lub uwierzytelnionego kanału przesyłania danych. Biorąc pod uwagę warstwowość sieciowego modelu ISO/OSI protokół SSL można umiejscowić powyżej protokołu TCP czyli warstwy transportowej ale poniżej warstw wyższych. Protokół SSL w imieniu warstw wyższych modelu ISO/OSI wykorzystuje protokół TCP do ustanowienia kanału wymiany danych. Analizując działania protokołu SSL można wyróżnić kilka zdarzeń, które mogą zajść w trakcie korzystania z protokołu SSL. Są to: 
  * Uwierzytelnienie serwera wspierającego SSL – strona będąca klientem połączenia SSL ma możliwość zweryfikowania tożsamości strony serwera poprzez wykorzystanie mechanizmów kryptografii klucza publicznego i sprawdzenie czy certyfikat strony serwera jest poprawny oraz czy został podpisany przez znaną klientowi zaufaną stronę trzecia, centrum certyfikacji(CA, _ang. Certification Authority_).


  * Uwierzytelnienie klienta wspierającego SSL – strona będąca serwerem ma możliwość zweryfikować tożsamość klienta żądającego nawiązania bezpiecznego połączenia. Serwer przeprowadza proces weryfikacji klienta identycznie jak zostało to opisane powyżej.


  * Nawiązanie szyfrowanego połączenia – obie strony połączenia dążą do nawiązania bezpiecznego połączenia którym mogą być przesyłane poufne dane.


Aby lepiej zrozumieć proces nawiązania połączenia, poniżej wymieniono najważniejsze etapy zachodzące w protokole SSL: 
  1. Serwer uwierzytelniania się przed klientem.
  2. Klient i serwer wymieniają między sobą informacje pozwalające uzgodnić im najsilniejsze mechanizmy kryptograficzne jakie obie strony wspierają np. algorytm funkcji skrótu kryptograficznego, algorytm służący do szyfrowania.
  3. Jeżeli zachodzi taka potrzeba klient uwierzytelnia się przed serwerem.
  4. Klient i serwer używając mechanizmów kryptografii klucza publicznego uzgadniają między sobą tajny klucz określany mianem shared secret.
  5. Zostaje ustanowiony bezpieczny kanał wymiany danych między obiema stronami.


### Etap nawiązania sesji SSL
Pierwszym krokiem w celu utworzenia bezpiecznego kanału wymiany danych między serwerem a klientem jest etap przywitania(_ang. handshake_) w którym strona serwera uwierzytelnia się przed stroną klienta oraz opcjonalnie strona klienta uwierzytelnia się przed stroną serwera. Oba procesy uwierzytelnia wykorzystują mechanizmy kryptografii klucza publicznego aby w wiarygodny sposób zweryfikować tożsamość drugiej strony. Poniżej zaprezentowano kolejne etapy w procesie przywitania między stroną serwera i klienta. 
  1. Strona klienta wysyła do strony serwera numer obsługiwanej wersji protokołu SSL, możliwe do użycia algorytmy szyfrujące oraz zestaw danych losowych.
  2. Strona serwera wysyła do strony klienta numer obsługiwanej wersji protokołu SSL, możliwe do użycia algorytmy szyfrujące, zestaw danych losowych oraz własny certyfikat zawierający publiczny klucz serwera. Może również zdarzyć się, że serwer zażąda aby klient uwierzytelnił się. W takiej sytuacji serwer wysyła również żądanie o certyfikat strony klienta.
  3. Strona klienta przystępuje do weryfikacji tożsamości strony serwera. Jeżeli wystąpi problem z weryfikacją tożsamości strony serwera użytkownik jest o tym informowany.
  4. Po pomyślnym uwierzytelnieniu strony serwera, strona klienta generuje tajny ciąg znaków określany mianem _premaster secret_. Dysponując certyfikatem strony serwera, strona klienta używa klucza publicznego strony serwera, szyfruje tajny ciąg _premaster secret_ i wysyła go do strony serwera.
  5. Opcjonalnie, serwer może zażądać aby strona klienta uwierzytelniła się. Strona klienta wysyła do strony serwera swój certyfikat z kluczem publicznym oraz podpisany swoim kluczem prywatnym losowy ciąg znaków znany stronie klienta i serwera.
  6. Strona serwera przystępuje do weryfikacji tożsamości strony klienta. Jeżeli wystąpi problem z weryfikacją sesja SSL jest przerywana. Jeżeli weryfikacja zakończy się pozytywnie strona serwera używając swojego klucza prywatnego odszyfrowuje ciąg _premaster secret_ i na jego podstawie generuje tajny ciąg znaków określany mianem _master secret_(strona klienta również na podstawie ciągu _premaster secret_ generuje ciąg _master secret_).
  7. Obie strony połączenia na podstawie tajnego ciągu znaków _master secret_ generują ciąg _session key_. Tajny ciąg _session key_ posłuży jako klucz dla algorytmu symetrycznego szyfrowania służącego do szyfrowania komunikacji między stronami.
  8. Obie strony połączenia informują siebie wzajemnie, że od tej chwili komunikacja między nimi będzie szyfrowana.
  9. Proces ustanowienia sesji SSL zostaje zakończony, bezpieczny kanał komunikacji został ustanowiony.


## Infrastruktura klucza publicznego i certyfikaty cyfrowe
Protokół SSL wykorzystuje dwie technologie odnośnie mechanizmów szyfrowania. Jest to kryptografia symetryczna i kryptografia asymetryczna. Kryptografia symetryczna służy do szyfrowania danych wymienianych między stronami. Kryptografia asymetryczna służy do uzgodnienia między stronami tajnego klucza sesyjnego. Połączenie obu technologii pozwala na bezpieczne korzystanie z protokołu SSL. Omawiając protokół SSL należy również wspomnieć o Infrastrukturze klucza publicznego(_ang. PKI, Public Key Infrastructure_)oraz certyfikatach standardu X.509. 
PKI to koncepcja rozbudowanego systemu kryptograficznego w którym sieć wzajemnych powiązań między elementami tego systemu gwarantuje bezpieczeństwo komunikacji a konkretnie bezpieczeństwo i możliwość weryfikacji informacji o użytkownikach tego systemu. W skład PKI wchodzą: 
  * Urzędy certyfikacji(_ang. CA, Certification Authority_) odpowiedzialne za poświadczanie tożsamości klientów, tzw. zaufana strona trzecia(_ang. trusted third party_).
  * Użytkownicy dla których wydawane są certyfikaty.
  * Urzędy rejestracji(_ang. RA, Registration Authority_) odpowiedzialne za weryfikację danych o użytkownikach oraz ich rejestrację.
  * Oprogramowanie oraz sprzęt niezbędny do posługiwania się certyfikatami.
  * Repozytoria kluczy, certyfikatów i listy odwołanych certyfikatów(_ang. CRL, Certificate Revocation List_)


Struktura PKI przypomina drzewo, w którym w roli korzenia występuje główny urząd certyfikacji, który określa politykę certyfikacji np. dla danego kraju. Poniżej znajdują się podległe urzędy certyfikacji zajmujące się obsługą np. poszczególnych grup użytkowników lub świadczące usługi certyfikacji dla określonych zastosowań. Na samym dole tego drzewa jako liście występują użytkownicy, którzy zgłaszają się do urzędów certyfikacji w celu wydania im certyfikatów. Instytucja certyfikująca wydaje certyfikat i poświadcza tożsamość użytkownika któremu wydaje certyfikat. Użytkownik może sprawdzić jaki urząd wydał dany certyfikat, może również sprawdzić całą ścieżkę zaufania od danego użytkownika do głównego urzędu certyfikacji. Cała struktura drzewiasta tworzy hierarchię zaufania. Należy zwrócić uwagę iż w certyfikacie znajduje się tylko klucz publiczny użytkownika. Klucz prywatny(tajny), który jest zawsze matematycznie powiązany z kluczem publicznym jest znany tylko użytkownikowi. Urząd certyfikacji wydając certyfikat poświadcza, że podpis wykonany tajnym kluczem użytkownika został złożony przez tego użytkownika. 
Struktura PKI podlega standaryzacji. Standard opiera się na dwóch elementach. Jednym jest standard X.509 opisujący strukturę certyfikatów oraz drugi standard określany mianem PKCS(_ang. Public Key Cryptography Standards_) którego autorem jest firma RSA Data Security. 
Certyfikat cyfrowy jest informacją elektroniczną poświadczającą związek między danym użytkownikiem a kluczem, którego używa dany użytkownik do procedury podpisywania dokumentów. Standard X.509 definiuje budowę takiego certyfikatu i wskazuje jakie elementy powinny być zawarte w certyfikacie. Są to m.in.: 
  * numer wersji standardu X.509
  * numer wystawionego certyfikatu
  * identyfikator algorytmu podpisu certyfikatu
  * nazwa funkcji skrótu kryptograficznego użyta przez wystawcę
  * nazwa wystawcy certyfikatu
  * daty ważności certyfikatu
  * nazwa podmiotu dla którego wystawiany jest certyfikat
  * parametry klucza publicznego podmiotu
  * klucz publiczny podmiotu
  * opcjonalne rozszerzenia
  * podpis wystawcy certyfikatu


### Zarządzanie PKI
Z zarządzaniem infrastrukturą PKI wiąże się kilka zadań jakie muszą być możliwe w realizacji. Są to: 
  * Rejestracja użytkowników(_ang. registration_) - użytkownicy składają wnioski o wydanie certyfikatów.
  * Wydawanie certyfikatów(_ang. certification_) - urzędy certyfikacyjne wydają certyfikaty dla użytkowników.
  * Generowanie par kluczy(_ang. key generation_) - para kluczy(publiczny i prywatny) może zostać wygenerowana przez urząd certyfikacji. Klucz publiczny zostanie później podpisany a prywatny zostanie dostarczony klientowi w bezpieczny sposób. Bezpieczniejszym rozwiązaniem jest samodzielna generacja pary kluczy i dostarczenie urzędowi do podpisu tylko publicznego klucza.
  * Wzajemna certyfikacja(_ang. cross certification_) – sytuacja, gdy urzędy certyfikacji wystawiają sobie wzajemnie certyfikaty podnosząc tym samym poziom zaufania do siebie oraz co równie ważne pozwala to tworzyć relacje zaufania między użytkownikami mającymi wydane certyfikaty przez różne urzędu certyfikacji.
  * Odnawianie certyfikatów(_ang. certificates update_) – urząd certyfikacji wydaje certyfikaty dla użytkowników na określony czas. Po upływie wyznaczonego okresu certyfikat przestaje być ważny i należy ponownie zwrócić się do urzędu po nowy certyfikat.
  * Unieważnianie certyfikatów(_ang. revocation certificates_) Certyfikat jest wydawany na określony czas. Czasami może zdarzyć się wyjątkowa sytuacja, gdy certyfikat musi być unieważniony przed upływem tego czasu. Takie wyjątkowe sytuacje to np. ujawnienie klucza prywatnego właściciela certyfikatu, kompromitacja urzędu certyfikacji, który wydał dany certyfikat(w takiej sytuacji wszystkie wydane certyfikaty przez taki urząd muszą zostać unieważnione), zmiana informacji o użytkowniku, która powoduje, że dane w aktualnym certyfikacie będą nieaktualne.
  * Odzyskiwanie klucza(_ang. key recovery_) Niekiedy może się zdarzyć sytuacja, że użytkownik zgubi swoje klucze. Jeśli klucze były przechowywane przez urząd certyfikacji to użytkownik będzie mógł je odzyskać.


## Oprogramowanie OpenSSL
Oprogramowanie Openssl jest ogólnie dostępną biblioteką funkcji kryptograficznych. Openssl zawiera popularną implementację protokołu SSL. Najczęściej można ją spotkać w systemach Unix/Linux, gdzie dużo oprogramowania korzysta z tej biblioteki. Openssl to nie tylko biblioteka funkcji użytecznych dla wymagającego obsługi protokołu SSL oprogramowania. Użytkownicy za pomocą tej biblioteki mogą również samodzielnie tworzyć część infrastruktury klucza publicznego poprzez utworzenie własnego centrum certyfikacji, generowanie par kluczy oraz wystawianie certyfikatów. W dalszej części opracowania zostanie pokazane w jaki sposób można utworzyć własne centrum certyfikacji, wygenerować prośbę o wystawienie certyfikatu oraz jak wystawić certyfikat. 
Wraz z biblioteką Openssl dostarczany jest zestaw użytecznych skryptów, które ułatwiają realizację wyżej wymienionych zadań. 
### Tworzenie własnego centrum certyfikacji
Do tworzenia własnego centrum certyfikacji można wykorzystać skrypt CA.sh lub CA.pl. Oba skrypty zapewniają identyczną funkcjonalność z tym, że pierwszy został napisany w języku interpretera bash a drugi w języku perl. Aby wygenerować utworzyć własne centrum certyfikacji należy wydać komendę: 
```
./CA.sh –newca

```

Poniżej zaprezentowano przykład utworzenia centrum certyfikacji: 
```
testowy:/usr/share/ssl/misc # ./CA.sh -newca
CA certificate filename (or enter to create) 
Making CA certificate ...
Generating a 1024 bit RSA private key
........++++++
..................++++++
writing new private key to './demoCA/private/./cakey.pem'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
phrase is too short, needs to be at least 4 chars
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:**PL**
State or Province Name (full name) [Some-State]:**WLKP**
Locality Name (eg, city) []:**Poznań**
Organization Name (eg, company) [Internet Widgits Pty Ltd]:**Politechnika Poznańska**
Organizational Unit Name (eg, section) []:**Instytut Informatyki**
Common Name (eg, YOUR name) []:**ca_localhost**
Email Address []:**ca_admin@localhost.pl**
testowy:/usr/share/ssl/misc #

```

Pogrubionym drukiem zaznaczono przykładowy tekst, który został wpisany przez użytkownika. Utworzenie centrum certyfikacji spowoduje utworzenie podkatalogu demoCA. W tym katalogu będzie znajdował się plik **cacert.pem** , który jest certyfikatem dla utworzonego urzędu certyfikacji. W podkatalogu **demoCA/private/** będzie znajdował się klucz prywatny urzędu certyfikacji, plik **cakey.pem**. Podczas procesu tworzenia centrum certyfikacji skrypt zapyta użytkownika o frazę hasłową, która będzie użyta do zaszyfrowania klucza prywatnego centrum certyfikacji przechowywanego w pliku **cakey.pem**. UWAGA! Zgubienie tego klucza spowoduje niemożność wystawiania certyfikatów przez to centrum certyfikacji. 
### Generowanie prośby o wystawienie certyfikatu
Aby uzyskać certyfikat od urzędu certyfikatu należy najpierw zgłosić żądanie wystawienia certyfikatu. Polecenie: 
```
./CA.sh -newreq

```

wygeneruje prośbę o wystawienie certyfikatu w formie pliku tekstowego. Poniżej zaprezentowano przykład generacji żądania o wystawienie certyfikatu: 
```
testowy:/usr/share/ssl/misc # ./CA.sh -newreq

```
```
Generating a 1024 bit RSA private key
................++++++
.++++++
writing new private key to 'newreq.pem'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:PL
State or Province Name (full name) [Some-State]:WLKP
Locality Name (eg, city) []:Poznań
Organization Name (eg, company) [Internet Widgits Pty Ltd]:FIRMA X
Organizational Unit Name (eg, section) []:Dział Y
Common Name (eg, YOUR name) []:nazwa_serwera_firmy_X
Email Address []:admin@firma_x.pl 
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
Request (and private key) is in newreq.pem
testowy:/usr/share/ssl/misc #

```

W pliku _newreq.pem_ będzie znajdowało się żądanie wydania certyfikatu oraz klucz prywatny podmiotu żądającego wystawienia certyfikatu. 
### Wystawienie certyfikatu
Aby wystawić certyfikat na podstawie żądania wystawienie certyfikatu należy wydać polecenie: 
```
./CA.sh -sign

```

Poniżej zaprezentowano przebieg procedury wystawienia certyfikatu: 
```
testowy:/usr/share/ssl/misc # ./CA.sh -sign
Using configuration from /etc/ssl/openssl.cnf
Enter pass phrase for ./demoCA/private/cakey.pem:
Check that the request matches the signature
Signature ok
Certificate Details:
    Serial Number: 1 (0x1)
    Validity
      Not Before: Jul 15 09:10:00 2006 GMT
      Not After : Jul 15 09:10:00 2007 GMT
    Subject:
      countryName        = PL
      stateOrProvinceName    = WLKP
      localityName       = Pozna\C5\84
      organizationName     = FIRMA X
      organizationalUnitName  = Dzia\C5\82 Y
      commonName        = nazwa_serwera_firmy_X
      emailAddress       = admin@firma_x.pl
    X509v3 extensions:
      X509v3 Basic Constraints:
        CA:FALSE
      Netscape Comment:
        OpenSSL Generated Certificate
      X509v3 Subject Key Identifier:
        12:B8:BF:4D:BF:B9:40:C9:2E:C1:7A:DE:A8:4B:75:58:D8:C6:CD:3D
      X509v3 Authority Key Identifier:
        keyid:BF:62:BF:05:7C:05:30:E5:E3:7A:90:82:0C:61:45:60:7E:D8:F3:49
        DirName:/C=PL/ST=WLKP/L=Pozna\xC5\x84/O=Politechnika Pozna\xC5\x84ska/OU=Instytut Informatyki/CN=ca_localhost/emailAddress=ca_admin@localhost.pl
        serial:8D:A7:61:FC:60:94:39:C1

```
```
Certificate is to be certified until Jul 15 09:10:00 2007 GMT (365 days)
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
Certificate:
  Data:
    Version: 3 (0x2)
    Serial Number: 1 (0x1)
    Signature Algorithm: md5WithRSAEncryption
    Issuer: C=PL, ST=WLKP, L=Pozna\xC5\x84, O=Politechnika Pozna\xC5\x84ska, OU=Instytut Informatyki, CN=ca_localhost/emailAddress=ca_admin@localhost.pl
    Validity
      Not Before: Jul 15 09:10:00 2006 GMT
      Not After : Jul 15 09:10:00 2007 GMT
    Subject: C=PL, ST=WLKP, L=Pozna\xC5\x84, O=FIRMA X, OU=Dzia\xC5\x82 Y, CN=nazwa_serwera_firmy_X/emailAddress=admin@firma_x.pl
    Subject Public Key Info:
      Public Key Algorithm: rsaEncryption
      RSA Public Key: (1024 bit)
        Modulus (1024 bit):
          00:b8:b1:2b:00:8b:de:2a:bf:93:ca:e4:a9:ac:2b:
          7a:be:b5:3e:0c:ca:24:55:f7:65:6b:66:fa:34:d2:
          0c:96:76:bb:01:f0:2b:24:27:99:65:11:78:51:f9:
          6b:a7:96:ee:b7:98:45:99:46:ed:1e:13:c9:bb:ab:
          99:c1:59:0e:ac:b8:89:9f:6a:11:b4:04:97:66:7b:
          92:c1:19:c1:82:90:5e:df:c1:85:96:e7:9b:44:d3:
          ee:67:8a:c1:e9:e3:14:a2:ef:0c:13:39:c0:55:19:
          8a:3b:25:aa:49:b9:1e:ab:c4:1d:81:56:90:cc:76:
          89:b1:ea:d8:40:e7:c7:0b:4f
        Exponent: 65537 (0x10001)
    X509v3 extensions:
      X509v3 Basic Constraints:
        CA:FALSE
      Netscape Comment:
        OpenSSL Generated Certificate
      X509v3 Subject Key Identifier:
        12:B8:BF:4D:BF:B9:40:C9:2E:C1:7A:DE:A8:4B:75:58:D8:C6:CD:3D
      X509v3 Authority Key Identifier:
        keyid:BF:62:BF:05:7C:05:30:E5:E3:7A:90:82:0C:61:45:60:7E:D8:F3:49
        DirName:/C=PL/ST=WLKP/L=Pozna\xC5\x84/O=Politechnika Pozna\xC5\x84ska/OU=Instytut Informatyki/CN=ca_localhost/emailAddress=ca_admin@localhost.pl
        serial:8D:A7:61:FC:60:94:39:C1

```
```
  Signature Algorithm: md5WithRSAEncryption
    b2:bb:a6:c5:cf:5b:c7:25:42:dd:49:6d:34:f7:a0:8f:33:1d:
    2a:3f:6a:12:62:b6:48:d3:c2:1a:4a:d6:5b:14:4e:8e:98:86:
    e9:86:94:57:14:92:1a:38:46:76:0d:7f:8c:82:a0:c8:99:9c:
    60:03:f7:5a:f8:46:d7:f5:07:7a:97:19:46:5c:b8:f0:e8:ce:
    e6:0b:cd:fd:4d:22:91:28:83:af:a1:4a:b4:51:eb:bb:7d:1a:
    47:b3:8d:b5:f3:ba:dc:75:a9:5a:7d:02:43:ae:e4:37:8c:8d:
    b4:47:70:b4:86:2a:a3:d2:94:86:23:d8:8d:43:db:18:a8:1b:
    c1:39
-----BEGIN CERTIFICATE-----
MIID+jCCA2OgAwIBAgIBATANBgkqhkiG9w0BAQQFADCBrDELMAkGA1UEBhMCUEwx
DTALBgNVBAgTBFdMS1AxEDAOBgNVBAcUB1Bvem5hxYQxIDAeBgNVBAoUF1BvbGl0
ZWNobmlrYSBQb3puYcWEc2thMR0wGwYDVQQLExRJbnN0eXR1dCBJbmZvcm1hdHlr
aTEVMBMGA1UEAxQMY2FfbG9jYWxob3N0MSQwIgYJKoZIhvcNAQkBFhVjYV9hZG1p
bkBsb2NhbGhvc3QucGwwHhcNMDYwNzE1MDkxMDAwWhcNMDcwNzE1MDkxMDAwWjCB
lDELMAkGA1UEBhMCUEwxDTALBgNVBAgTBFdMS1AxEDAOBgNVBAcUB1Bvem5hxYQx
EDAOBgNVBAoTB0ZJUk1BIFgxETAPBgNVBAsUCER6aWHFgiBZMR4wHAYDVQQDFBVu
YXp3YV9zZXJ3ZXJhX2Zpcm15X1gxHzAdBgkqhkiG9w0BCQEWEGFkbWluQGZpcm1h
X3gucGwwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALixKwCL3iq/k8rkqawr
er61PgzKJFX3ZWtm+jTSDJZ2uwHwKyQnmWUReFH5a6eW7reYRZlG7R4TyburmcFZ
Dqy4iZ9qEbQEl2Z7ksEZwYKQXt/BhZbnm0TT7meKwenjFKLvDBM5wFUZijslqkm5
HqvEHYFWkMx2ibHq2EDnxwtPAgMBAAGjggFAMIIBPDAJBgNVHRMEAjAAMCwGCWCG
SAGG+EIBDQQfFh1PcGVuU1NMIEdlbmVyYXRlZCBDZXJ0aWZpY2F0ZTAdBgNVHQ4E
FgQUEri/Tb+5QMkuwXreqEt1WNjGzT0wgeEGA1UdIwSB2TCB1oAUv2K/BXwFMOXj
epCCDGFFYH7Y80mhgbKkga8wgawxCzAJBgNVBAYTAlBMMQ0wCwYDVQQIEwRXTEtQ
MRAwDgYDVQQHFAdQb3puYcWEMSAwHgYDVQQKFBdQb2xpdGVjaG5pa2EgUG96bmHF
hHNrYTEdMBsGA1UECxMUSW5zdHl0dXQgSW5mb3JtYXR5a2kxFTATBgNVBAMUDGNh
X2xvY2FsaG9zdDEkMCIGCSqGSIb3DQEJARYVY2FfYWRtaW5AbG9jYWxob3N0LnBs
ggkAjadh/GCUOcEwDQYJKoZIhvcNAQEEBQADgYEAsrumxc9bxyVC3UltNPegjzMd
Kj9qEmK2SNPCGkrWWxROjpiG6YaUVxSSGjhGdg1/jIKgyJmcYAP3WvhG1/UHepcZ
Rly48OjO5gvN/U0ikSiDr6FKtFHru30aR7ONtfO63HWpWn0CQ67kN4yNtEdwtIYq
o9KUhiPYjUPbGKgbwTk=
-----END CERTIFICATE-----
Signed certificate is in newcert.pem
testowy:/usr/share/ssl/misc #

```

Po zakończeniu procedury wystawienia certyfikatu w pliku _newcert.pem_ znajduje się wystawiony certyfikat. 
## Podsumowanie
Biblioteka Openssl jest szeroko stosowanym oprogramowaniem, które często jest elementem obowiązkowym innych programów. Niewątpliwą zaletą tej biblioteki jest również możliwość tworzenia certyfikatów w przyjazny dla użytkownika sposób, co pozwala ja wykorzystanie wsparcia dla SSL np. w serwerach www np. serwer Apache. 
## Zadanie
  * Utworzenie własnego centrum certyfikacji przy pomocy biblioteki Openssl.
  * Wygenerowanie żądania wystawienia certyfikatu
  * Wystawienie certyfikatu
  * Weryfikacja informacji o urzędzie certyfikacji i podmiocie żądającym certyfikatu za pomocą poleceń c_issuer, c_info i c_name.


## Problemy do dyskusji
  * Zalety i wady PKI
  * Jakie informacje powinny znaleźć się w certyfikatach cyfrowych?
  * Jakie usługi sieciowe korzystają z wsparcia biblioteki Openssl?
  * Jakie cechy kryptografii publicznej i prywatnej są wykorzystywane w protokole SSL?

---


# Tworzenie sieci VPN w środowisku Linux i Windows

# Bezpieczeństwo systemów komputerowych - laboratorium 11:Tworzenie sieci VPN w środowisku Linux i Windows
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
Tworzenie sieci VPN w środowisku Linux i Windows 
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Zastosowania technologii VPN](https://wazniak.mimuw.edu.pl/<#Zastosowania_technologii_VPN>)
  * [3 Oprogramowanie OpenVPN](https://wazniak.mimuw.edu.pl/<#Oprogramowanie_OpenVPN>)
    * [3.1 Podstawy](https://wazniak.mimuw.edu.pl/<#Podstawy>)
    * [3.2 Połączenie VPN Linux - Linux z wykorzystaniem mechanizmu współdzielonego klucza](https://wazniak.mimuw.edu.pl/<#Połączenie_VPN_Linux_-_Linux_z_wykorzystaniem_mechanizmu_współdzielonego_klucza>)
      * [3.2.1 Plik konfiguracyjny dla strony serwera](https://wazniak.mimuw.edu.pl/<#Plik_konfiguracyjny_dla_strony_serwera>)
      * [3.2.2 Plik konfiguracyjny dla strony klienta](https://wazniak.mimuw.edu.pl/<#Plik_konfiguracyjny_dla_strony_klienta>)
    * [3.3 Połączenie VPN Linux - Linux z wykorzystaniem mechanizmu certyfikatów cyfrowych](https://wazniak.mimuw.edu.pl/<#Połączenie_VPN_Linux_-_Linux_z_wykorzystaniem_mechanizmu_certyfikatów_cyfrowych>)
      * [3.3.1 Plik konfiguracyjny dla strony serwera](https://wazniak.mimuw.edu.pl/<#Plik_konfiguracyjny_dla_strony_serwera_2>)
      * [3.3.2 Plik konfiguracyjny dla strony klienta](https://wazniak.mimuw.edu.pl/<#Plik_konfiguracyjny_dla_strony_klienta_2>)
    * [3.4 Połączenie VPN Linux - Windows z wykorzystaniem mechanizmu współdzielonego klucza](https://wazniak.mimuw.edu.pl/<#Połączenie_VPN_Linux_-_Windows_z_wykorzystaniem_mechanizmu_współdzielonego_klucza>)
      * [3.4.1 OpenVPN w menu START](https://wazniak.mimuw.edu.pl/<#OpenVPN_w_menu_START>)
      * [3.4.2 Nowe urządzenie sieciowe](https://wazniak.mimuw.edu.pl/<#Nowe_urządzenie_sieciowe>)
      * [3.4.3 Uruchomienie OpenVPN pod Windows](https://wazniak.mimuw.edu.pl/<#Uruchomienie_OpenVPN_pod_Windows>)
      * [3.4.4 Konsola tekstowa](https://wazniak.mimuw.edu.pl/<#Konsola_tekstowa>)
      * [3.4.5 Nowe połączenie VPN](https://wazniak.mimuw.edu.pl/<#Nowe_połączenie_VPN>)
    * [3.5 Podsumowanie możliwości programu OpenVPN](https://wazniak.mimuw.edu.pl/<#Podsumowanie_możliwości_programu_OpenVPN>)
  * [4 Protokół IPsec](https://wazniak.mimuw.edu.pl/<#Protokół_IPsec>)
    * [4.1 Podstawy](https://wazniak.mimuw.edu.pl/<#Podstawy_2>)
    * [4.2 Budowanie sieci VPN z użyciem oprogramowania Openswan](https://wazniak.mimuw.edu.pl/<#Budowanie_sieci_VPN_z_użyciem_oprogramowania_Openswan>)
    * [4.3 Połączenie VPN Linux - linux z użyciem kluczy RSA](https://wazniak.mimuw.edu.pl/<#Połączenie_VPN_Linux_-_linux_z_użyciem_kluczy_RSA>)
      * [4.3.1 Generacja kluczy RSA](https://wazniak.mimuw.edu.pl/<#Generacja_kluczy_RSA>)
      * [4.3.2 Edycja pliku konfiguracyjnego ipsec.conf](https://wazniak.mimuw.edu.pl/<#Edycja_pliku_konfiguracyjnego_ipsec.conf>)
      * [4.3.3 Utworzenie połączenia VPN](https://wazniak.mimuw.edu.pl/<#Utworzenie_połączenia_VPN>)
    * [4.4 Podsumowanie możliwości programu Openswan](https://wazniak.mimuw.edu.pl/<#Podsumowanie_możliwości_programu_Openswan>)
  * [5 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [6 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [7 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)
  * [8 Dodatek A](https://wazniak.mimuw.edu.pl/<#Dodatek_A>)
    * [8.1 Utworzenie certyfikatu dla centrum certyfikacji(_ang. CA_)](https://wazniak.mimuw.edu.pl/<#Utworzenie_certyfikatu_dla_centrum_certyfikacji\(ang._CA\)>)
    * [8.2 Utworzenie pliku z kluczem prywatnym wraz z prośbą o wydanie certyfikatu dla danej strony połączenia VPN](https://wazniak.mimuw.edu.pl/<#Utworzenie_pliku_z_kluczem_prywatnym_wraz_z_prośbą_o_wydanie_certyfikatu_dla_danej_strony_połączenia_VPN>)
    * [8.3 Wydanie certyfikatu](https://wazniak.mimuw.edu.pl/<#Wydanie_certyfikatu>)


## Wprowadzenie
W wielu sytuacjach w których mamy do czynienia z rozbudowaną architekturą sieciową zależy nam aby całe środowisko rozproszone(np. oddziały firmy w różnych lokalizacjach) było jak najbardziej spójne. Dotyczy to również adresacji IP. Technologia wirtualnych sieci prywatnych(_ang. Virtual Private Network_) pozwala na rozwiązanie takich problemów. Dzięki utworzeniu sieci VPN można zbudować logiczną sieć komputerową, która będzie łączyć całe rozproszone środowisko ukrywając sieci łączące odległe od siebie lokalizacje i tym samym uprości wymianę danych między nimi. Budując sieć VPN tworzymy logiczne tunele między wyznaczonymi lokalizacjami. W ten sposób technologia VPN tworzy iluzję w której odległe od siebie lokalizacje są fizycznie bezpośrednio połączone. Ta cecha sieci VPN wpływa na uproszenie sposobu wymiany ruchu między tymi lokalizacjami. W obecnej chwili myśląc o technologii VPN oraz jej możliwościach oprócz wyżej wymienionej cechy bierzemy pod uwagę stopień bezpieczeństwa jaki zapewnia nam połączenie VPN. Tworzenie sieci VPN bez wsparcia dla bezpieczeństwa przysyłanych informacji w obecnej chwili jest rzadko stosowane z uwagi na wzrost poziomu poufności przesyłanych danych. Wielu producentów sprzętu sieciowego w swojej ofercie handlowej oferuje różnego typu rozwiązania do kompleksowej budowy sieci VPN. Rozwiązania te cechują się różnym stopniem bezpieczeństwa, skalowalności oraz łatwości wdrożenia. Przeważająca część tych rozwiązań VPN posiada wsparcie dla kryptograficznych mechanizmów ochrony poufności i/lub integralności przesyłanych danych. Najprostsze rozwiązania mogą w ogóle nie wspierać ochrony poufności przesyłanych danych, bardziej zaawansowane mogą korzystać z mechanizmu współdzielonego klucza i algorytmów kryptografii symetrycznej do ochrony poufności, najbardziej zaawansowane rozwiązania korzystają z mechanizmów kryptografii klucza publicznego, certyfikatów cyfrowych. 
Słowa kluczowe: ssl, vpn, ipsec, certyfikat cyfrowy, openvpn, openswan, tun/tap 
## Zastosowania technologii VPN
Głównym zastosowaniem technologii VPN jest tworzenie logicznych kanałów między zdalnymi lokalizacjami. Wiele dużych firm telekomunikacyjnych oferuje swoim klientom możliwość zestawiania połączeń VPN między zdalnymi lokalizacjami zamiast dzierżawy fizycznych łącz z uwagi na oszczędności dla klienta oraz większą elastyczności w zarządzaniu takimi połączeniami dla operatora telekomunikacyjnego. W rozwiązaniach typu SOHO(_ang. Small Office Home Office_) bardziej rozbudowane rozwiązania również wspierają tworzenie sieci VPN. Przydaje się to w sytuacjach, gdy pracownik pracuje w domu i potrzebuje połączenia do sieci firmowej. Inna możliwość to użycie odpowiedniego oprogramowania klienckiego na komputerze pracownika pracującego poza siedzibą firmy. Takie oprogramowanie zestawia połączenie VPN między komputerem pracownika a urządzeniem dostępowym w siedzibie firmy. Oprócz tradycyjnych rozwiązań VPN wspierających protokół IPsec istnieje druga, również popularna grupa rozwiązań opartych o wykorzystanie protokołu SSL jako mechanizmu do budowy bezpiecznych kanałów wymiany danych. Sieci tworzone z użyciem mechanizmu SSL VPN określane są również jako „sieci bez klienta”(_ang. clientless_) z uwagi, że inaczej niż ma to miejsce w klasycznych sieciach VPN opartych o IPsec, nie jest potrzebne dedykowane oprogramowanie klienckie dla klienta takiej sieci, wystarczy przeglądarka stron www wspierająca protokół SSL. Klient posiadający przeglądarkę wspierającą protokół SSL łączy się z serwerem dostępowym i po ustanowieniu połączenia SSL, po przez przeglądarkę uzyskuje dostęp do wewnętrznych zasobów sieci VPN. Istnieją również inne rozwiązania SSL, które posiadają dedykowane oprogramowanie do zestawiania połączeń SSL VPN. Dzięki takiemu podejściu możliwości połączeń SSL VPN zbliżają się do klasycznych sieci VPN opartych o protokół IPsec i pozwalają przesyłać ruch sieciowy dowolnej aplikacji opakowując go protokołem SSL. Takim rozwiązaniem jest program OpenVPN. 
## Oprogramowanie OpenVPN
Program OpenVPN jest narzędziem służącym do tworzenia szyfrowanego połączenia VPN w sieci TCP/IP. Instalacja tego programu nie wymaga ingerencji w jądro systemu operacyjnego Linux przez co rozwiązanie to jest proste i łatwe w uruchomieniu. Tunel jest tworzony z wykorzystaniem wirtualnych interfejsów sieciowych TUN/TAP. Utworzenie tunelu sprowadza się do utworzenia pliku konfiguracyjnego opisującego parametry połączenia i uruchomienie programu openvpn z tym plikiem jako parametrem. Z drugiej strony tunelu również wykorzystujemy ten sam program ale w roli klienta i przyłączamy się do poprzednio uruchomionego serwera. Bardzo dużą zaletą programu OpenVPN jest możliwość tworzenia szyfrowanych tuneli z hostami korzystającymi z systemu Windows ,co w niektórych sytuacjach może okazać się kluczowe przy wyborze darmowego oprogramowania do tworzenia sieci VPN. OpenVPN pozwala tworzyć szyfrowane połączenia w oparciu o dwie metody: 
  * „Pre-shared key” mechanizm w którym strony połączenia współdzielą między sobą tajny klucz służący do uwierzytelniania stron i szyfrowania komunikacji. OpenVPN wykorzystuje kryptograficzny algorytm blowfish z 128 bitowym kluczem w trybie CBC(ang. Cipher Block Chaining)
  * Certyfikaty cyfrowe SSL, OpenVPN wykorzystuje bibliotekę OpenSSL do tworzenia certyfikatów cyfrowych SSL(tryb SSL/TLS)


### Podstawy
Wygenerowanie współdzielonego klucza i zapisanie go do pliku następuje po wykonaniu komendy: 
```
openvpn -genkey -secret shared.key

```

W pliku shared.key w bieżącym katalogu zostanie zapisany klucz, który posłuży do utworzenia bezpiecznego połączenia VPN. 
Program OpenVPN nie posiada wyróżnionej części klienta i serwera. Dla obu stron połączenia wykorzystywany jest ten sam program zapisany w wykonywalnym pliku o nazwie openvpn. Odpowiednia opcja w pliku konfiguracyjnym wymusza działanie w trybie klienta lub serwera. Poniżej zaprezentowano komendę uruchamiającą program OpenVPN: 
```
openvpn –config /etc/openvpn/static.conf

```

Program OpenVPN pozwala aby opcje konfiguracyjne zostały podane jako parametry podczas wywołania pliku wykonywanego openvpn jednak zapisanie opcji w pliku wydaje się bardziej wygodne. 
Poniżej zaprezentowano przykładową architekturę połączenia VPN: 
[![Przyklad arch vpn.png](https://wazniak.mimuw.edu.pl/images/2/2c/Przyklad_arch_vpn.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Przyklad_arch_vpn.png>)
Nawiązane połączenie VPN między komputerem przenośnym o serwerem powinno utworzyć podsieć 10.8.0.0/24 i po przez to połączenie komputer przenośny powinien uzyskać dostęp do dwóch podsieci po stronie serwera tj. 192.168.11.0/24 i 192.168.10.0/24. 
### Połączenie VPN Linux - Linux z wykorzystaniem mechanizmu współdzielonego klucza
Uwierzytelniania i szyfrowanie następuje z wykorzystaniem mechanizmu współdzielonego klucza. Serwer na którym jest uruchomiony program OpenVPN jest dostępny pod adresem ip 150.254.30.19 i nasłuchuje na porcie tcp 1194. Koniec połączenia VPN do strony serwera ma adres ip 10.8.0.1 a od strony klienta: 10.8.0.2. 
#### Plik konfiguracyjny dla strony serwera
```
dev tun
ifconfig 10.8.0.1 10.8.0.2
secret /etc/openvpn/static.key
proto tcp-serwer
daemon
verb 4
log-append /var/log/openvpn.og
keepalive 10 900
inactive 3600
comp-lzo

```

Opcja tcp-server wymusza użycie protokołu TCP warstwy czwartej do utworzenia logicznego kanału danych oraz określa bieżącą stronę połączenia jako serwerową czyli oczekującą na połączenia. OpenVPN pozwala również na utworzenie połączenia VPN z użyciem protokołu UDP. 
Opcja ifconfig definiuje oba końce połączenia VPN. 
Opcja secret wskazuje na plik z współdzielonym kluczem. 
Opis wszystkich parametrów programu OpenVPN znajduje się na stronie domowej projektu OpenVPN oraz w podręczniku systemowym do programu openvpn(_man openvpn_). 
#### Plik konfiguracyjny dla strony klienta
```
dev tun
remote 150.254.30.19 1194
proto tcp-client
ifconfig 10.8.0.2 10.8.0.1
secret /home/piotr/openvpn.conf
keepalive 10 60
route 192.168.10.0 255.255.255.0
route 192.168.11.0 255.255.255.0
comp-lzo

```

Opcja remote określa adres i numer portu pod jakim serwer OpenVPN jest dostępny. Opcja ifconfig definiuje oba końce połączenia VPN. Należy zwrócić uwagę na kolejność parametrów polecenie ifconfig. 
Opis wszystkich parametrów programu OpenVPN znajduje się na stronie domowej projektu OpenVPN oraz w podręczniku systemowym do programu openvpn(_man openvpn_). 
### Połączenie VPN Linux - Linux z wykorzystaniem mechanizmu certyfikatów cyfrowych
Program OpenVPN pozwala wykorzystać infrastrukturę klucza publicznego do tworzenia bezpiecznych kanałów wymiany danych. Certyfikaty SSL pozwalają wynegocjować parametry połączenia VPN oraz uzgodnić jednorazowy klucz sesyjny służący do szyfrowania komunikacji między stronami połączenia. Użycie certyfikatów SSL to najbardziej zaawansowana i najbezpieczniejsza konfiguracja programu OpenVPN. 
#### Plik konfiguracyjny dla strony serwera
```
dev tun 
proto tcp-server
ifconfig 10.8.0.1 10.8.0.2
keepalive 10 60
verb 4
deamon
comp-lzo
log-append /var/log/openvpn.log
persist-tun
persist-local-ip
persist-remote-ip
persist-key
#############SSL#####
tls-server
tls-remote nazwa_strony_klienta
ca cacert.pem
dh dh1024.pem
cert newcert.pem
key newreq.pem
cipher aes-256-cbc
#############SSL#####

```

Opcja tls-remote wymaga podania nazwy Common name z certyfikatu klienta. Opcja dh wskazuje na plik z dużą liczbą pierwszą. 
Opis wszystkich parametrów programu OpenVPN znajduje się na stronie domowej projektu OpenVPN oraz w podręczniku systemowym do programu openvpn(_man openvpn_). 
#### Plik konfiguracyjny dla strony klienta
```
dev tun
proto tcp-client
comp-lzo
verb 4
log-append /var/log/openvpn.log
persist-tun
persist-local-ip
persist-remote-ip
persist-key
ifconfig 10.8.0.2 10.8.0.1
route 192.168.10.0 255.255.255.0
route 192.168.11.0 255.255.255.0
########SSL#####
tls-client
tls-remote nazwa_strony_serwera
ca cacert.pem
cert newcert.pem
key newreq.pem
cipher aes-256-cbc
########SSL#####

```

### Połączenie VPN Linux - Windows z wykorzystaniem mechanizmu współdzielonego klucza
OpenVPN jest narzędziem, które pozwala na tworzenie tuneli nie tylko miedzy hostami działającymi pod kontrolą systemu Linux ale również pod Windows. Program openvpn posiada specjalną wersję pod Windows, która pozwala na uruchomienie tunelu np. między Linuxem a systemem Windows. Poniżej pokazano jak można utworzyć tunel VPN z użyciem mechanizmu współdzielonego klucza. Konfiguracja z użyciem certyfikatów SSL jest również możliwa. 
#### OpenVPN w menu START
Po zainstalowaniu pod Windows OpenVPN posiada osobne podmenu. 
[![Openvpn w menu.png](https://wazniak.mimuw.edu.pl/images/f/f7/Openvpn_w_menu.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openvpn_w_menu.png>)
#### Nowe urządzenie sieciowe
Niezbędnym elementem zarówno w systemie Linux jak w Windows jest wirtualne urządzenie sieciowe wykorzystywane przez OpenVPN do komunikacji sieciowej. Instalując OpenVPN pod Windows oprócz samego programu, instalowany jest wirtualny interfejs sieciowy _TAP-win32 Adapter_. 
[![Openvpn sterownik tap.png](https://wazniak.mimuw.edu.pl/images/a/a9/Openvpn_sterownik_tap.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openvpn_sterownik_tap.png>)
#### Uruchomienie OpenVPN pod Windows
Wystarczy wybrać z menu kontekstowego odpowiednią opcję. Należy zwrócić uwagę na kilka rzeczy: 
  * plik konfiguracyjny musi mieć rozszerzenie .ovpn
  * plik konfiguracyjny musi znajdować się w katalogu config programu openvpn (patrz ramka z adresem folderu)


[![Openvpn uruchomienie.png](https://wazniak.mimuw.edu.pl/images/1/1a/Openvpn_uruchomienie.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openvpn_uruchomienie.png>)
#### Konsola tekstowa
Wybranie opcji uruchomienia OpenVPN z menu kontekstowego spowoduje otwarcie okna konsoli tekstowej w której można obserwować postęp w negocjacji połączenia. Jeżeli zdecydujemy się aby logowanie odbywało się do pliku, na konsoli nie zobaczymy logów. Utworzenie tunelu następuje po zakończeniu procedury negocjacji parametrów połączenia(patrz ostatnia linia na zrzucie ekranowym poniżej). 
[![Openvpn konsola.png](https://wazniak.mimuw.edu.pl/images/c/cc/Openvpn_konsola.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openvpn_konsola.png>)
#### Nowe połączenie VPN
Po zakończeniu procedury tworzenia tunelu wykonując polecenie systemowe ipconfig obserwujemy obecność nowego interfejsu sieciowego o adresie ip identycznym jak adres końca połączenia VPN dla danej strony. 
[![Openvpn ipconfig.png](https://wazniak.mimuw.edu.pl/images/a/a5/Openvpn_ipconfig.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openvpn_ipconfig.png>)
### Podsumowanie możliwości programu OpenVPN
Program OpenVPN jest ciekawą alternatywą dla klasycznych rozwiązań VPN opartych o protokół IPsec. Konfiguracja połączeń VPN jest bardzo prosta i zrozumiała nawet dla użytkownika nieobeznanego z technologią sieci VPN. Bardzo dużą zaletą OpenVPN jest korzystanie z biblioteki OpenSSL, co sprawia, że rozwiązanie OpenVPN może być uznawane za mechanizm tworzenie sieci VPN o wysokim stopniu bezpieczeństwa. Można również zestawiać połączenia VPN z użyciem mechanizmu współdzielonego klucza dla mniej zaawansowanych przypadków użycia. Warto również zwrócić uwagę na możliwość łatwego zestawiania połączeń w środowisku mieszanym w którym występują systemy Linux i Windows. Wadą programu OpenVPN jest jego skalowalność. Chcąc zestawić więcej połączeń VPN z danego hosta należy uruchomić kolejną instancję programu OpenVPN. Wadą ta jest częściowo rekompensowana przez bardzo przejrzystą strukturę pliku konfiguracyjnego. 
## Protokół IPsec
Protokół sieciowy IP w wersji 4 nie posiada mechanizmów służących do sprawdzania integralności przesyłanych danych oraz zapewniania poufności tych danych. Słabości protokołu IP pod tym względem ma usprawnić protokół IPsec. W przypadku protokołu IP w wersji 4 IPsec jest opcjonalnym dodatkiem. W protokole IP w wersji 6 funkcjonalność IPsec jest wymagana. 
### Podstawy
Głównymi zdaniami protokołu IPsec jest ochrona integralności przesyłanych danych i zapewnienie poufności. Mechanizmy odpowiedzialne za te funkcjonalności są konfigurowalne i w razie potrzeby można je wyłączyć w zależności od aktualnych potrzeb. Kolejna cecha protokołu IPsec to jego przezroczystość dla protokołów warstw wyższych. Protokół IPsec działa na poziomie warstwy 3 modelu sieciowego ISO/OSI i dlatego możliwe jest przysyłanie za jego pomocą ruchu sieciowego niezależnie od aplikacji generującej ten ruch oraz, co równie ważne obecność IPsec jest nie widoczna dla tych aplikacji. Ma to bardzo duże znaczenie praktyczne, gdyż nie ma potrzeby modyfikacji aplikacji sieciowych już napisanych a to w istotny sposób obniża koszty wdrożenia protokołu IPsec. Protokół IPsec w ogólności składa się z kilku elementów. Są to protokoły AH i ESP oraz mechanizm negocjacji parametrów połączenia IKE. Protokół AH(_ang. Authentication Header_) jest odpowiedzialny za ochronę integralności przesyłanych danych jak i nagłówka samego pakietu. Jako mechanizmy zapewniające integralność stosowane są funkcje tworzące skrót kryptograficzny np. MD5, SHA1, RIPEMD-160. Protokół ESP(_ang. Encapsulation Security Payload_) jest odpowiedzialny za zapewnienie poufności przesyłanych danych. Wykorzystywane algorytmy do szyfrowania to DES, 3DES, Blowfish, Rijndael/AES. IPsec może działać w dwóch trybach: transportowym i tunelowym. W trybie transportowym między nagłówek IP a nagłówek warstwy wyższej umieszczany jest nagłówek protokołu IPsec np. ESP. W ten sposób chroniona jest zawartość pakietu ale podsłuchujący wiem kto z kim wymienia dane, co nie koniecznie może być jawne. W trybie tunelowym cały pakiet danych wymienianych między stronami jest ukrywany przez zaszyfrowanie i opakowany przez protokół ESP. Ten tryb jest rozwiązaniem bardziej bezpiecznym i przydaje się w konfiguracji określanej NET-to-NET w której pomiędzy dedykowanymi hostami(SA, _ang. Security Gateway_) zestawione jest połączenie VPN trybie tunelowym a za hostami znajdują się wewnętrzne sieci. W taki skonfigurowanym połączeniu VPN podsłuchujący nie ma możliwości podejrzenia kto z kim wymienia dane ponieważ ruch sieciowy wymieniany jest tylko między hostami SA. Protokół IKE(_ang. Internet Key Exchange_) jest odpowiedzialny za automatyczną negocjację parametrów połączenia VPN. IKE składa się z dwóch części: 
  * ISAKMP(ang. Internet Security Association and Key Management Protocol) protokół negocjacji parametrów połączenia.
  * Oakley protokół wymiany kluczy za pomocą algorytmu Diffie-Hellmana.


### Budowanie sieci VPN z użyciem oprogramowania Openswan
Program Openswan jest ogólnie dostępną implementacją IPsec pod systemy Linux. Openswan pozwala wykorzystać możliwości IPsec i zestawiać połączenia nie tylko między systemami Linux ale również z systemami Windows oraz routerami czy bramami VPN. Openswan występuje jako rozszerzenie dla jądra systemu Linux. Można go pobrać ze strony projektu w postaci źródeł jak i postaci przygotowanego zestawu np. rpm. W niektórych dystrybucjach Linuxa np. SuSE Openswan jest dostarczany w formie rpm a jądro wspiera IPsec. 
### Połączenie VPN Linux - linux z użyciem kluczy RSA
Jedną z najprostszych konfiguracji połączenia VPN z użyciem Openswan jest zestawienie połączenia z użyciem kluczy RSA. Pliki konfiguracyjne dla obu stron połączenia VPN są bardzo podobne. Poniżej zaprezentowano przykładową architekturę sieci w której między dwoma serwerami zostanie utworzone połączenie VPN. 
[![Openswan przykladowa architektura.png](https://wazniak.mimuw.edu.pl/images/c/c7/Openswan_przykladowa_architektura.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Openswan_przykladowa_architektura.png>)
#### Generacja kluczy RSA
```
ipsec newhostkey --output /etc/ipsec.secrets --hostname nazwa_domenowa_hosta

```

#### Edycja pliku konfiguracyjnego ipsec.conf
Aby zdefiniować połączenie VPN w pliku ipsec.conf należy dopisać nową sekcję, która będzie definiować parametry połączenia. Poniżej zaprezentowano przykładowy plik konfiguracyjny dla rysunku powyżej. 
```
conn nazwa_polaczenia
left=172.123.20.9
leftsubnet=192.168.10.0/24
leftnexthop=%defaultroute
leftrsasigkey=...
right=150.254.20.35
rightsubnet=172.116.20.0/24
rightnexthop=%defaultroute
rightnexthop=...
authby=rsasig
auto=start

```

Parametry leftrsasigkey i rightrsasigkey wymagają jawnego podania wartości kluczy. Aby to zrobić ja jednym systemie będącym lewą stroną połączenia należy wydać polecenie: 
```
ipsec showhostkey –-left

```

Na hoście będącym prawą stroną połączenia należy wydać polecenie: 
```
ipsec showhostkey --right

```

Wykonanie poleceń spowoduje wypisanie na okno terminala odpowiednich kluczy. Należy je skopiować pod podane wyżej parametry(leftrsasigkey i rightrsasigkey). Po zakończeniu tej procedury obie strony połączenia powinny dysponować identycznym plikiem ipsec.conf. Kwestia, która strona jest lewą lub prawą jest umowna. 
#### Utworzenie połączenia VPN
Z uwagi na wartość ostatniego parametru(auto=start) ustanowienie połączenia VPN nastąpi w chwili uruchomienie programu ipsec. W systemach SuSE będzie to polecenie /etc/init.d/ipsec start i ipsec auto –up nazwa_polaczenia 
### Podsumowanie możliwości programu Openswan
Program Openswan jest rozwiązaniem bardziej zaawansowanym niż OpenVPN. Pozwala tworzyć bardziej zaawansowane konfiguracje. Z uwagi na wykorzystywany protokół IPsec Openswan może służyć jako mechanizm do zestawiania połączeń z sieciowymi urządzeniami wspierającymi tworzenie sieci VPN takimi jak routery czy bramy VPN. Openswan wspiera również wykorzystanie certyfikatów cyfrowych. 
## Zadania
  * Zestawienie połączenia VPN z użyciem programu OpenVPN z wykorzystaniem mechanizmu współdzielonego klucza
  * Zestawienie połączenia VPN z użyciem programu OpenVPN z wykorzystaniem mechanizmu certyfikatów cyfrowych
  * Zestawienie połączenia VPN z użyciem programu Openswan z wykorzystaniem kluczy RSA


## Problemy do dyskusji
  * Jakie zagrożenia dla bezpieczeństwa niesie za sobą mechanizm współdzielonego klucza?
  * Czy używanie certyfikatów SSL jest bezpieczniejsze niż mechanizm współdzielonego klucza i dlaczego?
  * Czy można zestawiać połączenia VPN bez szyfrowania komunikacji?
  * W jakich sytuacjach rozwiązania SSL VPN są wyborem bardziej optymalnym niż rozwiązania oparte o IPsec?


## Bibliografia
  * strona domowa projektu OpenVPN _<http://www.openvpn.net>_
  * Artykuł „VPN na miarę" Maciej Koziński _<http://www.pckurier.pl/archiwum/art0.asp?ID=6130>_
  * Techniczny biuletyn zabezpieczeń IT firmy Clico „Rozważania nt. Wariantów wdrożenia sieci IPsec VPN i SSL VPN" _<http://www.clico.pl/b/t/no_9/vpn_ipsec_ssl_fin.pdf>_


## Dodatek A
Generacja certyfikatów SSL. Wykorzystany zostanie skrypt CA.sh znajdujący się w podkatalogu misc/ biblioteki OpenSSL. 
### Utworzenie certyfikatu dla centrum certyfikacji(_ang. CA_)
```
CA.sh -newca

```

### Utworzenie pliku z kluczem prywatnym wraz z prośbą o wydanie certyfikatu dla danej strony połączenia VPN
```
CA.sh -newreq

```

Należy podać wszystkie dane niezbędne do utworzenia certyfikatu. Należy zwrócić uwagę na pole Common Name. Tekst wpisany w tym polu będzie potrzeby jako parametr dla pola tls-remote drugiej strony połączenia. 
### Wydanie certyfikatu
```
CA.sh -sign

```

Po wykonaniu wszystkich kroków zostaną utworzone następujące pliki: 
  * cacert.pem - plik z certyfikatem dla centrum certyfikacji(krok nr 1)
  * newreq.pem - plik z prośbą o wydanie certyfikatu oraz kluczem prywatnym jednej ze stron połączenia(krok nr 2)
  * newcert.pem - plik z certyfikatem i z kluczem publicznym dla danej strony połączenia(krok 3)


Krok nr 1 należy wykonać tylko raz. Kroki nr 2 i 3 należy wykonać dwa razy po jednym dla każdej strony połączenia VPN. 
---


# Systemy programowych zapór sieciowych

# Bezpieczeństwo systemów komputerowych - laboratorium 12:Systemy programowych zapór sieciowych
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Informacje o zaporach sieciowych](https://wazniak.mimuw.edu.pl/<#Informacje_o_zaporach_sieciowych>)
    * [2.1 Ogólne założenie zapory sieciowej z systemie operacyjnym Linux](https://wazniak.mimuw.edu.pl/<#Ogólne_założenie_zapory_sieciowej_z_systemie_operacyjnym_Linux>)
    * [2.2 Konfiguracja iptables](https://wazniak.mimuw.edu.pl/<#Konfiguracja_iptables>)
    * [2.3 Diagram przepływu pakietów przez zaporę sieciową IPTABLES](https://wazniak.mimuw.edu.pl/<#Diagram_przepływu_pakietów_przez_zaporę_sieciową_IPTABLES>)
    * [2.4 Składnia polecenia iptables (składnia reguły)](https://wazniak.mimuw.edu.pl/<#Składnia_polecenia_iptables_\(składnia_reguły\)>)
    * [2.5 Translacja adresów](https://wazniak.mimuw.edu.pl/<#Translacja_adresów>)
      * [2.5.1 SNAT](https://wazniak.mimuw.edu.pl/<#SNAT>)
      * [2.5.2 DNAT](https://wazniak.mimuw.edu.pl/<#DNAT>)
    * [2.6 Moduły rozszerzające IPTABLES](https://wazniak.mimuw.edu.pl/<#Moduły_rozszerzające_IPTABLES>)
      * [2.6.1 Krótkie opisy modułów](https://wazniak.mimuw.edu.pl/<#Krótkie_opisy_modułów>)
        * [2.6.1.1 Dotyczące IPSec:](https://wazniak.mimuw.edu.pl/<#Dotyczące_IPSec:>)
        * [2.6.1.2 Dopasowujące się do nagłówka pakietu IP:](https://wazniak.mimuw.edu.pl/<#Dopasowujące_się_do_nagłówka_pakietu_IP:>)
        * [2.6.1.3 Nadzorujące połączenia (stanowość):](https://wazniak.mimuw.edu.pl/<#Nadzorujące_połączenia_\(stanowość\):>)
        * [2.6.1.4 Określające typ pakietu:](https://wazniak.mimuw.edu.pl/<#Określające_typ_pakietu:>)
        * [2.6.1.5 Określające limity:](https://wazniak.mimuw.edu.pl/<#Określające_limity:>)
        * [2.6.1.6 Znakowanie pakietów:](https://wazniak.mimuw.edu.pl/<#Znakowanie_pakietów:>)
        * [2.6.1.7 Ułatwiające tworzenie reguł:](https://wazniak.mimuw.edu.pl/<#Ułatwiające_tworzenie_reguł:>)
        * [2.6.1.8 Rozszerzone sprawdzanie pakietów:](https://wazniak.mimuw.edu.pl/<#Rozszerzone_sprawdzanie_pakietów:>)
        * [2.6.1.9 Określające częstość:](https://wazniak.mimuw.edu.pl/<#Określające_częstość:>)
        * [2.6.1.10 Monitorujące:](https://wazniak.mimuw.edu.pl/<#Monitorujące:>)
        * [2.6.1.11 Inne:](https://wazniak.mimuw.edu.pl/<#Inne:>)
      * [2.6.2 Krótkie opisy celów (TARGETs)](https://wazniak.mimuw.edu.pl/<#Krótkie_opisy_celów_\(TARGETs\)>)
        * [2.6.2.1 Zmiana adresów IP:](https://wazniak.mimuw.edu.pl/<#Zmiana_adresów_IP:>)
        * [2.6.2.2 Znakowanie pakietów:](https://wazniak.mimuw.edu.pl/<#Znakowanie_pakietów:_2>)
        * [2.6.2.3 Zmieniające nagłówek pakietu:](https://wazniak.mimuw.edu.pl/<#Zmieniające_nagłówek_pakietu:>)
        * [2.6.2.4 Śledzenie pakietów:](https://wazniak.mimuw.edu.pl/<#Śledzenie_pakietów:>)
        * [2.6.2.5 Logowanie:](https://wazniak.mimuw.edu.pl/<#Logowanie:>)
        * [2.6.2.6 Inne:](https://wazniak.mimuw.edu.pl/<#Inne:_2>)
      * [2.6.3 Szczegółowe informacje](https://wazniak.mimuw.edu.pl/<#Szczegółowe_informacje>)
  * [3 Przykłady](https://wazniak.mimuw.edu.pl/<#Przykłady>)
  * [4 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [5 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [6 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Programowe zapory sieciowe (_ang. firewall_) wykorzystywane mogą być do przeróżnych celów w zależności od złożoności takiej zapory programowej. Wyróżniamy zapory osobiste (_ang. personal firewall_) oraz zapory ogólnego przeznaczenia. 
Zapora sieciowa ma za zadanie filtrować ruch przychodzący i wychodzący z danego urządzenia sieciowego (na przykład komputera). Dzięki filtrowaniu ruchu możemy zapewnić bezpieczeństwo sieciowe urządzenia, jednak należy pamiętać, iż nigdy nie zapewnimy 100% bezpieczeństwa sieciowego, chyba że odłączymy komputer od sieci. 
Celem ćwiczenia jest zapoznania się z programową zaporą sieciową systemu Linux IPTABLES oraz wykorzystanie jej możliwości do rozwiązania postawionych problemów. 
## Informacje o zaporach sieciowych
Zapora sieciowa zawiera filtr pakietów, którego zadaniem jest sprawdzanie nagłówków pakietów przepływających przez stos protokołów. Decyduje o ich losie, **akceptując**(ang. _accept_) lub **odrzucając** (ang. _drop_) poszczególne pakiety. 
Zapory sieciowe dzielimy na osobiste oraz ogólnego przeznaczenia, różnice są znaczne, pierwsze z wymienionych nadają się wyłącznie do ochrony komputera używanego jako jednostki końcowej do pracy (lub zabawy), najczęściej zapory tego typu pytają się użytkownika czy ma przepuścić czy nie dany ruch sieciowy. Natomiast zapory ogólnego przeznaczenia charakteryzują się bardziej różnorodnym zastosowaniem, jednakże wymagają większej wiedzy, aby poprawnie je skonfigurować. 
Iptables jest zaporą ogólnego przeznaczenia, dlatego skupimy się nad jego możliwościami od najbardziej podstawowych po bardziej złożone. 
### Ogólne założenie zapory sieciowej z systemie operacyjnym Linux
W systemie Linux filtrowanie pakietów IP jest wbudowane w jądro systemu operacyjnego. Od wersji 2.3.15 jądra odpowiedzialny jest za to moduł o nazwie netfilter, oferujący niezależną filtrację pakietów przychodzących, wychodzących oraz routowanych. Moduł ten pracuje jako swoisty rdzeń umożliwiający dołączanie różnych modułów konfiguracji i administracji filtracji pakietów, np. modułu iptables. Z kolei narzędzie iptables służy do dynamicznego konstruowania reguł filtracji. Reguły przechowywane są w pamięci jądra, a ich stałą dostępność można zapewnić przechowując wybrane konfiguracje w plikach (wykorzystując skrypty iptables-save i iptables-restore). 
### Konfiguracja iptables
Konfigurowanie filtracji polega na definiowaniu tzw. reguł _(ang. rule_). Pojedyncza reguła składa się z wzorca i akcji. Gdy wiadomość poddawana jest analizie, najpierw dopasowywana jest do wzorca; jeśli do niego pasuje, o dalszym losie wiadomości decyduje akcja reguły. Jeśli zaś dane w wiadomości nie pasują do wzorca danej reguły, pod uwagę brana jest kolejna reguła. Reguły przeglądane są w takim porządku, w jakim zostały wprowadzone. Dla danej wiadomości przeszukiwanie reguł trwa do momentu pierwszego dopasowania do wzorca lub (w przypadku braku dopasowania) do wyczerpania reguł. 
Akcja reguły zależy od jej typu. Wyróżnia się trzy typy reguł: 
  * reguły filtrujące,
  * reguły translacji NAT,
  * reguły do manipulacji zaawansowanymi opcjami protokołu IP.


Dla przykładu, w regułach filtrujących akcją jest najczęściej odrzucenie (**DROP**) lub akceptacja wiadomości (**ACCEPT**). Wszystkie reguły tego samego typu pamiętane są w strukturze zwanej tablicą (_ang. table)_ , od której pakiet bierze swą nazwę. Istnieją zatem trzy wbudowane tablice: 
  * filter (dla reguł filtrujących),
  * nat (dla reguł translacji NAT),
  * mangle (dla reguł manipulujących opcjami IP).


Datagramy IP również dzielą się na kilka rodzajów. Rodzaj datagramu zależy od kombinacji adresów źródłowego i docelowego w nim zawartych. Wyróżnia się zatem: 
  * datagramy, dla których dana stacja jest celem,
  * datagramy, których dana stacja jest źródłem,
  * kombinację rodzajów 1 i 2,
  * datagramy rutowane.


W zależności od rodzaju datagramu, jego przetwarzanie przebiega w kilku etapach. Na przykład dla datagramów rutowanych etapy te w uproszczeniu wyglądają następująco: 
1 - pakiet dociera do interfejsu wejściowego, 
2 - zostaje wybrany dla niego właściwy interfejs wyjściowy, 
3 - pakiet opuszcza stację przez interfejs wyjściowy. 
Na każdym etapie można stosować do datagramu różne typy reguł. Dlatego wewnątrz każdej tablicy reguły są dodatkowo grupowane ze względu na etap przetwarzania pakietu. Wobec tego różne tablice mogą zawierać grupy reguł związanych z tym samym etapem. Sekwencja reguł powstała przez połączenie tych grup nazywa się'_'_**łańcuchem** (_ang. chain_). Pakiet iptables zawiera pięć wbudowanych łańcuchów: 
  * INPUT (dla datagramów pierwszego rodzaju),
  * OUTPUT (dla pakietów drugiego rodzaju),
  * FORWARD (dla pakietów rutowanych)
  * PREROUTING,
  * POSTROUTING.


Dwa ostatnie łańcuchy zawarte są jedynie w tablicach **nat** i **mangle**. 
### Diagram przepływu pakietów przez zaporę sieciową IPTABLES
[![Bsi 12 01.png](https://wazniak.mimuw.edu.pl/images/a/a7/Bsi_12_01.png)](https://wazniak.mimuw.edu.pl/</index.php?title=Plik:Bsi_12_01.png>)
### Składnia polecenia iptables (składnia reguły)
Ogólna postać reguły: 
iptables [ -t tablica ] komenda [wzorzec] [akcja] 
Komendy: 
  * -P _łańcuch polityka -_ ustawienie domyślnej polityki dla łańcucha. Domyślna polityka stosowana jest dopiero wówczas, gdy pakiet nie pasuje do żadnej reguły łańcucha,
  * -A _łańcuch_ - dodanie reguły do określonego łańcucha,
  * -I _łańcuch_[_nr reguły_] _-_ wstawienie reguły do określonego łańcucha, jeśli zostanie podany nr reguły wtedy reguła zostanie wpisane w to miejsce zmieniając kolejność pozostałych,
  * -L [_łańcuch_] - wyświetlenie wszystkich reguł łańcucha (lub wszystkich łańcuchów w danej tablicy); często używane z opcjami -n i -v,
  * -F [_łańcuch_] - usunięcie wszystkich reguł łańcucha (lub ze wszystkich łańcuchów danej tablicy),
  * -D _łańcuch_ [_nr reguły_] - usunięcie konkretnej reguły w określonym łańcuchu, jeśli zostanie podany nr reguły wtedy zostanie usunięta reguła o tym numerze,
  * -R _łańcuch nr_reguły -_ zastąpienie reguły numer w określonym łańcuchu.


Opcje wzorca: 
  * -s [!] _ip_[_/netmask_] - adres IP źródłowy (może być uogólniony do adresu sieci),
  * -d [!] _ip_[_/netmask_] - adres IP docelowy (może być uogólniony do adresu sieci),
  * -p [!] _protokół_ - wybór protokołu: tcp, udp, icmp lub all (wszystkie protokoły stosu TCP/IP),
  * -i [!] _interfejs wejściowy_
  * -o [!]_interfejs wyjściowy_
  * --sport [!] _port_ :[_port_] - port źródłowy,
  * --dport [!] _port_ :[_port_] - port docelowy,
  * -m _moduł_ - załadowanie modułu rozszerzającego, dzięki temu można wykorzystać kolejne opcje danego modułu.


Najważniejsze akcje: 
  * -j ACCEPT - przepuszczenie dopasowanych pakietów,
  * -j DROP - usunięcie dopasowanych pakietów,
  * -j REJECT - odrzucenie dopasowanych pakietów,
  * -j LOG - logowanie dopasowanych pakietów, bez usunięcia ich z łańcucha,
  * -j RETURN - usunięcie pakietu z łańcucha, pozwalając jednocześnie, aby dalej był pakiet sprawdzany w kolejnych łańcuchach,
  * -j SNAT - translacja adresów źródłowych,
  * -j DNAT - translacja adresów docelowych,
  * -j SAME - translacja adresów źródłowych i docelowych,
  * -j REDIRECT - przekierowanie pakietów do lokalnego systemu,
  * -j MASQUERADE - translacja adresów źródłowych na adres dynamicznie przyznawany na interfejsie.


### Translacja adresów
Technologia translacji adresów sieciowych (ang. _Network Address Translation, w skrócie NAT_) została po raz pierwszy zaproponowana przez firmę Cisco i w roku 1993 opisana w dokumencie RFC1631. Od końca lat 80-tych liczba komputerów dołączanych do sieci Internet wzrasta wykładniczo. To spowodowało, że przestrzeń adresów IP już w latach 90-tych się wyczerpywała. Zaobserwowano wówczas, że jeśli tempo zużycia przestrzeni IP się utrzyma, to w niedalekiej przyszłości (przewidywanej na lata 1994-95) zupełnie zabraknie publicznych adresów IP dla nowobudowanych sieci. Technologia NAT i leżące u jej podstaw nowe podejście do projektowania sieci IP, pozwoliły przedłużyć tę „niedaleką przyszłość" co najmniej do dziś. Poniżej opisana została idea technologii NAT. 
Wiele dzisiejszych sieci IP nie opiera się już na publicznych adresach sieci, bo takich już brakuje. Zamiast tego stosowane są dla tych sieci adresy prywatne. Należą do nich: 
• dla klasy A - adresy z zakresu 10.0.0.0 - 10.255.255.255 
• dla klasy B - adresy z zakresu 172.16.0.0 - 172.31.255.255 
• dla klasy C - adresy z zakresu 192.168.0.0 - 192.168.255.255 
Ponieważ powyższe adresy nie są rejestrowane, może istnieć wiele sieci wykorzystujących tę samą pulę adresów prywatnych, a to czyni sieć Internet skalowalną. Ale z drugiej strony fakt, że adresy prywatne nie są unikalne, stwarza pewne ograniczenie. Otóż pakiety z takimi adresami nie mogą być przesyłane w Internecie, gdyż nie można określić dla nich trasy. I właśnie ten problem rozwiązuje technologia NAT. Dzięki niej do uzyskania łączności sieci prywatnej z Internetem wystarcza jeden adres publiczny IP - adres zewnętrznego interfejsu rutera. Od strony Internetu cała sieć prywatna widziana jest pod tym jednym (lub wieloma) adresem. Dalej opisano dwie główne odmiany NAT: translację adresów źródłowych SNAT (ang. _Source NAT_) i adresów docelowych DNAT (ang. _Destination NAT_). 
#### SNAT
Translacja SNAT umożliwia komputerom w sieci prywatnej dostęp do Internetu, a dokładniej - do usług oferowanych przez różne serwery. Oznacza to, że pakiety, których źródłem są komputery sieci prywatnej, powinny docierać do tych serwerów, a odpowiedzi - wracać z powrotem. Proces translacji SNAT przebiega w dwóch krokach: 
  * gdy pakiet opuszcza sieć źródłową, ruter zamienia prywatny adres IP źródła na adres swojego publicznego interfejsu oraz numer portu źródłowego na inny, nie zajęty numer portu. Zapamiętuje tę zmianę w tablicy translacji w postaci odwzorowania oryginalny_adres_IP:oryginalny_port→nowy_adres_IP:nowy_port. Dzięki zamianie adresu źródłowego na publiczny można dla pakietu z odpowiedzią jednoznacznie określić trasę. Nowy numer portu zaś pozwala dodatkowo rozróżniać poszczególne adresy prywatne, dzięki czemu z usług Internetu może jednocześnie korzystać wiele komputerów sieci prywatnej.
  * gdy ruter otrzymuje pakiet-odpowiedź, publiczny adres docelowy (będący adresem źródłowym w poprzednim pakiecie) wraz z numerem portu docelowego są zamieniane z powrotem na oryginalne wartości zgodnie z zapamiętanym wcześniej odwzorowaniem. Dzięki temu odpowiedź dociera do właściwego procesu na właściwym komputerze.


#### DNAT
Translacja DNAT umożliwia komputerom z sieci publicznej dostęp do usług oferowanych przez serwery znajdujące się w sieci prywatnej. Oznacza to, że pakiety, których źródłem są komputery sieci publicznej, powinny docierać do tych serwerów, a odpowiedzi - wracać z powrotem. Usługi sieci prywatnej dostępne są dla sieci zewnętrznej pod publicznym adresem interfejsu rutera. Translacja DNAT przebiega w dwóch krokach: 
  * gdy pakiet dociera do sieci prywatnej, jego adres IP docelowy jest ustawiony na publiczny adres zewnętrznego interfejsu rutera; pod tym adresem bowiem usługa jest dostępna. Ruter zamienia ten adres na właściwy adres serwera; w najprostszym przypadku numer portu docelowego nie ulega zmianie.
  * gdy ruter otrzymuje pakiet-odpowiedź, z powrotem zamienia prywatny adres źródłowy na adres publiczny swojego zewnętrznego interfejsu.


### Moduły rozszerzające IPTABLES
NetFilter jest zbudowany z modułów, które rozszerzają możliwości zapory sieciowej. Kilka z nich jest używane domyślnie, na przykład tcp, udp. Poniżej krótko omówiono większość z dostępnych modułów pakietu NetFilter. Wiele z wymienionych modułów dostępna jest w dodatku _patch-o-matic-ng_ , który nie zawsze jest całkowicie instalowany. 
#### Krótkie opisy modułów
##### Dotyczące IPSec:
  * ah - dopasowują się do pola "spi" w nagłówku AH pakietu,
  * esp - dopasowują się do pola "spi" w nagłówku ESP pakietu,
  * policy - dopasowują się do "policy" pakietu.


##### Dopasowujące się do nagłówka pakietu IP:
  * dscp - dopasowuje się do 6 bitów DSCP znajdujących się w polu ToS,
  * ecn - sprawdza bit ECN w nagłówku pakietu,
  * ipv4options (*) - sprawdza różne opcje nagłówka pakietu, np. source routing, record route,
  * tcpmss - sprawdza pole MSS (Maximum Segment Size),
  * tos - pole ToS (Type of Service),
  * ttl - pole TTL (Time To Live).


##### Nadzorujące połączenia (stanowość):
  * state - umożliwia zidentyfikowanie istniejących połączeń oraz nowych,
  * conntrack - rozszerza możliwości modułu state,
  * helper - pozwala określić "pomocnika" do przekazywania połączenia, np. standardowym pomocnikiem jest moduł pozwalający przekazywać połączenia ftp-data w trybie aktywnym.


##### Określające typ pakietu:
  * icmp - dopasowuje się do pakietów typu ICMP,
  * tcp - dotyczy pakietów typu TCP,
  * udp - dotyczy pakietów typu UDP,
  * unclean(*) - dotyczy pakietów zniszczonych i niepoprawnych.


##### Określające limity:
  * connlimit(*) - umożliwia określenie maksymalnej liczby połączeń do konkretnego adresu IP z jednego adresu IP klienta,
  * connrate(*) - umożliwia określenie maksymalnego/minimalnego transferu,
  * hashlimit - umożliwia określenie maksymalnego transferu do danej usługi/serwera.


##### Znakowanie pakietów:
  * mark - umożliwia znalezienie oznakowanego pakietu,
  * connmark - umożliwia znalezienie każdego pakietu związanego z oznakowanym połączeniem.


##### Ułatwiające tworzenie reguł:
  * iprange - umożliwia wpisanie zakresu adresów IP,
  * mac - umożliwia sprawdzenie adresu sprzętowego karty sieciowej MAC,
  * multiport - umożliwia wpisanie zakresu portów,
  * owner - dla lokalnych połączeń umożliwia określenie który użytkownik wysłał dany pakiet,
  * pkttype - określa typ pakietu (unicast, multicast, broadcast)
  * set(*) - wykorzystanie stworzonych zbiorów adresów (polecenie ipset),
  * time(*) - określenie daty i/lub czasu,
  * comment - umożliwia dopisanie komentarza do każdej reguły.


##### Rozszerzone sprawdzanie pakietów:
  * length - sprawdzające wielkość pakietu,
  * string(*) - dopasowujące się do zawartości pakietu w polu DATA,
  * ipp2p(*) - dopasowujące się do ruchu generowanego przez aplikacje typu P2P.


##### Określające częstość:
  * limit - określa jak często reguła będzie dopasowana, np. 3 razy na sekundę - 3/s,
  * nth(*) - określa co jaką liczbę pakietów będzie dopasowana reguła, np. co 5 pakiet,
  * random(*) - określa dopasowanie reguły do pakietu z zadanym prawdopodobieństwem, np. 50% pakietów.


##### Monitorujące:
  * recent - tworzy listy adresów wykorzystających łącze (przechodzących przez tą regułę), wyniki zapisywane są w katalogu /proc/net/ipt_recent/NAZWA,
  * account(*) - zlicza ruch do określonych adresów, wyniki w katalogu /proc/net/ipt_account/NAZWA,
  * quota(*) - określa quota'ę dla określonych pakietów.


##### Inne:
  * condition(*) - pozwala warunkować stosowanie reguły, poprzez plik w katalogu /proc/net/ipt_condition/NAZWA
  * osf(*) - odczytuje pasywnie "odcisk palca" (fingerprint) konkretnego adresu IP i zapisuje w pliku /proc/sys/net/ipv4/osf
  * psd(*) - pozwala wykryć skanowanie portów TCP i UDP.


(*) moduły te nie znajdują się w domyślnej instalacji systemu SuSE Linux 10.0 i nie są dostępne w laboratorium ćwiczeniowym. 
#### Krótkie opisy celów (TARGETs)
Cele określają co zostanie zrobione z danym pakietem, domyślnymi celami są akceptacja (ACCEPT) i odrzucenie (DROP) pakietu. Jednak tworcy zapory postanowili rozszerzyć listę dopuszczalnych celów, które również mogą być tworzone przez nas samych dla naszych potrzeb. 
Lista celów została podzielona na kategorie: 
##### Zmiana adresów IP:
  * BALANCE(*) - podobne do DNAT, ale równomiernie rozkłada obciążenie na wiele adresów IP,
  * DNAT - Destination NAT,
  * MASQUERADE - ukrywanie źródłowych adresów IP,
  * NETMAP - statyczna zamiana adresów całych podsieci,
  * REDIRECT - przekierowanie ruchu na lokalny komputer,
  * SAME - podobne do DNAT/SNAT, ale zawsze przydziela te same adresy IP konkretnym klientom,
  * SNAT - Source NAT.


##### Znakowanie pakietów:
  * CONNMARK - znakuje połączenia,
  * IPMARK(*) - znakowanie pakietów na podstawie adresu IP,
  * MARK - znakuje pakiety.


##### Zmieniające nagłówek pakietu:
  * DSCP - umożliwia zmianę 6 bitów DSCP pola ToS,
  * ECN - umożliwia usunięcie bitu ECN,
  * IPV4OPTSSTRIP(*) - usunięcie wszystkich opcji IP z nagłówka pakietu,
  * TCPMSS - ustawienie pola MSS,
  * TOS - ustawienie pola ToS,
  * TTL - ustawienie pola TTL.


##### Śledzenie pakietów:
  * NOTRACK - wyłącza śledzenie połączenia,
  * TARPIT(*) - przechwytuje połączenia i zawiesza je, w celu zabezpieczenie się przez skanowaniem typu Code Red i Nimda,
  * TRACE(*) - włącza śledzenie połączenia.


##### Logowanie:
  * LOG - logowanie pakietów,
  * ULOG - logowanie w przestrzeni użytkownika,


##### Inne:
  * REJECT - odrzuca pakiety wysyłając określony kod błędu do nadawcy,
  * ROUTE(*) - pozwala nadpisać wpisy tablicy tras,
  * SET(*) - dodaje/usuwa adresy z zakresów (polecenie ipset),
  * XOR(*) - pozwala zastosować proste zabezpieczenie danych pakietu, poprzez wykonanie funkcji XOR na danych i określonym haśle.


#### Szczegółowe informacje
Wszystkie dodatkowe informacje odnoście każdego z wyżej wymienionych modułów i celów można uzyskać z plików pomocy. 
Uzyskanie pomocy o module: 
```
 iptables -m <moduł> -h

```

Uzyskanie pomocy o celu: 
```
 iptables -j <cel> -h

```

## Przykłady
Ustawienie domyślnej polityki łańcucha INPUT na DROP: 
```
 iptables -P INPUT DROP

```

Akceptacja pakietów o adresie źródłowym 150.254.20.20: 
```
 iptables -A INPUT -s 150.254.20.20 -j ACCEPT

```

Translacja adresów źródłowych dla podsieci 192.168.1.0/24 na adres 150.254.20.20 
```
 iptables -t nat -I PREROUTING -s 192.168.1.0/24 -j SNAT \ 

```

–-to 150.254.20.20 
```
 wpisy równoważne
 iptables -t nat -I PREROUTING -s 192.168.1.0/24 -j SAME \

```

–-to 150.254.20.20 Translacja adresów docelowych z 150.254.20.21 na 192.168.1.2: 
```
 iptables -t nat -A POSTROUTING -d 150.254.20.21 -j DNAT \ 

```

–-to 192.168.1.2 
```
 wpisy równoważne
 iptables -t nat -A POSTROUTING -d 150.254.20.21 -j SAME \

```

–-to 191.168.1.2 Translacja adresów źródłowych na zakres adresów: 
```
 iptables -t nat -A PREROUTING -s 192.168.1.0/24 -j SNAT \

```

--to 150.254.20.20 – 150.254.20.30 
```
 wpisy równoważne
 iptables -t nat -A PREROUTING -s 192.168.1.0/24 -j SAME \

```

--to 150.254.20.20 – 150.254.20.30 Translacja adresów i portów docelowych, jedynie dla wybranego portów: 
```
 iptables -t nat -A POSTROUTING -p tcp -d 150.254.20.21 \

```

-–dport 80 -j DNAT –to 192.168.1.3:8080 
```
 wpisy równoważne
 iptables -t nat -A POSTROUTING -p tcp -d 150.254.20.21 \

```

-–dport 80 -j SAME –to 192.168.1.3:8080 Akceptacja pakietów ustanowionych i związanych z innymi połączeniami: 
```
 iptables -A INPUT -m state –-state ESTABLISHED,RELATED \

```

-j ACCEPT Blokada więcej niż 2 połączeń na port 23 
```
 iptables -A INPUT -p tcp –-syn –-dport 23 -m connlimit \

```

--connlimit-above 2 -j REJECT \ --reject-with icmp-host-unreachable Umożliwienie tylko jednego na minutę połączenia z portem 22 
```
 iptables -A INPUT -p tcp --dport 22 -m hashlimit \

```

--hashlimit 1/min --hashlimit-mode srcip \ --hashlimit-name ssh -m state --state NEW -j ACCEPT Blokada pakietów większych niż 1000 bajtów 
```
 iptables -A INPUT -m length --length 1000: -j DROP

```

Akceptacja 3 połączeń na minutę 
```
 iptables -A INPUT -m limit --limit 3/min -j ACCEPT

```

Stworzenie statystyk połączeń z portem 80 
```
 iptables -A INPUT -p tcp --dport 80 -m recent --name www \

```

--set -j ACCEPT Utworzenie zbiorów adresów prywatnych i ich blokowanie 
```
 ipset --create priv nethash
 ipset --add priv 10.0.0.0/8
 ipset --add priv 172.16.0.0/12
 ipset --add priv 192.168.0.0/16
 ipset --add priv 169.254.0.0/16
 iptables -A INPUT -m set --set priv src -j DROP

```

## Zadania
Wykorzystać zaprezentowane powyżej informacje do zbudowania różnego typu reguł oraz przetestowanie ich poprawnego działania: 
  * Ograniczyć maksymalną wielkość pakietu ICMP-echo do 1kB.
  * Ograniczyć do 3 na minutę liczbę pakietów ICMP-echo.
  * Utworzyć statystyki odbierania pakietów.
  * Ograniczyć żądania http do 2kB wielkości i do 3 na minutę.
  * Logować pakiety, które naruszają regułę numer 4, ale ich nie usuwać.
  * Zmienić wartość pola TTL dla każdego pakietu na 56 i sprawdzić wykorzystując sniffer.
  * Usuwać pakiety większe niż 3 kB zwracając komunikat błędy ICMP-net-unreachable.
  * Zmienić wartość pola MSS - sprawdzić wykorzystując sniffer.
  * Wykorzystać moduł comment w celu opisania reguł zapory sieciowej.
  * Wykorzystać moduł pkttype w celu zablokowania pakietów ICMP-echo wysyłanych na adres rozgłoszeniowy. Wcześniej należy zdjąć blokadę jądra systemu:

```
 echo ”0” > /proc/sys/net/ipv4/icmp_echo_ignore_broadcast

```

## Problemy do dyskusji
  * Architektura IPTABLES, wady i zalety.
  * Modułowość IPTABLES zaleta czy wada?
  * Mnogość łańcuchów i tablic w iptables, czy ma to swoje uzasadnienie?
  * Jaki jest związek między "szczelnością" a elastyczności reguł filtracji?
  * Technologia NAT, dobre, złe rozwiązanie?
  * Inne metody rozwiązania wyczerpujących się się adresów Ipv4?
  * SNAT, DNAT dlaczego każdy z nich może być wykonywany tylko w określonych łańcuchach?
  * Czy wszystkie z opisanych modułów rozszerzających są warte używania, proszę o podanie przykładów oraz dyskusji dlaczego?


---


# Systemy wykrywania włamań IDS (snort)

# Bezpieczeństwo systemów komputerowych - laboratorium 13:Systemy wykrywania włamań IDS (snort)
Z Studia Informatyczne
[Przejdź do nawigacji](https://wazniak.mimuw.edu.pl/<#column-one>)[Przejdź do wyszukiwania](https://wazniak.mimuw.edu.pl/<#searchInput>)
Systemy wykrywania włamań 
## Spis treści
  * [1 Wprowadzenie](https://wazniak.mimuw.edu.pl/<#Wprowadzenie>)
  * [2 Zastosowanie systemów wykrywania włamań](https://wazniak.mimuw.edu.pl/<#Zastosowanie_systemów_wykrywania_włamań>)
  * [3 System Snort](https://wazniak.mimuw.edu.pl/<#System_Snort>)
    * [3.1 Podstawy](https://wazniak.mimuw.edu.pl/<#Podstawy>)
    * [3.2 Koncepcja preprocesorów](https://wazniak.mimuw.edu.pl/<#Koncepcja_preprocesorów>)
    * [3.3 Moduły wyjściowe](https://wazniak.mimuw.edu.pl/<#Moduły_wyjściowe>)
    * [3.4 Reguły Snorta](https://wazniak.mimuw.edu.pl/<#Reguły_Snorta>)
    * [3.5 Opcje w regułach programu Snort](https://wazniak.mimuw.edu.pl/<#Opcje_w_regułach_programu_Snort>)
  * [4 Podsumowanie](https://wazniak.mimuw.edu.pl/<#Podsumowanie>)
  * [5 Zadania](https://wazniak.mimuw.edu.pl/<#Zadania>)
  * [6 Problemy do dyskusji](https://wazniak.mimuw.edu.pl/<#Problemy_do_dyskusji>)
  * [7 Bibliografia](https://wazniak.mimuw.edu.pl/<#Bibliografia>)


## Wprowadzenie
Systemy wykrywania intruzów(_ang. Intrusion detection systems_) należą do jednych z najmłodszych rozwiązań w arsenale obronnym administratorów systemów. Systemy te maja na celu wspomagać administratorów w wykrywaniu prób naruszeń polityki bezpieczeństwa. Docelowym dążeniem twórców takich rozwiązań jest pełna automatyzacja w procesie wykrywaniu różnego rodzaju nadużyć systemów informatycznych. Naturalnym dążeniem oprócz pełnej automatyzacji wykrywania intruzów jest chęć doposażenia takich systemów w możliwości udaremniania ataków. Systemy IDS dzięki temu przeobrażają się w systemy zapobiegania włamaniom(_ang. Intrusion Prevention Systems_). Takie systemy z natury rzeczy są jeszcze bardziej skomplikowane niż systemy IDS, posiadają możliwość blokowania akcji wykonywanych przez inne programy, np. dynamiczna modyfikacja firewalla i zablokowanie ruchu sieciowego. Dlatego też wymagania stawiane takim programom są bardzo wysokie. 
Słowa kluczowe: IDS, IPS, Snort, wykrywanie włamań. 
## Zastosowanie systemów wykrywania włamań
Główną przyczyną stosowania rozwiązań IDS/IPS w środowiskach sieciowych jest wzrastająca liczba różnego rodzaju ataków przeprowadzanych automatycznie np. za pomocą robaków internetowych czy wirusów jak i tych groźniejszych w których intruz aktywnie pracuje nad uzyskaniem nieuprawnionego dostępu do chronionego systemu. Ochrona systemów komputerowych jest kosztowna i czasochłonna. Systemy IDS/IPS w założeniach mają pomóc obniżyć koszty takiej ochrony oraz podnieść jej efektywność poprzez automatyzację analizy zdarzeń, które mogą świadczyć o potencjalnym naruszeniu polityki bezpieczeństwa danej organizacji. 
## System Snort
Przykładem systemu IDS jest program Snort. Obecnie Snort jest uważany za najlepsze tego typu rozwiązanie Open Source. Mimo, że Snort jest darmowy okazał się na tyle dobry, że wiele firm szkoleniowych oferuje płatne profesjonalne kursy uczące zarządzania aplikacją Snort. Również firmy zajmujące się komercyjnie tworzeniem systemów IDS doceniły Snorta i oferują wsparcie dla reguł Snorta w swoich produktach. 
### Podstawy
Uruchomienie programu Snort w trybie wykrywania intruzów z plikiem konfiguracyjnym snort.conf. Snort będzie działał jako demon: 
```
snort -c snort.conf -D

```

Możliwe jest również uruchomienie programu Snort w trybie sniffera: 
```
snort -v -e -i eth0

```

Inny tryb pozwala logować pakiety: 
```
snort -l /ścieżka/do/katalogu

```

W przypadku logowania pakietów możliwe jest również logowanie do formatu akceptowanego przez program tcpdump, co jest bardzo dużą zaletą tego programu Snort. Logowanie binarne o którym mowa jest o wiele szybsze i pozwala zastosować Snorta w sieciach o szybkości 100Mbit/s: 
```
snort -l /scieżka/do/katalogu -b

```

Snort posiada jeden plik konfiguracyjny. W domyślnej konfiguracji wystarczy zmienić kilka opcji aby uruchomić program. Plik konfiguracyjny posiada komentarze pomocne przy konfiguracji. Najważniejsze opcje to: 
  * HOME_NET – definiuje lokalną przestrzeń adresową, ustawić można ja na wartość $eth0_ADDRESS lub jawnie podać adres podsieci wraz z maską postaci /xx
  * EXTERNAL_NET – definiuje przestrzeń adresową nie należącą do sieci HOME_NET, można ustawić na any lub podać adres lub adresy sieci.


### Koncepcja preprocesorów
Aby umożliwić użytkownikom łatwe dodawanie nowych funkcjonalności do programu Snort, powstała koncepcja modułów nazywanych preprocesorami. Każdy preprocesor zawiera nową funkcjonalność wraz z możliwościami konfiguracji. Przykładowy preprocesor portscan loguje początek i koniec skanowania portów. Skanowanie portów w tym przypadku jest definiowane jako próby połączeń do więcej niż p portów w przeciągu t sekund. Preprocesor portscan zawiera kilka parametrów: 
  * adres sieci dla której ma być monitorowane skanowanie portów
  * ilość przeskanowanych portów w założonym czasie
  * okres w sekundach w którym następuje skanowanie portów
  * ścieżka do pliku w którym będą zapisywane informacje o próbach skanowania


Załączenie w snort.conf preprocesora portscan: 
```
preprocessor portscan: 20.1.2.0/24 5 7 /var/llog/snort/portscan.log

```

Preprocesor portscan-ignorehosts pozwala ignorować niektóre hosty lub całe sieci przed wykrywaniem ich przez preprocesor portscan. Dzięki temu możliwe jest ograniczenie podatności preprocesora portscan na fałszywe komunikaty o próbach skanowania portów. Załączenie preprocesor portscan-ignorehosts: 
```
preprocesor portscan-ignorehosts: 192.168.1.432

```

### Moduły wyjściowe
Dzięki modułom wyjściowym użytkownik ma możliwość określić, gdzie mają trafiać informacje od systemu Snort. Ogólna postać polecenia ładującego moduł wyjściowy wygląda następująco: 
```
output <name>: <options> np: output alert_syslog: log_auth log_alert

```

Moduł alert_fast pozwala logować skróconą postać komunikatu bez nagłówka pakietu, który spowodował uaktywnienie reguły tworzącej zapis w logach. Inne dostępne moduły to alert_full, alert_unixsock, log_tcpdump. Możliwe jest również logowanie do bazy danych jak również wyłączenie logowania za pomocą modułu log_null. 
### Reguły Snorta
To, co stanowi o sile systemu Snort to tryb wykrywania włamań i systemem tworzenia reguł, dzięki którym Snort potrafi wykrywać różnego rodzaju ataki. Język tworzenia reguł Snorta jest dość skomplikowany . Zostaną tutaj zaprezentowane tylko podstawowe elementy niezbędne do wykonania ćwiczeń. Przykład kompletnej reguły: 
```
alert tcp any any -> 192.168.1.0/24 111 (content: 00 01 86 a5 ; msg: mount access ;)

```

Reguła Snorta jest podzielona na dwie logiczne części: część nagłówka i cześć z opcjami. Część nagłówkowa zawiera akcję jaką należy wykonać, rodzaj protokołu, adres ip źródła , port źródłowy oraz adres ip docelowy oraz numer docelowego portu. Możliwe jest równie użycie wieloznacznego słowa any, które symbolizuje dowolny adres ip, dowolny port. Część w nawiasach okrągłych zawiera zestaw opcji użytych dla tej reguły, Każda opcja zakończona jest średnikiem. Po odebraniu pakietu porównuje nagłówki reguł oraz opcje zawarte w regułach z pakietem. Jeśli nastąpi porównanie wykonywana jest zapisana w regule akcja. Możliwe do wykonania akcje to: 
  * alert, generuje alarm i loguje pakiet
  * log, tylko loguje pasujący pakiet
  * pass, przepuszcza pakiet
  * activate, wywołuje alarm i uruchamia dynamiczną regułę
  * dynamic, reguła pozostająca w bezczynności aż do momentu aktywacji przez regułę typu activate


### Opcje w regułach programu Snort
Dzięki rozbudowanym i licznym opcjom jest możliwe wykonywanie wielu testów na pakietach. Każda opcja składa się z słowa kluczowego, po nim dwukropka i argumentu dla danej opcji. Przykładowe opcje: 
```
Opcja: msg: <tekst>;

```

Opcja pozwala dodawać tekst do reguł, dzięki temu informacje zapisane w plikach logu są bardziej czytelne. 
```
Opcja flag:[!|*|+]<FSRPAU0>[,<FSRPAU0>];

```

Opcja pozwala analizować nagłówek pakietu pod kątem ustawionych w nim flag: 
```
F – FIN
S - SYN
R – RST
P – PSH
A – ACK
U – URG
0 – brak ustawionych flag
+ - dopasuj do danej flagi i opcjonalnie do reszty
* - dopasuj do którejkolwiek z podanych flag 
! - dopasuj jeśli podanej flagi nie są ustawione w pakiecie

```
```
Np. alert tcp any any -> any any (flags:SF;)

```

## Podsumowanie
Program Snort jest zaawansowanym narzędziem IDS/IPS. Istnieje szereg dodatkowych funkcjonalności dla programu Snort ,co sprawia, że jest to rozbudowane narzędzie którym nie łatwo zarządzać. Nauka posługiwania Snortem może zająć trochę czasu ale warto poświęcić czas na naukę obsługi tego rozwiązania ponieważ może ono pomóc lepiej chronić środowisko sieciowe. 
## Zadania
  * Uruchom program Snort w trybie sniffera.
  * Uruchom program Snort w trybie logowania pakietów i sprawdź w jaki sposób Snort zapisuje pakiety.
  * Uruchom program Snort w trybie wykrywania włamań z preprocesorem skanowania portów. Użyj narzędzia nmap do zasymulowania skanowania portów. Sprawdź czy program Snort wykryje działanie programu nmap. Sprawdź zawartość pliku logów.


## Problemy do dyskusji
  * Zapoznaj się z rozwiązaniem Snort_inline
  * Jakie niebezpieczeństwa niesie za sobą używanie programów typu IPS?

---

