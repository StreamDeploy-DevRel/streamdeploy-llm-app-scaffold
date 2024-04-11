<script lang="ts">
    let message: string = '';
    let answer: string = '';
    async function sendMessageToLLMModel(): Promise<void> {
        const myHeaders: Headers = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const raw = JSON.stringify({
            "message": message 
        });

        const requestOptions : RequestInit = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };
        
        const response = await fetch('http://localhost:8000/generate/', requestOptions);
        const data = await response.json();
        answer = data; // Assuming the backend responds with the generated text directly
    }
</script>

<main class="mainGridContainer">
    <div class="infoSidebar">
        <h2><span>Scaffold</span> LLM App</h2>

        <h3>Built with:</h3>
        <p>SvelteKit + Golang + MongoDB Atlas + Llama2-7B</p>
        <h3>Team Members:</h3>
        <p>Tony Loehr</p>
        <p>Ambro Quach</p>
    </div>

    <div class="chatApp">
        <h1>Welcome to <span>Scaffold!</span></h1>

        <img src="/scaffold-llama.jpeg" alt="scaffold-llama" style="width: 200px; height: 200px;" />

        <p>Enter your message to start chatting with the <span>Mistral-7B</span> LLM model:</p>
        <input type="text" bind:value={message} placeholder="I want to hack MongoDB Atlas! 🤫" style="width: 500px; height: 100px; border: 1px solid, border-radius: 5px;" />
        <br />
        <button on:click={() => {
            sendMessageToLLMModel(); // Call the function with the current message
            message = ''; // Clear the input message after sending
        }}>Send</button>
        <p>Your chat is {message.length} characters long</p>
    </div>

    <div class="displayResult">
        <h1>The <span>result</span> you are looking for:</h1>
        <div>
            <p>{answer}</p>
        </div>
    </div>
</main>

<style>
    main {
        display: grid;
        place-items: flex-start;
        grid-template-columns: 30%, 70%, auto;
        grid-template-rows: 25% 25% 25% 25% 25% 25%;
        text-align: center;
        font-family: Futura;
        padding: 1em;
        max-width: 1200px;
        margin: 0 auto;
        gap: 20px;
        border-radius: 5px;
    }

    span {
        color: #b48323;
    }

    button {
        color: #b48323;
        font-size: 1rem;
        font-family: Futura;
    }

    .infoSidebar {
        text-align: center;
        grid-column: 1 / 2;
        grid-row: 2 / 5;
        padding: 1em;
        width: 50%;
        border: 1px solid #b48323;
    }

    .chatApp {
        display: flex;
        place-items: center;
        flex-direction: column;
        grid-column: 2 / 3;
        grid-row: 1 / 4;
        padding: 1em;
        width: 100%;
        border: 1px solid #b48323;
    }

    .displayResult {
        grid-column: 2 / 3;
        grid-row: 4 / 6;
        padding: 1em;
        width: 100%;
        border: 1px solid #4d4d4d;
    }

    input {
        width: 100%;
        padding: 0.7em;
        margin-top: 0.5em;
    }
</style>
