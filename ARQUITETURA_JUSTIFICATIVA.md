# 📊 JUSTIFICATIVA DE ARQUITETURA - FLASHSCORE

## Padrão MVC (Model-View-Controller) e Camadas (Layers)

Este documento apresenta a justificativa arquitetural do projeto LigaScore, demonstrando como a implementação cumpre rigorosamente os requisitos de padrões MVC e Camadas para o projeto acadêmico de Arquitetura de Software.

---

## PARÁGRAFO 1: Implementação do MVC

A arquitetura da plataforma LigaScore segue fielmente o padrão MVC, com separação clara e física das três responsabilidades fundamentais. A camada **Model** é implementada em `app/models/team.py` como uma entidade de domínio que encapsula os dados e as propriedades calculadas de um time (pontos, saldo de gols, diferença de gols), representando a estrutura do negócio sem conhecer detalhes de persistência ou apresentação. A camada **View** é materializada no front-end em `frontend/public/index.html`, um cliente web que renderiza a interface gráfica através de HTML5 semântico e CSS3 responsivo, consumindo dados apenas através de requisições REST sem contato direto com a lógica de negócio. A camada **Controller** é implementada nas rotas REST em `app/routes/teams.py`, que expõem endpoints HTTP que recebem requisições do front-end, delegam o processamento para a camada de Serviço (LeagueService), e retornam as respostas em JSON. Essa separação permite que cada componente evolua independentemente: o Model pode ser reutilizado por diferentes tipos de Views (web, mobile, desktop) ou Controllers, o View pode ser completamente reescrito sem afetar a lógica de negócio, e o Controller pode ser substituído por outras tecnologias REST sem quebrar o contrato com o front-end.

---

## PARÁGRAFO 2: Implementação da Arquitetura em Camadas (Layers)

Além do MVC, o projeto implementa explicitamente a arquitetura em Camadas (Layers) com **4 camadas distintas** que garantem isolamento de responsabilidades e facilitam manutenção e testes. A **Camada de Domínio** contém os Modelos (`app/models/team.py`) com as entidades e regras de negócio inerentes, como o cálculo de pontos (vitória=3, empate=1, derrota=0) e saldo de gols. A **Camada de Serviço** (`app/services/league_service.py`) encapsula toda a lógica de negócio complexa, implementando o algoritmo de ordenação da tabela (por pontos, saldo de gols, gols a favor) e a lógica de registro de partidas, garantindo que nenhuma regra do domínio seja violada; esta camada comunica-se apenas através de interfaces de Repository, não conhecendo implementações de banco de dados. A **Camada de Acesso a Dados** (`app/database/team_repository.py`) abstrai completamente a persistência através do padrão Repository, permitindo trocar de SQLite para PostgreSQL ou MongoDB sem alterar o código de Services; ela executa as operações CRUD (Create, Read, Update) e transações com o banco. A **Camada de Apresentação** (`app/routes/teams.py` e `frontend/`) expõe a aplicação ao usuário através de HTTP REST e HTML/CSS/JS, validando entrada (Pydantic models) e transformando dados do domínio em DTOs (Data Transfer Objects) apropriados; esta camada é a mais "suja", lidando com detalhes técnicos como headers HTTP, serialização JSON e CORS, mantendo as camadas internas limpas e agnósticas em relação ao protocolo de comunicação.

---

## PARÁGRAFO 3: Benefícios da Arquitetura Escolhida

A implementação rigorosa de MVC e Camadas traz benefícios concretos ao projeto que atendem aos critérios acadêmicos e empresariais de qualidade. Primeiro, **testabilidade**: cada camada pode ser testada isoladamente (testes unitários do Model e Service sem dependência do banco; testes de integração do Repository; testes E2E do Controller e View) porque as dependências fluem de forma unidirecional (de fora para dentro), permitindo injeção de mocks e fakes. Segundo, **manutenibilidade**: quando surgir requisito de mudar o cálculo de pontos do campeonato, a alteração é feita apenas em `league_service.py` e se propaga automaticamente para todas as Views (web, mobile, etc.) porque as Views não contêm lógica; se o banco de dados precisar ser migrado, apenas `team_repository.py` muda, sem afetar Services ou Controllers. Terceiro, **escalabilidade e deploy em nuvem**: a separação física entre front-end e back-end permite que cada um escale independentemente (back-end no Railway em container, front-end estático na Vercel); o front-end pode ser cacheado em CDN global enquanto o back-end concentra-se em performance computacional. Quarto, **conformidade acadêmica**: o projeto demonstra domínio de conceitos sólidos de Engenharia de Software, com código que serve como referência didática para princípios SOLID (Single Responsibility em cada classe, Dependency Inversion através de Repositories, Open/Closed em Services), padrões de Design (Repository, Service Locator, DTO) e arquitetura em Camadas que é amplamente utilizada em produção em empresas de tecnologia globais.

---

## Diagrama Visual da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                     CAMADA DE APRESENTAÇÃO                       │
│  ┌──────────────────┐                    ┌──────────────────┐    │
│  │   FRONT-END      │                    │  BACK-END        │    │
│  │  (HTML/CSS/JS)   │  ◄──────────────►  │  (Routes REST)   │    │
│  │  MVC - View      │    JSON via HTTP   │  MVC - Controller│    │
│  └──────────────────┘                    └──────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ API REST
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CAMADA DE SERVIÇO (Business Logic)            │
│                                                                   │
│           LeagueService (Regras do Campeonato)                  │
│  • get_league_standings() - ordena por pontos/SG/GF            │
│  • record_match() - registra partida e calcula novo estado    │
│  • get_team_statistics() - calcula médias e percentuais       │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              CAMADA DE ACESSO A DADOS (Repository)               │
│                                                                   │
│    TeamRepository (Abstração de Persistência)                  │
│  • get_all_teams()  - lê do banco                              │
│  • update_team()    - persiste alterações                       │
│  • create_team()    - insere novo time                          │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  CAMADA DE DOMÍNIO (Models)                      │
│                                                                   │
│      Team (Entidade com Propriedades Calculadas)               │
│  • points = wins*3 + draws*1                                   │
│  • goal_difference = goals_for - goals_against                 │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  CAMADA DE PERSISTÊNCIA                           │
│                                                                   │
│             SQLite (ligascore.db)                              │
│        Tabela: teams (id, name, wins, draws, ...)             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Checklist de Conformidade Acadêmica

- ✅ **MVC Completo**: Model (`team.py`), View (HTML/CSS/JS), Controller (routes REST)
- ✅ **Camadas Isoladas**: Domínio → Serviço → Repositório → Apresentação
- ✅ **REST API**: Endpoints HTTP com métodos corretos (GET, POST)
- ✅ **Front/Back Desacoplados**: Comunicação apenas via JSON over HTTP
- ✅ **Inversão de Controle**: Services não conhecem Repository concreto
- ✅ **Princípio da Responsabilidade Única**: Cada classe tem uma razão para mudar
- ✅ **Padrão Repository**: Abstração de persistência
- ✅ **Padrão Service**: Lógica de negócio centralizada
- ✅ **Cloud-Ready**: Procfile + requirements.txt para Railway, vercel.json para Vercel
- ✅ **Dados Mock**: 6 times fictícios pré-carregados

---

## Como Apresentar na Defesa

1. **Abra a estrutura de pastas** no VS Code e aponte cada camada
2. **Mostre um modelo**: `app/models/team.py` → propriedades calculadas
3. **Mostre o service**: `app/services/league_service.py` → lógica de negócio
4. **Mostre o repository**: `app/database/team_repository.py` → isolamento de dados
5. **Mostre as rotas**: `app/routes/teams.py` → delegation pattern
6. **Rode a aplicação**: `python -m uvicorn app.main:app --reload`
7. **Abra o front-end**: Mostre a tabela sendo preenchida da API
8. **Registre uma partida**: Demonstre o cálculo de pontos em tempo real
9. **Conclua**: "Este projeto implementa padrões de produção usado em empresas como Airbnb, Uber, Netflix"

---

## Recursos para Estudo

- Clean Architecture - Robert C. Martin
- Domain-Driven Design - Eric Evans
- Designing Data-Intensive Applications - Martin Kleppmann
- FastAPI Documentation: https://fastapi.tiangolo.com
- Repository Pattern: https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design

---

**Gerado automaticamente para LigaScore**  
*Projeto Acadêmico de Arquitetura de Software* © 2024
