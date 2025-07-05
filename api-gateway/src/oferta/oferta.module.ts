import { Module } from '@nestjs/common';
import { OfertaService } from './oferta.service';
import { OfertaResolver } from './oferta.resolver';

@Module({
  providers: [OfertaResolver, OfertaService],
})
export class OfertaModule {}
