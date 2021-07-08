from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return 'Hello World'

class Jugador(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, root, nombre, apellido):
        print(nombre, apellido)
        return Jugador(ok=True)

class Mutation(graphene.ObjectType):
    nuevoJugador = Jugador.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

schema.execute('''
  query {
    hello
  }
''')
    

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)