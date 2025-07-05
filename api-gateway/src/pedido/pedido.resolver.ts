import { Resolver, Query, Args, Int } from '@nestjs/graphql';
import { PedidoService } from './pedido.service';
import { Pedido } from './dto/create-pedido.input';

@Resolver(() => Pedido)
export class PedidoResolver {
  constructor(private readonly pedidoService: PedidoService) {}

  @Query(() => [Pedido], { name: 'pedidos' })
  async getPedidos(): Promise<Pedido[]> {
    return this.pedidoService.findAll();
  }

  @Query(() => Pedido, { name: 'pedido' })
  async getPedido(@Args('id', { type: () => Int }) id: number): Promise<Pedido> {
    return this.pedidoService.findOne(id);
  }
}
