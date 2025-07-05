import { ObjectType, Field, Int } from '@nestjs/graphql';

@ObjectType()
export class Pedido {
  @Field(() => Int, { description: 'Example field (placeholder)' })
  exampleField: number;
}
