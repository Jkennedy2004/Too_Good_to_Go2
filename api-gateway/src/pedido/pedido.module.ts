import { Module } from '@nestjs/common';
import { PedidoService } from './pedido.service';
import { PedidoResolver } from './pedido.resolver';

@Module({
  providers: [PedidoResolver, PedidoService],
})
export class PedidoModule {}
