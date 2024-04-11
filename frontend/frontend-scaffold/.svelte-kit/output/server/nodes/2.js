

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/2.5e24e33a.js","_app/immutable/chunks/index.63dde02a.js"];
export const stylesheets = ["_app/immutable/assets/2.3a946ddd.css"];
export const fonts = [];
