import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Entrega {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ type: 'timestamp' })
  fechaEntrega: Date;

  @Column()
  repartidorId: number;

  @Column()
  rutaEntrega: string;
}
