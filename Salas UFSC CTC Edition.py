_author_ = 'Fabiano Junior Maia Manschein' #(15204840)
#Objetivo: Facilitar a localização de salas no CTC da UFSC.
#Baseado no "Mapeamento das edificações do Centro Tecnológico da UFSC" -> http://portal.ctc.ufsc.br/edificacoes/
#OBSERVAÇÕES:
# 1- Laboratório = LAB;
# 2- As palavras-chave para os laboratórios aparecem de duas possíveis formas: por extenso ou pela sua sigla ("LAB DE ALGUMA COISA" ou "LAC");
# 3- Departamento = DEPTO;
# 4- Engenharia = ENG;
# 5- Acentos, travessões e espaços são levados em consideração;
# 6- Salas de professores não incluídas;
# 7- As respostas não são case-sensitive.

#==---==#

from turtle import *  #A biblioteca turtle será utilizada para o mapa da UFSC
from time import sleep  #Sleep será utilizado para colocar um delay antes de fechar o programa

setup(width = 900, height = 900, startx = None, starty = None)  #Resolução 900x900 e começa fora da tela
bgpic("mapaufsc900.gif")  #Mapa da UFSC como background do turtle
color("black","red")  #Contorno preto preenchido de vermelho no turtle
turtlesize(2,2,2)    #tamanho da seta
speed(0)  #Velocidade da luz para q o turtle n apareca saindo da tela
penup()
goto(2411,6969)  #Turtle vai para fora da tela
pensize(2)           #grossura da linha
speed(5)          #velocidade rápida 



#Funções para 'resposta'
sim = ["sim", "si", "yes", "yah", "yarrr"]
nao = ["nao", "não", "no", "nope", "nop"]


#== PRÉDIOS CTC ==#

#Bloco A - Salas Pós-ARQ
ctc01 = ["XEROX", "BANCO DO BRASIL", "BB", "ENS", "DEPTO ENS", "DEPARTAMENTO ENS", "PÓS-ARQ","SECRETARIA DEPTO PÓS-ARQ",
          "SALA DE MEIOS DEPTO PÓS-ARQ", "COORDENADORIA DEPTO PÓS-ARQ", "SECRETARIA PÓS-ARQ","SALA DE MEIOS PÓS-ARQ",
          "COORDENADORIA PÓS-ARQ", "PÓS ARQ","PÓSARQ", "POSARQ", "POS-ARQ", "RECURSOS AUDIOVISUAIS", "PPGEAS",
          "SECRETARIA PPGEAS", "AUTOJUN", "LCA", "CONTROLE E INSTRUMENTAÇÃO DAS", "LAPSE", "PET EEL", "PETEEL", "LPDS",
          "C2E"]

#Bloco B - Salas 101 a 113, 201 a 210, 301 a 306 e laboratórios de informática
ctc02 = ["CTC101", "CTC102", "CTC103", "CTC104", "CTC105", "CTC106", "CTC107", "CTC108", "CTC109", "CTC110", "CTC111",
          "CTC112", "CTC113", "CTC201", "CTC202", "CTC203", "CTC204", "CTC205", "CTC206", "CTC207", "CTC208", "CTC209",
          "CTC210", "CTC301","CTC302", "CTC303", "CTC304", "CTC305", "CTC306", "CTC307", "LIICT1", "LIICT2", "LIICT3",
          "LIICT4", "LIICT5", "LIICT6", "LIICT7", "LIICT8", "LIICT9", "LIICT"]

#Bloco C - Administrativo- Salas de professores DAS e EEL.
ctc03 = ["LTIC","EXPERIENCIAS DE PROCESSOS DE IMAGENS","EXPERIÊNCIAS DE PROCESSOS DE IMAGENS", "LMM", "PG ENS", "PGENS",
          "LPR", "LCA", "LAN", "LIN", "LAI", "LABLEGO", "LAR DO ZOMER", "SALA DE PROFESSORES", "PPGEAS", "SECRETARIA DAS",
          "SALA 1 EEL", "SALA 2 EEL", "SALA 3 EEL", "SALA 4 EEL", "LABPLAN", "DAS", "DEPTO DE AUTOMAÇÃO E SISTEMAS", "ZOMER"]

#Bloco D - Laboratório Vibrações e Acústica- Salas e laboratórios LARI, PISA e GTVA.
ctc04 = ["ENSAIOS AUDIOMÉTRICOS E MECÂNICOS", "LGTVA", "ENSAIOS ELETRO-ACÚSTICOS", "LAB GTV A", "LABORATÓRIO DE VIBRAÇÕES E ACÚSTICA",
          "SAMIR", "ADMINISTRAÇÃO DOS ENSAIOS", "PISA", "LARI", "PARMEGIANA", "EXPERIÊNCIAS GERAIS DE VIBRAÇÕES E ACÚSTICA", "PHD",
          "GTVA"]

#Bloco E - Engenharia Elétrica- Salas 03, 04, 08, 09 e 10.
ctc05 = ["MAGLAB", "LABORATÓRIO DE EFICIÊNCIAS ENERGÉTICAS", "EEL001", "EEL002", "EEL003", "EEL004", "EEL08", "EEL09",
          "EEL010", "EEL011", "EEL012", "LABMAQ", "GPQCOM", "GEMCO", "LINSE", "LABPROJETO/LABMICRO", "LABPROJETO",
          "LABMICRO", "LABDIGITAL", "LPDS", "LABCIRCUITOS", "LABTELECO", "LCI", "LAMATE", "LPDS", "GRUCAD", "LABSPOT",
          "LAESP", "LAESP GRUCAD", "LABENERGIA"]

#Bloco F - Engenharia Elétrica (INEP)- Salas e Auditório.
ctc06 = ["LABENSAIOS", "LAB ENSAIOS", "LAB ENSINO ELETRÔNICA DE POTËNCIA", "LAB CÉLULAS E COMBUSTÍVEIS", "LAB CONTROLES DIGITAIS",
          "LAB DESENVOLVIMENTO", "LAB DE LAYOUT", "LAB LAYOUT E PROTÓTIPO"]

#Bloco G - Engenharia de Produção e Sistemas
ctc07 = ["NURS", "NÚCLEO DE REDE E SUPRIMENTOS", "LAB ERGONOMIA E ESTUDO DE INFORMÁTICA", "PET EPS", "PETEPS", "EJEP", "LAB MCDA", "MCDA",
          "LAB DE METODOLOGIA MULTICRITÉRIO DE APOIO Á DECISÃO", "LPP", "LAB PROJETO DE PRODUTO", "LAB AV", "LAB A V"]

#Anexo EPS - Salas de aula 01,02 e 03.
ctceps = ["PPGEGC", "ANEXO EPS", "AUDITÓRIO EPS"]

#NPD
ctc08 = ["LAB LATIN", "ANFITEATRO PPGEP", "DATACENTER", "REDE UFSC", "LAB INTEROP", "LAB GESTÃO PARA SUSTENTABILIDADE",
       "IGTI", "IGTI NÚCLEO DE ESTUDOS", "LAB DE CUSTOS", "NPD", "NÚCLEO DE PROCESSAMENTO DE DADOS"]

#Bloco I – Engenharia Mecânica
ctc09 = ["LAB DE CLUSTER", "LAB DE BULIÔMETRO", "LAB ROBÓTICA", "ROBOTICA", "LAB CADCAN", "LABCADCAM", "GEMAC", "GRANTE", "I9", "DEPTO EMC",
          "LAB SOLAR", "LABSOLAR", "LAB CET", "SIGER", "SALA DE VISUALIZAÇÃO 3D", "3D", "SINMEC", "LAB DE COMPUTADORES",
          "LMPT", "POSMEC", "PGMAT", "AERODESIGN", "I9 CONSULTORIA", "NEPET"]

#Bloco K – Engenharia Mecânica
ctc11 = ["GRUCON", "SALA RUGOSÍMETRO", "USICON", "LMP", "LASER", "LAB PLASMA", "LAB USINAGEM DE ULTRAPRECISÃO",
          "LAB ANÁLISE TÉRMICA", "LABMAT", "BAJA", "BAJA SAE", "NEDIP", "LAB METALOGRAFIA", "LAB HIPERBÁRICA", "LAB LHW",
          "SALA TÚNEL VENTO", "LAB TERMO", "LAB TRANSDUTORES FLUXO CALOR", "PLASMA", "CERMAT", "PÓS EMC", "XEROX EMC",
          "LABHIP", "LAB HIP", "MONTAGEM HIDRÁULICA", "ELETRÔNICA", "LAB HIDRÁULICA PNEUMÁTICA", "UN POTËNCIA", "LAB CEMA",
          "LABCET", "LAB CET", "LAB SIST COMPACTOS DE CO-GERAÇÃO", "LAB SISTEMAS COMPACTOS DE CO-GERAÇÃO", "LAB COMPACTO DE COGERAÇÃO",
          "TÉCNICO LAB TERMO", "DINAMÔMETRO", "CEMA", "LAB CONFORMAÇÃO MECÂNICA", "LAB ESTUDOS", "LABSOLDA", "LAB SOLDA",
          "LAB USICON", "GRUCON GRIMA", "LAB GRUCON", "CPD", "LAB LMP", "NEDIP", "INJECT", "LAB PROTOTIPAGEM", "LAB CINJECT",
          "SALA PÓS CERÂMICA", "LABTUCAL", "LAB LEPTEN", "LAB EBULIÇÃO E CONDENSAÇÃO", "LAB INSTRUMENTOS", "LAB CARACTERIZAÇÃO MAGNÉTICA",
          "MICROSCOPIA ELETRÔNICA DE VARREDURA", "CIMM", "GETEC", "LAB INSTRUMENTAL", "LAB PNEUMÁTICA", "LAB CET", "SALA COMBUSTÃO",
          "SALA EXPERIMENTOS", "LAB CÉLULAS COMBUSTÍVEIS", "LAB CGT", "LAB RADIOGRÁFICO", "LAB ELETRÔNICA"]

#Bloco L + Ligação – Engenharia Sanitária e Ambiental
ctc12 = ["LABTOX", "COT", "C.O.T.", "CROMATOGRAFIA LÍQUIDA", "ABSORÇÃO ATÔMICA", "MICROBIOLOGIA", "MICROSCOPIA", "LAPOÁ",
          "COLILERT", "XEROX ESA", "LAB IMA", "LABCQAR", "LAB IMA/CQAR", "LAB REMAS", "LAB IMA/REMAS", "REMAS", "LAB HIDRO",
          "LAB TOX", "EJESAM", "LAHIMAR", "LAB LAGA", "LAB PING ALTO", "LAB CONTROLE E QUALIDADE DE AR", "LAB HIDROLOGIA",
          "GESAD", "NEA", "LABEFLU", "TSGA", "LARESO", "LARA", "TOMB RAIDER", "LAB REUSO DAS ÁGUAS"]

#CETEC- Restaurante e Centros Acadêmicos.
ctc13 = ["CAECA", "CALEC", "CALESA", "CALEQA", "CALIPRO", "CAME", "CALICO", "CAEE", "CAMAT", "CASIN", "NEAMB"]

#Almoxarifado e Salas de Aula- Salas e Laboratórios.
ctc14 = ["GRUPO DE ENGENHARIA DE PRODUTOS DE PROCESSOS", "GEPP", "LAB DE INOVAÇÃO"]

#Bloco P – Arquitetura (madeira)
ctc16 = []

#Subestação I – CTC17
ctc17 = []

#Bloco A – Engenharia Química- Laboratórios.
ctc18 = ["LAB DE ENERGIA E MEIO AMBIENTE", "LAB MATERIAIS CORROSÃO", "LABOPE", "LAFETE", "LABOPE-LAFETE",
         "LAB DE FENÔMENOS DE TRANSFERÊNCIA E OPERAÇÕES UNITÁRIAS I E II", "LAB DE FENÔMENOS DE TRANSFERÊNCIA E OPERAÇÕES UNITÁRIAS 1 E 2",
         "LAB DE FENÔMENOS DE TRANSFERÊNCIA E OPERAÇÕES UNITÁRIAS"]

#Bloco B – Engenharia. Química- Salas e Laboratórios.
ctc19 = ["CONAQ", "CALEQA", "LAB TRATAMENTO BIOLÓGICO DE RESÍDUOS"]

#Bloco C – Eng. Química- Laboratórios
ctc20 = ["LAB DE PROCESSAMENTO DE ALIMENTOS"]

#Bloco D – Engenharia Química- Salas e Laboratórios.
ctc21 = ["NEUROLAB", "CULTURA DE CÉLULAS E TECIDOS", "INTELAB", "LATESC", "LAB QUÍMICO"]

#Departamento de Serviços Gerais- Salas de aula 15,16,17 e 18.
dag02 = ["ARQUIVO DEPTO ARQUIVO CENTRAL", "DEPTO PATRIMÔNIO", "DEPTO DE SERVIÇOS GERAIS", "ARQUIVO CENTRAL"]

#Bloco E – Engenharia Química- Salas de aula 19 a 23 e E111.
ctc24 = ["EQA019", "E111", "XEROX ENG QUÍMICA", "CENTRAL DE ANÁLISES", "ENQ", "EQA", "EQA020", "EQA021", "EQA022", "EQA023"]

#Convivência – Servidores
ctc25 = ["GRÊMIO SÓCIO CULTURAL DOS SERVIDORES"]

#Bloco T (A) – Engenharia Civil- Salas e Laboratórios.
ctc27 = ["ALTATENSÃO", "LMS", "LABTRANS", "LAB TRANS", "LABCIG", "LAB CIG", "GEAP", "LAB PAVIMENTAÇÃO", "LABFSG", "LAB FSG",
         "RETAC", "GEOENG", "NPC"]

#Bloco U (B) – Engenharia. Civil
ctc28 = ["LAB DE MATERIAIS DE CONSTRUÇÃO", "LAB DE NANOTECNOLOGIA", "GIEM", "GPEND", "LEE", "LABEEE", "INFOHAB", "GDA",
         "GESTCON", "GTEC", "LAE", "GRUPEX", "ECV", "PET ECV", "EPEC ECV", "LABINFO", "LABINFO-MICROS", "LAB INFORMÁTICA",
         "LMCC"]

#Bloco V – Adm. Central e FEESC
ctc30 = ["FEESC", "CPD", "CDI"]

#Departamento de Informática e Estatística- Salas, Laboratórios e Auditório.
ctc31 = ["SETIC", "INE", "LAB DE ENSINO DE INFORMÁTICA", "LABSEC", "EDUGRAF", "LAB DE SOFTWARE EDUCACIONAL", "LRG", "GENESS",
         "LRG", "LAB DE REDES E GERÊNCIA", "LISHA", "LAB DE SEGURANÇA EM COMPUTAÇÃO", "LAPIX", "LAB DE PROCESSAMENTO DE IMAGENS",
         "LAB DE COMPUTAÇÃO GRÁFICA", "LAPS", "LAB DE AUTOMAÇÃO DE PROJETOS E REDES", "LSC", "IATE",
         "INTELIGÊNCIA ARTIFICIAL E TECNOLOGIA EDUCACIONAL", "LAB NIME", "NIME", "LAB SALA LIMPA", "LABSOFT", "LAB LEEGI", "LAB SOFT",
         "LABLEEGI", "APILAB", "LBC", "LAPESD", "LEA", "EXTREME LAB", "LAB LISA", "LISA"]

#Novo Bloco da Engenharia Química (etapa 1)- Salas e Laboratórios.
ctc32 = ["PROFI", "LAB PROFI", "LAB LEMA", "LEMA", "LAB DE ENERGIA MEIO AMBIENTE", "LAB DE SISTEMAS POROSOS", "LASIPO",
         "LASEM", "LABSIN", "LABMASSA", "ENG BIO"]

#Bloco J (A2) – Engenharia Mecânica
ctc37 = ["POLO", "LAB ESCOAMENTO MULTIFÁSICO", "SLOPE", "THERMINAL SLOPE", "LAB CONTROLES E SISTEMAS DE REFRIGERAÇÃO",
         "LAVABO"]

#Laboratórios – Engenharia Sanitária Ambiental- Salas de aula 211,212,213,214,215,216 e 217. !!!!! CHECAR CODIGO SALAS DE AULA !!!!!
ctc38 = ["LAB HIDRÁULICA", "LAHIMAR", "LABTOX1", "LABTOX2", "LABTOX", "ABSORÇÃO ATÔMICA", "LAB INTEGRADO LIMA",
         "LIMA", "LCQAR", "OLFATOMETRIA", "LAB POLUIÇÃO ATMOSFÉRICA", "LAPOA", "LABHIDRO"]

#Blocos A, B e C – Arquitetura- Salas 01 a 12, Laboratórios e Auditório.
ctc39 = ["LABCISCO", "LAB DE SISTEMAS CONSTRUTIVOS", "LAB RESTAURO", "ARQ001", "ARQ002", "PGAU", "LABCON", "LAB DE CONFORTO",
         "APEU", "GIPEDU", "LAB URB", "LABURB", "LABRESTAURO", "LAB CISCO", "LAB CON", "ARQ103", "ARQ104", "ARQ105",
         "ARQ03", "ARQ04", "ARQ05", "ARQ01", "ARQ02", "ARQ06", "ARQ07", "ARQ08", "ARQ09", "ARQ10", "ARQ11", "ARQ12",
         "ARQ301," "ARQ306", "ARQ307", "ARQ308", "ARQ309", "ARQ310", "ARQ311", "ARQ312", "LAB DE CONFORTO AMBIENTAL",
         "MAQUETARIA", "LDA", "LAB DE DOCUMENTAÇÃO E ACERVO", "ARQ001", "ARQ002", "ARQ003", "ARQ004", "ARQ005", "ARQ006",
         "ARQ007", "ARQ008", "ARQ009", "ARQ010", "ARQ011", "ARQ012", "ARQ013", "ARQ101", "ARQ102", "ARQ103", "ARQ104", "ARQ105",
         "ARQ106", "ARQ107", "ARQ108", "ARQ109", "ARQ110", "ARQ111", "ARQ112", "ARQ301", "ARQ302", "ARQ303", "ARQ304",
         "ARQ305", "ARQ306", "ARQ307", "ARQ308", "ARQ309", "ARQ310", "ARQ311", "ARQ312"]

#Lab. do Ensino à Distância (EAD) (junto a IU)
ctc41 = ["LGR", "REDE EGCLABS", "EGCLABS", "LEC", "NGS"]


#==---==#


#Função que chamará outra função dependendo do centro digitado pelo usuário.
#Observação: Nesta edição do Salas UFSC, apenas o centro CTC está incluido.
def centros(centro):
    print("Buscando centro", centro.upper())
    if centro == "CTC":
        print("Centro encontrado.")
        sala = input("Por favor, digite a sala desejada. Ex: 'CTC103' ").upper()
        ctc(sala)
    else:
        centro = input("Centro não encontrado. Tente 'CTC': ").upper()
        return centros(centro)


#Salas do CTC, com suas coordenadas e nomes.
def ctc(sala):
    print("Buscando sala", sala.upper())
    if sala in ctc01:  #Hall CTC
        x = 135
        y = -75
        predio = "Hall CTC"
        desenho(x, y, predio)

    elif sala in ctc02:  #Bloco B de salas de aula
        x = 120
        y = -60
        predio = "Bloco B"
        desenho(x, y, predio)

    elif sala in ctc03:  #DAS
        x = 147
        y = -65
        predio = "DEPTO de Automação e Sistemas"
        desenho(x, y, predio)

    elif sala in ctc04:  #Laboratório Vibrações e Acústica
        x = 125
        y = -82
        predio = "LAB Vibrações e Acústica"
        desenho(x, y, predio)

    elif sala in ctc05:  #Engenharia Elétrica
        x = 150
        y = -90
        predio = "ENG Elétrica"
        desenho(x, y, predio)

    elif sala in ctc06:  #Eng Elétrica (INEP)
        x = 150
        y = -90
        predio = "ENG Elétrica (INEP)"
        desenho(x, y, predio)

    elif sala in ctc07:  #Engenharia de Produção e Sistemas
        x = 120
        y = -118
        predio = "ENG de Produção e Sistemas"
        desenho(x, y, predio)

    elif sala in ctceps:  #Anexo Engenharia de Produção e Sistemas
        x = 120
        y = -118
        predio = "Anexo ENG de Produção e Sistemas"
        desenho(x, y, predio)

    elif sala in ctc08:  #NPD
        x = 145
        y = -108
        predio = "NPD"
        desenho(x, y, predio)

    elif sala in ctc09:  #Bloco I - Engenharia Mecânica
        x = 118
        y = -150
        predio = "DEPTO de ENG Mecânica"
        desenho(x, y, predio)

    elif sala in ctc11:  #Bloco K - Engenharia Mecânica
        x = 73
        y = -130
        predio = "Bloco B da ENG Mecânica"
        desenho(x, y, predio)

    elif sala in ctc12:  #Engenharia Sanitária e Ambiental
        x = 101
        y = -83
        predio = "ENG Sanitária e Ambiental"
        desenho(x, y, predio)

    elif sala in ctc13:  #CETEC
        x = 124
        y = -103
        predio = "CETEC"
        desenho(x, y, predio)


    elif sala in ctc14:  #Almoxarifado e Salas de Aula
        x = 145
        y = -108
        predio = "Almoxarifado e salas de aula"
        desenho(x, y, predio)

    elif sala in ctc18:  #Bloco A - Engenharia Química- Laboratórios
        x = 330
        y = -22
        predio = "Bloco A da ENG Química"
        desenho(x, y, predio)

    elif sala in ctc19:  #Bloco B – Engenharia. Química- Salas e Laboratórios
        x = 330
        y = -22
        predio = "Bloco B da ENG Química"
        desenho(x, y, predio)

    elif sala in ctc20:  #Bloco C – Eng. Química- Laboratórios
        x = 330
        y = -22
        predio = "Bloco C da ENG Química"
        desenho(x, y, predio)

    elif sala in ctc21:  #Bloco D – Engenharia Química- Salas e Laboratórios.
        x = 330
        y = -22
        predio = "Bloco D da ENG Química"
        desenho(x, y, predio)

    elif sala in ctc24:  #Bloco E – Engenharia Química- Salas de aula 19 a 23 e E111. EQA.
        x = 315
        y = -20
        predio = "DEPTO de ENG Química"
        desenho(x, y, predio)

    elif sala in dag02:  #Departamento de Serviços Gerais- Salas de aula 15,16,17 e 18.
        x = 330
        y = 5
        predio = "DEPTO de Serviços Gerais"
        desenho(x, y, predio)

    elif sala in ctc27:  #Bloco T (A) – Engenharia Civil- Salas e Laboratórios.
        x = 270
        y = -45
        predio = "Bloco A da ENG Civil"
        desenho(x, y, predio)

    elif sala in ctc28:  #Bloco U (B) – Engenharia Civil.
        x = 270
        y = -45
        predio = "Bloco B da ENG Civil"
        desenho(x, y, predio)

    elif sala in ctc30:  #Bloco V – Adm. Central e FEESC
        x = 100
        y = -55
        predio = "Administração Central e FEESC"
        desenho(x, y, predio)

    elif sala in ctc31:  #Departamento de Informática e Estatística- Salas, Laboratórios e Auditório.
        x = 85
        y = -90
        predio = "DEPTO de Informática e Estatística"
        desenho(x, y, predio)

    elif sala in ctc32:  #Novo Bloco da Engenharia Química (etapa 1)- Salas e Laboratórios.
        x = 285
        y = -5
        predio = "ENG Química"
        desenho(x, y, predio)

    elif sala in ctc37:  #Bloco J (A2) – Engenharia Mecânica
        x = 118
        y = -150
        predio = "DEPTO de ENG Mecânica"
        desenho(x, y, predio)

    elif sala in ctc38:  #Laboratórios – Engenharia Sanitária Ambiental- Salas de aula 211,212,213,214,215,216 e 217.
        x = 101
        y = -83
        predio = "ENG Sanitária Ambiental"
        desenho(x, y, predio)

    elif sala in ctc39:  #Blocos A, B e C – Arquitetura- Salas 01 a 12, Laboratórios e Auditório.
        x = 105
        y = -215
        predio = "Arquitetura"
        desenho(x, y, predio)

    else:  #Se a 'sala' não for encontrada nas listas, perguntará ao user se ele quer procurar outra sala.
        print("----------")
        print("Sala não encontrada.")
        repetir()


#Função para desenhar um circulo nas coordenadas (x,y) do 'predio' da sala digitada.
def desenho(x, y, predio):
    print("Sala encontrada. Por favor, olhe o mapa.")
    clear()  #Remove quaisquer marcações anteriores
    penup()
    goto(x, y)  #Predio (x,y)
    pendown()
    circle(25)  #Circulo de raio 25
    penup()
    goto(x, y+25)  #Centro do circulo (x,y+25)
    pendown()
    tiltangle(angle=270)  #Turtle aponta para baixo
    stamp()  #Marca o centro do circulo
    penup()
    goto(x, y+52)  #Um pouco acima do circulo
    write(predio, False, align="center", font=("Calibri (Body)", 15, "bold"))  #Escreverá o 'predio' circulado
    goto(1000, 1000)  #Turtle sai da tela
    print("----------")
    repetir()


#Função para looping ou encerramento do programa.
def repetir():
    resposta = input("Gostarias de pesquisar outra sala? ").lower()  #Procurar outra sala ou sair do programa?
    if resposta in nao:  #Se o user digitar nao, o programa fecha.
        print("----------")
        print("Hasta la vista, user!") #Frase de despedida
        sleep(2)  #Delay antes de fechar o programa
        quit
    elif resposta in sim:  #Se o user digitar sim, retorna a função 'centros(centro)' para pesquisar outra sala.
        print("----------")
        centro = input("Por favor, digite o centro da sala desejada. Ex: 'CTC' ").upper()
        return centros(centro)
    else:                 #Se o user não digitar nem 'sim' nem 'não', retorna a função 'repetir()'.
        print("----------")
        print("Tente responder 'sim' ou 'não'")
        return repetir()


#==---==#


#Main Program:

print("Bem-vindo(a) ao Salas UFSC (CTC Edition)!")

centro = input("Por favor, digite o centro da sala desejada. Ex: 'CTC' ").upper()  #Usuário digita o centro desejado.
centros(centro)
