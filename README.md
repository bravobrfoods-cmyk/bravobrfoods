# Bravo BR Foods

Site oficial da Bravo BR Foods. Fontes diretamente na raiz, sem compilação, dependências de produção ou pasta de saída.

## Prévia e validação

- `npm run dev` — abre servidor local em `http://127.0.0.1:4173`.
- `npm run check` — valida sintaxe, assets, links internos, estrutura e orçamento do vídeo.
- Também pode ser servido por qualquer hospedagem de arquivos estáticos.

## Arquivos

- `index.html`: conteúdo e metadados da página principal.
- `styles.css`: identidade visual, componentes, responsividade e movimento reduzido.
- `app.js`: navegação, vídeo adaptativo, tabs, cases, depoimentos e modal.
- `privacidade.html`, `404.html`, `robots.txt`, `sitemap.xml`: páginas de apoio e SEO.
- `assets/imgs`, `assets/videos`: originais fornecidos, preservados.
- `assets/web`: versões otimizadas usadas no site, sem modificar os originais.
- O arquivo bruto de clientes em `assets/imgs/Clientes` é preservado localmente e ignorado no Git: inclui cerca de 600 MB de vídeos, fotos de alta resolução, PDFs de impressão e ZIPs. Todas as mídias utilizadas no site estão versionadas em `assets/web`; o site funciona integralmente após clonar o repositório.
- `assets/fonts`: fontes locais e licenças OFL.

## Publicação

Domínio informado: `https://bravobrconsultoria.com.br`. Publicar `index.html`, `styles.css`, `app.js`, `privacidade.html`, `404.html`, `robots.txt`, `sitemap.xml`, `assets/web`, `assets/fonts` e `assets/videos/hero-web.mp4`. Não publicar arquivos de desenvolvimento, Git, inspeção ou ferramentas. Configurar a hospedagem para responder HTTP 404 com `404.html` em endereços inexistentes; não reescrever tudo para a homepage.

Não há formulário, cookies, analytics ou serviços que exijam segredos. Os CTAs abrem o WhatsApp com a mensagem fornecida. O envio depende da ação do visitante.

## Conteúdo e manutenção

Os cases e depoimentos usam exclusivamente as informações fornecidas. Os carrosséis são manuais e aceitam botões, teclado e swipe. A apresentação institucional permanece desabilitada e claramente identificada como “Em breve”; para publicá-la, colocar o PDF nos assets e substituir o botão do componente `.presentation` por um link real.

O vídeo usa versão H.264 otimizada, sem áudio, com fast-start. Em telas abaixo de 768 px, conexão lenta, economia de dados ou movimento reduzido, o site usa poster. Há pausa manual no desktop e pausa automática fora da tela ou em aba oculta.

## Créditos

Logo e materiais de clientes fornecidos pela Bravo BR Foods. Cenas institucionais derivadas do vídeo local; nenhuma pessoa é apresentada como integrante da Bravo.

Fotografia gastronômica ilustrativa: Jason Edwards, [Unsplash](https://unsplash.com/photos/cooked-dish-on-white-ceramic-plate-ip5OlSjG88I), [licença Unsplash](https://unsplash.com/license). Arquivo local `assets/web/gastronomia-original.jpg`; versões WebP para a página.

Tipografia: Barlow Condensed e DM Sans, Google Fonts. Licenças OFL em `assets/fonts`.

`inspect-assets.py` e `prepare-media.py` são utilitários de manutenção (Pillow, imageio-ffmpeg e pypdfium2 para inspeção de PDFs). `.qa` e `.tools` são locais e ignorados pelo Git.
