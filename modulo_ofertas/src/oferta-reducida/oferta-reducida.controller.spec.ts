import { Test, TestingModule } from '@nestjs/testing';
import { OfertaReducidaController } from './oferta-reducida.controller';
import { OfertaReducidaService } from './oferta-reducida.service';

describe('OfertaReducidaController', () => {
  let controller: OfertaReducidaController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [OfertaReducidaController],
      providers: [OfertaReducidaService],
    }).compile();

    controller = module.get<OfertaReducidaController>(OfertaReducidaController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
