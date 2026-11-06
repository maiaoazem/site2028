// Roteia subdomínios para pastas do site.
// contexto.gira.guru  ->  /contexto/
// Qualquer outro endereço (gira.guru) segue igual: entrega os arquivos do repositório.
const SUBDOMINIOS = {
  'contexto.gira.guru': '/contexto',
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pasta = SUBDOMINIOS[url.hostname];
    if (!pasta) return env.ASSETS.fetch(request);

    if (!url.pathname.startsWith(pasta + '/')) {
      const dentro = new URL(url);
      dentro.pathname = pasta + url.pathname;
      const resp = await env.ASSETS.fetch(new Request(dentro, request));
      if (resp.status !== 404) return resp;
    }
    // arquivos da raiz (favicon etc.) continuam disponíveis no subdomínio
    return env.ASSETS.fetch(request);
  },
};
