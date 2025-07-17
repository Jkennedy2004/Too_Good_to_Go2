import { Test, TestingModule } from '@nestjs/testing';
import { InventarioProductoController } from './inventario-producto.controller';
import { InventarioProductoService } from './inventario-producto.service';

describe('InventarioProductoController', () => {
  let controller: InventarioProductoController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [InventarioProductoController],
      providers: [InventarioProductoService],
    }).compile();

    controller = module.get<InventarioProductoController>(InventarioProductoController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
