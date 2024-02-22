package main

import ( 
	"log"
	"backend/mongodb"
)

func main() {
    client, err := mongodb.ConnectToAtlas()
    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err := client.Disconnect(nil); err != nil {
            log.Fatal(err)
        }
    }()

    mongodb.TestOperations(client)
    
    // From here, you can use the `client` to interact with the database.
    log.Println("You're now connected to MongoDB!")
}
