# flask with Graphql
test for graphql 

## Start project

```
pip install -r requirements
python app.py

Viewer tester API
http://localhost:8080/graphql
```

### Simple Query Graphql

```
curl --location --request POST 'http://localhost:8080/graphql' \
--header 'Content-Type: application/json' \
--data-raw '{"query":"{hello}","variables":{}}'
```

### Mutation Query Graphql


```
curl --location --request POST 'http://localhost:8080/graphql' \
--header 'Content-Type: application/json' \
--data-raw '{"query":"mutation {nuevoJugador(nombre:\"Benjamin\",apellido:\"Casazza\"){ok}}","variables":{}}'
```



