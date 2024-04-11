

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.5445493c.js","_app/immutable/chunks/index.63dde02a.js","_app/immutable/chunks/singletons.8218923e.js"];
export const stylesheets = [];
export const fonts = [];
