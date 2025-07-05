import { ObjectType, Field, Int, Float } from '@nestjs/graphql';

@ObjectType()
export class Oferta {
  @Field(() => Int)
  id: number;

  @Field()
  descripcion: string;

  @Field(() => Float)
  precio_reducido: number;

  @Field()
  fecha_inicio: string;

  @Field()
  fecha_fin: string;

  @Field(() => Int)
  restaurante_id: number;
}
