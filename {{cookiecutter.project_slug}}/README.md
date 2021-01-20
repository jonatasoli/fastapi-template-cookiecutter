## Definições

- ext.database fica as configs do banco
- endpoints fica as rotas
- services ficam as regras de negócio
- dao ficam as queries
- models ficam os modelos de dados
- schemas ficam os schemas do pydantic

## Development

Para manter um código limpo, devemos instalar o pre-commit hook. Execute os seguintes comandos na raiz do projeto:

::

    $ chmod +x pre-commit.sh

    $ ln -s ../../pre-commit.sh .git/hooks/pre-commit
