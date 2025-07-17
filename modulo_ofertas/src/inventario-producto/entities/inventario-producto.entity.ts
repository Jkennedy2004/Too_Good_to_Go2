import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class InventarioProducto {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  productoNombre: string;

  @Column()
  cantidad: number;

  @Column({ type: 'decimal' })
  precioUnitario: number;
}
