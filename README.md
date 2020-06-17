# Filmes Favoritos

Utilizando Flask, um banco de dados de característica reacional foi montado.

Em app.py tanto a aplicação quanto o banco são instanciados.

No arquivo models.py encontra-se o modelo do banco. São duas tabelas, sendo uma as informações do usuário como nome, email e senha e outra as informações dos filmes. Vale destacar que as senhas do usuário vão para o banco já encriptadas.

Como um usuário pode ver vários filmes e um filme pode ser visto por mais de um usuário, as tabelas são relacionadas por meio da uma outra tabela, chamada 'favorite'.
