# Projeto-Integrador-em-Computa-o-I---PJI110
Mini International Neuropsychiatric Interview  Brazilian version 5.0.0  DSM IV 
Claro. Eu manteria a estrutura do plano anterior, mas mudaria a voz para **“minha proposta para o grupo”**, deixando explícito que somos oito integrantes e mostrando que o projeto não é apenas programação: ele integra **Engenharia de Software, Modelagem Estatística e Inferência Estatística**, além do domínio de saúde mental.

Há, porém, uma correção conceitual importante: o **M.I.N.I. (Mini International Neuropsychiatric Interview)** é uma entrevista diagnóstica estruturada, desenvolvida por pesquisadores da University of South Florida e da University of Paris, amplamente utilizada internacionalmente. Eu evitaria escrever que ele é simplesmente “um questionário padronizado pela APA”, porque isso seria tecnicamente impreciso. Podemos explicar no trabalho a relação dele com critérios diagnósticos padronizados, inclusive DSM, sem atribuir sua autoria à APA.

Segue a versão que eu levaria para o grupo:

# Plano de ação proposto para o Projeto Integrador

## Proposta: M.I.N.I. Triagem – Protótipo de sistema informatizado de apoio ao acolhimento em saúde mental no CAPS

Pessoal, pensando melhor em tudo que conversamos no grupo, no projeto que eu já vinha desenvolvendo em Python e Streamlit e, principalmente, nas exigências do Projeto Integrador, eu gostaria de propor que a gente desenvolva o projeto em cima do **M.I.N.I. Triagem**.

A ideia não seria simplesmente pegar um código que eu já tinha pronto e apresentar como trabalho. Acho que podemos transformar esse protótipo em um projeto de Engenharia de Software completo, partindo de um problema real, levantando requisitos com possíveis usuários, modelando a solução, desenvolvendo, testando e chegando ao final do semestre com uma versão beta documentada.

Além disso, acho que conseguimos aproveitar conhecimentos das disciplinas que já estudamos, principalmente **Engenharia de Software, Modelagem Estatística e Inferência Estatística**, fazendo com que o trabalho demonstre que estamos aplicando conhecimentos do curso e não apenas programando.

---

# 1. O que é o M.I.N.I.?

O **M.I.N.I. – Mini International Neuropsychiatric Interview** é uma entrevista diagnóstica estruturada utilizada para investigar transtornos psiquiátricos de maneira padronizada.

Ele possui módulos e perguntas organizadas segundo critérios diagnósticos. Uma característica importante é que existem perguntas que dependem das respostas dadas anteriormente. Portanto, nem todas as perguntas precisam necessariamente ser apresentadas em todas as entrevistas.

É justamente essa característica que torna o instrumento interessante do ponto de vista computacional.

No meu protótipo atual, por exemplo, estou trabalhando com a lógica de perguntas condicionais. Se uma resposta inicial indicar que determinado conjunto de critérios precisa ser investigado, o sistema apresenta as perguntas correspondentes; caso contrário, determinadas etapas podem ser puladas.

Então o problema de programação não é simplesmente:

> “mostrar perguntas na tela”.

Existe uma lógica de decisão que precisa ser corretamente modelada e implementada.

Também precisamos deixar claro no projeto que a aplicação não pretende substituir o profissional de saúde, realizar diagnóstico médico autônomo ou determinar condutas terapêuticas. A proposta é desenvolver uma ferramenta de apoio à aplicação estruturada da entrevista e à organização das informações.

---

# 2. Por que acho que esse projeto pode funcionar bem para o Projeto Integrador?

A principal vantagem é que ele permite trabalhar com um problema real.

Eu trabalho em um CAPS e podemos utilizar profissionais do serviço como possíveis usuários para entender como funciona o processo de acolhimento e quais dificuldades existem.

Não precisamos necessariamente implantar o sistema no CAPS.

Minha proposta seria chegarmos oficialmente a uma **versão beta**, realizando levantamento de requisitos e uma avaliação preliminar com potenciais usuários.

Assim conseguimos trabalhar com uma instituição e usuários reais, mas sem prometer uma implantação definitiva de um sistema de saúde.

A lógica do projeto seria:

**problema real**

↓

**levantamento das necessidades dos usuários**

↓

**requisitos**

↓

**modelagem**

↓

**desenvolvimento**

↓

**testes**

↓

**avaliação com usuários**

↓

**correções**

↓

**versão beta**

---

# 3. Problema que queremos investigar

Eu não apresentaria o problema como “queremos fazer um aplicativo”.

O aplicativo é a solução.

O problema que queremos investigar é a dificuldade de organizar e conduzir de maneira estruturada determinadas etapas do acolhimento e da entrevista em saúde mental.

Durante um atendimento, o profissional pode precisar lidar com diversas perguntas, critérios e caminhos diferentes de acordo com as respostas anteriores.

Quando esse processo é realizado manualmente, pode existir maior dificuldade para controlar a sequência das perguntas, lembrar quais critérios já foram investigados, identificar quais perguntas precisam ser feitas e organizar o resultado final.

A pergunta central do nosso projeto poderia ser:

**Como uma aplicação web pode auxiliar profissionais do CAPS na organização e aplicação estruturada de uma entrevista de triagem em saúde mental, mantendo o profissional como responsável pela avaliação?**

---

# 4. Tabela 1 – Alguns problemas identificados

| Problema identificado                                      | Consequência                                                   | Necessidade                                  |
| ---------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------- |
| Aplicação manual de entrevistas estruturadas               | Processo potencialmente mais demorado                          | Automatizar parte do fluxo                   |
| Grande quantidade de perguntas                             | Profissional precisa controlar manualmente a sequência         | Controle automático do fluxo                 |
| Perguntas condicionais                                     | Algumas perguntas dependem das respostas anteriores            | Implementar lógica condicional               |
| Necessidade de contabilizar critérios                      | Possibilidade de erro manual                                   | Processamento automático                     |
| Informações distribuídas durante a entrevista              | Dificuldade de organização                                     | Interface estruturada                        |
| Protótipo atual apresenta travamentos                      | Prejudica a utilização                                         | Refatoração e testes                         |
| Interface atual precisa ser melhorada                      | Pode dificultar a utilização                                   | Melhorar UI/UX                               |
| Parte do código inicial foi desenvolvida com auxílio de IA | Dificuldade de manutenção se a equipe não compreender o código | Documentação e refatoração                   |
| Ausência de documentação completa                          | Dificulta avaliação e continuidade                             | Documentação técnica e acadêmica             |
| Ausência de validação com usuários                         | Não sabemos se a solução realmente atende às necessidades      | Entrevistas e testes com potenciais usuários |

**UI** significa *User Interface*, ou Interface do Usuário.

**UX** significa *User Experience*, ou Experiência do Usuário.

---

# 5. Tabela 2 – Alguns problemas identificados e soluções propostas

| Problema                                | Solução proposta                    | Como verificar            |
| --------------------------------------- | ----------------------------------- | ------------------------- |
| Entrevista manual                       | Aplicação web estruturada           | Teste funcional           |
| Fluxo complexo                          | Navegação orientada pelas respostas | Testes de cenários        |
| Perguntas condicionais                  | Regras de salto                     | Testes da lógica          |
| Contagem manual de critérios            | Processamento automático            | Casos de teste            |
| Interface pouco amigável                | Reformulação da interface           | Avaliação de usabilidade  |
| Travamentos                             | Refatoração                         | Testes funcionais         |
| Código pouco documentado                | Documentação técnica                | Revisão do código         |
| Necessidades dos usuários desconhecidas | Entrevistas                         | Análise das respostas     |
| Ausência de validação                   | Testes com usuários potenciais      | Questionário de avaliação |
| Sistema ainda inicial                   | Evolução para versão beta           | Comparação entre versões  |

---

# 6. Objetivo geral

Desenvolver uma versão beta de uma aplicação web destinada a auxiliar profissionais no processo estruturado de triagem e entrevista em saúde mental no contexto do CAPS, utilizando princípios de Engenharia de Software, levantamento de requisitos, testes e avaliação preliminar com potenciais usuários.

---

# 7. Objetivos específicos

1. Identificar dificuldades existentes no processo de acolhimento e entrevista.

2. Entrevistar potenciais usuários, principalmente profissionais envolvidos no acolhimento em saúde mental.

3. Entrevistar gestores ou responsáveis pelo serviço para identificar necessidades institucionais.

4. Levantar requisitos funcionais e não funcionais.

5. Modelar o fluxo da aplicação.

6. Implementar perguntas condicionais e regras de navegação.

7. Melhorar a interface do protótipo atual.

8. Refatorar o código existente.

9. Implementar testes funcionais.

10. Avaliar preliminarmente a usabilidade da aplicação.

11. Utilizar técnicas de estatística descritiva para organizar e apresentar os resultados da avaliação.

12. Discutir, quando adequado, conceitos de inferência estatística para interpretar resultados obtidos a partir de uma amostra de usuários.

13. Documentar o desenvolvimento.

14. Entregar uma versão beta do sistema.

---

# 8. Levantamento de requisitos com futuros usuários

Essa acho que deveria ser uma das partes principais do nosso projeto.

Minha proposta é entrevistar diferentes perfis, porque cada um pode apresentar uma visão diferente do problema.

## 8.1 Enfermeiros e profissionais envolvidos no acolhimento

Queremos entender como o processo acontece na prática.

Algumas perguntas:

* Como ocorre atualmente o acolhimento?
* Quais informações precisam ser coletadas?
* Existe algum roteiro ou instrumento?
* Quanto tempo normalmente é necessário?
* Quais partes são mais trabalhosas?
* Existem perguntas que dependem de respostas anteriores?
* Existem situações em que perguntas precisam ser repetidas?
* Como as informações são registradas?
* Quais dificuldades aparecem?
* Uma ferramenta informatizada poderia ajudar?
* Quais informações deveriam aparecer na tela?
* O que tornaria o sistema mais fácil de utilizar?
* O que poderia atrapalhar?
* Quais informações deveriam aparecer ao final?
* O profissional utilizaria uma ferramenta desse tipo?

## 8.2 Gestor do CAPS

Aqui o foco seria mais institucional.

Perguntas:

* Quais são os principais desafios do acolhimento?
* Existe dificuldade de padronização?
* Existe preocupação com o tempo de atendimento?
* Quais informações são mais importantes?
* Quais seriam os benefícios da informatização?
* Quais seriam os riscos?
* Quem deveria ter acesso às informações?
* Que tipo de relatório seria útil?
* Quais seriam as principais barreiras para utilização?
* O que faria uma ferramenta desse tipo ser considerada útil?

## 8.3 Gestor de saúde

Poderíamos investigar:

* Como ocorre a informatização dos serviços?
* Quais dificuldades existem na implantação de novos sistemas?
* Quais requisitos de segurança são importantes?
* Quais profissionais poderiam utilizar a ferramenta?
* Quais seriam os obstáculos?
* Que indicadores poderiam ser úteis?
* A solução poderia futuramente ser adaptada para outros serviços?

---

# 9. Importante: não precisamos entrevistar pacientes

Minha sugestão é que o nosso usuário-alvo inicial seja o **profissional**, e não o paciente.

Isso torna o projeto mais adequado para a disciplina de Computação.

Nós queremos descobrir:

> “Como podemos construir uma ferramenta melhor para quem realiza o processo?”

e não realizar uma pesquisa clínica com pacientes.

Também não devemos utilizar dados reais identificáveis de pacientes no desenvolvimento ou nos testes.

---

# 10. Engenharia de Software aplicada ao projeto

Acho que essa é uma oportunidade importante para mostrar que o projeto não é somente programação.

Na disciplina de **Engenharia de Software**, estudamos que desenvolver software envolve várias etapas além de escrever código.

Podemos aplicar:

* levantamento de requisitos;
* análise de requisitos;
* requisitos funcionais;
* requisitos não funcionais;
* histórias de usuário;
* casos de uso;
* modelagem de processos;
* fluxogramas;
* arquitetura;
* controle de versão;
* GitHub;
* refatoração;
* testes;
* manutenção;
* documentação.

Por exemplo:

### Requisito funcional RF01

O sistema deverá apresentar as perguntas de forma estruturada.

### RF02

O sistema deverá registrar a resposta fornecida pelo profissional.

### RF03

O sistema deverá apresentar perguntas condicionais de acordo com respostas anteriores.

### RF04

O sistema deverá processar automaticamente os critérios definidos na lógica do instrumento.

### RF05

O sistema deverá permitir reiniciar a entrevista.

### RF06

O sistema deverá apresentar um resumo ao final.

Também teremos requisitos não funcionais.

### RNF01 – Usabilidade

A aplicação deverá apresentar uma interface compreensível para os profissionais.

### RNF02 – Desempenho

A aplicação deverá responder adequadamente às interações sem travamentos durante o uso.

### RNF03 – Segurança

A aplicação deverá evitar exposição desnecessária de informações pessoais.

### RNF04 – Manutenibilidade

O código deverá ser organizado de maneira que possa ser compreendido e modificado pela equipe.

---

# 11. Modelagem do sistema

Podemos construir um **diagrama de casos de uso**.

O principal ator seria:

**Profissional do CAPS**

E os principais casos de uso:

* iniciar entrevista;
* responder pergunta;
* avançar;
* retornar;
* visualizar resultado;
* reiniciar entrevista.

Também podemos construir fluxogramas.

Por exemplo:

**Início**

↓

Pergunta A1

↓

Resposta

↓

Pergunta A2

↓

**A2 é positiva?**

↓

Sim → apresentar perguntas relacionadas

Não → pular perguntas relacionadas

↓

Processamento dos critérios

↓

Resultado

↓

Fim

Isso também ajuda a resolver um dos problemas que já encontramos no código: a implementação correta das regras condicionais.

---

# 12. O que já temos e o que precisa ser melhorado

Eu já tenho um protótipo desenvolvido em **Python**, utilizando **Streamlit**, que é um framework utilizado para criar aplicações web interativas em Python.

O projeto já passou da fase inicial e já conseguimos executar algumas partes da aplicação.

Mas também identificamos problemas:

* travamentos;
* necessidade de melhorar o front-end;
* problemas de organização do código;
* necessidade de refatoração;
* problemas com componentes duplicados no Streamlit;
* necessidade de melhorar a lógica condicional;
* necessidade de incluir e organizar os módulos;
* necessidade de documentação;
* necessidade de testes.

Por exemplo, já encontramos problemas relacionados a elementos duplicados do Streamlit, que geraram erros como `StreamlitDuplicateElementId`.

Também encontramos problemas de indentação e organização do código.

Isso pode ser utilizado como parte da evolução do projeto.

Não precisamos esconder que o primeiro protótipo apresentou problemas.

Podemos mostrar:

**Protótipo inicial → problemas identificados → refatoração → testes → versão beta.**

Isso demonstra processo de desenvolvimento.

---

# 13. Modelagem Estatística

Acho que também podemos aproveitar o conteúdo de **Modelagem Estatística**.

Não precisamos transformar o aplicativo em um programa estatístico complexo.

A estatística pode entrar principalmente na **avaliação do sistema**.

Depois dos testes com usuários, podemos coletar variáveis como:

* tempo necessário para realizar determinada tarefa;
* quantidade de erros;
* quantidade de etapas realizadas;
* avaliação de facilidade de uso;
* satisfação;
* percepção de utilidade;
* intenção de utilizar a ferramenta.

Podemos utilizar **estatística descritiva**, por exemplo:

* média;
* mediana;
* frequência;
* proporção;
* desvio-padrão;
* distribuição das respostas.

Exemplo:

Se 8 profissionais avaliarem a facilidade de utilização em uma escala de 1 a 5, podemos calcular a média e a distribuição das respostas.

Isso não prova sozinho que o sistema é melhor.

Ele apenas descreve o comportamento observado na nossa amostra.

---

# 14. Inferência Estatística

Aqui podemos relacionar o projeto à disciplina de **Inferência Estatística**.

Inferência estatística é o conjunto de métodos utilizados para utilizar informações de uma **amostra** para obter conclusões sobre uma **população**, levando em consideração a incerteza.

Por exemplo:

Nossa população poderia ser:

> profissionais que potencialmente utilizariam uma ferramenta informatizada para apoiar processos de acolhimento em saúde mental.

Nossa amostra seria:

> profissionais que efetivamente participarem da avaliação do protótipo.

Se tivermos uma amostra suficiente, poderíamos discutir conceitos como:

* estimativa;
* intervalo de confiança;
* variabilidade;
* hipótese estatística;
* comparação entre grupos;
* significância estatística.

Mas precisamos ter cuidado para não exagerar na conclusão.

Se entrevistarmos poucas pessoas de um único serviço, não poderemos afirmar:

> “Os profissionais dos CAPS do Brasil aprovam o sistema.”

Podemos afirmar algo como:

> “Entre os profissionais participantes da avaliação preliminar, observou-se determinada percepção de facilidade de uso e utilidade.”

Essa diferença é justamente um exemplo de **inferência estatística e validade das conclusões**.

---

# 15. Exemplo de comparação estatística

Se conseguirmos medir o tempo necessário para realizar uma tarefa utilizando o processo convencional e depois utilizando o protótipo, poderíamos comparar os resultados.

Por exemplo:

**Método convencional**

Tempo médio = X minutos

**Protótipo**

Tempo médio = Y minutos

A diferença observada seria:

**Δ = X − Y**

Dependendo do tamanho e das características da amostra, poderíamos discutir qual método estatístico seria apropriado para avaliar essa diferença.

Não devemos escolher um teste estatístico simplesmente porque ele parece sofisticado.

Primeiro precisamos observar:

* tipo de variável;
* tamanho da amostra;
* distribuição;
* independência das observações;
* desenho do estudo;
* presença de dados pareados;
* variabilidade.

Isso conecta diretamente o projeto ao que estudamos em Modelagem e Inferência Estatística.

---

# 16. E os modelos estatísticos mais avançados que estudamos?

Também podemos utilizar o conhecimento adquirido durante o curso para interpretar os dados, mesmo que não seja necessário implementar todos esses modelos no aplicativo.

Por exemplo, estudamos modelos de regressão e modelos para diferentes tipos de variáveis.

Uma variável de interesse poderia ser:

> tempo de realização da entrevista.

Poderíamos investigar se esse tempo está associado a determinadas características do processo.

Em uma situação hipotética, poderíamos utilizar uma regressão linear se a variável resposta e as condições do modelo fossem adequadas.

Também estudamos modelos para dados de contagem, como a **regressão de Poisson**.

Isso poderia ser conceitualmente relacionado a variáveis como:

> número de erros durante a utilização;

> número de interrupções;

> número de perguntas necessárias;

> número de eventos observados.

Mas, novamente, não devemos colocar Poisson ou regressão no projeto apenas para dizer que usamos estatística.

A escolha do modelo deve depender do tipo de variável e das características dos dados.

Também estudamos o conceito de **superdispersão** em modelos de Poisson. Isso pode ser relevante se estivermos trabalhando com dados de contagem cuja variabilidade seja maior do que aquela assumida pelo modelo de Poisson.

Portanto, podemos demonstrar que sabemos não apenas “calcular uma média”, mas também escolher e avaliar modelos estatísticos de acordo com os dados.

---

# 17. Testes de software

Também quero aproveitar o que estudamos em Engenharia de Software.

Podemos construir uma matriz de testes.

| Teste | Entrada                   | Resultado esperado                 |
| ----- | ------------------------- | ---------------------------------- |
| T01   | Resposta negativa A1      | Fluxo segue corretamente           |
| T02   | A2 positiva               | Perguntas condicionais aparecem    |
| T03   | A2 negativa               | Perguntas condicionais são puladas |
| T04   | Todas respostas negativas | Resultado correspondente           |
| T05   | Reiniciar entrevista      | Dados anteriores são removidos     |
| T06   | Navegação                 | Sistema não trava                  |
| T07   | Resposta incompleta       | Sistema controla avanço            |
| T08   | Fluxo completo            | Resultado final apresentado        |

Assim podemos demonstrar **testes funcionais**, além de testes específicos da lógica.

---

# 18. Teste de usabilidade

Depois que tivermos uma versão mais estável, podemos apresentar a aplicação aos potenciais usuários.

Podemos propor uma tarefa:

> “Imagine que você está realizando o acolhimento de um usuário. Utilize o protótipo para percorrer o processo.”

Depois coletamos a percepção do profissional.

Perguntas:

* Foi fácil entender o que fazer?
* A sequência das perguntas foi clara?
* A interface ficou fácil de utilizar?
* Alguma parte gerou confusão?
* O sistema poderia economizar tempo?
* Faltou alguma informação?
* O resultado apresentado foi compreensível?
* O que você mudaria?
* Você utilizaria uma ferramenta assim?
* De 1 a 5, qual a facilidade de utilização?

Essas respostas poderão ser analisadas estatisticamente.

---

# 19. Divisão das tarefas para oito integrantes

Como somos oito pessoas, acho que podemos dividir o projeto por áreas, mas mantendo a responsabilidade coletiva.

## Integrante 1 – Coordenação e domínio do problema

Eu posso ficar responsável por:

* conhecimento do domínio;
* acompanhamento do funcionamento do M.I.N.I.;
* levantamento inicial do processo;
* contato com profissionais do CAPS;
* desenvolvimento da lógica clínica do protótipo;
* integração entre as áreas.

## Integrante 2 – Engenharia de Software

Responsável por:

* requisitos;
* requisitos funcionais;
* requisitos não funcionais;
* histórias de usuário;
* casos de uso;
* documentação técnica.

## Integrante 3 – Modelagem do sistema

Responsável por:

* fluxogramas;
* diagramas;
* arquitetura;
* modelagem dos processos;
* documentação da estrutura do sistema.

## Integrante 4 – Desenvolvimento

Responsável por:

* Python;
* Streamlit;
* implementação;
* refatoração;
* integração das funções;
* correção de bugs.

## Integrante 5 – Interface e UX/UI

Responsável por:

* front-end;
* organização das telas;
* navegação;
* usabilidade;
* experiência do usuário;
* avaliação visual.

## Integrante 6 – Testes e qualidade

Responsável por:

* casos de teste;
* testes funcionais;
* testes da lógica condicional;
* registro de bugs;
* validação das correções;
* controle da qualidade.

## Integrante 7 – Estatística

Responsável por:

* planejamento da coleta;
* definição das variáveis;
* estatística descritiva;
* organização dos dados;
* análise dos resultados;
* discussão de possíveis métodos inferenciais.

## Integrante 8 – Pesquisa e documentação

Responsável por:

* fundamentação teórica;
* referências;
* metodologia;
* documentação das entrevistas;
* organização do relatório;
* revisão da apresentação.

Mas acho importante que isso seja uma divisão de **responsabilidade principal**, não de trabalho isolado.

Todos participam das decisões e todos revisam o resultado final.

---

# 20. Organização do GitHub

Eu sugiro que o repositório principal seja o que decidirmos utilizar como projeto oficial.

O meu repositório antigo “mini psiquiatria” pode ficar como referência do desenvolvimento inicial.

A versão oficial poderia ter uma estrutura semelhante a:

```text
MINI-TRIAGEM-CAPS/
│
├── app/
│   ├── mini_app.py
│   ├── perguntas.py
│   ├── regras.py
│   ├── funcoes.py
│   └── resultados.py
│
├── docs/
│   ├── requisitos.md
│   ├── arquitetura.md
│   ├── testes.md
│   └── entrevistas.md
│
├── tests/
│   ├── test_fluxo.py
│   └── test_regras.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

Podemos utilizar branches para organizar o desenvolvimento:

```text
main
│
├── desenvolvimento
├── feature/interface
├── feature/logica
└── feature/testes
```

Assim também conseguimos demonstrar utilização de controle de versão e desenvolvimento colaborativo.

---

# 21. Estrutura do relatório exigido pela universidade

Podemos adaptar exatamente ao modelo apresentado.

## 1 Introdução

Apresentação do problema, contexto do CAPS, entrevistas estruturadas e proposta da aplicação.

## 2 Desenvolvimento

### 2.1 Objetivos

Objetivo geral e objetivos específicos.

### 2.2 Justificativa e delimitação do problema

Problema identificado, tabelas 1 e 2, público-alvo, justificativa e limites do projeto.

### 2.3 Fundamentação teórica

Podemos abordar:

* saúde mental;
* acolhimento;
* entrevistas estruturadas;
* M.I.N.I.;
* sistemas de informação;
* Engenharia de Software;
* requisitos;
* modelagem;
* UX/UI;
* testes;
* estatística descritiva;
* modelagem estatística;
* inferência estatística;
* segurança e proteção de dados.

### 2.4 Metodologia

A metodologia pode seguir:

**Identificação do problema**

↓

**Pesquisa bibliográfica**

↓

**Entrevistas**

↓

**Levantamento de requisitos**

↓

**Modelagem**

↓

**Desenvolvimento**

↓

**Testes**

↓

**Avaliação de usabilidade**

↓

**Correções**

↓

**Versão beta**

### 2.5 Resultados preliminares: solução inicial

Aqui apresentaremos:

* protótipo inicial;
* evolução do código;
* telas;
* fluxogramas;
* requisitos;
* testes;
* problemas encontrados;
* correções;
* resultados das entrevistas;
* avaliação dos usuários;
* análise estatística;
* versão beta.

### Referências

Fontes utilizadas na fundamentação teórica.

### Anexos

Documentos externos relevantes, quando necessários.

### Apêndices

Podemos colocar materiais produzidos pelo próprio grupo, como:

* roteiro de entrevista;
* questionário de avaliação;
* casos de teste;
* tabelas;
* documentação complementar.

---

# 22. Cronograma proposto

| Período     | Atividade                  | Produto                       |
| ----------- | -------------------------- | ----------------------------- |
| 23–30/08    | Definição do projeto       | Tema, problema e objetivos    |
| Até 06/09   | Plano de ação              | Plano entregue                |
| 07–13/09    | Pesquisa bibliográfica     | Referências                   |
| 07–20/09    | Entrevistas                | Dados dos potenciais usuários |
| 14–21/09    | Levantamento de requisitos | RF e RNF                      |
| 21–28/09    | Modelagem                  | Fluxogramas e casos de uso    |
| 21/09–12/10 | Desenvolvimento            | Nova versão                   |
| 05–19/10    | Testes                     | Casos de teste                |
| 12–26/10    | Avaliação com usuários     | Feedback                      |
| 26/10–09/11 | Correções                  | Versão beta                   |
| 09–16/11    | Documentação               | Relatório                     |
| 16–23/11    | Revisão                    | Versão final                  |
| Final       | Apresentação               | Demonstração                  |

As datas precisam ser ajustadas ao cronograma oficial disponibilizado no AVA.

---

# 23. O que precisamos fazer primeiro

Minha sugestão é não começarmos simplesmente mexendo no código.

Eu faria primeiro:

### Ação 1

Definir o nome e o escopo do projeto.

### Ação 2

Definir o problema.

### Ação 3

Definir objetivo geral e objetivos específicos.

### Ação 4

Dividir as oito responsabilidades.

### Ação 5

Montar o roteiro das entrevistas.

### Ação 6

Conversar com o CAPS para identificar profissionais que possam participar do levantamento de requisitos.

### Ação 7

Verificar quais autorizações institucionais são necessárias.

### Ação 8

Mapear os requisitos.

### Ação 9

Organizar o GitHub.

### Ação 10

Só então iniciar a nova versão do código.

---

# 24. O que eu acho que pode ser o diferencial do nosso projeto

Acho que nosso diferencial é justamente não apresentar:

> “Nós fizemos um aplicativo.”

Podemos apresentar:

> **“Nós identificamos um problema, investigamos as necessidades dos usuários, levantamos requisitos, modelamos uma solução computacional, desenvolvemos um protótipo, realizamos testes, coletamos dados, analisamos os resultados e evoluímos o sistema para uma versão beta.”**

Isso permite integrar várias disciplinas.

**Engenharia de Software** responde:

> Como devemos desenvolver e testar o sistema?

**Modelagem Estatística** responde:

> Como podemos organizar e analisar os dados obtidos?

**Inferência Estatística** responde:

> Até onde podemos generalizar os resultados obtidos a partir da nossa amostra?

**Programação** responde:

> Como transformar os requisitos e a lógica definida em uma aplicação funcional?

**UX/UI** responde:

> Como tornar o sistema compreensível e adequado ao usuário?

**Levantamento de requisitos** responde:

> O que os usuários realmente precisam?

E o conhecimento sobre saúde mental fornece o **domínio do problema**.

---

# 25. Delimitação importante

Eu proporia que oficialmente nosso projeto termine na:

**VERSÃO BETA**

e não na implantação definitiva.

O objetivo não será afirmar que o sistema está pronto para substituir processos clínicos ou ser utilizado autonomamente em um serviço de saúde.

O objetivo será demonstrar que conseguimos:

1. identificar um problema;
2. entender as necessidades dos usuários;
3. transformar essas necessidades em requisitos;
4. desenvolver uma solução;
5. testar a solução;
6. avaliar preliminarmente sua usabilidade;
7. analisar os resultados;
8. corrigir os problemas identificados;
9. entregar uma versão beta documentada.

---

# 26. Resumindo a proposta para o grupo

Então, minha proposta seria a gente pegar o projeto que eu já comecei, mas **não simplesmente entregar aquele código**.

A gente usa ele como ponto de partida.

A partir daí fazemos o projeto de verdade:

**problema real no CAPS**

→ **entrevistas com profissionais e gestores**

→ **levantamento de requisitos**

→ **Engenharia de Software**

→ **modelagem do sistema**

→ **desenvolvimento**

→ **testes**

→ **coleta de dados**

→ **estatística descritiva**

→ **discussão de inferência estatística quando os dados permitirem**

→ **avaliação de usabilidade**

→ **melhorias**

→ **versão beta**

→ **documentação para o Projeto Integrador**.

Acho que dessa forma o trabalho fica bem mais completo e conseguimos mostrar que estamos aplicando conteúdos de várias disciplinas do curso, e não somente programando.

E, principalmente, conseguimos partir de um problema real e de usuários reais, mas mantendo o escopo possível para o semestre e sem assumir uma implantação clínica definitiva.
