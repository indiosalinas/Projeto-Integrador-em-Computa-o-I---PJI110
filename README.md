M.I.N.I. Triagem — Projeto Integrador em Computação I

Protótipo de uma aplicação web desenvolvida em Python e Streamlit para apoiar a aplicação estruturada de uma entrevista em saúde mental.

Importante: o projeto não pretende substituir a avaliação profissional, realizar diagnóstico autônomo ou substituir o M.I.N.I. original. O objetivo do Projeto Integrador é desenvolver e avaliar uma implementação computacional do fluxo de uma entrevista estruturada, chegando a uma versão beta.

1. O que vamos desenvolver

A proposta do grupo é transformar um protótipo inicial em uma solução de Engenharia de Software, seguindo este processo:

Problema real → levantamento de requisitos → modelagem → desenvolvimento → testes → avaliação com usuários → melhorias → versão beta

O projeto será desenvolvido tendo como referência o M.I.N.I. (Mini International Neuropsychiatric Interview), uma entrevista diagnóstica estruturada utilizada internacionalmente.

O M.I.N.I. possui perguntas e módulos organizados segundo critérios diagnósticos e utiliza diferentes caminhos de acordo com as respostas. Essa característica permite transformar o fluxo da entrevista em regras computacionais.

Atenção sobre validação

O M.I.N.I. original já possui estudos de validade e confiabilidade. Estudos de validação compararam o instrumento com entrevistas diagnósticas estruturadas de referência, utilizando medidas como:

sensibilidade — capacidade de identificar corretamente casos positivos;

especificidade — capacidade de identificar corretamente casos negativos;

valor preditivo positivo (VPP);

valor preditivo negativo (VPN);

coeficiente kappa (κ) — concordância entre classificações, considerando a concordância esperada pelo acaso;

confiabilidade interavaliadores;

teste-reteste.

Portanto, nosso projeto não pretende validar novamente o instrumento psiquiátrico.

Nossa proposta é avaliar:

se a implementação computacional reproduz corretamente as regras do instrumento;

se o sistema funciona sem erros;

se a interface é compreensível;

se potenciais usuários consideram a aplicação útil e fácil de utilizar.

2. Como acessar e rodar o projeto

Passo 1 — Criar uma conta no GitHub

Quem ainda não tiver uma conta deve criar uma em:

https://github.com

Depois acessar o repositório oficial do projeto:

GitHub — Projeto Integrador em Computação I

https://github.com/indiosalinas/Projeto-Integrador-em-Comput-a-o-I---PJI110

Passo 2 — Baixar o projeto

No GitHub:

Code → Download ZIP

Depois:

extraia o arquivo;

coloque a pasta em um local fácil de encontrar;

abra a pasta do projeto.

Quem já conhece Git pode utilizar:

git clone URL_DO_REPOSITORIO

3. Instalar o Python

O projeto utiliza Python.

Baixe pelo site oficial:

https://www.python.org/downloads/

Durante a instalação no Windows, marque:

Add Python to PATH

Depois de instalar, abra o CMD ou PowerShell e verifique:

python --version

Se aparecer a versão do Python, está funcionando.

4. Instalar o Streamlit

O Streamlit é a ferramenta que transforma nosso código Python em uma aplicação web que pode ser executada pelo navegador.

No CMD ou PowerShell:

pip install streamlit

Se não funcionar:

python -m pip install streamlit

5. Entrar na pasta do projeto

No CMD ou PowerShell, entre na pasta onde o projeto foi extraído.

Exemplo:

cd "C:\Users\SEU_NOME\Downloads\Projeto-Integrador-em-Computacao-I---PJI110"

Uma maneira mais fácil no Windows:

abra a pasta do projeto;

clique na barra de endereço do Explorador de Arquivos;

digite cmd;

pressione Enter.

O CMD abrirá diretamente naquela pasta.

6. Rodar o sistema

Dentro da pasta do projeto, execute:

streamlit run mini_app.py

Se não funcionar:

python -m streamlit run mini_app.py

O navegador deverá abrir automaticamente.

Caso não abra, o terminal normalmente mostrará algo semelhante a:

Local URL: http://localhost:8501

Copie esse endereço e coloque no navegador.

Para encerrar o sistema:

Ctrl + C

no CMD/PowerShell.

7. Entendendo rapidamente as ferramentas

GitHub → onde fica armazenado e compartilhado o código do projeto.

Git → ferramenta utilizada para controlar as versões do código.

Python → linguagem de programação utilizada no projeto.

Streamlit → framework utilizado para transformar o código Python em uma aplicação web.

Branch → uma versão paralela do código utilizada para desenvolver uma funcionalidade sem alterar diretamente a versão principal.

8. Como vamos trabalhar no GitHub

O ideal é não alterar diretamente a branch main.

Cada integrante pode trabalhar em uma branch própria ou em uma branch relacionada à tarefa.

Exemplo:

main
│
├── desenvolvimento
├── feature-interface
├── feature-logica
├── feature-testes
└── feature-documentacao

Depois, as alterações podem ser revisadas e incorporadas à versão principal.

Regra básica

Antes de começar a trabalhar:

git pull

Depois de fazer alterações:

git add .
git commit -m "Descrição da alteração"
git push

Quem ainda não conhece Git não precisa dominar tudo de uma vez. Podemos aprender e resolver juntos.

9. O que precisamos fazer primeiro

Antes de sair modificando o código, a primeira tarefa de todos é:

conseguir acessar o GitHub;

baixar o projeto;

instalar Python;

instalar Streamlit;

executar o mini_app.py;

verificar se a aplicação abre;

identificar eventuais erros.

Primeiro queremos que todos consigam rodar a versão atual.

Depois vamos dividir as tarefas e começar a evolução do projeto.

10. Próximas etapas do Projeto Integrador

Depois que todos conseguirem executar o sistema, nossa sequência será:

1. Levantamento do problema

Entender melhor o processo de acolhimento e as dificuldades existentes.

2. Entrevistas com potenciais usuários

Pretendemos conversar, conforme disponibilidade e autorizações necessárias, com profissionais envolvidos no acolhimento, enfermeiros e gestores do CAPS.

3. Levantamento de requisitos

Transformar as necessidades identificadas nas entrevistas em requisitos funcionais e não funcionais.

4. Modelagem

Criar fluxogramas, casos de uso e representação da lógica do sistema.

5. Desenvolvimento

Melhorar o código atual, a lógica condicional e a interface.

6. Testes

Criar casos de teste para verificar se cada regra funciona corretamente.

7. Avaliação de usabilidade

Apresentar o protótipo a potenciais usuários e coletar feedback.

8. Análise dos dados

Utilizar estatística descritiva e, quando o desenho e o tamanho da amostra permitirem, discutir métodos de inferência estatística.

9. Melhorias

Corrigir os problemas encontrados.

10. Versão beta

Entregar uma versão beta documentada para o Projeto Integrador.

11. Estatística no projeto

A estatística será utilizada principalmente para analisar os resultados dos testes e da avaliação do sistema.

Podemos trabalhar com variáveis como:

tempo para realizar uma tarefa;

quantidade de erros;

número de etapas;

facilidade de utilização;

satisfação;

percepção de utilidade.

Podemos utilizar:

média;

mediana;

frequência;

proporção;

desvio-padrão;

distribuição dos dados.

Dependendo dos dados coletados, também poderemos discutir conceitos de inferência estatística, como estimativas, intervalos de confiança e testes de hipóteses.

Para variáveis de contagem, como número de erros, podemos discutir modelos como a regressão de Poisson quando apropriado. Se houver variabilidade maior do que a esperada pelo modelo de Poisson, podemos discutir o conceito de superdispersão e alternativas, como a regressão binomial negativa.

A escolha do método estatístico será feita depois de conhecermos os dados, e não o contrário.

12. Engenharia de Software no projeto

O projeto também será utilizado para aplicar conceitos estudados na disciplina de Engenharia de Software:

levantamento de requisitos;

requisitos funcionais;

requisitos não funcionais;

casos de uso;

modelagem;

arquitetura;

controle de versão;

Git/GitHub;

refatoração;

testes;

manutenção;

documentação;

usabilidade.

Um exemplo de requisito funcional:

RF03 — O sistema deverá apresentar perguntas condicionais de acordo com respostas anteriores.

Exemplo:

Resposta A2 = SIM
        ↓
Apresentar A6

Resposta A2 = NÃO
        ↓
Pular A6

Essa lógica será testada para garantir que a implementação computacional reproduza corretamente o fluxo definido.

13. Importante: se aparecer erro

Não tente resolver apagando arquivos ou alterando várias coisas ao mesmo tempo.

Mande no grupo:

print do erro;

comando que você executou;

diga qual sistema está usando (Windows/Linux/Mac);

se possível, copie também as últimas linhas que aparecem no terminal.

Assim conseguimos identificar o problema juntos.

14. Objetivo imediato

Meta inicial para todos:

Conseguir abrir a versão atual do M.I.N.I. Triagem no navegador utilizando o Streamlit.

Depois que todos conseguirem rodar, começamos oficialmente a divisão das tarefas e o desenvolvimento colaborativo.

Estrutura resumida

GitHub
   ↓
Baixar/clonar projeto
   ↓
Python
   ↓
Instalar Streamlit
   ↓
streamlit run mini_app.py
   ↓
Aplicação no navegador
   ↓
Testar versão atual
   ↓
Dividir tarefas
   ↓
Desenvolver
   ↓
Testar
   ↓
Avaliar
   ↓
Versão beta

Repositório

https://github.com/indiosalinas/Projeto-Integrador-em-Comput-a-o-I---PJI110
