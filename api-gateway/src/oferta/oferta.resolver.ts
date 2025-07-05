import { Resolver, Query, Args, Int } from '@nestjs/graphql';
import { OfertaService } from './oferta.service';
import { Oferta } from './dto/create-oferta.input';

@Resolver(() => Oferta)
export class OfertaResolver {
  constructor(private readonly ofertaService: OfertaService) {}

  @Query(() => [Oferta], { name: 'ofertas' })
  async getOfertas(): Promise<Oferta[]> {
    return this.ofertaService.findAll();
  }

  @Query(() => Oferta, { name: 'oferta' })
  async getOferta(@Args('id', { type: () => Int }) id: number): Promise<Oferta> {
    return this.ofertaService.findOne(id);
  }
}
