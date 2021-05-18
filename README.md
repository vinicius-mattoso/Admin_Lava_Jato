![Welcome](/lava_jato_admin.png?raw=true)

# Projeto feito no Django para administração de um Lava-Jato


PROJETO :point_right: <https://github.com/vinicius-mattoso/Admin_Lava_Jato>

Contato do Autor: [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-mattoso/)](https://www.linkedin.com/in/vinicius-mattoso/)[![Gmail Badge](https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:vinicius.vmrs@gmail.com)](mailto:vinicius.vmrs@gmail.com)

:construction: :warning: :construction:
Projeto ainda se encontra em fase de atualizações
aberto a quaisquer feedback e comentários
:construction: :warning: :construction:

# ***Objetivo*** :dart:
  O Objetivo desse projeto não é nenhuma recomendação de investimento, é apenas para ajudar o investidor a análisar os fundos imobiliários segundo algumas métricas adotadas pelo autor mas que podem ser facilmente alteradas de acordo com a vontade do usuário.

# ***Etapas*** :memo:

1. Web Scraping do ranking do site: https://www.fundsexplorer.com.br/ranking

2. Tratamento dos dados, object --> float

3. Segmentação pelo tipo de fundo

4. Criação dos seguintes filtros:

  - Fundos com valores patrimoniais acima de 1 Milhão; 
  - Fundos com valores P/VPA abaixo de 1.15;  
  - Fundos que possuem ativos físicos, precisam ter pelo menos 5 empreendimentos;  
  - Criação de uma nova coluna (DELTA), contendo o delta entre o preço atual e o VPA.

5. Aplicar um filtro limitando o DELTA a valores menores que 10 reais.

6. Fazer uma ordenação dos fundos com base no ['DY(12M)_ACUMULADO' , 'DIVIDEND_YIELD']

7. Analisar os 5 primeiros fundos de cada tipo e fazer uma análise mais detalhada

## **Atualizações** :memo:

- [ ] Ajuste dos parâmetros utilizados no filtro já existente; :construction: :warning: :construction:
- [ ] Criação de novos filtros; :construction: :warning: :construction:
- [x] Utilizar o Yahoo Finanças para buscar o histórico dos fundos escolhidos; ✅
- [ ] Fazer um pipeline dos filtros; :construction: :warning: :construction:
- [ ] Fazer uma análise gráfica do efeitos dos filtros; :construction: :warning: :construction:
