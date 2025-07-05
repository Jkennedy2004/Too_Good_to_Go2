import { Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql';
import { PedidoModule } from './pedido/pedido.module';
import { OfertaModule } from './oferta/oferta.module';

@Module({
  imports: [
    GraphQLModule.forRoot({
      autoSchemaFile: 'schema.gql', // Genera el schema automáticamente en la raíz del proyecto
      playground: true,             // Activa el playground GraphQL para pruebas
    }),
    PedidoModule,
    OfertaModule,
  ],
})
export class AppModule {}
