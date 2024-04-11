export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["Icon.png","Logo.png","favicon.png","scaffold-llama.jpeg"]),
	mimeTypes: {".png":"image/png",".jpeg":"image/jpeg"},
	_: {
		client: {"start":"_app/immutable/entry/start.467da394.js","app":"_app/immutable/entry/app.3ce74ce5.js","imports":["_app/immutable/entry/start.467da394.js","_app/immutable/chunks/index.63dde02a.js","_app/immutable/chunks/singletons.8218923e.js","_app/immutable/entry/app.3ce74ce5.js","_app/immutable/chunks/index.63dde02a.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();
