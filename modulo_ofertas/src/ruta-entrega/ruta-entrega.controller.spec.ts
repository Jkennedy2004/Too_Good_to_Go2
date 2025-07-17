import { Test, TestingModule } from '@nestjs/testing';
import { RutaEntregaController } from './ruta-entrega.controller';
import { RutaEntregaService } from './ruta-entrega.service';

describe('RutaEntregaController', () => {
  let controller: RutaEntregaController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [RutaEntregaController],
      providers: [RutaEntregaService],
    }).compile();

    controller = module.get<RutaEntregaController>(RutaEntregaController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
