import re

LONGEST_KEY = 1

hirastart = {
  "A": "あ",
  "O": "お",
  "E": "え",
  "U": "う",
  "EU": "い",
  "SA": "さ",
  "SO": "そ",
  "SE": "せ",
  "SU": "す",
  "SEU": "し",
  "TA": "た",
  "TO": "と",
  "TE": "て",
  "TU": "つ",
  "TEU": "ち",
  "PA": "か",
  "PO": "こ",
  "PE": "け",
  "PU": "く",
  "PEU": "き",
  "HA": "は",
  "HO": "ほ",
  "HE": "へ",
  "HU": "ふ",
  "HEU": "ひ",
  "KA": "な",
  "KO": "の",
  "KE": "ね",
  "KU": "ぬ",
  "KEU": "に",
  "WA": "ら",
  "WO": "ろ",
  "WE": "れ",
  "WU": "る",
  "WEU": "り",
  "RA": "ぱ",
  "RO": "ぽ",
  "RE": "ぺ",
  "RU": "ぷ",
  "REU": "ぴ",
  "TKA": "ま",
  "TKO": "も",
  "TKE": "め",
  "TKU": "む",
  "TKEU": "み",
  "PWA": "わ",
  "PWO": "を",
  "PWE": "ゑ",
  "PWEU": "ゐ",
  "HRA": "や",
  "HRO": "よ",
  "HRU": "ゆ",
}
katastart = {
  "A": "ア",
  "O": "オ",
  "E": "エ",
  "U": "ウ",
  "EU": "イ",
  "SA": "サ",
  "SO": "ソ",
  "SE": "セ",
  "SU": "ス",
  "SEU": "シ",
  "TA": "タ",
  "TO": "ト",
  "TE": "テ",
  "TU": "ツ",
  "TEU": "チ",
  "PA": "カ",
  "PO": "コ",
  "PE": "ケ",
  "PU": "ケ",
  "PEU": "キ",
  "HA": "ハ",
  "HO": "ホ",
  "HE": "ヘ",
  "HU": "フ",
  "HEU": "ヒ",
  "KA": "ナ",
  "KO": "ノ",
  "KE": "ネ",
  "KU": "ヌ",
  "KEU": "ニ",
  "WA": "ラ",
  "WO": "ロ",
  "WE": "レ",
  "WU": "ル",
  "WEU": "リ",
  "RA": "パ",
  "RO": "ポ",
  "RE": "ペ",
  "RU": "プ",
  "REU": "ピ",
  "TKA": "マ",
  "TKO": "モ",
  "TKE": "メ",
  "TKU": "ム",
  "TKEU": "ミ",
  "PWA": "ワ",
  "PWO": "ヲ",
  "PWE": "ヱ",
  "PW*U": "ヴ",
  "PWA*": "ヴァ",
  "PWO*": "ヴォ",
  "PW*E": "ヴェ",
  "PW*EU": "ヴィ",
  "PWEU": "ヰ",
  "HRA": "ヤ",
  "HRO": "ヨ",
  "HRU": "ユ"
}
smallhira = {
  'P':"ん",
  'R':"ぁ",
  'G':"ぉ",
  'B':"ぇ",
  'S':"ぅ",
  'BS':"ぃ",
  'T':"ー",
  'D':"、",
  'Z':"。",
  'L':"っ"
}
smallkata = {
  'P':"ン",
  'R':"ァ",
  'G':"ォ",
  'B':"ェ",
  'S':"ゥ",
  'BS':"ィ",
  'T':"ー",
  'D':"、",
  'Z':"。",
  'L':"ッ",
  'TS':"゠"
}
superforeign = {
  "EUBS":"イィ",
  "EUG":"イェ",
  "UR":"ウァ",
  "UBS":"ウィ",
  "US":"ウュ",
  "UB":"ウェ",
  "UG":"ウォ",
  "UZ":"ウゥ",
  "*U": "ヴ",
  "PW*U":"ヴ",
  "PW*UR":"ヴャ",
  "PW*UB":"ヴョ",
  "PW*UG":"ヴィェ",
  "PW*US":"ヴュ",
  "PEUGS":"キェ",
  "P*EUGS":"ギェ",
  "PUR":"クァ",
  "PUB":"クォ",
  "PUG":"クェ",
  "PUGS":"クィ",
  "P*UR":"グァ",
  "P*UB":"グォ",
  "P*UG":"グェ",
  "P*UGS":"グィ",
  "SEUG":"シェ",
  "S*EUG":"ジェ",
  "SUGS":"スィ",
  "S*UGS":"ズィ",
  "TEUG":"チェ",
  "TUR":"ツァ",
  "TUB":"ツォ",
  "TUG":"ツェ",
  "TUS":"ツュ",
  "TUGS":"ツィ",
  "TEGS":"ティ",
  "TOS":"トゥ",
  "TES":"テュ",
  "T*EGS":"ディ",
  "TO*S":"ドゥ",
  "T*ES":"デュ",
  "KEUG":"ニェ",
  "HEUG":"ヒェ",
  "H*EUG":"ビェ",
  "REUG":"ピェ",
  "HUR":"ファ",
  "HUB":"フォ",
  "HUG":"フェ",
  "HUGS":"フィ",
  "HURZ":"フャ",
  "HUBZ":"フョ",
  "HUGZ":"フィェ",
  "HUSZ":"フュ",
  "HOU":"ホゥ",
  "TKEUG":"ミェ",
  "WEUG":"リェ",
  "WA*":"ラ゚",
  "WO*":"ロ゚",
  "W*E":"レ゚",
  "W*U":"ル゚",
  "W*EU":"リ゚",
  "W*EUR":"リ゚ャ",
  "W*EUB":"リ゚ョ",
  "W*EUG":"リ゚ェ",
  "W*EUS":"リ゚ュ"
}
dakutenable = re.compile(r"^[STPH]([AO]\*|\*[EU]+)")
specials = {
  "TPHEULG":"{PLOVER:END_SOLO_DICT}",
  "R-R":"{#Return}{^}",
  "H-F":"？",
  "STKPWHR-FPLT":"!",
  "KW-GS":"「",
  "KR-GS":"」",
  "KW*GS":"『",
  "KR*GS":"』",
  "SR-":"　",
  "KPR-":"〜",
  "TKPW-":"・"
  }

def lookup(outline):
  #import pdb;pdb.set_trace()
  assert len(outline) == 1
  stroke = outline[0]
  #niggle to disable
  if stroke in specials.keys():
    return specials[stroke]
  #use katakana?
  kata = "F" in stroke
  stroke = stroke.replace("F","")
  #first character
  #split after last vowel
  #import pdb;pdb.set_trace()
  first,last,_ = re.split(r'([^AEIOU*\-]*)$', stroke,maxsplit=1)
  tranl = ""
  base = first.replace('*','')
  if kata and stroke in superforeign:
    tranl = superforeign[stroke]
  elif base in hirastart:
    if kata:
      tranl = katastart[base]
    else:
      tranl = hirastart[base]
    #add dakuten if * pressed
    if dakutenable.match(first):
      tranl = chr(ord(tranl)+1)
    #just one special case for hiragana here
    if first=="*U": 
      tranl = "ゔ"
    #prefix sokuen if L pressed
    if "L" in last and first[0] in "STPHR":
      if kata:
        tranl = "ッ"+tranl
      else:
        tranl = "っ"+tranl
    #suffix small ya or yo or yu
    if "EU" in first and len(tranl)==1:
      if "R" in last:
        if "G" in last or "B" in last or "S" in last:
          return KeyError
        if kata:
          tranl += "ャ"
        else:
          tranl += "ゃ"
      elif "G" in last:
        if "R" in last or "B" in last or "S" in last:
          return KeyError
        if kata:
          tranl += "ョ"
        else:
          tranl += "ょ"
      elif "S" in last:
        if "R" in last or "G" in last or "B" in last:
          return KeyError
        if kata:
          tranl += "ュ"
        else:
          tranl += "ゅ"
    #suffix long vowel dash if T pressed
    if "T" in last:
      tranl+="ー"
    #or else suffix -n if P pressed
    elif "P" in last:
      if kata:
        tranl+="ン"
      else:
        tranl+="ん"
  elif first=="-" and last in smallhira.keys():
    if kata:
      tranl = smallkata[last]
    else:
      tranl = smallhira[last]
  elif first =="P-" and "R" in last:
    if kata:
      tranl = "ヵ"
    else:
      tranl = "ゕ"
  elif first == "P-" and "G" in last:
    if kata:
      tranl = "ヶ"
    else:
      tranl = "ゖ"
  
  if tranl:
    return "{^}"+tranl
  else:
    raise KeyError
    
if __name__=="__main__":
  tests = {
  "-L":"っ",
  "-D":"、",
  "-Z":"。",
  "A": "あ",
  "O": "お",
  "E": "え",
  "U": "う",
  "*U": "ゔ",
  "EU": "い",
  "SA": "さ",
  "SO": "そ",
  "SE": "せ",
  "SU": "す",
  "SEU": "し",
  "TA": "た",
  "TO": "と",
  "TE": "て",
  "TU": "つ",
  "TEU": "ち",
  "PA": "か",
  "PO": "こ",
  "PE": "け",
  "PU": "く",
  "PEU": "き",
  "HA": "は",
  "HO": "ほ",
  "HE": "へ",
  "HU": "ふ",
  "HEU": "ひ",
  "KA": "な",
  "KO": "の",
  "KE": "ね",
  "KU": "ぬ",
  "KEU": "に",
  "SA*": "ざ",
  "SO*": "ぞ",
  "S*E": "ぜ",
  "S*U": "ず",
  "S*EU": "じ",
  "TA*": "だ",
  "TO*": "ど",
  "T*E": "で",
  "T*U": "づ",
  "T*EU": "ぢ",
  "PA*": "が",
  "PO*": "ご",
  "P*E": "げ",
  "P*U": "ぐ",
  "P*EU": "ぎ",
  "HA*": "ば",
  "HO*": "ぼ",
  "H*E": "べ",
  "H*U": "ぶ",
  "H*EU": "び",
  "KA*": "な",
  "KO*": "の",
  "K*E": "ね",
  "K*U": "ぬ",
  "K*EU": "に",
  "WA": "ら",
  "WO": "ろ",
  "WE": "れ",
  "WU": "る",
  "WEU": "り",
  "RA": "ぱ",
  "RO": "ぽ",
  "RE": "ぺ",
  "RU": "ぷ",
  "REU": "ぴ",
  "TKA": "ま",
  "TKO": "も",
  "TKE": "め",
  "TKU": "む",
  "TKEU": "み",
  "PWA": "わ",
  "PWO": "を",
  "PWE": "ゑ",
  "PWEU": "ゐ",
  "HRA": "や",
  "HRO": "よ",
  "HRU": "ゆ",
  "AP": "あん",
  "OP": "おん",
  "EP": "えん",
  "UP": "うん",
  "EUP": "いん",
  "SAP": "さん",
  "SOP": "そん",
  "SEP": "せん",
  "SUP": "すん",
  "SEUP": "しん",
  "TAP": "たん",
  "TOP": "とん",
  "TEP": "てん",
  "TUP": "つん",
  "TEUP": "ちん",
  "PAP": "かん",
  "POP": "こん",
  "PEP": "けん",
  "PUP": "くん",
  "PEUP": "きん",
  "HAP": "はん",
  "HOP": "ほん",
  "HEP": "へん",
  "HUP": "ふん",
  "HEUP": "ひん",
  "KAP": "なん",
  "KOP": "のん",
  "KEP": "ねん",
  "KUP": "ぬん",
  "KEUP": "にん",
  "SA*P": "ざん",
  "SO*P": "ぞん",
  "S*EP": "ぜん",
  "S*UP": "ずん",
  "S*EUP": "じん",
  "TA*P": "だん",
  "TO*P": "どん",
  "T*EP": "でん",
  "T*UP": "づん",
  "T*EUP": "ぢん",
  "PA*P": "がん",
  "PO*P": "ごん",
  "P*EP": "げん",
  "P*UP": "ぐん",
  "P*EUP": "ぎん",
  "HA*P": "ばん",
  "HO*P": "ぼん",
  "H*EP": "べん",
  "H*UP": "ぶん",
  "H*EUP": "びん",
  "KA*P": "なん",
  "KO*P": "のん",
  "K*EP": "ねん",
  "K*UP": "ぬん",
  "K*EUP": "にん",
  "WAP": "らん",
  "WOP": "ろん",
  "WEP": "れん",
  "WUP": "るん",
  "WEUP": "りん",
  "RAP": "ぱん",
  "ROP": "ぽん",
  "REP": "ぺん",
  "RUP": "ぷん",
  "REUP": "ぴん",
  "TKAP": "まん",
  "TKOP": "もん",
  "TKEP": "めん",
  "TKUP": "むん",
  "TKEUP": "みん",
  "PWAP": "わん",
  "PWOP": "をん",
  "PWEP": "ゑん",
  "PWEUP": "ゐん",
  "HRAP": "やん",
  "HROP": "よん",
  "HRUP": "ゆん",
  "-P": "ん",
  "SAL": "っさ",
  "SOL": "っそ",
  "SEL": "っせ",
  "SUL": "っす",
  "SEUL": "っし",
  "TAL": "った",
  "TOL": "っと",
  "TEL": "って",
  "TUL": "っつ",
  "TEUL": "っち",
  "PAL": "っか",
  "POL": "っこ",
  "PEL": "っけ",
  "PUL": "っく",
  "PEUL": "っき",
  "HAL": "っは",
  "HOL": "っほ",
  "HEL": "っへ",
  "HUL": "っふ",
  "HEUL": "っひ",
  "RAL": "っぱ",
  "ROL": "っぽ",
  "REL": "っぺ",
  "RUL": "っぷ",
  "REUL": "っぴ",
  "SAPL": "っさん",
  "SOPL": "っそん",
  "SEPL": "っせん",
  "SUPL": "っすん",
  "SEUPL": "っしん",
  "TAPL": "ったん",
  "TOPL": "っとん",
  "TEPL": "ってん",
  "TUPL": "っつん",
  "TEUPL": "っちん",
  "PAPL": "っかん",
  "POPL": "っこん",
  "PEPL": "っけん",
  "PUPL": "っくん",
  "PEUPL": "っきん",
  "HAPL": "っはん",
  "HOPL": "っほん",
  "HEPL": "っへん",
  "HUPL": "っふん",
  "HEUPL": "っひん",
  "RAPL": "っぱん",
  "ROPL": "っぽん",
  "REPL": "っぺん",
  "RUPL": "っぷん",
  "REUPL": "っぴん",
  "SEU": "し",
  "EUFBS":"イィ",
  "EUFG":"イェ",
  "UFR":"ウァ",
  "UFBS":"ウィ",
  "UFS":"ウュ",
  "UFB":"ウェ",
  "UFG":"ウォ",
  "UFZ":"ウゥ",
  "PW*UFR":"ヴャ",
  "PW*UFB":"ヴョ",
  "PW*UFG":"ヴィェ",
  "PW*UFS":"ヴュ",
  "PEUFGS":"キェ",
  "P*EUFGS":"ギェ",
  "PUFR":"クァ",
  "PUFB":"クォ",
  "PUFG":"クェ",
  "PUFGS":"クィ",
  "P*UFR":"グァ",
  "P*UFB":"グォ",
  "P*UFG":"グェ",
  "P*UFGS":"グィ",
  "SEUFG":"シェ",
  "S*EUFG":"ジェ",
  "SUFGS":"スィ",
  "S*UFGS":"ズィ",
  "TEUFG":"チェ",
  "TUFR":"ツァ",
  "TUFB":"ツォ",
  "TUFG":"ツェ",
  "TUFS":"ツュ",
  "TUFGS":"ツィ",
  "TEFGS":"ティ",
  "TOFS":"トゥ",
  "TEFS":"テュ",
  "T*EFGS":"ディ",
  "TO*FS":"ドゥ",
  "T*EFS":"デュ",
  "KEUFG":"ニェ",
  "HEUFG":"ヒェ",
  "H*EUFG":"ビェ",
  "REUFG":"ピェ",
  "HUFR":"ファ",
  "HUFB":"フォ",
  "HUFG":"フェ",
  "HUFGS":"フィ",
  "HUFRZ":"フャ",
  "HUFBZ":"フョ",
  "HUFGZ":"フィェ",
  "HUFSZ":"フュ",
  "HOUF":"ホゥ",
  "TKEUFG":"ミェ",
  "WEUFG":"リェ",
  "WA*F":"ラ゚",
  "WO*F":"ロ゚",
  "W*EF":"レ゚",
  "W*UF":"ル゚",
  "W*EUF":"リ゚",
  "W*EUFR":"リ゚ャ",
  "W*EUFB":"リ゚ョ",
  "W*EUFG":"リ゚ェ",
  "W*EUFS":"リ゚ュ"
  }

  for testin,testout in tests.items():
    print(testin,testout)
    assert lookup([testin])==testout
