import { ObjectType, Field, Int } from '@nestjs/graphql';

@ObjectType()
export class Pedido {
  @Field(() => Int)
  id: number;

  @Field()
  fecha_pedido: string;

  @Field(() => Int)
  usuario_id: number;

  @Field(() => Int)
  restaurante_id: number;
}
