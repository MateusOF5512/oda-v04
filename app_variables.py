

path_vac = "dados_gerais.csv"
path_posto = "dados_postos.csv"






#------------------------------------------------------------------------------------ HTML VARIABLES:

# --------------------------- INTRODUÇÂO --------------------------------------------------------------
html_title="""
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="project control, dashboard, management">
<meta name="description" content="project control dashboard">
<meta name="author" content="Mateus Ortiz Ferreira">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#4169e1; font-family:sans-serif">Observatório de Dados Abertos<br>
 <h2 style="color:#4169e1;font-family:sans-serif">Campanha de Vacinação Contra COVID-19 em Florianópolis-SC/BR</h3> <br>
 <hr style= "display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
#------------------------------- RODAPÈ -------------------------------
html_rodape="""
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style="color:Gainsboro; text-align: right;">By: mateus7ortiz@gmail.com</p>
"""

#------------------------- BEM VINDO --------------------------------------------------------

html_card_header_0A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1200px; height: 40px;font-size: 20px">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Bem-vindo!</h4>
  </div>
</div>
"""
html_card_body_0A_1_11="""
<div class="card" style="border-radius: 0px 0px 10px 10px; background: #F5F5F5; width: 1200px; height: 100px;
font-size: 16px;  padding-top: 15px; padding-left: 15px; padding-right:15px">
    <h8 class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; 
        font-family:sans-serif; text-align: justify;"
        >Apresentação Inicial... </h8>
</div>
"""

html_card_header_0A_1_21="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;font-size: 20px">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Descrição dos Dados</h4>
  </div>
</div>
"""
html_card_body_0A_1_21="""
<div class="card" style="border-radius: 0px 0px 10px 10px; background: #F5F5F5; width: 550px; height: 150px;
font-size: 16px;  padding-top: 15px; padding-left: 15px; padding-right:15px">
    <h8 class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; 
        font-family:sans-serif; text-align: justify;"
        >As vizualizações apresentam os Dados referentes à Campanha de Vacinação contra Covid-19, 
        da população residente em Florianópolis/SC, para melhor contraste das informações também utilizamos os
        Dados do CENSO de 2010 (mais recente).</h8>
</div>
"""
html_card_header_0A_1_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;font-size: 20px">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Links Importantes</h4>
  </div>
</div>
"""
#---------------------0 - DICAS DE EXPLORAÇÃO
html_header_02="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >0 - Dicas de Exploração</h2>
  </div>
</div>
"""
html_subheader_01="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >O que é a análise exploratória de dados?</h3>
  </div>
</div>
"""
html_card_header_00A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 750px; height: 40px;font-size: 20px">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Definição</h4>
  </div>
</div>
"""
html_card_body_00A_1_11="""
<div class="card" style="border-radius: 0px 0px 10px 10px; background: #F5F5F5; width: 750px; height: 200px;
font-size: 16px;  padding-top: 15px; padding-left: 15px; padding-right:15px">
    <h8 class="card-title" style="background-color:#F5F5F5; color:#0d0d0d; 
        font-family:sans-serif; text-align: justify;"
        >A análise exploratória de dados (AED) é usada por profissionais da área de dados para analisar e investigar 
        conjuntos de dados e resumir suas principais características, muitas vezes usando métodos de 
        visualização de dados, como presente nesta aplicação. Ela permite determinar a melhor forma de 
        controlar as fontes de dados para obter as respostas que você precisa, 
        tornando mais fácil descobrir padrões, detectar anomalias, testar uma hipótese ou verificar suposições.</h8>
</div>
"""
html_card_header_00A_1_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 350px; height: 40px;font-size: 20px">
    <h4 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Suas vantagens:</h4>
  </div>
</div>
"""
html_card_body_00A_1_12="""
<ul style="border-radius: 0px 0px 10px 10px; background: #F5F5F5; width: 350px; height: 200px;
font-size: 16px;  padding-top: 15px; padding-left: 15px; padding-right:15px">
  <li>Visualizar os dados</li>
  <li>Filtrar os dados</li>
  <li>Identificar desvios</li>
  <li>Geração de insights</li>
  <li>Verificar hipóteses</li>
  <li>Caracterizar diferenças entre grupos.</li>
</ul> 
"""
html_subheader_02="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >Explorando os gráfico</h3>
  </div>
</div>
"""
html_subheader_03="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >Explorando esta ferramenta</h3>
  </div>
</div>
"""

#------------------- 1.1 - Número de Doses & Vacinas Aplicadas -------------------------------------------

html_header_01="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >1 - Descrição da Campanha de Vacinação</h2>
  </div>
</div>
"""
html_subheader_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >1.1 - Número de Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""
html_card_header_1A1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados com 1° Dose: Proporção</h5>
  </div>
</div>
"""
html_card_header_1A2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados com 1° Dose: Quantidade</h5>
  </div>
</div>
"""
html_card_header_1A3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados Completamente: Quantidade</h5>
  </div>
</div>
"""
html_card_header_1A4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados Completamente: Proporção</h5>
  </div>
</div>
"""

html_card_header_1B11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Quantidade de Vacinas Aplicadas por Dose</h5>
  </div>
</div>
"""
html_card_header_1B12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Proporção entre as Vacinas Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1B2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 0;"
    >Dados dos Pacientes Vacinados</h5>
  </div>
</div>
"""
#--------------------------------------- 1.2 - Variação das Doses & Vacinas Aplicadas ----------------------
html_subheader_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >1.2 - Variação das Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""
html_card_header_1C11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação das Doses Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação das Vacinas Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C20="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Dados</h5>
  </div>
</div>
"""


#------------------------------------------------2 -
html_header_20="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >2 - Características da População Vacinada</h2>
  </div>
</div>
"""
html_subheader_2A_10="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.1 - Análise do Sexo Biológico</h3>
  </div>
</div>
"""
html_card_header_2A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Masculino</h5>
  </div>
</div>
"""
html_card_header_2A_1_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Proporção entre os Sexos</h5>
  </div>
</div>
"""
html_card_header_2A_1_13="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Feminino</h5>
  </div>
</div>
"""
html_card_header_2A_1_20="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1100px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0px;"
    >Sexo Biológico - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2A_1_30="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1100px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação de Vacinados</h5>
  </div>
</div>
"""


html_subheader_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.1 - Análise do Sexo Biológico</h3>
  </div>
</div>
"""
html_card_header_2B="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Masculino</h5>
  </div>
</div>
"""
html_subheader_2B_10="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.2 - Análise da Raça/Cor</h3>
  </div>
</div>
"""
html_card_header_2B_2_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >População Residente x População Vacinada</h5>
  </div>
</div>
"""
html_card_header_2B_2_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_21="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_subheader_2B_30="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.3 - Análise da Idade</h3>
  </div>
</div>
"""
html_card_header_2B_3_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Quantidade de Vacinados</h5>
  </div>
</div>
"""
html_card_header_2B_3_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_3_21="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Variação de Vacinados</h5>
  </div>
</div>
"""
html_card_header_2B_3_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Companha de Vacinação</h5>
  </div>
</div>
"""
#----------------------------- BLOCO C
html_header_30="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >3 - Informações dos Postos de Vacinação/BR</h2>
  </div>
</div>
"""
html_card_header_3A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;"
    >Mapa de Densidade dos Vacinados</h5>
  </div>
</div>
"""
html_card_header_3A_1_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;"
    >Mapa com Descrição dos Postos</h5>
  </div>
</div>
"""
html_card_header_3A_1_20="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1200px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 0px 0;"
    >Dados dos Postos de Vacinação</h5>
  </div>
</div>
"""