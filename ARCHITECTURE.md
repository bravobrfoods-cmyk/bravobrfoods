# Arquitetura editorial e técnica

## Redistribuição do conteúdo aprovado

| Conteúdo original                                           | Destino e adaptação                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Posicionamento além do marketing                            | Consultoria: visão transversal, oferta e canais em lugar de cardápio e delivery       |
| Método de cinco etapas                                      | Consultoria: metodologia central e links a partir das duas verticais                  |
| Soluções comerciais, marketing, gestão e tecnologia         | Consultoria: visão integrada; Empresarial: aplicação ao comércio e serviços           |
| Engenharia de cardápio e matriz popularidade/rentabilidade  | Foods, com fotografia e interação preservadas                                         |
| Delivery, marketplaces e operação de cozinha                | Foods, aprofundamento gastronômico                                                    |
| Presença local, site e Google Business                      | Empresarial, com nova jornada descoberta → confiança → atendimento → relacionamento   |
| Rosendo/Jambalaya                                           | Foods como case editorial dedicado; também presente na visão completa da Consultoria  |
| Farmácia Mogi Guaçu, WS Rocha Manutenção, Chaveiro WS Rocha | Empresarial e Consultoria, sem atribuir a restaurantes resultados de outros segmentos |
| Depoimentos                                                 | Consultoria, textos intactos e contexto histórico da Foods                            |
| Sobre, experiência e apresentação institucional futura      | Consultoria; as verticais explicam sua relação com a marca principal                  |
| Contato e privacidade                                       | Unificados sob a Bravo BR Consultoria                                                 |

## DNA compartilhado

Barlow Condensed, DM Sans e itálicos editoriais; vermelho institucional, azul/cinza, fundos claros; hero com vídeo local; hierarquia tipográfica forte; alternância de composições; indicadores e controles reais. Nenhuma logo foi redesenhada. Cabeçalhos e rodapés claros permitem usar as marcas transparentes sem quadrados de fundo.

A Foods mantém calor gastronômico, fotografia, matriz de cardápio e visão operacional. A Empresarial usa neutros frios, uma jornada comercial editorial e cases de varejo/serviços. A Consultoria reúne as especializações em uma entrada institucional própria.

## Componentes e interações

- Navegação global entre marcas e navegação interna por página, com estado ativo e menu móvel.
- Vídeo sem áudio e com poster, controle de reprodução, pausa fora da tela e respeito à preferência de movimento reduzido.
- Tabs de serviços e método com setas, Home/End, foco e painéis associados.
- Mapa de estratégia, matriz de cardápio, acordeões nativos e demonstração de atendimento.
- Cases com IDs estáveis: cada página seleciona os cases apropriados sem duplicar seus dados no JavaScript.
- Diálogo nativo de detalhes com fechamento por Escape e restauração do foco.
- Carrosséis manuais com botões e suporte adicional a swipe.
- Layouts responsivos, fontes locais e mídia otimizada compartilhada.

Os arquivos HTML na raiz são as fontes de cada página. Um único `styles.css`, um único `app.js` e a mesma biblioteca de assets sustentam o ecossistema. O código anterior permanece no histórico Git.
