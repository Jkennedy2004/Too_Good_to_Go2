import { Test, TestingModule } from '@nestjs/testing';
import { OfertaReducidaService } from './oferta-reducida.service';

describe('OfertaReducidaService', () => {
  let service: OfertaReducidaService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [OfertaReducidaService],
    }).compile();

    service = module.get<OfertaReducidaService>(OfertaReducidaService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
