# Testbestand CAMT
Om goede GAT en FAT testen te kunnen doen in PAL21 is het van belang om een bankbestand te kunnen genereren. Je wilt in het OTA deel geen productiegegevens hebben. Daarom is ervoor gekozen om een generator te maken die fictieve gegevens genereerd.

## Installatie
- Een installatie van Python en GIT is noodzakelijk alvorens de volgende stappen te zetten.
- Open een terminal (of gebruik die van Visual Studio Code), navigeer naar de gewenste installatielocatie en gebruik `git clone https://github.com/FreddyMeijer/CAMT-generator.git`
- Open in de terminal de map waarin de repository gekloond is.
- Geef het commando `pip install -r CAMT-generator/requirements.txt`
- Draai `create_camt.py`

## .gitignore
De gegenereerde bestanden hebben de extentie xml. Alle xml bestanden worden genegeerd en zullen niet opgenomen worden in de repository.

## De code
De generatie van het CAMT bestand gaat via `create_camt.py`. In dit bestand zit een functie die een IBAN genereerd (puur fictief). `iban.py` moet in dezelfde map staan als `create_camt.py`.

### iban.py
Het Nederlandse IBAN heeft het volgende formaat `[a-z]{2}[0-9]{2}[a-z]{4}[0-9]{10}`. Deze functie schrijft een IBAN die voldoet aan de gestelde lengte zoals hierboven. Het rekeningnummer dat teruggegeven wordt, zal zichtbaar worden in de XML:

```xml
<DbtrAcct>
    <Id>
        <IBAN>NL69XSAD1014574364</IBAN>
    </Id>
</DbtrAcct>
```

`iban.py` moet in dezelfde map staan als `create_camt.py`

### create_camt.py
Bij het uitvoeren van deze code wordt de gebruiker gevraagd om aan te geven hoeveel regels er in het CAMT bestand opgenomen moeten worden:

```bash
sh-5.2$ /bin/python "/home/freddy/Documenten/Generatie test CAMT bestanden/create_camt.py"
Hoeveel regels wil je in het CAMT bestand hebben? 2
sh-5.2$ 
```

In bovenstaand voorbeeld zullen er dus 2 betalingen in het bestand zitten. Op het moment dat de code uitgevoerd is, zal in de map waarin `create_camt.py` is opgenomen een XML bestand verschijnen. Dit is het testbestand.

## Automatisch matchen
Omdat in dit bestand fictieve betaalkenmerken gemaakt worden (zie regel 30 van `create_camt.py`) zal er bij inlezen dus nooit sprake zijn van automatisch matchen. Indien je vooraf automatische match wil forceren, zal je handmatig de XML moeten aanpassen.

#### Voorbeeld
In onderstaand voorbeeld zie je dat er blijkbaar 0,46 (in tag `AmtCcy`) wordt overgemaakt op betaalreferentie 1906350066203673 (in tags `EndToEndId` en `Ref`). Als je deze waarden aanpast met het juiste bedrag en het juiste betaalkenmerk, zou PAL21 dit automatisch moeten kunnen matchen.

```xml
<Ntry>
    <NtryRef>70814051733313</NtryRef>
    <AmtCcy="EUR">0.46</Amt>
    <CdtDbtInd>CRDT</CdtDbtInd>
    <Sts>BOOK</Sts>
    <BookgDt>
        <Dt>2024-05-17</Dt>
    </BookgDt>
    <ValDt>
        <Dt>2024-05-17</Dt>
    </ValDt>
    <AcctSvcrRef>70814051733313</AcctSvcrRef>
    <BkTxCd>
        <Domn>
            <Cd>PMNT</Cd>
            <Fmly>
                <Cd>RRCT</Cd>
                <SubFmlyCd>ESCT</SubFmlyCd>
            </Fmly>
        </Domn>
        <Prtry>
        <Cd>00112</Cd>
        <Issr>Rabobank</Issr>
        </Prtry>
    </BkTxCd>
    <NtryDtls>
        <TxDtls>
            <Refs>
                <EndToEndId>1906350066203673</EndToEndId>
            </Refs>
            <RltdPties>
                <Dbtr>
                    <Nm>Rekeninghouder1</Nm>
                </Dbtr>
                <DbtrAcct>
                    <Id>
                        <IBAN>NL69XSAD1014574364</IBAN>
                    </Id>
                </DbtrAcct>
            </RltdPties>
            <RltdAgts>
                <DbtrAgt>
                    <FinInstnId>
                        <BIC>RABONL2U</BIC>
                    </FinInstnId>
                </DbtrAgt>
            </RltdAgts>
            <RmtInf>
                <Strd>
                    <CdtrRefInf>
                        <Tp>
                            <CdOrPrtry>
                               <Cd>SCOR</Cd>
                            </CdOrPrtry>
                            <Issr>CUR</Issr>
                        </Tp>
                        <Ref>1906350066203673</Ref>
                    </CdtrRefInf>
                </Strd>
            </RmtInf>
        </TxDtls>
    </NtryDtls>
</Ntry>
```