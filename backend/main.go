package main

import (
	"backend/mongodb"
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Request struct {
	Message string `json:"message"`
}

type Response struct {
	Answer string `json:"answer"`
}

func askHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Only POST method is allowed", http.StatusMethodNotAllowed)
		return
	}

	var req Request
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Correctly calling the LLM service with the message from the request
	answer, err := callLlamaService(req.Message)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	res := Response{Answer: answer}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(res)
}

func callLlamaService(question string) (string, error) {
	// Llama service URL
	llamaServiceURL := "http://localhost:5000/ask"

	// Prepare the request body
	requestBody, err := json.Marshal(map[string]string{
		"message": question,
	})
	if err != nil {
		return "", err
	}

	// Make the request
	resp, err := http.Post(llamaServiceURL, "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	// Read the response
	var respBody struct {
		Answer string `json:"answer"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&respBody); err != nil {
		return "", err
	}

	return respBody.Answer, nil
}

func main() {
	client, err := mongodb.ConnectToAtlas()
	if err != nil {
		log.Fatal(err)
	}

	mongodb.TestOperations(client)

	// From here, you can use the `client` to interact with the database.
	log.Println("You're now connected to MongoDB!")

	http.HandleFunc("/ask", askHandler)
	fmt.Println("Server is listening on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
