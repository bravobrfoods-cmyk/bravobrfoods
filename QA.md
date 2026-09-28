# Validação da entrega

Revisão local em 28/09/2026, no navegador Chromium integrado, com servidor Node em `127.0.0.1:4173`.

## Verificações concluídas

- Sintaxe de JavaScript e servidor, estrutura das três páginas, um H1 por página, IDs únicos, âncoras, arquivos referenciados, dimensões e textos alternativos das imagens, JSON-LD e destinos ARIA.
- Layouts em 320, 390, 768, 1024 e 1440 px: sem transbordamento horizontal da página. Revisão visual de Hero, método, serviços, cardápio, cases, detalhes, automação e contato em tamanhos representativos.
- Menu móvel, fechamento após navegação, tabs e navegação por teclado, matriz de cardápio, fluxo ilustrativo de atendimento, seleção dos quatro cases, detalhes em diálogo, fechamento por Escape e botão, e alternância dos três depoimentos.
- Vídeo local reproduzido e pausado pelo controle. Poster e ausência de autoplay respeitam a preferência de movimento reduzido ativa no ambiente. Versão H.264 sem áudio de aproximadamente 1,25 MiB; fontes WOFF2 totalizam aproximadamente 70 KiB.
- URLs do WhatsApp com número e mensagem corretos, e-mail e Instagram conferidos no DOM. Nenhuma mensagem enviada durante os testes.
- Apresentação institucional desabilitada, sem arquivo inexistente ou link quebrado.
- Página de privacidade, retorno da página 404, HTTP 404 em endereço inexistente, bloqueio de arquivos internos e resposta 206 para carregamento parcial do vídeo.
- Auditoria HTTP de 26 URLs de páginas e recursos: respostas válidas. Nenhum erro ou aviso de console observado durante os testes da página principal.
- Cores principais verificadas: branco sobre vermelho institucional 4,54:1; texto institucional sobre fundo claro 10,27:1. Pequenos textos vermelhos sobre creme usam variante mais escura.
- Canonical, Open Graph, dados estruturados, robots e sitemap usam o domínio informado. Não há avaliações numéricas ou resultados inventados.

## Limites da validação

Os tamanhos de tela foram emulados; não houve teste em aparelhos físicos, Safari ou leitor de tela. O swipe está implementado com Pointer Events e alternativa por botões, mas o gesto não foi validado em hardware touch. O ambiente estava com movimento reduzido ativo; a reprodução explícita foi validada, enquanto a política de autoplay normal e economia de dados foi revisada no código.

Não foram atribuídas notas Lighthouse nem resultados reais de Core Web Vitals. Esses indicadores e respostas HTTP de produção devem ser medidos após configurar a hospedagem. Publicação, DNS e certificado do domínio não são configurados pelo push ao GitHub.
