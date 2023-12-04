# MoneyFlow
Money transfering project using Vue.js with TypeScript and Django
Este projeto tem como objetivo viabilizar a transferência entre carteiras. Existem 2 tipos de usuários: os comuns, e os lojistas. Os lojistas podem apenas receber transferências, enquanto os comuns podem receber e transferir entre si e para os lojistas.
Haverá a tela de cadastro do usuário, de login, e a tela principal, que variará de acordo com o usuário logado.
A transferência só poderá ser realizada se o usuário tiver saldo suficiente para isso, e é necessário que um mock externo seja utilizado para simular uma notificação de que a operação foi bem sucedida.
##
Como rodar o projeto:
Backend:
1- Clone este repositório (git clone https://github.com/ErickGrCosta/MoneyFlow.git).
2- Navegue até o diretório do backend (cd nome-do-repositorio/backend-django).
3- Crie um ambiente virtual e ative-o.
4- Instale as dependências do python contidas no requirements.txt.
5- Configure o banco de dados no arquivo settings.py, que está em SQLite. Ou seja, execute as migrações.
6- Inicie o servidor.
Frontend: 
1- Navegue até o diretório do frontend (cd nome-do-repositorio/money-transaction-vue).
2- Instale as dependências do node dando um npm i.
3- Inicie o servidor de desenvolvimento.
##
