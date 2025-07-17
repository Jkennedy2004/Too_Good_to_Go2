import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';

import { EntregaModule } from './entrega/entrega.module';
import { InventarioProductoModule } from './inventario-producto/inventario-producto.module';
import { OfertaReducidaModule } from './oferta-reducida/oferta-reducida.module';
import { RepartidorModule } from './repartidor/repartidor.module';
import { RutaEntregaModule } from './ruta-entrega/ruta-entrega.module';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'tu_usuario',
      password: 'tu_contraseña',
      database: 'nombre_base_de_datos',
      autoLoadEntities: true, // para registrar entidades automáticamente
      synchronize: true, // ⚠️ solo para desarrollo
    }),
    EntregaModule,
    InventarioProductoModule,
    OfertaReducidaModule,
    RepartidorModule,
    RutaEntregaModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
