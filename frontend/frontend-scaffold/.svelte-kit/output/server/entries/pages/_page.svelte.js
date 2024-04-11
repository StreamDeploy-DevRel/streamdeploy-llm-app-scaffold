import { c as create_ssr_component, d as add_attribute, e as escape } from "../../chunks/index.js";
const _page_svelte_svelte_type_style_lang = "";
const css = {
  code: "main.svelte-6femyd{display:grid;place-items:flex-start;grid-template-columns:30%, 70%, auto;grid-template-rows:25% 25% 25% 25% 25% 25%;text-align:center;font-family:Futura;padding:1em;max-width:1200px;margin:0 auto;gap:20px;border-radius:5px}span.svelte-6femyd{color:#b48323}button.svelte-6femyd{color:#b48323;font-size:1rem;font-family:Futura}.infoSidebar.svelte-6femyd{text-align:center;grid-column:1 / 2;grid-row:2 / 5;padding:1em;width:50%;border:1px solid #b48323}.chatApp.svelte-6femyd{display:flex;place-items:center;flex-direction:column;grid-column:2 / 3;grid-row:1 / 4;padding:1em;width:100%;border:1px solid #b48323}.displayResult.svelte-6femyd{grid-column:2 / 3;grid-row:4 / 6;padding:1em;width:100%;border:1px solid #4d4d4d}input.svelte-6femyd{width:100%;padding:0.7em;margin-top:0.5em}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let message = "";
  let answer = "";
  $$result.css.add(css);
  return `<main class="mainGridContainer svelte-6femyd"><div class="infoSidebar svelte-6femyd"><h2><span class="svelte-6femyd">Scaffold</span> LLM App</h2>

        <h3>Built with:</h3>
        <p>SvelteKit + Golang + MongoDB Atlas + Llama2-7B</p>
        <h3>Team Members:</h3>
        <p>Tony Loehr</p>
        <p>Ambro Quach</p></div>

    <div class="chatApp svelte-6femyd"><h1>Welcome to <span class="svelte-6femyd">Scaffold!</span></h1>

        <img src="/scaffold-llama.jpeg" alt="scaffold-llama" style="width: 200px; height: 200px;">

        <p>Enter your message to start chatting with the <span class="svelte-6femyd">Lllama2-7B</span> LLM model:</p>
        <input type="text" placeholder="I want to hack MongoDB Atlas! 🤫" style="width: 500px; height: 100px; border: 1px solid, border-radius: 5px;" class="svelte-6femyd"${add_attribute("value", message, 0)}>
        <br>
        <button class="svelte-6femyd">Send</button>
        <p>Your chat is ${escape(message.length)} characters long</p></div>

    <div class="displayResult svelte-6femyd"><h1>The <span class="svelte-6femyd">result</span> you are looking for:</h1>
        <div><p>${escape(answer)}</p></div></div>
</main>`;
});
export {
  Page as default
};
