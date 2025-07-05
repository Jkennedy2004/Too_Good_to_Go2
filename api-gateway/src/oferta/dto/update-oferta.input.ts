import { CreateOfertaInput } from './create-oferta.input';
import { InputType, Field, Int, PartialType } from '@nestjs/graphql';

@InputType()
export class UpdateOfertaInput extends PartialType(CreateOfertaInput) {
  @Field(() => Int)
  id: number;
}
