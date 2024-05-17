from datetime import datetime
import random
from iban import IBAN

today = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z+02:00")
rndID = str(random.randint(10000000, 99999999))
rndSeqNb = str(random.randint(100, 999))
fromDate = datetime.now().strftime("%Y-%m-%dT00:00:00")
toDate = datetime.now().strftime("%Y-%m-%dT23:59:59")
date = datetime.now().strftime("%Y%m%d")
dateNtry = datetime.now().strftime("%Y-%m-%d")
id = date + "000" + rndSeqNb
filename = str(date)+"_"+rndSeqNb+"_testbestand_CAMT.xml"

XMLheader = "<?xml version='1.0' encoding='UTF-8'?><Document xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"urn:iso:std:iso:20022:tech:xsd:camt.053.001.02\"><BkToCstmrStmt>"
GprHdr = "<GrpHdr><MsgId>" + today + "</MsgId><CreDtTm>" + today + "</CreDtTm><MsgRcpt><Nm>Testbedrijf gemeente Leiden</Nm><Id><OrgId><Othr><Id>" + rndID + "</Id></Othr></OrgId></Id></MsgRcpt></GrpHdr>"
Stmt = "<Stmt><Id>" + id + "</Id><ElctrncSeqNb>" + rndSeqNb + "</ElctrncSeqNb><CreDtTm>" + today + "</CreDtTm><FrToDt><FrDtTm>" + fromDate + "</FrDtTm><ToDtTm>" + toDate + "</ToDtTm></FrToDt>"
Acct = "<Acct><Id><IBAN>NL18RABO0123459876</IBAN></Id><Tp><Cd>CACC</Cd></Tp><Ccy>EUR</Ccy><Ownr><Nm>Testbedrijf gemeente Leiden</Nm></Ownr><Svcr><FinInstnId><BIC>RABONL2U</BIC></FinInstnId></Svcr></Acct>"
Bal = "<Bal><Tp><CdOrPrtry><Cd>PRCD</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt>"+ dateNtry +"</Dt></Bal><Bal><Tp><CdOrPrtry><Cd>OPBD</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt><Dt>"+ dateNtry +"</Dt></Dt></Bal><Bal><Tp><CdOrPrtry><Cd>CLBD</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt><Dt>"+ dateNtry +"</Dt></Dt></Bal><Bal><Tp><CdOrPrtry><Cd>CLAV</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt><Dt>"+ dateNtry +"</Dt></Dt></Bal><Bal><Tp><CdOrPrtry><Cd>FWAV</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt><Dt>"+ dateNtry +"</Dt></Dt></Bal><Bal><Tp><CdOrPrtry><Cd>FWAV</Cd></CdOrPrtry></Tp><Amt Ccy=\"EUR\">0.00</Amt><CdtDbtInd>CRDT</CdtDbtInd><Dt><Dt>"+ dateNtry +"</Dt></Dt></Bal>"

entryAmount = int(input("Hoeveel regels wil je in het CAMT bestand hebben? "))

Ntry = []
totaalAmt = 0

for i in range(entryAmount):
    rekeninghouder = "Rekeninghouder " + str(i + 1)
    bankrekening = IBAN()
    ref = str(random.randint(1000000000000000,9999999999999999))
    NtryRef = str(random.randint(10000000000000,99999999999999))
    multiplier = random.choice([10,100,1000,1000000])
    Amt = round((random.random() * multiplier),2) 
    totaalAmt = totaalAmt + Amt
    NtryRule = "<Ntry><NtryRef>" + NtryRef + "</NtryRef><Amt Ccy=\"EUR\">" + str(Amt) + "</Amt><CdtDbtInd>CRDT</CdtDbtInd><Sts>BOOK</Sts><BookgDt><Dt>"+ dateNtry +"</Dt></BookgDt><ValDt><Dt>"+ dateNtry +"</Dt></ValDt><AcctSvcrRef>" + NtryRef + "</AcctSvcrRef><BkTxCd><Domn><Cd>PMNT</Cd><Fmly><Cd>RRCT</Cd><SubFmlyCd>ESCT</SubFmlyCd></Fmly></Domn><Prtry><Cd>00112</Cd><Issr>Rabobank</Issr></Prtry></BkTxCd><NtryDtls><TxDtls><Refs><EndToEndId>" + ref + "</EndToEndId></Refs><RltdPties><Dbtr><Nm>" + rekeninghouder + "</Nm></Dbtr><DbtrAcct><Id><IBAN>" + bankrekening + "</IBAN></Id></DbtrAcct></RltdPties><RltdAgts><DbtrAgt><FinInstnId><BIC>RABONL2U</BIC></FinInstnId></DbtrAgt></RltdAgts><RmtInf><Strd><CdtrRefInf><Tp><CdOrPrtry><Cd>SCOR</Cd></CdOrPrtry> <Issr>CUR</Issr></Tp><Ref>" + ref + "</Ref></CdtrRefInf></Strd></RmtInf></TxDtls></NtryDtls></Ntry>"
    Ntry.append(NtryRule)

totaalAmt = round(totaalAmt,2)
txsSummry = "<TxsSummry><TtlNtries><NbOfNtries>"+ str(entryAmount) +"</NbOfNtries><Sum>"+ str(totaalAmt) +"</Sum></TtlNtries><TtlCdtNtries><NbOfNtries>" + str(entryAmount) + "</NbOfNtries><Sum>"+ str(totaalAmt) +"</Sum></TtlCdtNtries><TtlDbtNtries><NbOfNtries>0</NbOfNtries><Sum>0.00</Sum></TtlDbtNtries></TxsSummry>"

with open(filename,'w', encoding='UTF-8') as f:
    f.write(XMLheader + GprHdr + Stmt + Acct + Bal + txsSummry + "".join(Ntry) + "</Stmt></BkToCstmrStmt></Document>")
