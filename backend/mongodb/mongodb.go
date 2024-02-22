package mongodb

import (
    "context"
    "fmt"
    "log"
    "time"

    "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/mongo"
    "go.mongodb.org/mongo-driver/mongo/options"
)

func ConnectToAtlas() (*mongo.Client, error) {
    // Replace the uri string with your MongoDB deployment's connection string.
    uri := "mongodb+srv://ambroquach:Koosmongo2958@cluster0.4yfd0xh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client, err := mongo.NewClient(options.Client().ApplyURI(uri))
		
    if err != nil {
        log.Fatal(err)
    }
    return client, nil
}

func TestOperations(client *mongo.Client) {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    err := client.Connect(ctx)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Disconnect(ctx)

    // Getting a handle for your collection
    collection := client.Database("test").Collection("numbers")

    // Inserting a document
    res, insertErr := collection.InsertOne(ctx, bson.D{{"name", "pi"}, {"value", 3.14159}})
    if insertErr != nil {
        log.Fatal(insertErr)
    }
    fmt.Printf("Inserted document with _id: %v\n", res.InsertedID)

    // Querying documents
    var result struct {
        Name  string
        Value float64
    }
    filter := bson.D{{"name", "pi"}}
    queryErr := collection.FindOne(ctx, filter).Decode(&result)
    if queryErr != nil {
        log.Fatal(queryErr)
    }
    fmt.Printf("Found a document: %+v\n", result)
}
