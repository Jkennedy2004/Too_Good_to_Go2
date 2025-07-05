import { Test, TestingModule } from '@nestjs/testing';
import { OfertaResolver } from './oferta.resolver';
import { OfertaService } from './oferta.service';

describe('OfertaResolver', () => {
  let resolver: OfertaResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [OfertaResolver, OfertaService],
    }).compile();

    resolver = module.get<OfertaResolver>(OfertaResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});
