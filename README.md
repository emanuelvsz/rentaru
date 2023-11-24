# rentaru

### Requisitos

-  if/else e/ou swicth/elif (1,0 ponto)
- while/do..while e/ou for (1,0 ponto)
- subprogramas (1,0 ponto)
- matrizes/listas (1,0 ponto)
- cadeia de caracteres/string (1,0 ponto)
- estruturas(registros/dicionários/tuplas) (1,0 ponto)
- arquivos (1,0)


### Quais foram as demandas encontradas no estabelecimento para o projeto? 

Em uma locadora de filmes, identificamos os seguintes problemas:

- Dificuldade de gerir os filmes locados por clientes
- Falta de um local para identificar os filmes já locados e os disponíveis
- Dificuldade para gerir os dados dos filmes e clientes.

### Quais foram os objetivos traçados para o seu projeto?
   
* Criar um sistema que cadastre, leia, atualize e exclua filmes e clientes (CRUD).
Cadastro de locações de filmes

### Quais os requisitos desenvolvidos para o seu projeto? 
* ``Python``
* ``Django Framework``(Framework para Python)
* ``Docker`` (Gerenciador de containers)
* ``Postgres``(Banco de dados)

### O que foi atendido pelo seu projeto? 
- Com o projeto, os problemas citados acima foram solucionados. Além disso, o sistema ajudou a automatizar o processo de cadastro de filmes. Por tanto, ajudou a melhorar o processo de cadastro e locação de filmes.

### Quais e onde foram utilizadas as estruturas no código?
* ``Estruturas de decisão(IF):`` No sistema, algumas validações para as queries(consultas no banco) foram feitas utilizando tais estruturas.
* ``Estruturas de repetição(For, While e etc.):`` Também, no sistema há algumas funcionalidades de listagem de vários itens, sendo possível tratar e percorrer  um por um. 
* ``Funções/Subprogramas:`` Em todos os endpoints(caminhos de URL) são criados métodos para listagem de itens. Esse processo, é feito através de três camadas: views, selectors e serviços.
* ``Matrizes/Listas:`` Para listagens de filmes ou clientes existentes do banco de dados.
* ``Cadeias de caracteres:`` Utilizado como nomes de clientes, filmes e descrições.
* ``Estruturas:`` Utilizados para listar filmes e clientes
* ``Arquivos:`` Criamos vários arquivos para subdividir o código e suas responsabilidades
