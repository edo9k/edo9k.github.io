**Título:** Modelagem de Banco de Dados para Sistema de Agendamento de Salas de Aula

**Descrição do Problema:**

Você foi designado para desenvolver a modelagem de banco de dados para um sistema de agendamento de salas de aula em uma instituição de ensino. O sistema tem o propósito de facilitar a gestão eficaz das reservas de salas, evitando conflitos de agendamento e permitindo o acesso às informações necessárias.

**Requisitos de Banco de Dados:**

1. **Informações dos Usuários:** O sistema precisa armazenar as informações dos usuários, incluindo ID do usuário, nome, endereço de e-mail e nível de permissão. O nível de permissão determinará quais ações um usuário pode realizar.

2. **Registros de Salas:** É necessário registrar as informações das salas de aula, como ID da sala, número da sala, capacidade máxima de alunos e recursos disponíveis.

3. **Reservas de Salas:** O sistema deve permitir que um usuário reserve uma ou várias salas de aula. Uma reserva inclui detalhes como ID da reserva, ID do usuário que fez a reserva, ID da(s) sala(s) reservada(s), data, horário de início e horário de término da reserva.

4. **Validação de Conflitos:** Uma sala não pode ser reservada por mais de um usuário no mesmo horário. Portanto, o banco de dados deve ser capaz de verificar se uma sala já está reservada para determinado horário.

5. **Histórico de Reservas:** Pense em como o banco de dados pode manter um histórico das reservas anteriores, incluindo os detalhes das reservas passadas.

6. **Notificações:** Considere como o sistema poderia registrar o envio de notificações aos usuários sobre suas reservas, incluindo a data e hora em que a notificação foi enviada.

7. **Relacionamentos:** Estabeleça os relacionamentos apropriados entre as entidades (tabelas) do banco de dados. Lembre-se de que um usuário pode fazer várias reservas, mas uma reserva está associada a um usuário e a uma ou várias salas.

8. **Flexibilidade:** A modelagem deve ser flexível o suficiente para acomodar futuras atualizações, como novos tipos de eventos, recursos adicionais para as salas, etc.

**Instruções:**

Com base nos requisitos acima, projete a estrutura do banco de dados, identificando as entidades, atributos e relacionamentos necessários para atender aos requisitos. Certifique-se de que a estrutura seja coesa, eficiente e capaz de lidar com os desafios de agendamento e gerenciamento de salas de aula.
