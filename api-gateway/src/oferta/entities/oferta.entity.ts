import { ObjectType, Field, Int } from '@nestjs/graphql';

@ObjectType()
export class Oferta {
  @Field(() => Int, { description: 'Example field (placeholder)' })
  exampleField: number;
}
