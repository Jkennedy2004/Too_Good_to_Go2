import { Test, TestingModule } from '@nestjs/testing';
import { InventarioProductoService } from './inventario-producto.service';

describe('InventarioProductoService', () => {
  let service: InventarioProductoService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [InventarioProductoService],
    }).compile();

    service = module.get<InventarioProductoService>(InventarioProductoService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
