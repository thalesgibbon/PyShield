# PySHIELD

O PySHIELD é uma extensão para aplicativos de mapas com foco no problema de segurança urbana de pedestres. 

## Descrição

Dado um conjunto de ruas pertencente à um trajeto, tem como objetivo usar as bases públicas de Boletins de Ocorrência para classificar a periculosidade do trajeto a ser percorrido, seguindo um método análogo ao que é realizado com informaões de trânsito. Seu funcionamento se dá de tal maneira:

  - Input do usuário para o trajeto a ser realizado;
  - Consulta na API do GoogleMaps das ruas pertencentes ao trajeto a ser percorrido;
  - Consulta das quantidades de Boletins de Ocorrência para as ruas retornadas pela API do GoogleMaps;
  - Classificação do trajeto conforme quantida de Boletins de Ocorrência;
 
## Construido com:

O PySHIELD foi construído com as bibliotecas:

* [Python 3.5+] - Processamento dos base de dados de Ocorrência e geração da nota de Classificação de trajetos.
* [Django Framework 2.0+] - API de integração com a base de Boletins de Ocorrência!

## Instalação

Clonar diretamente do repositório no GitHub.

Processamento dos dados públicos:
```sh
$ git clone https://github.com/thalesgibbon/PyShield
```

Comunicação com os app de mapa:
```sh
$ git clone https://github.com/thalesgibbon/PyShield_api
```

## Contribuidores

| Nome | GitHub 
|---|---|
| Bruno Leme | @brunoleme |
| Julio Henrique  | @juliohds  |
| Kleber Alves |  @kl3ber |
| Victor Paulillo | @thalesgibbon |
| Thales Gibbon | @victorpaulillo |

## To Do

 - Prospecção de novas bases de dados para consulta de ocorrências e características sobre as ruas do trajeto selecionado;
 - Incluir ocorrências para automóveis e transportes publicos e bicicletas.

## Licença

Livre

